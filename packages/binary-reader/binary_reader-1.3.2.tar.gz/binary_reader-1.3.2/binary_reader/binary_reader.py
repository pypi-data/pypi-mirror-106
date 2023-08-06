__author__ = "SutandoTsukai181"
__copyright__ = "Copyright 2021, SutandoTsukai181"
__license__ = "MIT"
__version__ = "1.3.2"

import struct
from contextlib import contextmanager
from enum import Flag, IntEnum
from typing import Tuple, Union

FMT = dict()
for c in ["b", "B", "s"]:
    FMT[c] = 1
for c in ["h", "H", "e"]:
    FMT[c] = 2
for c in ["i", "I", "f"]:
    FMT[c] = 4
for c in ["q", "Q"]:
    FMT[c] = 8


class Endian(Flag):
    LITTLE = False
    BIG = True


class Whence(IntEnum):
    BEGIN = 0
    CUR = 1
    END = 2


class BinaryReader:
    """A buffer reader/writer containing a mutable bytearray.\n
    Allows reading and writing various data types, while advancing the position of the buffer on each operation."""
    __buf: bytearray
    __idx: int
    __endianness: Endian
    __encoding: str

    def __init__(self, buffer: bytearray = bytearray(), endianness: Endian = Endian.LITTLE, encoding='utf-8'):
        """Constructs a BinaryReader with the given buffer, endianness, and encoding and sets its position to 0.\n
        If buffer is not given, a new bytearray() is created. If endianness is not given, it is set to little endian.\n
        Default encoding is UTF-8. Will throw an exception if encoding is unknown.
        """
        self.__buf = bytearray(buffer)
        self.__endianness = endianness
        self.__idx = 0
        self.set_encoding(encoding)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__buf.clear()

    def pos(self) -> int:
        """Returns the current position in the buffer."""
        return self.__idx

    def size(self) -> int:
        """Returns the size of the buffer."""
        return len(self.__buf)

    def buffer(self) -> bytearray:
        """Returns the buffer as a bytearray."""
        return bytearray(self.__buf)

    def pad(self, size: int) -> None:
        """Pads the buffer by 0s with the given size and advances the buffer position.\n
        Will advance the buffer position only if the position was at the end of the buffer.
        """
        if self.__idx == self.size():
            self.__idx += size

        self.extend([0] * size)

    def align(self, size: int) -> int:
        """Aligns the buffer to the given size.\n
        Extends the buffer from its end by (size - (buffer_size % size)).\n
        Will advance the buffer position only if the position was at the end of the buffer.\n
        Returns the number of bytes padded.
        """
        pad = 0

        if self.size() % size:
            pad = size - (self.size() % size)
            self.pad(pad)

        return pad

    def extend(self, buffer: bytearray) -> None:
        """Extends the BinaryReader's buffer with the given buffer.\n
        Does not advance buffer position.
        """
        self.__buf.extend(buffer)

    def trim(self, size: int) -> int:
        """Trims the buffer to the given size.\n
        If size is greater than the buffer's length, no bytes will be removed.\n
        If the position of the buffer was in the trimmed range, it will be set to the end of the buffer.\n
        Returns the number of bytes removed.
        """
        trimmed = 0

        if size > 0:
            trimmed = self.size() - size

        if (trimmed > 0):
            self.__buf = self.__buf[:size]
            if (self.__idx > size):
                self.__idx = self.size()
        else:
            trimmed = 0

        return trimmed

    def seek(self, offset: int, whence: Whence = Whence.BEGIN) -> None:
        """Changes the current position of the buffer by the given offset.\n
        The seek is determined relative to the whence:\n
        Whence.BEGIN will seek relative to the start.\n
        Whence.CUR will seek relative to the current position.\n
        Whence.END will seek relative to the end (offset should be positive).
        """
        new_offset = self.__idx

        if whence == Whence.BEGIN:
            new_offset = offset
        elif whence == Whence.CUR:
            new_offset = self.__idx + offset
        elif whence == Whence.END:
            new_offset = len(self.__buf) - offset
        else:
            raise Exception('BinaryReader Error: invalid whence value.')

        if new_offset > len(self.__buf) or new_offset < 0:
            raise Exception(
                'BinaryReader Error: cannot seek farther than buffer length.')

        self.__idx = new_offset

    @contextmanager
    def seek_to(self, offset: int, whence: Whence = Whence.BEGIN) -> 'BinaryReader':
        """Same as `seek(offset, whence)`, but can be used with the `with` statement in a new context.\n
        Upon returning to the old context, the original position of the buffer before the `with` statement will be restored.\n
        Will return a reference of the BinaryReader to be used for `as` in the `with` statement.\n
        The original BinaryReader that this was called from can still be used instead of the return value.
        """
        prev_pos = self.__idx
        self.seek(offset, whence)
        yield self

        self.__idx = prev_pos

    def set_endian(self, endianness: Endian) -> None:
        """Sets the endianness of the BinaryReader."""
        self.__endianness = endianness

    def set_encoding(self, encoding: str) -> None:
        """Sets the default encoding of the BinaryReader when reading/writing strings.\n
        Will throw an exception if the encoding is unknown.
        """
        str.encode('', encoding)
        self.__encoding = encoding

    def __read_type(self, format: str, count=1):
        i = self.__idx
        self.__idx += FMT[format] * count

        end = ">" if self.__endianness else "<"

        return struct.unpack_from(end + str(count) + format, self.__buf, i)

    def read_bytes(self, length=1) -> bytes:
        """Reads a bytes object with the given length from the current position."""
        return self.__read_type("s", length)

    def read_str(self, length=0, encoding=None) -> str:
        """Reads a string with the given length from the current position.\n
        If length is `0` (default), will read until the first null byte (which the position will be set after).\n
        If encoding is `None` (default), will use the BinaryReader's encoding.
        """
        encode = self.__encoding if encoding is None else encoding

        if length == 0:
            string = bytearray()
            while self.__idx < len(self.__buf):
                string.append(self.__buf[self.__idx])
                self.__idx += 1
                if string[-1] == 0:
                    break

            return string.split(b'\x00', 1)[0].decode(encode)

        return self.read_bytes(length)[0].split(b'\x00', 1)[0].decode(encode)

    def read_int64(self, count=1) -> Union[int, Tuple[int]]:
        """Reads a signed 64-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("q", count)
        return self.__read_type("q")[0]

    def read_uint64(self, count=1) -> Union[int, Tuple[int]]:
        """Reads an unsigned 64-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("Q", count)
        return self.__read_type("Q")[0]

    def read_int32(self, count=1) -> Union[int, Tuple[int]]:
        """Reads a signed 32-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("i", count)
        return self.__read_type("i")[0]

    def read_uint32(self, count=1) -> Union[int, Tuple[int]]:
        """Reads an unsigned 32-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("I", count)
        return self.__read_type("I")[0]

    def read_int16(self, count=1) -> Union[int, Tuple[int]]:
        """Reads a signed 16-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("h", count)
        return self.__read_type("h")[0]

    def read_uint16(self, count=1) -> Union[int, Tuple[int]]:
        """Reads an unsigned 16-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("H", count)
        return self.__read_type("H")[0]

    def read_int8(self, count=1) -> Union[int, Tuple[int]]:
        """Reads a signed 8-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("b", count)
        return self.__read_type("b")[0]

    def read_uint8(self, count=1) -> Union[int, Tuple[int]]:
        """Reads an unsigned 8-bit integer.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("B", count)
        return self.__read_type("B")[0]

    def read_float(self, count=1) -> Union[float, Tuple[float]]:
        """Reads a 32-bit float.\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("f", count)
        return self.__read_type("f")[0]

    def read_half_float(self, count=1) -> Union[float, Tuple[float]]:
        """Reads a 16-bit float (half-float).\n
        If count is greater than 1, will return a tuple of values instead of 1 value.
        """
        if count > 1:
            return self.__read_type("e", count)
        return self.__read_type("e")[0]

    def __write_type(self, format: str, value, is_iterable: bool) -> None:
        i = self.__idx

        end = ">" if self.__endianness else "<"

        count = 1
        if is_iterable or type(value) is bytes:
            count = len(value)

        if i + (FMT[format] * count) > len(self.__buf):
            self.pad(FMT[format] * count)
        else:
            self.__idx += FMT[format] * count

        if is_iterable:
            struct.pack_into(end + str(count) + format, self.__buf, i, *value)
        else:
            struct.pack_into(end + str(count) + format, self.__buf, i, value)

    def write_bytes(self, value: bytes) -> None:
        """Writes a bytes object to the buffer."""
        self.__write_type("s", value, is_iterable=False)

    def write_str(self, string: str, null=False, encoding=None) -> int:
        """Writes a whole string to the buffer.\n
        If null is `True`, will append a null byte (`0x00`) after the string.\n
        If encoding is `None` (default), will use the BinaryReader's encoding.\n
        Returns the number of bytes written (including the null byte if it was added).
        """
        bytes_obj = string.encode(
            self.__encoding if encoding is None else encoding) + (b'\x00' if null else b'')
        self.write_bytes(bytes_obj)
        return len(bytes_obj)

    def write_int64(self, value: int, is_iterable=False) -> None:
        """Writes a signed 64-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("q", value, is_iterable)

    def write_uint64(self, value: int, is_iterable=False) -> None:
        """Writes an unsigned 64-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("Q", value, is_iterable)

    def write_int32(self, value: int, is_iterable=False) -> None:
        """Writes a signed 32-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("i", value, is_iterable)

    def write_uint32(self, value: int, is_iterable=False) -> None:
        """Writes an unsigned 32-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("I", value, is_iterable)

    def write_int16(self, value: int, is_iterable=False) -> None:
        """Writes a signed 16-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("h", value, is_iterable)

    def write_uint16(self, value: int, is_iterable=False) -> None:
        """Writes an unsigned 16-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("H", value, is_iterable)

    def write_int8(self, value: int, is_iterable=False) -> None:
        """Writes a signed 8-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("b", value, is_iterable)

    def write_uint8(self, value: int, is_iterable=False) -> None:
        """Writes an unsigned 8-bit integer.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("B", value, is_iterable)

    def write_float(self, value: float, is_iterable=False) -> None:
        """Writes a 32-bit float.\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("f", value, is_iterable)

    def write_half_float(self, value: float, is_iterable=False) -> None:
        """Writes a 16-bit float (half-float).\n
        If is_iterable is True, will write all of the values in the given iterable.
        """
        self.__write_type("e", value, is_iterable)

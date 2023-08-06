import io, typing, math

from .cipher import BufcryptCipher

INTEGER_SIZE = 8
PART_SIZE = 8192
PLAINTEXT_HEADER_SIZE = INTEGER_SIZE*2

def int2bytes(value:int) -> bytes:
    return int.to_bytes(value, INTEGER_SIZE, "little", signed=False)

def bytes2int(data:bytes) -> int:
    return int.from_bytes(data, "little", signed=False)

def get_int(data:bytes, index:int) -> int:
    data_index = INTEGER_SIZE*index
    data = data[data_index:(data_index+INTEGER_SIZE)]

    return bytes2int(data)

def readfully(file:io.BufferedIOBase, size=-1, eof=False) -> bytes:
    if size < 0:
        return bytes(file.read())
    else:
        data = bytearray()
        remaining = size

        while remaining > 0:
            data_part = file.read(remaining)

            if len(data_part) == 0:
                if eof:
                    return bytes(data)
                else:
                    raise EOFError()

            data.extend(data_part)
            remaining -= len(data_part)
        
        return bytes(data)

class LoadedPart:
    index:int
    data:bytearray

    def __repr__(self):
        return repr({
            "index":self.index,
            "data":self.data
        })

# One of the golden rules here is that there should
# never be any "empty" parts (parts with a size of 0).
# If such were to be allowed, this code would be 
# vulnerable to truncation attacks.
# There is either no part or a part with a size of
# at least 1 and at most PART_SIZE.
class BufcryptIO(io.BufferedIOBase):
    file:io.BufferedIOBase
    cipher:BufcryptCipher
    
    closed:bool = False

    _newline:bytes

    _pointer:int = 0
    
    _partsize:int = PART_SIZE

    _loaded:LoadedPart = None

    @classmethod
    def analyze(cls, file:io.BufferedIOBase, cipher:BufcryptCipher) -> typing.Generator[bytes, None, None]:
        encrypted_header_size = cipher.cipherlen(PLAINTEXT_HEADER_SIZE)
        encrypted_part_size = cipher.cipherlen(PART_SIZE)

        file.seek(0)
        try:
            yield cipher.decrypt(0, readfully(file, encrypted_header_size))
        except EOFError:
            return

        cipher_index = 1
        while True:
            encrypted_part_data = readfully(file, encrypted_part_size, eof=True)
            if encrypted_part_data:
                yield cipher.decrypt(cipher_index, encrypted_part_data)
                cipher_index += 1
            else:
                break

    def __init__(self, file:io.BufferedIOBase, cipher:BufcryptCipher, *, append=False, newline=b'\n'):
        self.file = file
        self.cipher = cipher
        self._newline = newline
        
        try:
            self._partsize, _ = self._header
        except EOFError:
            self._partsize = PART_SIZE
            self._header = PART_SIZE, 0

            zerofirst = self.cipher.encrypt(self._get_cipher_index(0), bytes())
            self.file.seek(self.cipher.cipherlen(PLAINTEXT_HEADER_SIZE))
            self.file.write(zerofirst)

        if append:
            self.seek(self._size)
        else:
            self.seek(0)
    
    # Header: (partsize, size)
    @property
    def _header(self) -> typing.Tuple[int, int]:
        self.file.seek(0)
        ciphertext_header_size = self.cipher.cipherlen(PLAINTEXT_HEADER_SIZE)

        encrypted_header = readfully(self.file, ciphertext_header_size)
        decrypted_header = self.cipher.decrypt(0, encrypted_header)

        partsize = get_int(decrypted_header, 0)
        size = get_int(decrypted_header, 1)

        return partsize, size
    
    # Header: (partsize, size)
    @_header.setter
    def _header(self, header:typing.Tuple[int, int]):
        partsize, size = header

        plaintext_header = int2bytes(partsize) + int2bytes(size)
        encrypted_header = self.cipher.encrypt(0, plaintext_header)

        self.file.seek(0)
        self.file.write(encrypted_header)
    
    _size_cached:int = None

    # Part count must always be at least 1.
    @property
    def _size(self) -> int:
        if self._size_cached is None:
            _, self._size_cached = self._header

        return self._size_cached
    
    @_size.setter
    def _size(self, size:int):
        self._header = self._partsize, size
        self._size_cached = size

    def _get_part_index(self, seek:int=None) -> int:
        return math.floor(seek/self._partsize)

    def _get_part_pointer(self, pointer:int, part_index:int) -> int:
        return pointer - (self._partsize*part_index)
    
    def _get_underlying_pointer(self, part_index:int):
        pointer = 0
        pointer += self.cipher.cipherlen(PLAINTEXT_HEADER_SIZE)
        pointer += part_index * self.cipher.cipherlen(self._partsize)

        return pointer
    
    @property
    def _loaded_part_pointer(self) -> int:
        return self._get_part_pointer(self._pointer, self._loaded.index)
    
    def _get_cipher_index(self, part_index:int) -> int:
        return part_index + 1
    
    # Can return -1
    @property
    def _last_part_index(self) -> int or -1:
        last_byte_index = self._size - 1
        return math.floor(last_byte_index/self._partsize)
    
    @property
    def _partcount(self) -> int:
        return self._last_part_index + 1

    def _read_part(self, part_index:int) -> bytearray or None:
        last_part_index = self._last_part_index

        last_part_size:int

        if (part_index > last_part_index) or (last_part_index < 0):
            return None
        elif part_index == last_part_index:
            size_floor = self._partsize*part_index
            last_part_size = self._size - size_floor
        elif part_index < last_part_index:
            last_part_size = self._partsize

        underlying_last_part_size = self.cipher.cipherlen(last_part_size)
        underlying_seek = self._get_underlying_pointer(part_index)

        cipher_index = self._get_cipher_index(part_index)

        self.file.seek(underlying_seek)
        encrypted_part = readfully(self.file, underlying_last_part_size)
        decrypted_part = self.cipher.decrypt(cipher_index, encrypted_part)

        return bytearray(decrypted_part)

    def _is_loaded(self, part_index:int) -> bool:
        if self._loaded is None:
            return False
        else:
            return self._loaded.index == part_index

    # Flushes automatically when called
    def _load_part(self, part_index:int) -> bool:
        if self._is_loaded(part_index):
            return True
        
        self._flush0()
        self._loaded = None
        
        part_data = self._read_part(part_index)

        if part_data is None:
            return False
        
        self._loaded = LoadedPart()
        self._loaded.index = part_index
        self._loaded.data = part_data

        return True
    
    def _flush0(self):
        # Only write if the loaded part is not empty
        if (self._loaded is not None) and (len(self._loaded.data) > 0):
            loaded_part_underlying_pointer = self._get_underlying_pointer(self._loaded.index)
            loaded_part_data_encrypted = \
                        self.cipher.encrypt(
                            self._get_cipher_index(self._loaded.index), 
                            bytes(self._loaded.data)
                            )
            
            self.file.seek(loaded_part_underlying_pointer)
            self.file.write(loaded_part_data_encrypted)

        self.file.flush()
    
    def flush(self):
        self._check_closed()

        self._flush0()

    def close(self):
        if self.closed:
            return
        
        self._flush0()
        self.file.close()
        
        self.closed = True

    def _iterate_bytes(self) -> typing.Generator[typing.Tuple[int, int], None, None]:
        pointer = self._pointer

        while True:
            data = self.read1()

            if data:
                for b in data:
                    yield pointer, b
                    pointer += 1
            else:
                return
    
    def _indexof(self, sequence:bytes) -> int or None:
        mark = self._pointer

        found:int = None
        
        sequence_pointer = 0
        for pointer, byte in self._iterate_bytes():
            if byte == sequence[sequence_pointer]:
                sequence_pointer += 1
            else:
                sequence_pointer = 0

            if sequence_pointer == len(sequence):
                found = pointer - sequence_pointer
                break

        self.seek(mark)
        return found
    
    def _check_closed(self):
        if self.closed:
            raise ValueError("I/O operation on closed file.")

    def readline(self, size=-1) -> bytes:
        self._check_closed()

        if size == 0:
            return bytes()

        next_newline_index = self._indexof(self._newline)

        if next_newline_index is None:
            to_read = size
        else:
            to_read = next_newline_index - self._pointer + len(self._newline)

            if (to_read > size) and (size is not None) and (size > 0):
                to_read = size
        
        line = self.read(to_read)

        return line
    
    def readlines(self, hint=-1) -> typing.Generator[bytes, None, None]:
        self._check_closed()

        if (not hint) or (hint < 0): # None, 0, or less than 0
            while True:
                line = self.readline()

                if line:
                    yield line
                else:
                    return
        else:
            while hint > -1:
                line = self.readline()

                if line:
                    hint -= len(line)
                    yield line
                else:
                    return
    
    def __iter__(self):
        return self.readlines()
    
    def seek(self, offset:int, whence=io.SEEK_SET) -> bool:
        self._check_closed()

        if whence == io.SEEK_SET:
            whence = 0
        elif whence == io.SEEK_CUR:
            whence = self._pointer
        elif whence == io.SEEK_END:
            whence = self._size
        else:
            return False
        
        self._pointer = offset + whence

    def seekable(self):
        return True
    
    def tell(self):
        return self._pointer

    def truncate(self, size=None):
        self._check_closed()

        if size is None:
            size = self._pointer
        
        if size < 0:
            raise IndexError(size)

        if size == self._size:
            return
        elif size > self._size:
            previous_position = self._pointer
            to_write = size - self._size

            self.seek(self._size)
            self.write(to_write*b"\x00")

            self.seek(previous_position)
        else:
            new_last_part_index = self._get_part_index(size)
            new_last_part_size = self._get_part_pointer(size, new_last_part_index)
            
            new_last_part_data = self._read_part(new_last_part_index)
            new_last_part_data = new_last_part_data[0:new_last_part_size]

            underlying_pointer = self._get_underlying_pointer(new_last_part_index)
            new_last_part_data_encrypted = \
                self.cipher.encrypt(
                    self._get_cipher_index(new_last_part_index),
                    new_last_part_data
                )
            
            self.file.seek(underlying_pointer)
            self.file.write(new_last_part_data_encrypted)

            self._size = size
            self.file.truncate(underlying_pointer + len(new_last_part_data_encrypted))
    
    def writable(self) -> bool:
        return True
    
    def writelines(self, lines:typing.Iterable[bytes]):
        self._check_closed()

        for line in lines:
            self.write(line)

    def detach(self):
        raise io.UnsupportedOperation()
    
    def read(self, size=-1) -> bytes:
        self._check_closed()

        if size == 0:
            return bytes()
        elif (size is None) or (size < 0):
            def read():
                while True:
                    tmp = self.read1()

                    if tmp:
                        yield tmp
                    else:
                        break
        else:
            def read():
                remaining = size

                while remaining > 0:
                    tmp = self.read1(remaining)

                    if tmp:
                        remaining -= len(tmp)
                        yield tmp
                    else:
                        return
        
        return bytes().join(read())

    def read1(self, size=-1) -> bytes:
        self._check_closed()

        loaded = self._load_part(self._get_part_index(self._pointer))

        if not loaded:
            return bytes()
        
        index = self._loaded_part_pointer # TODO

        # part_remaining can't be less than 1, can it?
        # If it is, that would mean that the part wouldnt be loaded...
        part_remaining = len(self._loaded.data) - index

        if (not size) or (size < 0) or (size > part_remaining):
            size = part_remaining

        content = self._loaded.data[index:(index + size)]
        self._pointer += size
        
        return bytes(content)
    
    def _readinto(self, buffer:bytearray, read) -> int:
        data = read(len(buffer))

        buffer[0:len(data)] = data

        return len(data)
    
    def readinto(self, buffer:bytearray) -> int:
        self._check_closed()

        return self._readinto(buffer, self.read)
    
    def readinto1(self, buffer:bytearray) -> int:
        self._check_closed()

        return self._readinto(buffer, self.read1)

    def _write1(self, data:typing.Sequence[int], recursive_write_function=False) -> int:
        self._check_closed()

        if len(data) == 0:
            return 0

        part_index = self._get_part_index(self._pointer)
        loaded:bool = self._load_part(part_index)

        if not loaded:
            if self._size < self._pointer:
                to_zerofill = self._pointer - self._size

                self.seek(self._size)
                self.write(to_zerofill*[0], recursive_write_function=True)

                return self._write1(data)
            elif self._size == self._pointer:
                self._loaded = LoadedPart()
                self._loaded.index = part_index
                self._loaded.data = bytearray()
            elif self._size > self._pointer:
                # https://media.tenor.com/images/6dc9d95222f173497415446b6ec215f7/tenor.gif
                return 0

        lower_range = self._loaded_part_pointer
        upper_range = lower_range + len(data)

        if upper_range > self._partsize:
            upper_range = self._partsize

        len_before = len(self._loaded.data)
        
        written = upper_range - lower_range
        self._loaded.data[lower_range:upper_range] = data[0:written]

        len_after = len(self._loaded.data)
        
        self._size += (len_after - len_before)
        self._pointer += written

        return written

    def write(self, data:typing.Sequence[int], recursive_write_function=False) -> int:
        self._check_closed()

        total = len(data)

        while len(data) > 0:
            written = self._write1(data, recursive_write_function)
            data = data[written:]

        return total
    
    def isattty(self):
        return False
    
    def readable(self):
        return True
    
    def fileno(self):
        raise OSError()

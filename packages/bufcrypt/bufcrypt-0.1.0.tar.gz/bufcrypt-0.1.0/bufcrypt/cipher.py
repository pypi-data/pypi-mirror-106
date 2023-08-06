import abc, os

class BufcryptCipher(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def encrypt(self, index:int, data:bytes) -> bytes:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def decrypt(self, index:int, data:bytes) -> bytes:
        raise NotImplementedError()
    
    # The returned value should not change if plainlen does not change.
    # For example, it's algorithm should not depend on any variables or
    # "outside" sources that include, but are not limited to, user input
    # and/or random/pseudorandom data. If it does, it could seriously
    # f*ck things up! Imagine explaining that to your superiors...
    @abc.abstractmethod
    def cipherlen(self, plainlen:int) -> int:
        raise NotImplementedError()

try:
    class IncrementalFernetCipher(BufcryptCipher):
        key:bytes # In base64url form

        def __init__(self, key:bytes):
            self.key = key

        def getkey(self, index:int) -> bytes:
            import hashlib, base64

            key = base64.urlsafe_b64decode(self.key)

            for _ in range(0, index):
                key = hashlib.sha256(key).digest()

            return base64.urlsafe_b64encode(key)

        def encrypt(self, index:int, data:bytes) -> bytes:
            from cryptography.fernet import Fernet

            key = self.getkey(index)
            return Fernet(key).encrypt(data)

        def decrypt(self, index: int, data:bytes) -> bytes:
            from cryptography.fernet import Fernet

            key = self.getkey(index)
            return Fernet(key).decrypt(data)
        
        def cipherlen(self, plainlen: int) -> int:
            import math

            raw_fernet_len:int = 57 + 16*math.ceil((plainlen+1)/16)

            return 4 * math.ceil(raw_fernet_len/3.0)
        
except ModuleNotFoundError:
    pass
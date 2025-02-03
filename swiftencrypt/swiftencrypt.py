# Copyright (c) 2025 Sean Yeatts. All rights reserved.

from __future__ import annotations


# IMPORTS ( EXTERNAL )
from cryptography.fernet import Fernet

# IMPORTS ( STANDARD )
import base64
from abc import ABC as Abstract
from abc import abstractmethod
from typing import Any


# CLASSES
class Encryptor(Abstract):
    """Extendable base class for data encryption."""

    # INTRINSIC METHODS
    def __init__(self, keygen: Keygen):
        super().__init__()

    # PUBLIC METHODS
    @abstractmethod
    def encrypt(self, data: bytes) -> bytes:
        ... # extended by subclasses

    @abstractmethod
    def decrypt(self, data: bytes) -> bytes:
        ... # extended by subclasses


class FernetCipher(Encryptor):
    """A Fernet-style encryption strategy."""
    
    # INTRINSIC METHODS
    def __init__(self, keygen):
        super().__init__(keygen)
        key = keygen.retrieve()
        self.cipher = Fernet(key)

    # OVERRIDDEN METHODS : Encryptor
    def encrypt(self, data):
        super().encrypt(data)
        return self.cipher.encrypt(data)
    
    def decrypt(self, data):
        super().decrypt(data)
        return self.cipher.decrypt(data)


class Keygen:
    """Provides an encryption key to an Encryptor."""
    
    # PUBLIC METHODS
    @abstractmethod
    def retrieve(self) -> Any:
        ... # extended by subclasses


class ExampleKeygen(Keygen):
    """NOT SAFE FOR PRODUCTION CODE; FOR DEMONSTRATION PURPOSES ONLY"""

    # OVERRIDDEN METHODS : Keygen
    def retrieve(self) -> base64.urlsafe_b64decode:
        super().retrieve()
        return base64.urlsafe_b64decode(b'LVU5U3FPNDQyaDMwcUg3UENPOTBPVG1nWXBvUS1yd3JQNDczMHgxckNtcz0=')

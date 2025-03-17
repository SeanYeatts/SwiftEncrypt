SwiftEncrypt
============

*Copyright (c) 2025 Sean Yeatts. All rights reserved.*

A simple way to handle basic data encryption. Easily extendable to support custom encryption algorithms.


Key Features
------------
- Implements an intuitive, straightforward encryptor-keygen paradigm.


Quickstart
----------

**Example** - basic Fernet-style symmetrical encryption :

.. code:: python

    # IMPORTS
    from swiftencrypt import FernetCipher, ExampleKeygen


    # MAIN DEFINITION
    def main() -> None:

        # [1] Prepare some data
        original = b'test'

        # [2] Choose an encryption strategy
        keygen      = ExampleKeygen()
        encryptor   = FernetCipher(keygen)

        # [3] Perform encryption
        encrypted = encryptor.encrypt(original)

        # [4] ( DEBUG ) Verify the encryption ( for symmetrical strategies )
        decrypted = encryptor.decrypt(encrypted)

        print(original)
        print(encrypted)
        print(decrypted)


    # ENTRY POINT
    if __name__ == "__main__":
        main()


Installation
------------
**Prerequisites:**

- Python 3.8 or higher is recommended
- pip 24.0 or higher is recommended

**For a pip installation:**

Open a new Command Prompt. Run the following command:

.. code:: sh

  py -m pip install swiftencrypt

**For a local installation:**

Extract the contents of this module to a safe location. Open a new terminal and navigate to the top level directory of your project. Run the following command:

.. code:: sh

  py -m pip install "DIRECTORY_HERE\swiftserialize\dist\swiftencrypt-1.0.0.tar.gz"

- ``DIRECTORY_HERE`` should be replaced with the complete filepath to the folder where you saved the SwiftEncrypt module contents.
- Depending on the release of SwiftEncrypt you've chosen, you may have to change ``1.0.0`` to reflect your specific version.

 
"""AES CFB Stream Cipher Tool"""
 
from Crypto.Cipher import AES
from Crypto import Random
from argparse import ArgumentParser
import base64, sys
 
def main():
    # Set-up a command-line argument parser
    parser = ArgumentParser(description=__doc__, epilog="""Input is read from
        stdin and output is written to stdout. Use the stream redirection
        features of your shell to pass data through this program. If a key is
        not specified, it is generated and written to stderr.""")
    parser.add_argument('-d', '--decrypt', action='store_true')
    parser.add_argument('-k', '--key', metavar='key')
    args = parser.parse_args()
 
    # Decode the key if it was supplied
    key = base64.b64decode(args.key) if args.key else None
 
    # -- DECRYPT --
 
    if args.decrypt:
        # Check to see if a key was supplied
        if key is None:
            sys.stderr.write('Error: Please supply a decryption key.\n')
            exit(1)
 
        # Read in the initialization vector
        iv = sys.stdin.read(AES.block_size)
 
        # Create the cipher object and process the input stream
        cipher = AES.AESCipher(key, AES.MODE_CFB, iv)
        method = cipher.decrypt
 
        # Stream is processed below...
 
    # -- ENCRYPT --
 
    else:
        # Create a file object that produces random data when read from
        random = Random.new()
 
        # Generate a key if one was not supplied
        if key is None:
            key = random.read(AES.key_size[0])
            sys.stderr.write('Encryption Key: %s\n' % base64.b64encode(key))
 
        # Create the initialization vector
        iv = random.read(AES.block_size)
        sys.stdout.write(iv)
 
        # Create the cipher object and process the input stream
        cipher = AES.AESCipher(key, AES.MODE_CFB, iv)
        method = cipher.encrypt
 
        # Stream is processed below...
 
    # Process the input stream
    while True:
        data = sys.stdin.read(AES.block_size)
        if data == '': break # Check for EOF
        sys.stdout.write(method(data))
 
if __name__ == '__main__':
    main()

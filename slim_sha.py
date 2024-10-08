import sys

import hashlib

from enum import Enum

from colors import Color, color_reset

class HashType(Enum):
    SHA256 = 'sha256'
    SHA512 = 'sha512'

def get_hash(hash_type):
    if hash_type == HashType.SHA256:
        hash_obj = hashlib.sha256()
    elif hash_type == HashType.SHA512:
        hash_obj = hashlib.sha512()
    else:
        raise ValueError("Invalid hash type. Please choose 'sha256'or'sha512'")

    file_name = input("Enter the filename: ")
    try:
        with open(file_name,"rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_obj.update(byte_block)
        print(Color.DARKCYAN + f"{hash_type} value has been calculated")
        color_reset()
        get_hash.hash_digested = hash_obj.hexdigest()
        return get_hash.hash_digested
    except FileNotFoundError:
        print(f"File '{file_name}")

def which_hash():
    sha_type_input = input("Which hash do you want to calculate? sha256 OR sha512?  \n")

    try:
        sha_type = HashType(sha_type_input)
        get_hash(sha_type)
        verify_checksum()
    except ValueError:
        print("Type " + Color.UNDERLINE + "sha256" +  Color.END + " or " + Color.UNDERLINE + "sha512")

def verify_checksum():
    """Function for comparing calcuated hash with hash provided by developer"""
    given_checksum = input("Enter Checksum Provided by Authorized Distrubutor or Developer... \n")
    print(Color.PURPLE + "You entered: " + given_checksum + Color.END)
    print("Calculated : " + Color.GREEN + get_hash.hash_digested)
    if given_checksum == get_hash.hash_digested:
        safe_results()
    else:
        bad_results()

def safe_results():
    safe_result = (Color.BOLD + Color.GREEN + "Checksum Verfied! File is OK.")
    print(safe_result)
    color_reset()
    sys.exit()
def bad_results():
    bad_result = (Color.BOLD + Color.RED + "WARNING!!! Checksum is NOT verified. Verify checksum entry with the checuksum source. Verify correct file or package. This is a potentially harmful file or package! Do not proceed! Notify developer or distributor if correct software is being checked and teh calculated checksum continues to not match checksum from developer or distributor.")
    print(bad_result)
    color_reset()
    sys.exit()

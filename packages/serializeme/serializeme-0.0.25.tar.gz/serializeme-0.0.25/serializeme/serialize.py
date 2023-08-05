"""
Serialize object that can encode data into a byte array.
"""
# Author: Justin Roosenschoon <jeroosenschoon@gmail.com>

# Licence: MIT License (c) 2021 Justin Roosenschoon

import re
from math import ceil
from socket import inet_aton
from serializeme.field import Field

# Constants representing various ways to handle variable-length data.
NULL_TERMINATE = "null_terminate"  # Data + byte of zeros
PREFIX_LENGTH = "prefix_length"  # Length of data (in bytes) + Data
# Length of data (in bytes) + Data + bytes of zeros
PREFIX_LEN_NULL_TERM = "prefix_len_null_term"
IPv4 = "ipv4"
VAR_PREFIXES = [NULL_TERMINATE, PREFIX_LENGTH, PREFIX_LEN_NULL_TERM]


class Serialize:
    """
    Serialize object that can encode data into a byte array. This allows users to enter values and the desired size (in
    bits or bytes), and the Serialize object will automatically handle the conversion of these values to a byte array.
    Serialize also supports variable-length data by one of the above constants.
    Parameters
    ----------
    :param data: dictionary
        The data to be converted to a byte array. The dictionary key-value pairs are of the form field_name: size/value
        size/vlaue has a variety of options we can specify:
            - (a, b): 2-tuple of integers where a is the number of bits, and b is the value.
            - (a, b): 2-tuple of a string and integer where a (the string) is of the form "xb" for x-bits or "xB" for
                      x-bytes, and b is an integer representing the value of the field.
            - (a, b): 2-tuple of constant (from above) and list of strings will operate on each string in a way dictated
                      by the constant specified.
            - a: int specifying the number of zero-bits the field is.
            - a: str where a (the string) is of the form "xb" for the number of zero x-bits or "xB" for the number of
                  zero x-bytes
        If any of the values cannot be held in the specified number of bits or bytes, an exception will be thrown.

    Attributes
    ----------
    fields: list of Field objects representing the Fields that were generated by the dictionary.

    """

    def __init__(self, data):
        self.data = data

        self.fields = []

        self.__extract_fields()


    def packetize(self):
        """
        Generate a byte string from the list of fields in the object.
        :return: A byte string of the fields.
        """
        byte_str = b''

        # Bit string to accumulate bit values until we are ready to convert it into bytes
        bit_str = ""

        for field in self.fields:
            #if the current field is a special type, the bit_str value to the byte string and clear the accumulated bit_str.
            if not isinstance(field.size, int) and len(bit_str) != 0:
                byte_str += self.encode_bit_str(bit_str)
                bit_str = ""
            if field.size == NULL_TERMINATE:
                byte_str += self.encode_null_term(field.value)
            elif field.size == PREFIX_LENGTH:
                byte_str += self.encode_prefix_length(field.value)
            elif field.size == PREFIX_LEN_NULL_TERM:
                byte_str += self.encode_prefix_length_null_term(field.value)
            elif field.size == IPv4:
                byte_str += self.encode_ipv4(field.value)
            elif field.size == 1:  # One bit, just add it to our bit string.
                bit_str += "0" if field.value == 0 else "1"
            else:
                if isinstance(field.value, int):
                        bit_str += "0" * (field.size - len(bin(field.value)[2:])) + bin(field.value)[2:]
                elif isinstance(field.value, bytes):
                        bit_str += field.value.decode('latin-1')
        #clear the bit string one last time
        if len(bit_str) != 0:
            byte_str += self.encode_bit_str(bit_str)
            bit_str = ""

        return byte_str

    def encode_bit_str(self, input):
        """
        Helper function to turn a bit string to a byte string. If the bit string length is not divisible by 8, it is padded with zeroes before conversion.
        :param input: The bit string
        :return: The byte string equivalent.
        """
        byte_len = ceil(len(input) / 8)
        byte_ouput = int(input, 2).to_bytes(byte_len, "big")
        return byte_ouput

    def encode_prefix_length_null_term(self, input):
        """
        Helper function to encode a string/list of string into a prefix length format with a null terminator
        :param input: a string or a list of string
        :return: The byte string equivalent.
        """
        return self.encode_prefix_length(input) + b'\x00'

    def encode_null_term(self, input):
        """
        Helper function to encode a string with a null terminator added
        :param input: a string
        :return: The byte string equivalent, with a null character at the end.
        """
        return input.encode() + b'\x00'

    def encode_prefix_length(self, input):
        """
        Helper function to encode a string/list of string into a prefix length format
        :param input: a string or a list of string
        :return: The byte string equivalent.
        """
        if isinstance(input, str):
            return len(input).to_bytes(1, "big") + input.encode()
        else :
            byte_str = b''
            for part in input:
                byte_str += len(part).to_bytes(1, "big") + part.encode()
            return byte_str

    def encode_ipv4(self, input):
        """
        Helper function to encode an IPv4 string into a byte string
        :param input: an IPv4 string
        :return: The byte string equivalent.
        """
        return inet_aton(input)

    def get_field(self, field_name):
        """
        Get a specified field from the fields list, or return None if specified field does not exist.
        :param field_name: The name of the desired field to find.
        :return: Field: Field object with the specified name.
        """
        for f in self.fields:
            if f.name.lower() == field_name.lower():
                return f
        return None

    # Helper
    def __check_bit_size(self, value, num_bits):
        """
        Helper function to check if the specified value can fit in the specified number of bits.
        :param value: The value trying to fit in num_bits
        :param num_bits: The number of bits we want to see if value can fit in.
        :return: True if value can fit in num_bits number of bits. False otherwise.
        """
        is_fit = False
        if value <= 2 ** num_bits - 1:
            is_fit = True
        return is_fit

    # Helper
    def __extract_fields(self):
        """
        Helper function to parse the user-specified dictionary of fields upon creation of Serialize object.
        """
        for name, stuff in self.data.items():
            if stuff == ():  # Empty tuple == 1 bit, value of 0
                self.fields.append(Field(name=name, value=0, size=1))
            elif isinstance(stuff, int):  # int == specified value, value of 0
                self.fields.append(Field(name=name, value=0, size=stuff))
            elif isinstance(stuff, str):  # str == specified value, value of 0
                pattern = re.compile("[0-9]+[bB]")
                if pattern.match(stuff):
                    if "b" in stuff: # bits specified
                        size = int(stuff[:stuff.lower().index("b")])
                        self.fields.append(Field(name=name, value=0, size=size))
                    elif "B" in stuff: # Bytes specified
                        size = int(stuff[:stuff.lower().index("b")]) * 8
                        self.fields.append(Field(name=name, value=0, size=size))
                else: # No other string option, so must have been one of the "vary" constants from above.
                    self.fields.append(Field(name=name, value=stuff, size="vary"))
            elif isinstance(stuff, tuple) or isinstance(stuff, list):  # specified value and size.
                if isinstance(stuff[0], str):
                    if "b" in stuff[0]: # Bits
                        size = int(stuff[0][:stuff[0].lower().index("b")])
                       # if not self.__check_bit_size(stuff[1], size):
                        #    raise Exception("error. " + str(stuff[1]) + " cannot be fit in " + str(size) + " bits.")
                        self.fields.append(Field(name=name, value=stuff[1], size=size))
                    elif "B" in stuff[0]: # Bytes
                        size = int(stuff[0][:stuff[0].lower().index("b")]) * 8
                       # if not self.__check_bit_size(stuff[1], size):
                         #   raise Exception("error. " + str(stuff[1]) + " cannot be fit in " + str(size) + " bits.")
                        self.fields.append(Field(name=name, value=stuff[1], size=size))
                    elif stuff[0].lower() == NULL_TERMINATE:
                        self.fields.append(Field(name=name, value=stuff[1], size=NULL_TERMINATE))
                    elif stuff[0].lower() == PREFIX_LENGTH:
                        self.fields.append(Field(name=name, value=stuff[1], size=PREFIX_LENGTH))
                    elif stuff[0].lower() == PREFIX_LEN_NULL_TERM:
                        self.fields.append(Field(name=name, value=stuff[1], size=PREFIX_LEN_NULL_TERM))
                    elif stuff[0].lower() == IPv4:
                        self.fields.append(Field(name=name, value=stuff[1], size=IPv4))
                elif isinstance(stuff[0], int):
                   # if not self.__check_bit_size(stuff[1], stuff[0]):
                     #   raise Exception("error. " + str(stuff[1]) + " cannot be fit in " + str(stuff[0]) + " bits.")
                    self.fields.append(Field(name=name, value=stuff[1], size=stuff[0]))

    def __str__(self):
        """
        Generate a string representation of the Serialize object by listing out all of the fields, their value,
        and their sizes.
        :return: A string representation of the Serialize object.
        """
        s = ""
        for field in self.fields:
            if field.size not in VAR_PREFIXES:
                s += field.name + ": " + str(field.size) + " bits with value " + str(field.value) + ".\n"
            else:
                s += field.name + ": variable size: " + str(field.size) + ", with value " + str(field.value) + ".\n"

        return s
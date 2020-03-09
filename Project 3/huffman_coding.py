"""Huffman Coding
CPE202

Author:
    Put your name here
"""
from huffman import HuffmanNode
from min_pq import MinPQ

def cnt_freq(filename):
    """returns a Python list of 256 integers the frequencies of characters in file
    """
    pass

def create_huff_tree(list_of_freqs):
    """returns the root node of a Huffman Tree
    """
    pass

def create_code(root_node):
    """returns a Python list of 256 strings representing the code
    Return an array of size 256 whose idex corresponds to ascii code of a letter.
    """
    pass

def huffman_encode(in_file, out_file):
    """encodes in_file and writes the it to out_file
    This function calls cnt_freq, create_huff_tree, and create_code functions.
    """
    pass

def huffman_decode(list_of_freqs, encoded_file, decode_file):
    """decode encoded_file and write the decoded text to decode_file.
    This function calls create_huff_tree function.
    It is recommended to write a helper function which traverse the tree and
    find a character mapped to a code or None if the code does not map to any character.
    """
    pass


"""HuffmanNode
CPE202

Author:
    Put your name here
"""
class HuffmanNode:
    """Write docstring for this class
    """
    def __init__(self, frequency, char=None, left=None, right=None):
        self.freq = frequency
        self.char = char
        self.left = left
        self.right = right

    def __eq__(self, other):
        pass

    def __repr__(self):
        pass

    def __lt__(self, other):
        """Implementing this function let you compare two HuffmanNode objects
         with < in your program
        Args:
            other (HuffmanNode): other HUffmanNode object to be compared with self
        Returns:
            True if self <= other, else return False
        """
        pass



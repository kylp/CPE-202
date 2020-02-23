"""Contains starter code for lab 5

CPE202

Instructions:
    Complete this file by writing python3 code.

"""
import random

#implement BSTNode class and get,contains,insert,delete functions in bst.py
import bst_rev as bst

#classmate.py is implemented for you
from classmate import classmate_factory 


class TreeMap:
    """Write the docstring
    """
    def __init__(self):
        self.tree = None
        self.num_items = 0

    def __repr__(self):
        return 'TreeMap (%s, %d)' % (repr(self.tree), self.num_items)

    def __eq__(self, other):
        return isinstance(other, TreeMap) and self.tree == other.tree and self.num_items == other.num_items

    def __getitem__(self, key):
        """implementing this method enables getting an item with [] notation
        This function calls your get method.

        Args:
            key (any) : a key which is compareable by <,>,==
        Returns:
            any : the value associated with the key
        Raises:
            KeyError : it raises KeyError because the get function in bst.py raises the error.
        """
        return self.get(key)

    def __setitem__(self, key, val):
        """implementing this method enables setting a key value pair with [] notation
        This function calls your put method.

        Args:
            key (any) : a key which is compareable by <,>,==
            val (any): the value associated with the key
        """
        self.put(key, val)

    def __contains__(self, key):
        """implementing this method enables checking if a key exists with in notaion

        Args:
            key (any) : a key which is comparable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False 
        """
        return self.contains(key)

    def put(self, key, val):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (any) : a key which is comparable by <,>,==
            val (any): the value associated with the key
        """
        #this method is already written for you
        self.tree = bst.insert(self.tree, key, val)
        self.num_items += 1

    def get(self, key):
        """put a key value pair into the map
        Calls insert function in bst.py

        Args:
            key (any) : a key which is comparable by <,>,==
        Returns:
            any : the value associated with th key
        Raises:
            KeyError : if the key does not exist
        """
        #this method is already written for you
        return bst.get(self.tree, key)

    def contains(self, key):
        """Write the docstring
        Args:
            key (any) : a key which is comparable by <,>,==
        Returns:
            bool : True is the key exists, otherwise False 
        """
        #call a function in the bst module
        return bst.contains(self.tree, key)

    def delete(self, key):
        """Write the docstring
        Args:
            key (any) : a key which is comparable by <,>,==
        Raises:
            KeyError : if the key does not exist
        """
        #call a function in the bst module
        #and decrement the num_items
        return bst.delete(self.tree, key)

    def size(self):
        """returns the number of items in the map
        Returns:
            int : the number of items in the map
        """
        return self.num_items

    def find_min(self):
        """returns the minimum key and the value associated
        Returns:
            any: minimum key
            any: value at the aforementioned key
        """
        #---- to do ----
        # complete this method by calling bst.find_min()
        # return the key and the value associated with the smallest key in the tree
        # raise ValueError if the tree is empty
        #---------------
        return bst.find_min(self.tree)

    def find_max(self):
        """returns the maximum key and the value associated
        Returns:
            any: max key
            any: value at the aforementioned key
        """
        #---- to do ----
        # complete this method by calling bst.find_max()
        # return the key and the value associated with the largest key in the tree 
        # raise ValueError if the tree is empty
        #---------------
        return bst.find_max(self.tree)

    def inorder_list(self):
        """returns a list of keys representing in-order traversal of tree(bst)
        Returns:
            list: a list of keys from inorder traversal of the tree
        """
        #---- to do ----
        # complete this method by calling bst.inorder_list()
        # return a list of BST keys representing ineorder traversal of BST
        #---------------
        return bst.inorder_list(self.tree)

    def preorder_list(self):
        """returns a list of keys representing pre-order traversal of tree(bst)
        Returns:
            list: a list of keys from pre-order traversal of the tree
        """
        #---- to do ----
        # complete this method by calling bst.preorder_list()
        # return a list of BST keys representing preorder traversal of BST
        #---------------
        return bst.preorder_list(self.tree)

    def tree_height(self):
        """returns the height of the tree or -1 if the tree is empty
        Returns:
            int: the height of the tree
        """
        #---- to do ----
        # complete this method by calling bst.tree_height()
        # return the height of the tree
        # return -1 if the tree is empty
        #---------------
        return bst.tree_height(self.tree)

    def range_search(self, lo, hi):
        """returns a list of values that are within the given range
        Args:
            lo(int): lower limit of range
            hi(int) higher limit of range
        Returns:
            list: the list of values within lo and hi
        """
        #---- to do ----
        # complete this method by calling bst.range_search()
        # return a list of values that fall within the given range
        #---------------
        return bst.range_search(self.tree, lo, hi)


def import_classmates(filename):
    """Imports classmates from a tsv file

    Design Recipe step 4 (Templating) is doen for you.
    Complete this function by following the template.

    Args:
        filename (str) : the file name of a tsv file containing classmates

    Returns:
        TreeMap : return an object of TreeMap containing classmates.
    """
    #create an object of TreeMap
    tree_map = TreeMap()
    #create an empty list for classmates
    classmates = []
    #---- to do ----
    # complete this function by following the comments below
    #
    #open the file whose name is passed as the argument filename
    # with python builtin open() function.
    #read all lines in the file and assign it to variable lines
    #for each line in lines
        #split the line at tabs (\t) and assign it to a variable tokens
        #classmate = classmate_factory(tokens)
        #append the classmate to a list classmates
    #---------- ----
    with open(filename) as file:
        lines = file.readlines()


    classmate = classmate_factory(tokens)

    #shuffle the classmates
    random.seed(2)
    random.shuffle(classmates)

    #---- to do ----
    # complete this function by following the comments below
    #
    #for each classmate in classmates
        #put the classmate into the tree_map using its sid as the key
    #---------- ----
    return tree_map

def search_classmate(tmap, sid):
    """Searches a classmate in a TreeMap using the sid as a key

    Args:
        tmap (TreeMap) : an object of TreeMap
        sid (int) : the id of a classmate
    Returns:
        Classmate : a Classmate object
    Raises:
        KeyError : if a classmate with the id does not exist
    """
    if sid in tmap:
        return tmap[sid]
    else:
        raise KeyError("A classmate with the id: %d does not exist!" % (sid)) 



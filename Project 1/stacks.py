"""Contains code for StackADTs
CPE202
Project 1

Author:
    Jae Park
"""
import array_list
import linked_list


class StackArray:
    """Stack using array list
    Attributes:
        arr_list (ArrayList) : An array
        num_items (int) : number of items
    """

    def __init__(self):
        self.arr_list = array_list.ArrayList()  # importing from lab 2
        self.num_items = 0  # new instance for new class, num_items contains 0 initially

    def __repr__(self):
        return 'StackArray(%s, %d)' % (repr(self.arr_list), self.num_items)  # string representation of an instance

    def __eq__(self, other):
        return isinstance(other, StackArray) and other.arr_list == self.arr_list and other.num_items == self.num_items

    def is_empty(self):
        """ Checks if the stack array is empty
        Args:
        Returns:
            bool: True if empty, False if not.
        """
        if self.num_items == 0:
            return True
        return False

    def push(self, item):
        """ Pushes item onto top of the stack
        Args:
            item(object): item to be placed onto stack
        Returns:
        """
        self.arr_list = array_list.insert(self.arr_list, item, self.num_items)
        self.num_items += 1

    def pop(self):
        """ Removes and returns item at the top of stack
        Args:
        Returns:
            object: item at top of stack
        Raises:
            IndexError if stack is empty
        """
        self.arr_list, temp = array_list.pop(self.arr_list, self.num_items - 1)
        self.num_items -= 1
        return temp

    def peek(self):
        """ Returns value at top of stack without removing
        Args:
        Returns:
            object: item at top of stack
        Raises:
            IndexError if stack is empty
        """
        return array_list.get(self.arr_list, self.num_items - 1)

    def size(self):
        """ Returns size of stack
        Args:
        Returns:
            int: size of stack
        """
        return self.num_items


class StackLinked:
    """Stack using linked list
    Attributes:
        top (Node) : a linked list
        num_items (int) : number of items
    """

    def __init__(self):
        self.top = None
        self.num_items = 0

    def __repr__(self):
        return 'StackLinked(%s, %d)' % (repr(self.top), self.num_items)  # string representation of an instance

    def __eq__(self, other):
        return isinstance(other, StackLinked) and other.top == self.top and other.num_items == self.num_items

    def is_empty(self):
        """ Checks if the stack is empty
        Args:
        Returns:
            bool: True if empty, False if not.
        """
        if self.num_items == 0:
            return True
        return False

    def push(self, item):
        """ Pushes item onto top of the stack
        Args:
            item(object): item to be placed onto stack
        Returns:
        """
        self.top = linked_list.insert(self.top, item, 0)
        self.num_items += 1

    def pop(self):
        """ Removes and returns item at the top of stack
        Args:
        Returns:
            object: item at top of stack
        Raises:
            IndexError if stack is empty
        """
        self.top, temp = linked_list.pop(self.top, 0)
        self.num_items -= 1
        return temp

    def peek(self):
        """ Returns value at top of stack without removing
        Args:
        Returns:
            object: item at top of stack
        Raises:
            IndexError if stack is empty
        """
        return linked_list.get(self.top, 0)

    def size(self):
        """ Returns size of stack
        Args:
        Returns:
            int: size of stack
        """
        return self.num_items

"""Jae Park CPe 202 Lab 4 Ordered List
"""


class Node:
    """ A node of a list
    Attributes:
        val (int): the payload
        next (Node): the next item in the list
        prev (Node): the previous item in the list
    """

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return 'Node(%d, %s, %s)' % (self.val, repr(self.next), repr(self.prev))

    def __eq__(self, other):
        return isinstance(other, Node) and other.val == self.val and other.next == self.next and other.prev == self.prev


class OrderedList:
    """an ordered list
    Attributes:
        head (Node): a pointer to the head of the list
        tail (Node): a pointer to the tail of the list
        num_items (int): the number of items stored in the list
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_items = 0

    def __eq__(self, other):
        return isinstance(other, OrderedList) \
               and other.head == self.head \
               and other.tail == self.tail \
               and other.num_items == self.num_items

    def __repr__(self):
        return 'OrderedList(%s, %s, %d)' % (repr(self.head), repr(self.tail), self.num_items)

    def add(self, item):
        """adds a specified value as an item in the list while maintaining ascending order.
        Args:
            item (int): a value to be added as an item in the list
        """
        if self.num_items == 0:
            self.head = Node(item, None, None)
            self.tail = self.head
            self.num_items += 1
            return
        if self.head.val >= item:
            temp = self.head
            self.head = Node(item, temp, None)
            temp.prev = self.head
            self.num_items += 1
            return
        if self.tail.val < item:
            temp = self.tail
            self.tail = Node(item, None, temp)
            temp.next = self.tail
            self.num_items += 1
            return
        temp = self.head
        while temp.val < item:
            temp = temp.next
        new_node = Node(item, temp, temp.prev)
        temp.prev.next = new_node
        temp.prev = new_node
        self.num_items += 1

        pass

    def remove(self, item):
        """removes the first occurrence of a specified value in the list while maintaining ascending order.
        Args:
            item (int): a value to be removed
        Returns:
            int: the position where the item removed
        Raises:
            ValueError: when the item is not found in the list
        """
        if self.num_items == 0:
            raise IndexError()
        if self.head.val > item:
            raise ValueError()
        if self.tail.val < item:
            raise ValueError()
        if self.head.val == item:
            if self.num_items == 1:
                self.tail = None
                self.head = None
                self.num_items = 0
                return 0
            self.head = self.head.next
            self.head.prev = None
            self.num_items -= 1
            return 0
        temp = self.head
        idx = 0
        while temp.val != item:
            temp = temp.next
            idx += 1
        if temp is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            self.num_items -= 1
            return idx
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.num_items -= 1
        return idx

    def search_forward(self, item):
        """searches a specified item in the list starting from the head.
        Args:
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        temp = self.head
        while temp is not None and temp.val != item:
            temp = temp.next
        if temp is None:
            return False
        return True

    def search_backward(self, item):
        """searches a specified item in the list backward starting from the tail.
        Args:
            item (int): the value to be searched in the list
        Returns:
            bool: True if found, False otherwise.
        """
        temp = self.tail
        while temp is not None and temp.val != item:
            temp = temp.prev
        if temp is None:
            return False
        return True

    def is_empty(self):
        """checks if the list is empty.
        Returns:
            bool: True if it is empty, False otherwise.
        """
        if self.num_items == 0:
            return True
        return False

    def size(self):
        """gets the number of items stored in the list.
        Returns:
            int: the number of items in the list.
        """
        return self.num_items

    def index(self, item):
        """gets the position of the first occurrence of a specified item in the list.
        Args:
            item (int): the value to be found
        Returns:
            int: the position in the list
        Raises:
            LookupError: if the value is not found in the list
        """
        temp = self.head
        idx = 0
        while temp is not None and temp.val != item:
            temp = temp.next
            idx += 1
        if temp is None:
            raise LookupError()
        return idx

    def pop(self, pos=None):
        """removes the item at a specified position and returns its value.
        The last item in the list is removed if the argument is not passed.
        Args:
            pos (int): the position of the item to be removed. The default value is None
        Returns:
            int: the value of the item that is removed
        Raises:
            IndexError: if the position is out of bound
        """
        if pos is None:
            pos = self.num_items-1
        if self.num_items == 0 or pos < 0 or pos >= self.num_items:
            raise IndexError()
        if pos == 0:
            temp = self.head.val
            if self.num_items == 1:
                self.tail = None
                self.head = None
                self.num_items = 0
                return temp
            self.head = self.head.next
            self.head.prev = None
            self.num_items -= 1
            return temp
        temp = self.head
        idx = 0
        while idx != pos:
            temp = temp.next
            idx += 1
        if temp is self.tail:
            val = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            self.num_items -= 1
            return val
        val = temp.val
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        self.num_items -= 1
        return val

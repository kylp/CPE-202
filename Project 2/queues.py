"""Starter code for Lab 3
CPE202

Replace this doc string with your information.
All classes/methods/functions also need doc strings.
"""
from linked_list import Node


class QueueArray: 
    def __init__(self, capacity): 
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.items = [None] * (capacity + 1)
        self.num_items = 0

    def __repr__(self):
        return 'QueueArray(%d, %s, %d)' % (self.capacity, self.items, self.num_items)

    def __eq__(self, other):
        return isinstance(other, QueueArray) and other.capacity == self.capacity and other.front == self.front and \
               other.rear == self.rear and other.items == self.items and other.num_items == self.num_items

    def is_empty(self):
        """
        Checks if the queue is empty
        Args:
            self(list)
        Returns:
            Bool- True if true False if false
        """
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """
        Checks if queue is full
        Args:
            self(list)
        Returns:
            Bool- True if true False if false
        """
        if self.num_items == self.capacity:
            return True
        return False


    def enqueue(self, item):
        """enqueues an item to the rear of the queue
        Args:
            self (list)
            item (int): item to be inserted to the rear of queue
        """
        if self.is_full():
            raise IndexError()
        self.items[self.rear] = item
        self.rear += 1
        self.rear %= self.capacity + 1
        self.num_items += 1

    def dequeue(self):
        """dequeues the item at the front of the list and returns its value
        Args:
            self (list)
        Returns:
            int: value of the front of the list
        """
        if self.is_empty():
            raise IndexError()
        temp = self.items[self.front]
        # self.items[self.front] = None
        self.front += 1
        self.front %= self.capacity + 1
        self.num_items -= 1
        return temp

    #returns the number of items in the queue
    def size(self):
        """Returns the size of the queue array
        Args:
            self(list)
        Returns:
            int: size of list
        """
        return self.num_items

#You must have the same functionalities for the Linked List Implementation
class QueueLinked: 
    def __init__(self, capacity):
        """Checks if the queue is empty
            Args:
                self(Node)
            Returns:
                Bool- True if true False if false
        """
        #the maximum number of items that can be stored in queue
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.num_items = 0

    def __repr__(self):
        return 'QueueLinked(%d, %s, %d)' % (self.capacity, self.front, self.num_items)

    def __eq__(self, other):
        return isinstance(other, QueueLinked) and other.capacity == self.capacity and other.front == self.front and \
               other.rear == self.rear and other.num_items == self.num_items

    def is_empty(self):
        """
        Checks if the queue is empty
        Args:
            self(Node)
        Returns:
            Bool- True if true False if false
        """
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """
        Checks if queue is full
        Args:
            self(Node)
        Returns:
            Bool- True if true False if false
        """
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        """enqueues an item to the rear of the queue
        Args:
            self (Node)
            item (int): item to be inserted to the rear of queue
        """
        if self.is_full():
            raise IndexError()
        temp = self.rear
        self.rear = Node(item, None)
        if temp is None:
            self.front = self.rear
        else:
            temp.next = self.rear
        self.num_items += 1

    def dequeue(self):
        """dequeues the item at the front of the list and returns its value
        Args:
            self (Node)
        Returns:
            int: value of the front of the list
        """
        temp = self.front
        if self.front is None:
            raise IndexError()
        if self.front is self.rear:
            self.rear = None
        self.front = temp.next
        self.num_items -= 1
        return temp.val

    def size(self):
        """Returns the size of the queue array
        Args:
            self(Node)
        Returns:
            int: size of list
        """
        return self.num_items



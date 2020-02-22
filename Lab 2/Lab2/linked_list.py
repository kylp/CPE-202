# add your module doc integer, including your name, here.


class Node:
    """Linked List is one of None or Node
    Attributes:
        val (int): an item in the list
        next (Node): a link to the next item in the list (Linked List)
    """

    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return 'Node {{ v={}, n={:!r} }}'.format(self.val, self.nxt)

    def __eq__(self, other):
        pass


def insert(lst, val, pos):
    """inserts the integer at the position pos in the linked list recursively.
    Args:
        lst (Node): the list
        val (int): the value to be inserted in the list
        pos (int): the position
    Returns:
        Node: the head of a LinkedList
    Raises:
        IndexError: when the position is out of bound ( > num_items).
    """
    if pos == 0:
        return Node(val, lst)

    if lst is None:
        raise IndexError()

    return Node(lst.val, insert(lst.nxt, val, pos - 1))


def get(lst, pos):
    """gets an item stored at the specified position recursively.
    Args:
        lst (Node): a head of linked list
        pos (int): the specified position
    Returns:
        int: the value of the item at the position pos.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if lst is None:
        raise IndexError()
    if pos == 0:
        return lst.val
    return get(lst.nxt, pos - 1)


def search(lst, val):
    """searches for a specified value in a given list.
    Args:
        lst (Node): an object of Node (LinkedList)
        val (int): a value to search for
    Returns:
        int: the position where the value is stored in the list. It returns None if the value is not found.
    """
    if lst is None:
        return None

    if lst.val == val:
        return 0

    temp = search(lst.nxt, val)

    if temp is None:
        return None
    else:
        return temp + 1


def contains(lst, val):
    """checks if a specified value exists in a given list.
    This function calls search function.
    Args:
        lst (Node): the head of a LinkedList
        val (int): a value to search for
    Returns:
        bool: True if the value is found or False if not.
    """
    if lst is None:
        return False

    if lst.val == val:
        return True

    return contains(lst.nxt, val)


def remove(lst, val):
    """removes the first occurrence of a specified value in a given list recursively.
    Args:
        lst (Node): the head of a LinkedList
        val (int): a value to be removed
    Returns:
        Node: the head of the linked list with the first occurrence of the value removed.
    """
    if lst is None:
        return None
    if lst.val == val:
        return lst.nxt
    return Node(lst.val, remove(lst.nxt, val))


def pop(lst, pos):
    """removes the item at a specified position in a given list recursively
    Args:
        lst (Node): the head of a LinkedList
        pos (int): the position in the list where an item is removed
    Returns:
        Node: the head of the LinkedList with the item removed
        int: the removed item’s value.
    Raises:
        IndexError: when the position is out of bound ( >= num_items).
    """
    if lst is None:
        raise IndexError()

    if pos == 0:
        return lst.nxt, lst.val

    temp_1, temp_2 = pop(lst.nxt, pos - 1)

    return Node(lst.val, temp_1), temp_2



def size(lst):
    """returns the number of items stored in the LinkedList recursively.
    Args:
        lst (Node): the head of a LinkedList
    Returns:
        int: the number of items stored in the list
    """
    if lst is None:
        return 0

    return size(lst.nxt) + 1

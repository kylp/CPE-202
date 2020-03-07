from linked_list import *


class KeyVal:
    def __init__(self, key, val):
        self.key = key
        self.val = val


def hash_string(string, size):
    hash = 0
    for c in string:
        hash = (hash * 31 + ord(c)) % size
    return hash


class HashTableSepchain:
    """
    Args:

    Returns:

    """

    def __init__(self, table_size = 11):
        self.array = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.collision_count = 0

    def put(self, key, val):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            self.array[key_hash] = Node(KeyVal(key, val))
            self.num_items += 1
            if self.load_factor() > 1.5:
                self.resize(2 * self.table_size + 1)
            return
        self.collision_count += 1
        if self.array[key_hash].val.key == key:
            self.array[key_hash].val.val = val
            return
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                temp.next.val.val = val
                return
            temp = temp.next
        self.num_items += 1
        temp.next = Node(KeyVal(key, val))
        if self.load_factor() > 1.5:
            self.resize(2 * self.table_size + 1)

    def get(self, key):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            raise KeyError()
        if self.array[key_hash].val.key == key:
            return self.array[key_hash].val.val
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                return temp.next.val.val
            temp = temp.next
        raise KeyError()

    def contains(self, key):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            return False
        if self.array[key_hash].val.key == key:
            return True
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                return True
            temp = temp.next
        return False

    def remove(self, key):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            raise KeyError()
        if self.array[key_hash].val.key == key:
            temp = self.array[key_hash]
            self.array[key_hash] = self.array[key_hash].next
            self.num_items -= 1
            return temp
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                stress = temp.next
                temp.next = temp.next.next
                self.num_items -= 1
                return stress
            temp = temp.next
        raise KeyError()

    def resize(self, new_size):
        old_array = self.array
        old_size = self.table_size
        self.array = [None] * new_size
        self.table_size = new_size
        self.num_items = 0
        for i in range(old_size):
            temp = old_array[i]
            while temp is not None:
                self.put(temp.val.key, temp.val.val)
                temp = temp.next

    def size(self):
        return self.num_items

    def load_factor(self):
        return self.num_items / self.table_size

    def collisions(self):
        return self.collision_count

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)

    def __contains__(self, key):
        return self.contains(key)

class HashTableSepchain:
    """
    Args:

    Returns:

    """

    def __init__(self, table_size = 11):
        self.array = [None] * table_size
        self.table_size = table_size
        self.num_items = 0
        self.collision_count = 0

    def put(self, key, val):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            self.array[key_hash] = Node(KeyVal(key, val))
            self.num_items += 1
            if self.load_factor() > 1.5:
                self.resize(2 * self.table_size + 1)
            return
        self.collision_count += 1
        if self.array[key_hash].val.key == key:
            self.array[key_hash].val.val = val
            return
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                temp.next.val.val = val
                return
            temp = temp.next
        self.num_items += 1
        temp.next = Node(KeyVal(key, val))
        if self.load_factor() > 1.5:
            self.resize(2 * self.table_size + 1)

    def get(self, key):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            raise KeyError()
        if self.array[key_hash].val.key == key:
            return self.array[key_hash].val.val
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                return temp.next.val.val
            temp = temp.next
        raise KeyError()

    def contains(self, key):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            return False
        if self.array[key_hash].val.key == key:
            return True
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                return True
            temp = temp.next
        return False

    def remove(self, key):
        key_hash = hash_string(key, self.table_size)
        if self.array[key_hash] is None:
            raise KeyError()
        if self.array[key_hash].val.key == key:
            temp = self.array[key_hash]
            self.array[key_hash] = self.array[key_hash].next
            self.num_items -= 1
            return temp
        temp = self.array[key_hash]
        while temp.next is not None:
            if temp.next.val.key == key:
                stress = temp.next
                temp.next = temp.next.next
                self.num_items -= 1
                return stress
            temp = temp.next
        raise KeyError()

    def resize(self, new_size):
        old_array = self.array
        old_size = self.table_size
        self.array = [None] * new_size
        self.table_size = new_size
        self.num_items = 0
        for i in range(old_size):
            temp = old_array[i]
            while temp is not None:
                self.put(temp.val.key, temp.val.val)
                temp = temp.next

    def size(self):
        return self.num_items

    def load_factor(self):
        return self.num_items / self.table_size

    def collisions(self):
        return self.collision_count

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)

    def __contains__(self, key):
        return self.contains(key)

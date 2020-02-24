class MaxPQ:
    """
   Author: Aidan Chandrasekaran
   max heap class, max heap implemented with binary tree structure in array
   """

    def __init__(self, arr=None):
        if arr:
            self.capacity = len(arr)
            self.num_items = len(arr)
            self.arr = arr
            self.count = self.heapify(self.arr)
        else:
            self.capacity = 2
            self.arr = [None] * self.capacity
            self.num_items = 0

    def __repr__(self):
        return str(self.arr)

    def __eq__(self, other):
        return self.arr == other.arr

    def heapify(self, arr):
        """
       author: aidan chandrasekaran
       initialize the queue with a given array and convert the array into a max heap
       Args:
       arr (list): an array
       Returns:
       None : it returns nothing
       """
        counter = 0
        for i in range((len(arr) - 1) // 2, -1, -1):
            counter += self.shift_down(i)
        return counter

    def shift_down(self, idx):
        """
       Author: Aidan chandrasekaran
       shifts down an item in the queue using tail recursion.
       Use only < operator to compare two items: do not use <=, >, >=.
       YOU NEED TO DETERMINE WHERE THE END OF THE HEAP IS.
       YOU CAN USE self.num_items FOR DOING SO.
       Args:
       idx (int): the index of the item to be shifted down in the array.
       Returns:
       None : it returns nothing
       """
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left >= self.num_items or right >= self.num_items:
            return 1
        if self.arr[idx] < self.arr[left] and self.arr[left] >= self.arr[right]:
            tmp = self.arr[idx]
            self.arr[idx] = self.arr[left]
            self.arr[left] = tmp
            return 1 + self.shift_down(left)
        if self.arr[idx] < self.arr[right]:
            tmp = self.arr[idx]
            self.arr[idx] = self.arr[right]
            self.arr[right] = tmp
            return 1 + self.shift_down(right)
        return 1

    def dequeue(self):
        """
       Author: Aidan chandrasekaran
       dequeues the maximum item in the queue
       Returns:
           any : it returns the maximum item, which has just been deleted
       """
        return_val = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.num_items -= 1
        counter = self.shift_down(0)
        return return_val, counter

    def heap_sort(self):
        """
       Author: Aidan Chandrasekaran
       :return: (int) count of compares
       """
        counter = 0
        while self.num_items > 1:
            new_sorted_bound = self.num_items - 1
            self.arr[new_sorted_bound], update = self.dequeue()
            counter += update
        return counter

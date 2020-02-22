"""LAB1
CPE202
"""


# 1
def get_max(nums):
    """Gets the max value inside a list
    Args:
        nums(list): a list of integers
    Returns:
        int : maximum value or None if empty
    """
    if len(nums) == 0:
        return None

    temp = nums[0]
    i = 1
    while i < len(nums):
        if temp < nums[i]:
            temp = nums[i]
        i += 1
    return temp


# 2
def reverse(string):
    """ Reverses a string
    Args:
        string(string): a string of characters
    Returns:
        string : reversed string
    """
    length = len(string)
    if length > 0:
        return string[length - 1] + reverse(string[0:length - 1])

    return ""


# 3
def search(nums, target):
    """ Searches a list of integers for the target value and returns its index.
        If the target is not present, returns None. The list must be sorted in ascending order.
    Args:
        nums(list): list of integers
        target(int): target value to search for
    Returns:
        int: the index of target value or None.
    """
    if len(nums) == 0:
        return None

    mid = len(nums) // 2

    if nums[mid] > target:
        return search(nums[0:mid], target)

    if nums[mid] < target:
        temp = search(nums[mid + 1:len(nums)], target)
        if temp is None:
            return None
        return temp + mid + 1

    return mid


# 4
def fib(index):
    """ Outputs the nth value of the Fibonacci sequence
    Args:
        index(int): the index of the target value
    Returns:
        int: nth value of Fibonacci sequence
    """
    if index > 1:
        return fib(index - 1) + fib(index - 2)

    if index == 1:
        return 1

    return 0


# 5.1 factorial iterative version
def factorial_iter(index):
    """ Returns index! using loops instead of recursion.
    Args:
        index(int): input to the factorial function
    Returns:
        index!
    """
    i = index
    temp = 1
    while i > 0:
        temp = i*temp
        i -= 1
    return temp


# 5.2 factorial recursive version
def factorial_rec(index):
    """Returns index! using recursion.
    Args:
        index(int): input to the factorial function
    Returns:
        index!
    """
    if index > 0:
        return factorial_rec(index-1)*index

    return 1

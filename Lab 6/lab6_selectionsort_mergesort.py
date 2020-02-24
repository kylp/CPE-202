# Merge sort and selection sort
# Nathan Tang


def selection_sort(items):
    """Author: Nathan Tang
    sorts a list using selection_sort
    Args:
        items(list): a list of integers
    Returns:
        int: the number of comparisons
    """
    count = 0
    size = len(items)
    for i in reversed(range(1, size)):
        count += 1
        max_idx = 0
        for j in range(1, i):
            count += 1
            if items[j] > items[max_idx]:
                max_idx = j
        items[max_idx], items[i] = items[i], items[max_idx]
    return count


def merge_sort(items, count=0):
    """Author: Nathan Tang
    sort a list of items in ascending order using the merge sort algorithm
    Args:
        items(list): a list of integers or strings
    Returns:
        list: a copy of the original list with items sorted in ascending order
    """
    count += 1
    if len(items) <= 1:
        return items, count
    mid = len(items) // 2
    left, count_merge = merge_sort(items[:mid])
    count += count_merge
    right, count = merge_sort(items[mid:])
    count += count_merge
    count_merge, merged = merge(left, right)
    count += count_merge
    return merged, count


def merge(left, right):
    """Author: Nathan Tang
    merge two list into one as sorting items in ascending order
    Args:
        left(list): the left part of a list to be merged
        right(list): the right part of a list to be merged
    Returns:
        list: a merged and sorted list
    """
    count = 0
    merged = []
    left_idx = right_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        count += 1
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    if left_idx < len(left):
        for i in range(left_idx, len(left)):
            merged.append(left[i])
    if right_idx < len(right):
        for i in range(right_idx, len(right)):
            merged.append(right[i])
    return count, merged

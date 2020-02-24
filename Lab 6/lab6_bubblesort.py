def bubble_sort(lst):
    """
    Author: Aidan Chandrasekaran
    :param lst: lst to be sorted
    :return: (int) number of compares
    """
    counter = 0
    for j in range(len(lst)):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                placeholder = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = placeholder
            counter += 1
    return counter

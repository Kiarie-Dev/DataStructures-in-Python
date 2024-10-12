def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    # Base case: A stopping condition 
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)

    # conquer step
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list) // 2

    left = list[:mid] # mid is not included
    right = list[mid:] # mid is included here

    return left, right

def merge(left, right):
    """
    Merges two lists(arrays), sorting them in the process
    Returns a new merged list
    """
    list_ = []
    i , j = 0, 0 

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list_.append(left[i])
            i += 1
        else:
            list_.append(right[j])
            j += 1
    while i < len(left):
        list_.append(left[i])
        i += 1
    
    while j < len(right):
        list_.append(right[j])
        j += 1
    return list_

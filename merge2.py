def merge_sort2(list):
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    right = merge_sort2(right_half)
    left = merge_sort2(left_half)

    return merge(left, right)
def split(list):
    mid = len(list) // 2
    left = list[:mid] # To solve... two variables
    right = list[mid:] # To solve

    return left, right
def merge(left, right):
    list_ = []
    i, j = 0, 0

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
def verify(list_):
    n = len(list_)
    
    # Base case for recursion
    if n == 0 or n == 1:
        return True
    return list_[0] <= list_[1] and verify(list_[1:])

# Testing locally
unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = merge_sort2(unsorted_list)
print("Sorted List:", sorted_list)
print("Is Sorted:", verify(sorted_list))



    


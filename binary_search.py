def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        

        if list[mid_point] == target:
            return mid_point
        elif list[mid_point] > target:
            last = mid_point - 1
        else:
            first = mid_point + 1
    
    return None

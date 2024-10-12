def recursive_binary_search(list, target):
    # Some edge case
    # Base case
    if len(list) == 0:
        return False
    mid_point = (len(list)) // 2

    if list[mid_point] == target:
        return True
    if list[mid_point] < target:
        return recursive_binary_search(list[mid_point+1:], target)
    else:
        return recursive_binary_search(list[:mid_point], target)
    
def verify(result):
    print("Target found: ", result)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binary_search(numbers, 12)
result2 = recursive_binary_search(numbers, 6)
verify(result)
verify(result2)

# Recursion
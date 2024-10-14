# Import heapq
import heapq

def sort(nums):
    heap = nums[:]
    heapq.heapify(heap)
    sorted_list = []
    while heap:
        sorted_list.append(heapq.heappop(heap))
    return sorted_list
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_nums = sort(nums)
print(sorted_nums)  # Output: [1, 1, 2, 3, 5, 9, 4, 6, 5]


# # python implementation of a heap
import heapq
# heap = []
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 9)
# heapq.heappush(heap, 11)
# heapq.heappush(heap, 4)
# print(heap)
# heapq.heappop(heap)
# print(heap)
# heappushpop demo
# nums = [1, 3, 5, 7, 9]
# heap_ = nums[:]
# heapq.heapify(heap_)
# smallest = heapq.heappushpop(heap_, 2)
# print(smallest)
# print(heap_)
"""
Heapify
"""
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
heap_ = nums[:]
heapq.heapify(heap_)
print(heap_)


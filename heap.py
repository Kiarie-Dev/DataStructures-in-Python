# python implementation of a heap
import heapq
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 9)
heapq.heappush(heap, 11)
heapq.heappush(heap, 4)
print(heap)
heapq.heappop(heap)
print(heap)

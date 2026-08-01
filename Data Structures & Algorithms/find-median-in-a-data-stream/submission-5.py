class MedianFinder:

    def __init__(self):
        self.minHeap = [] # stores the larger half
        self.maxHeap = [] # stores the smaller half

    def addNum(self, num: int) -> None:
        # add if num is greater than the smallest element in minHeap
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        # balance
        # If one heap becomes larger than the other by more than 1, move the top element to the other heap
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap)) % 2 == 0:
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2.0
        else:
            if len(self.minHeap) > len(self.maxHeap):
                return self.minHeap[0]
            else:
                return (-self.maxHeap[0])
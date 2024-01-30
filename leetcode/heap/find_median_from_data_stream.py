import heapq


class FindMedianFromDataStream:
    def __init__(self):
        self.less_max_heap = []
        self.more_min_heap = []

    def addNum(self, num: int) -> None:
        if (not self.less_max_heap or num <= -
        self.less_max_heap[0]):
            heapq.heappush(self.less_max_heap, -num)
        else:
            heapq.heappush(self.more_min_heap, num)

        if len(self.less_max_heap) - len(self.more_min_heap) >= 2:
            popped = heapq.heappop(self.less_max_heap)
            heapq.heappush(self.more_min_heap, -popped)
        elif len(self.more_min_heap) - len(self.less_max_heap) >= 2:
            popped = heapq.heappop(self.more_min_heap)
            heapq.heappush(self.less_max_heap, -popped)

    def findMedian(self) -> float:
        if len(self.less_max_heap) == len(self.more_min_heap):
            return (-self.less_max_heap[0] + self.more_min_heap[0]) / 2.0
        elif len(self.less_max_heap) > len(self.more_min_heap):
            return -self.less_max_heap[0]
        else:
            return self.more_min_heap[0]


if __name__ == '__main__':
    init = FindMedianFromDataStream()
    print(init.addNum(1))  # arr = [1]
    print(init.addNum(2))  # arr = [1, 2]
    print(init.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
    print(init.addNum(3))  # arr[1, 2, 3]
    print(init.findMedian())  # return 2.0

import heapq


class Findmedianfromdatastream:
    def __init__(self):
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        if not self.left_max or num <= -self.left_max[0]:
            heapq.heappush(self.left_max, -num)
        else:
            heapq.heappush(self.right_min, num)

        if len(self.left_max) - len(self.right_min) >= 2:
            popped = heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, -popped)
        elif len(self.right_min) - len(self.left_max) >= 2:
            popped = heapq.heappop(self.right_min)
            heapq.heappush(self.left_max, -popped)

    def findMedian(self) -> float:
        if len(self.left_max) == len(self.right_min):
            return (-self.left_max[0] + self.right_min[0]) / 2.0
        elif len(self.left_max) > len(self.right_min):
            return -self.left_max[0]
        else:
            return self.right_min[0]


if __name__ == '__main__':
    init = Findmedianfromdatastream()
    print(init.addNum(1))  # arr = [1]
    print(init.addNum(2))  # arr = [1, 2]
    print(init.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
    print(init.addNum(3))  # arr[1, 2, 3]
    print(init.findMedian())  # return 2.0

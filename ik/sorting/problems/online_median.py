import heapq


def online_median(stream):
    left_max = []
    right_min = []
    result = []
    for num in stream:
        if not left_max or num <= -left_max[0]:
            heapq.heappush(left_max, -num)
        else:
            heapq.heappush(right_min, num)

        if len(left_max) - len(right_min) == 2:
            popped = heapq.heappop(left_max)
            heapq.heappush(right_min, -popped)
        elif len(right_min) - len(left_max) >= 2:
            popped = heapq.heappop(right_min)
            heapq.heappush(left_max, -popped)

        if len(left_max) == len(right_min):
            result.append(int((-left_max[0] + right_min[0]) // 2.0))
        elif len(left_max) > len(right_min):
            result.append(-left_max[0])
        else:
            result.append(right_min[0])

    return result


if __name__ == '__main__':
    # print(online_median([3, 8, 5, 2]))
    print(online_median([4, 3, 2, 1]))  # 4,3,3,2

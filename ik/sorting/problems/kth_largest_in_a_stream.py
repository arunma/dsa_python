import heapq


def kth_largest(k, initial_stream, append_stream):
    pq = []

    for num in initial_stream:
        heapq.heappush(pq, num)
        if len(pq) > k:
            heapq.heappop(pq)

    result = []
    for num in append_stream:
        heapq.heappush(pq, num)
        if len(pq) > k:
            heapq.heappop(pq)
        result.append(pq[0])
    return result


if __name__ == '__main__':
    print(kth_largest(2, [4, 6], [5, 2, 20]))

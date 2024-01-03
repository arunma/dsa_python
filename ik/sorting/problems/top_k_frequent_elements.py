# def find_top_k_frequent_elements(arr, k):
#     counter = Counter(arr)
#     input = [(count, num) for num, count in counter.items()]
#     N = len(input)
#     low = 0
#     high = N - 1
#
#     while low <= high:
#         part_index = partition(arr, low, high)
#         if part_index==k:
#             print(input[:k])
#         elif part_index>k:
#
#         break
#
#     return []
#
#
# def partition(arr, low, high):
#     pivot = high
#     lowpos = low
#     for i in range(low, high):
#         if arr[i] < arr[pivot]:
#             arr[lowpos], arr[i] = arr[i], arr[lowpos]
#             lowpos += 1
#     arr[pivot], arr[lowpos] = arr[lowpos], arr[pivot]
#     print(f"pivot: {arr[pivot]}, array:{arr}")
#     return lowpos

def find_top_k_frequent_elements(arr, k):
    pq = []


if __name__ == '__main__':
    print(find_top_k_frequent_elements([1, 1, 1, 2, 2, 3], 2))  # [1, 2]
    print(find_top_k_frequent_elements([1, 2, 3, 2, 4, 3, 2], 2))  # [3, 2]

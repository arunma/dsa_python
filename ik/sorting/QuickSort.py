class QuickSort:

    # def quick_sort(self, arr):
    #     if not arr:
    #         return arr
    #     N = len(arr)
    #     return self._quick_sort(arr, 0, N - 1)
    #
    # def _quick_sort(self, arr, low, high):
    #     if low <= high:
    #         partition = self.partition(arr, low, high)
    #         self._quick_sort(arr, low, partition - 1)
    #         self._quick_sort(arr, partition + 1, high)
    #     return arr
    #
    # def partition(self, arr, low, high):
    #     pivot = high
    #     low_pos = low
    #     for i in range(low, high):
    #         if arr[i] < arr[pivot]:
    #             arr[low_pos], arr[i] = arr[i], arr[low_pos]
    #             low_pos += 1
    #     arr[low_pos], arr[pivot] = arr[pivot], arr[low_pos]
    #     print(f"pivot: {arr[pivot]}, array:{arr}")
    #     return low_pos

    def quick_sort(self, arr):
        if not arr:
            return arr
        low = 0
        high = len(arr) - 1
        self._quick_sort(arr, low, high)
        return arr

    def _quick_sort(self, arr, low, high):
        if low <= high:
            part_index = self.partition(arr, low, high)
            self._quick_sort(arr, part_index + 1, high)
            self._quick_sort(arr, low, part_index - 1)
        return arr

    def partition(self, arr, low, high):
        pivot = high
        low_pos = low
        for i in range(low, high):
            if arr[i] <= arr[pivot]:
                arr[low_pos], arr[i] = arr[i], arr[low_pos]
                low_pos += 1
        arr[pivot], arr[low_pos] = arr[low_pos], arr[pivot]
        print(f"pivot: {arr[pivot]}, array:{arr}")
        return low_pos


if __name__ == '__main__':
    init = QuickSort()
    # print(init.quick_sort(arr=[-1000000000, 0, 1000000000]))
    print(init.quick_sort(arr=[5, 8, 3, 9, 4, 1, 7]))

class MergeSort:

    def merge_sort(self, arr):
        if not arr:
            return arr
        elif len(arr) == 1:
            return arr

        N = len(arr)
        mid = N // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left or right
        return result


if __name__ == '__main__':
    init = MergeSort()
    print(init.merge_sort(arr=[-1000000000, 0, 1000000000]))
    print(init.merge_sort(arr=[5, 8, 3, 9, 4, 1, 7]))

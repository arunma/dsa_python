class BubbleSort:

    def bubble_sort(self, arr):
        """
        Args:
         arr(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        N = len(arr)

        for i in range(N):
            for j in range(N - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return arr


if __name__ == '__main__':
    init = BubbleSort()
    print(init.bubble_sort(arr=[-1000000000, 0, 1000000000]))

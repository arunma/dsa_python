class InsertionSort:

    def insertion_sort(self, arr):
        """
        Args:
         arr(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        N = len(arr)

        for i in range(N):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1
            arr[j + 1] = temp

        return arr


if __name__ == '__main__':
    init = InsertionSort()
    print(init.insertion_sort(arr=[-1000000000, 0, 1000000000]))
    print(init.insertion_sort(arr=[5, 8, 3, 9, 4, 1, 7]))

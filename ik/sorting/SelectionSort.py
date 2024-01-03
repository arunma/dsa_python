class SelectionSort:

    def selection_sort(self, arr):
        """
        Args:
         arr(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        N = len(arr)

        for i in range(N):
            min_index = i
            for j in range(i, N):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr


if __name__ == '__main__':
    init = SelectionSort()
    print(init.selection_sort(arr=[-1000000000, 0, 1000000000]))

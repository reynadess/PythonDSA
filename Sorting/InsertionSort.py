from Sorting.SortingInterface import SortingInterface


class InsertionSort(SortingInterface):
    def __init__(self, arr: list):
        """
        Picks an element and traverses until it is in the right order.
        Insertion order is maintained.
        :param arr: list of elements to be sorted
        """
        super().__init__(arr)

    def sort(self):
        for idx in range(1, len(self.arr)):
            curr_idx = idx
            while curr_idx - 1 >= 0 and self.arr[curr_idx] < self.arr[curr_idx - 1]:
                self.arr[curr_idx], self.arr[curr_idx - 1] = self.arr[curr_idx - 1], self.arr[curr_idx]
                curr_idx -= 1


if __name__ == '__main__':
    sortObj = InsertionSort([43, 123, 213, -32, 438])
    sortObj.sort()
    print(sortObj.arr)

from Sorting.SortingInterface import SortingInterface


class SelectionSort(SortingInterface):
    def __init__(self, arr: list):
        """
        Selection sort is where we pick the next element from unsorted part
        Does not maintain insertion order
        :type arr: list
        """
        super().__init__(arr)

    def sort(self):
        for idx in range(len(self.arr)):
            min_idx = self.find_min_ele(idx)
            self.arr[idx], self.arr[min_idx] = self.arr[min_idx], self.arr[idx]

    def find_min_ele(self, idx: int) -> int:
        min_idx = idx
        for idx in range(idx + 1, len(self.arr)):
            if self.arr[idx] < self.arr[min_idx]:
                min_idx = idx
        return min_idx


if __name__ == '__main__':
    sortObj = SelectionSort([8, 5, 43, 21, 23])
    sortObj.sort()
    print(sortObj.arr)

from Sorting.SortingInterface import SortingInterface


class QuickSort(SortingInterface):
    def __init__(self, arr):
        super().__init__(arr)

    def sort(self):
        self.quick_sort(low=0, high=len(self.arr) - 1)

    def quick_sort(self, low: 0, high: int):
        if low >= high:
            return
        mid = self.find_pivot(low, high)
        self.quick_sort(low, mid - 1)
        self.quick_sort(mid, high)

    def find_pivot(self, low: int, high: int) -> int:
        pivot = self.arr[low]
        left_idx = low + 1
        right_idx = high
        while left_idx < right_idx:
            while left_idx < right_idx and pivot >= self.arr[left_idx]:
                left_idx += 1

            while right_idx > left_idx and pivot < self.arr[right_idx]:
                right_idx -= 1

            if left_idx < right_idx:
                self.arr[left_idx], self.arr[right_idx] = self.arr[right_idx], self.arr[left_idx]

        if self.arr[low] >= self.arr[left_idx]:
            self.arr[low], self.arr[left_idx] = self.arr[left_idx], self.arr[low]

        return left_idx


if __name__ == '__main__':
    sort_obj = QuickSort([1, 5, 23, 54, 54, 232, 5423, 5454353, 65656, 6578])
    sort_obj.sort()
    print(sort_obj.arr)

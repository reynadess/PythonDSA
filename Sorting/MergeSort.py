from Sorting.SortingInterface import SortingInterface


class MergeSort(SortingInterface):
    def __init__(self, arr: list):
        super().__init__(arr)

    def sort(self):
        self.merge_sort(low=0, high=len(self.arr) - 1)

    def merge_sort(self, low: 0, high):
        if high <= low:
            return
        mid = (low + high) // 2
        self.merge_sort(low, mid)
        self.merge_sort(mid + 1, high)
        self.merge(low, mid, high)

    def merge(self, low: int, mid: int, high: int):
        temp_arr = list()
        idx1 = low
        idx2 = mid + 1
        while idx1 <= mid and idx2 <= high:
            if self.arr[idx1] < self.arr[idx2]:
                temp_arr.append(self.arr[idx1])
                idx1 += 1
            else:
                temp_arr.append(self.arr[idx2])
                idx2 += 1
        while idx1 <= mid:
            temp_arr.append(self.arr[idx1])
            idx1 += 1
        while idx2 <= high:
            temp_arr.append(self.arr[idx2])
            idx2 += 1

        for ele in temp_arr:
            self.arr[low] = ele
            low += 1


if __name__ == '__main__':
    sort_obj = MergeSort([12, 32, 645, 34, 54, 66, 1])
    sort_obj.sort()
    print(sort_obj.arr)

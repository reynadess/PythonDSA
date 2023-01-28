from SortingInterface import SortingInterface


class BubbleSort(SortingInterface):
    def __init__(self, arr: list):
        """
        Swapping elements until they are in the order.
        :param arr: list of elements
        """
        super().__init__(arr)

    def sort(self):
        for i in range(len(self.arr)):
            swapped = False
            for j in range(len(self.arr) - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True

            if not swapped:
                break


if __name__ == '__main__':
    sortObj = BubbleSort([5, 1, 4, 2, 8])
    sortObj.sort()
    print(sortObj.arr)

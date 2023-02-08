from SearchingInterface import SearchingInterface


class BinarySearch(SearchingInterface):
    def __init__(self, nums):
        super().__init__(nums)

    def search(self, element_to_find):
        low = 0
        high = len(self.nums) - 1
        while low <= high:
            mid = ((high - low) // 2) + low
            if self.nums[mid] == element_to_find:
                return mid
            elif self.nums[mid] < element_to_find:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def lower_bound(self, element_to_find):
        low = 0
        high = len(self.nums) - 1
        low_idx = -1
        while low <= high:
            mid = ((high - low) // 2) + low
            if self.nums[mid] == element_to_find:
                low_idx = mid
                high = mid - 1
            elif self.nums[mid] < element_to_find:
                low_idx = mid
                low = mid + 1
            else:
                high = mid - 1
        if 0 <= low_idx < len(self.nums) and self.nums[low_idx] == element_to_find:
            low_idx -= 1
        return low_idx

    def upper_bound(self, element_to_find):
        low = 0
        high = len(self.nums) - 1
        high_idx = len(self.nums)
        while low <= high:
            mid = ((high - low) // 2) + low
            if self.nums[mid] == element_to_find:
                high_idx = mid
                low = mid + 1
            elif self.nums[mid] < element_to_find:
                low = mid + 1
            else:
                high_idx = mid
                high = mid - 1
        if high_idx < len(self.nums) and self.nums[high_idx] <= element_to_find:
            high_idx += 1
        return high_idx


if __name__ == '__main__':
    binarySearch = BinarySearch([1, 1, 3])
    low_idx = binarySearch.lower_bound(3)
    high_idx = binarySearch.upper_bound(3)
    count = high_idx - low_idx - 1
    print(f'low_idx:{low_idx}, high_idx:{high_idx}\nCount:{count}')

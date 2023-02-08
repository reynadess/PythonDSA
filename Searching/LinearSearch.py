from Searching.SearchingInterface import SearchingInterface


class LinearSearch(SearchingInterface):
    def __init__(self, nums:list):
        super(LinearSearch, self).__init__(nums)

    def search(self, element_to_find):
        for idx in range(len(self.nums)):
            if self.nums[idx] == element_to_find:
                return idx

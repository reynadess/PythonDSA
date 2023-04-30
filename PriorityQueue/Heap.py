from typing import Any

from PriorityQueue import PriorityQueue


class Heap(PriorityQueue):
    def __init__(self, arr=[], min_queue=True):
        super().__init__(arr, min_queue)
        self.heapify()

    def heapify(self):
        for idx in range(len(self.arr) - 1, -1, -1):
            self.heapifyUtil(idx)

    def heapifyUtil(self, parent_idx):
        if 2 * parent_idx + 1 >= len(self.arr):
            return
        left_child_idx = 2 * parent_idx + 1
        right_child_idx = 2 * parent_idx + 2
        self.swapHeap(parent_idx, left_child_idx)
        self.swapHeap(parent_idx, right_child_idx)
        return

    def insert(self, num):
        self.arr.append(num)
        child_idx = len(self.arr) - 1
        parent_idx = ((child_idx - 1) // 2)
        while self.min_queue and parent_idx >= 0 and self.arr[parent_idx] > self.arr[child_idx]:
            self.swap(parent_idx, child_idx)
            child_idx = parent_idx
            parent_idx = ((child_idx - 1) // 2)

        while not self.min_queue and parent_idx >= 0 and self.arr[parent_idx] < self.arr[child_idx]:
            self.swap(parent_idx, child_idx)
            child_idx = parent_idx
            parent_idx = ((child_idx - 1) // 2)

    def pop(self):
        if len(self.arr) == 0:
            return None

        self.swap(0, len(self.arr) - 1)
        minValue = self.arr.pop()
        self.heapifyUtil(0)
        return minValue

    def getMin(self):
        if self.min_queue:
            return self.arr[0]
        else:
            pass  # TODO pick the leaf nodes minimum

    def getMax(self):
        if not self.min_queue:
            return self.arr[0]
        else:
            pass  # TODO pick the leaf nodes maximum

    def swapHeap(self, parent_idx, child_idx):
        if parent_idx >= len(self.arr) or child_idx >= len(self.arr):
            return

        if self.min_queue and self.arr[parent_idx] > self.arr[child_idx]:
            self.swap(parent_idx, child_idx)
            self.heapifyUtil(child_idx)

        if not self.min_queue and self.arr[parent_idx] < self.arr[child_idx]:
            self.swap(parent_idx, child_idx)
            self.heapifyUtil(child_idx)

    def swap(self, idx1, idx2):
        self.arr[idx1] = self.arr[idx1] ^ self.arr[idx2]
        self.arr[idx2] = self.arr[idx1] ^ self.arr[idx2]
        self.arr[idx1] = self.arr[idx1] ^ self.arr[idx2]


if __name__ == '__main__':
    heap = Heap([1, 2, 3, 4, 5, 45, 42314, 5454], True)
    print(heap.arr)
    print(heap.getMin())
    heap.insert(1000000)
    print(heap.arr)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.arr)
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.pop())
    print(heap.arr)

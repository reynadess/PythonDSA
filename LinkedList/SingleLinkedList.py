from LinkedList.LinkedListInterface import LinkedListInterface
from typing import Optional


class SingleLinkedList(LinkedListInterface):
    def __init__(self, arr=None):
        super().__init__(arr)

    class Node:
        def __init__(self, data=0):
            self.data = data
            self.next = None

        def __str__(self):
            return str(self.data)

    def append(self, data):
        self.tail.next = self.Node(data)
        self.tail = self.tail.next

    def arr_to_linked_list(self, arr: list):
        if not arr:
            return
        if self.head is None:
            self.head = self.Node(arr[0])
            self.tail = self.head
        for idx in range(1, len(arr)):
            self.append(arr[idx])

    def reverse(self):
        if not self.head or not self.head.next:
            return self.head

        prev_node = None
        curr_node = self.head
        next_node = self.head.next
        self.tail = self.head
        self.tail.next = None
        while curr_node:
            curr_node.next = prev_node
            prev_node = curr_node
            if not next_node:
                self.head = prev_node
                return self.head
            curr_node = next_node
            next_node = next_node.next

    def recursive_reverse(self, head, prev=None):
        if not head or not head.next:
            return head
        if not head.next:
            head.next = prev
            return head

        new_head = self.recursive_reverse(head.next, head)
        head.next = prev
        return new_head

    def detectCycle(self, head: Optional[Node]) -> Optional[Node]:
        if not head or not head.next:
            return None

        slow_ptr = head
        fast_ptr = head
        while True:
            slow_ptr = slow_ptr.next
            if not fast_ptr.next or not fast_ptr.next.next:
                return None
            fast_ptr = fast_ptr.next.next
            if slow_ptr == fast_ptr:
                return slow_ptr

        slow_ptr = head
        while True:
            if slow_ptr == fast_ptr:
                return slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return None

    def removeZeroSumSublists(self, head: Optional[Node]) -> Optional[Node]:
        prevPtr = None
        startPtr = head
        endPtr = head
        sum = 0
        while startPtr:
            flag = False
            while endPtr:
                sum += endPtr.data
                endPtr = endPtr.next
                if sum == 0:
                    if prevPtr:
                        prevPtr.next = endPtr
                        startPtr = endPtr
                    else:
                        head = endPtr
                        startPtr = endPtr
                    flag = True
                    break
            if not flag:
                prevPtr = startPtr
                startPtr = startPtr.next
                endPtr = startPtr
                sum = 0
        return head


if __name__ == '__main__':
    single_linked_list = SingleLinkedList([1,2,3,-3,4])
    print(single_linked_list.removeZeroSumSublists(single_linked_list.head))


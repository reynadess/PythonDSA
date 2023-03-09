from LinkedList.LinkedListInterface import LinkedListInterface


class DoublyLinkedList(LinkedListInterface):

    def __init__(self, arr=None):
        super.__init__(arr)

    class Node:
        def __init__(self, data=0):
            self.data = data
            self.next = None
            self.prev = None

        def __str__(self):
            return str(self.data)

    def append(self, data):
        self.tail.next = self.Node(data)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def arr_to_linked_list(self, arr: list):
        if not arr:
            return
        if self.head is None:
            self.head = self.Node(arr[0])
            self.tail = self.head
        for idx in range(1, len(arr)):
            self.append(arr[idx])


if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList([5, 6, 7, 78, 1, 21])
    print(doubly_linked_list)
    print(doubly_linked_list.find_mid())

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next

    def arr_to_linked_list(self, arr: list):
        if self.head is None:
            self.head = Node(arr[0])
            self.tail = self.head
        for idx in range(1, len(arr)):
            self.append(arr[idx])

    def __str__(self):
        curr_node = self.head
        print_str = ""
        while curr_node:
            print_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        return print_str


if __name__ == '__main__':
    single_linked_list = SingleLinkedList()
    elements = [5, 6, 7, 78]
    single_linked_list.arr_to_linked_list(elements)
    print(single_linked_list)

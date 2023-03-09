class LinkedListInterface:
    def __init__(self, arr=None):
        self.head = None
        self.tail = None
        self.arr_to_linked_list(arr)

    def __str__(self):
        curr_node = self.head
        print_str = ""
        while curr_node:
            print_str += str(curr_node.data) + " "
            curr_node = curr_node.next
        return print_str.strip()

    def find_mid(self):
        if not self.head:
            return None
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr:
            if fast_ptr.next is None:
                return slow_ptr
            if fast_ptr.next.next is None:
                return slow_ptr.next
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

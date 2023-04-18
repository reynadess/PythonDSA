class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodesMap = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.nodesMap:
            return -1
        node = self.nodesMap.get(key)
        prevNode = node.prev
        nextNode = node.next
        if prevNode is None and nextNode is None:
            return node.value
        node.next = None
        node.prev = None
        if prevNode is not None:
            prevNode.next = nextNode
        if nextNode is not None:
            nextNode.prev = prevNode
        if  node == self.tail:
            prevNode.next = node
            node.prev = prevNode
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next
        if node == self.head and nextNode is not None:
            self.head = nextNode
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodesMap:
            self.get(key)
            self.nodesMap[key].value = value
            return

        node = Node(key, value)
        self.nodesMap[key] = node

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            prevNode = self.tail
            self.tail = self.tail.next
            self.tail.prev = prevNode

        while len(self.nodesMap) > self.capacity:
            key = self.head.key
            self.nodesMap.pop(key)
            self.head = self.head.next
            self.head.prev = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    lRUCache = LRUCache(1)
    lRUCache.put(2, 1)
    print(lRUCache.get(2))
    lRUCache.put(3, 2)
    print(lRUCache.get(3))
    # lRUCache.get(2)
    # lRUCache.put(4, 3)
    # lRUCache.get(3)
    # lRUCache.get(4)

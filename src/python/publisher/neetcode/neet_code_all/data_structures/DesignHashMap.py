class ListNode:
    def __init__(self, key=1, value=1, next=None):
        self.key = key
        self.value = value
        self.next = next

class DesignHashMap:
    def __init__(self):
        self.listMap = [ListNode() for i in range(1000)]
        return

    def put(self, key: int, value:int) -> None:
        currentNode = self.listMap[self.hash(key=key)]# Chaining linked list
        while currentNode.next:
            if currentNode.next.key == key:
                currentNode.next.value = value
                return
            currentNode = currentNode.next
        currentNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        currentNode = self.listMap[self.hash(key=key)].next
        while currentNode:
            if currentNode.key == key:
                return currentNode.value
            currentNode = currentNode.next
        return -1

    def remove(self, key: int):
        currentNode = self.listMap[self.hash(key=key)]
        while currentNode and currentNode.next:
            if currentNode.next.key == key:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next

    def hash(self, key):
        return key % len(self.listMap) # Chaining linked list
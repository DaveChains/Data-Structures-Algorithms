from typing import List


class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class SinglyLinkedList(object):
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.next_node
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next_node

        return -1  # Index Out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val=val)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node
        # if list was empty before inserting
        if not new_node.next_node:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next_node = Node(val=val)
        self.tail = self.tail.next_node

    def remove(self, index: int) -> bool:

        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next_node

        # remove the node ahead of curr
        if curr and curr.next_node:
            if curr.next_node == self.tail:
                self.tail = curr
            curr.next_node = curr.next_node.next_node
            return True
        return False

    def getValue(self) -> List[int]:

        curr = self.head.next_node
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next_node
        return res

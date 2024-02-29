class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class SimpleLinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def add_node(self, new_node: Node):
        current = self.head
        if self.head:
            print("1. ", self.head.value, " is not null, will check next head")
            while current.next:
                print("2. current node.next is not null, ", current.next.value, "jumping current to next")
                current = current.next

            print("3. current next is null, assigning , new node=", new_node, "to next head")
            current.next = new_node
        else:
            print("0. self head is null/empty, adding new node=", new_node, " to the head")
            self.head = new_node

    def get_by_position(self, position):
        counter = 1
        current = self.head
        # 1 if the position is less than 1
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return counter


# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
new_linked_list = SimpleLinkedList()
new_linked_list.add_node(new_node=e1)
new_linked_list.add_node(new_node=e2)
new_linked_list.add_node(new_node=e3)
new_linked_list.add_node(new_node=e4)


print("get Position ", new_linked_list.get_by_position(1).value)

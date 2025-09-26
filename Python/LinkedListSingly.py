# Create Simple Singly Linked List DS

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, value):
        remove_node = Node(value)
        if self.head is None:
            return False
        else:
            current = self.head
            while current:
                # print(current.value, remove_node.value)
                if current.value == remove_node.value:
                    current.head.next = current.next
                    break
                current = current.next
            self.length -= 1


linked_list = SinglyLinkedList(12)
linked_list.prepend(11)
linked_list.append(13)
linked_list.remove(12)
i = linked_list.head
while i:
    print(i.value)
    i = i.next

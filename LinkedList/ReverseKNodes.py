#!/usr/bin/python3


# Node class
class Node:

    # Constructor to initialise data and next
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:

    # Constructor to initialise head
    def __init__(self):
        self.head = None

    # Function to reverse K nodes of linked list
    def reverse_k_nodes(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.reverse_k_nodes(next, k)

        return prev

    # Function to Insert data at the beginning of the linked list
    def insert_at_beg(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    # Function to print the linked list
    def print_data(self):
        current = self.head
        while current is not None:
            print(current.data, '-> ', end='')
            current = current.next
        print('None')

if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insert_at_beg(7)
    linked_list.insert_at_beg(6)
    linked_list.insert_at_beg(5)
    linked_list.insert_at_beg(4)
    linked_list.insert_at_beg(3)
    linked_list.insert_at_beg(2)
    linked_list.insert_at_beg(1)
    linked_list.print_data()
    linked_list.head = linked_list.reverse_k_nodes(linked_list.head, 3)
    linked_list.print_data()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def has_loop(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)

my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop())

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)

print(my_linked_list_2.has_loop())



class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None
        self.tail = None
        self.length = 0
    
    def __len__(self):
        return self.length

    def add_to_tail(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        # value is actual value, and hasn't been wrapped in a Node yet
        new_node = Node(value)
        # what if the list is empty?
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # self.assertEqual(len(self.stack), 1)   AssertionError: 0 != 1
            # self.assertEqual(len(self.stack), 2)   AssertionError: 1 != 2
            self.length += 1
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to?
            # the last node in the list
            # we can get to the last node in the list by traversing it
            # we're at the end of the linked list
            self.tail.next_node = new_node
            self.tail = new_node
            self.length += 1

    def remove_from_end(self):
        current = self.head
        # what if it isn't empty?
        # AssertionError: None != 105 error fixed
        if self.length > 0:
            previous = None
            while current.next_node != None:
                previous = current
                current = current.get_next()
            # what if it isn't empty?
            if previous != None:
                previous.set_next(None)
                self.tail = previous
                self.length -= 1
                return current.value
            # what if the list is empty?
            else:
                self.head = None
                self.tail = None
                self.length = 0
                return current.value
        # what if the list is empty?
        else:
            return None
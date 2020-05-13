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
            # self.length += 1
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to?
            # the last node in the list
            # we can get to the last node in the list by traversing it
            # we're at the end of the linked list
            self.tail.next_node = new_node
            self.tail = new_node
    
    def remove_tail(self):
        # what if the list is empty?
        if not self.tail and not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current tail
            value = self.tail.get_value()
            # remove the value at the tail
            # update self.tail
            self.tail = self.tail.get_next()
            self.head = self.head.get_next()
            return value

    def add_to_head(self, value):
        new_node = Node(value)
        # what if the list is empty?
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node

    def remove_head(self):
        # current = self.head
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value

    def contains(self):
        pass

    def get_max(self):
        # if empty
        if self.head is None and self.tail is None:
            return None
        # create current
        current_node = self.head
        # set current to equal (something)
        current_max = self.head.value
        # loop through node
        while current_node is not None:
            # if current value is greater than (something)
            if current_node.value > current_max:
                # set current max to (something)
                current_max = current_node.value
            current_node = current_node.get_next()
        # then return that value
        return current_max

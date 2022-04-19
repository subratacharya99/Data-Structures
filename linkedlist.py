class Node:
    
    def __init__(self, input = None):
        self.data = input


class LinkedList:

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def add_to
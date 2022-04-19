"""
Practice of implementing Linked Lists in Python.
Creates a Singly Linked List with following functions:
isEmpty() -> returns whether linked list is empty
addToFront() -> adds element to head of list
addToBack() -> adds element to back of list
pop() -> removes element at head of list


reverseList() -> returns reverse of list

"""

class Node:
    
    def __init__(self, input = None):
        self.data = input
        self.next = None

    def __repr__(self):
        return f"<Node>: {self.data}"


class LinkedList:

    def __init__(self):
        self.head = None
    
    def __repr__(self):
        if self.isEmpty():
            return "<Empty>"
        else:
            rep_array = [f"[Head: {self.head.data}]"]
            current = self.head.next
            while current:
                if current.next == None:
                    rep_array.append(f"[Tail: {current.data}]")
                else:
                    rep_array.append(f"[{current.data}]")
                current = current.next

            return "->".join(rep_array)
        
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def addToFront(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            del temp

    def addToBack(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            current = self.head
            while current:
                if not current.next:
                    current.next = Node(data)
                    return True
                current = current.next


if __name__ == "__main__":
    n = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n.next= n2
    n2.next = n3
    n3.next = n4

    l = LinkedList()
    m = LinkedList()
    l.head = n
    
    m.addToFront(4)
    m.addToFront(6)
    m.addToFront(8)
    print(m)
    m.addToBack(10)
    m.addToFront(12)
    print(m)
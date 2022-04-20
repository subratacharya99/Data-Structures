"""
Practice of implementing Linked Lists in Python.
Creates a Singly Linked List with following properties and functions:

LinkedList has one property "head" which points to the head of the list
Node has two properties, "data" which stores the data in the node,
and "next" which points to the next node in the linked list

    isEmpty() -> returns whether linked list is empty
    addToFront() -> adds element to head of list
    addToBack() -> adds element to back of list
    copy() -> creates and returns a deep copy of list
    insert() -> adds element at a given index
    remove() -> removes all instances of element given the data
    removeAtPosition() -> removes data at given index
    pop() -> removes element at front of list and returns data
    dequeue() -> removes element at back of list and returns data
    getIndex() -> returns index of element in list (0-based)
    reverse() -> returns the reverse of the list

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
    
    """O(n)"""
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
        
    
    """O(1)"""
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    """O(1)"""
    def addToFront(self, data):
        if self.isEmpty():
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
            del temp

    """O(n)"""
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

    def insert(self, data, index):
        if index >= self.length():
            self.addToBack(data)
        elif index == 0:
            self.addToFront(data)
        else:
            count = 0
            current = self.head
            while count < index:
                if count == index-1:
                    insertData = Node(data)
                    nex = current.next
                    current.next = insertData
                    insertData.next = nex
                    del insertData
                current = current.next
                count+=1

    def remove(self, data):
        if self.isEmpty():
            print("List is Empty")
        else:
            prev = None
            current = self.head

            while current:
                if current.data == data:
                    if prev == None:
                        self.head = current.next
                        current = current.next
                    else:
                        prev.next = current.next
                        current = current.next
                else:
                    prev = current
                    current = current.next

    def removeAtPosition(self, index):
        if self.isEmpty():
            print("List is Empty")
        elif index >= self.length():
            print("Index is out of Bounds")

    def length(self):
        if self.isEmpty():
            return 0
        else:
            current = self.head
            count = 0
            while current:
                current = current.next
                count +=1
            return count

    """O(n)"""
    def copy(self):
        if self.isEmpty():
            return LinkedList()
        else:
            newList = LinkedList()
            current = self.head
            newList.head = Node(current.data)
            ncurrent = newList.head
            current = current.next
            while current:
                ncurrent.next = Node(current.data)
                current = current.next
                ncurrent= ncurrent.next
            return newList
    
    """O(1)"""
    def pop(self):
        if self.isEmpty():
            print("List is empty!")
        else:
            data = self.head.data
            self.head = self.head.next
            return data
    
    """O(n)"""
    def dequeue(self):
        if self.isEmpty():
            print("List is empty!")
        elif not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next:
                nextNode = current.next
                if not nextNode.next:
                    data = nextNode.data
                    current.next = None
                    del nextNode
                    return data
                current = current.next

    """O(n)"""
    def getIndex(self, data):
        current = self.head
        count = 0
        while current:
            if current.data == data:
                return count
            count+=1
            current = current.next

    """O(n)"""
    def reverse(self):
        if self.isEmpty():
            print("List is Empty")
            return None
        else:
            revList= self.copy()
            prev = None
            current = revList.head
            nex = current.next
            while current:
                current.next = prev
                prev = current
                current = nex
                if current.next:
                    nex = current.next
                else:
                    current.next = prev
                    revList.head = current
                    return revList





"""Testing the Functions Below"""
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
    m.addToBack(10)
    m.addToFront(12)

    # print(m)
    # print(m.reverse())
    # print(m)
    l.insert(1.5, 1)
    l.addToBack(1.5)
    print(l)
    l.remove(1.5)
    print(l)
    #print(m.getIndex(12))
   
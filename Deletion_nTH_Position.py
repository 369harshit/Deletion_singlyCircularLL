# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    # Add new element at the end of the list
    def push_back(self, newElement):
        newNode = Node(newElement)
        if self.head is None:
            self.head = newNode
            newNode.next = self.head
            return
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head

    # Delete an element at the given position
    def pop_at(self, position):
        nodeToDelete = self.head
        temp = self.head
        NoOfElements = 0

        if temp is not None:
            NoOfElements += 1
            temp = temp.next
        while temp != self.head:
            NoOfElements += 1
            temp = temp.next

        if position < 1 or position > NoOfElements:
            print("\nInvalid position.")
        elif position == 1:
            if self.head.next == self.head:
                self.head = None
            else:
                while temp.next != self.head:
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head
                nodeToDelete = None

        else:
            temp = self.head
            for i in range(1, position - 1):
                temp = temp.next
            nodeToDelete = temp.next
            temp.next = temp.next.next
            nodeToDelete = None

    # display the content of the list
    def PrintList(self):
        temp = self.head
        if temp is not None:
            print("The list contains:", end=" ")
            while True:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.head:
                    break
            print()
        else:
            print("The list is empty.")


# test the code
MyList = LinkedList()

# Add three elements at the end of the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.PrintList()

# Delete an element at position 2
MyList.pop_at(2)
MyList.PrintList()

# Delete an element at position 1
MyList.pop_at(1)
MyList.PrintList()

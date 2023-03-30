# node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# class LinkedList
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

    # Delete first node of the list
    def pop_front(self):
        if self.head is not None:
            if self.head.next == self.head:
                self.head = None
            else:
                temp = self.head
                firstNode = self.head
                while temp.next != self.head:
                    temp = temp.next
                self.head = self.head.next
                temp.next = self.head
                firstNode = None

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

# Add four elements in the list.
MyList.push_back(10)
MyList.push_back(20)
MyList.push_back(30)
MyList.push_back(40)
MyList.PrintList()

# Delete the first node
MyList.pop_front()
MyList.PrintList()

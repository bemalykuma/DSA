class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, count=0):
        self.count = count
        self.head = None

    def insert_front(self, data):
        newNode = DataNode(data)
        self.count += 1
        newNode.next = self.head
        self.head = newNode

    def insert_last(self, data):
        newNode = DataNode(data)
        self.count += 1
        if self.head == None:
            self.head = newNode
        else:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = newNode

    def traverse(self):
        if self.head == None:
            print("This is an empty list.")
            return
        else:
            temp = ''
            start = self.head
            while start != None:
                temp += " -> " + start.data
                start = start.next
        print(temp.replace(" -> ", "", 1))

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()

main()
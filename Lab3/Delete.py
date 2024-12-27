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

    def insert_before(self, node, data):
        newNode = DataNode(data)
        prev = self.head
        if prev == None:
            print(f"Cannot insert, "+node+" does not exist.")
            return
        self.count += 1
        found = None
        if prev.data == node:
            newNode.next = prev
            self.head = newNode
        else:
            start = prev.next
            while start:
                if start.data == node:
                    found = True
                    newNode.next = start
                    prev.next = newNode
                    return
                prev = start
                start = prev.next
            if found != True:
                print(f"Cannot insert, "+node+" does not exist.")

    def delete(self, data):
        prev = self.head
        found = None
        if prev == None:
            print(f"Cannot delete, "+data+" does not exist.")
            return

        if prev.data == data and self.count == 1:
            self.head = None
            return

        self.count -= 1
        if prev.data == data:
            self.head = prev.next
        else:
            start = prev.next
            while start:
                if start.data == data:
                    found = True
                    prev.next = start.next
                    return
                prev = start
                start = prev.next
            if found != True:
                print(f"Cannot delete, "+data+" does not exist.")
        

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
        text = input().strip()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
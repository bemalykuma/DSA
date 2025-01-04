class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = BSTNode(data)
        else:
            self.recursive_insert(self.root, data)

    def recursive_insert(self, current, data):
        if data < current.data:
            if current.left != None:
                self.recursive_insert(current.left, data)
            else:
                current.left = BSTNode(data)
        else:
            if current.right != None:
                self.recursive_insert(current.right, data)
            else:
                current.right = BSTNode(data)

    def preorder(self):
        if self.root != None:
            self.recursive_preorder(self.root)
    
    def recursive_preorder(self, current):
        if current != None:
            print("->", current.data, end=" ")
            self.recursive_preorder(current.left)
            self.recursive_preorder(current.right)
        

def main():
    my_bst = BST()
    for i in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()

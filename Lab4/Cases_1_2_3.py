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

    def delete(self, data):
        if self.is_empty():
            return print("Delete Error,", data,"is not found in Binary Search Tree.")
        self._delete_(self, self.root, data)
        # find = self.find_data(self.root, data)
        # return print(find)
    def _delete_(self, root, data):
        if data < root:
            pass

        
    # def find_data(self, current, data):
    #     if current.data == data:
    #         return current
    #     if data < current.data:
    #         if current.data != data:
    #             self.find_data(current.left, data)
    #         else:
    #             return current
    #     else:
    #         if current.data != data:
    #             self.find_data(current.right, data)
    #         else:
    #             return current

    def find_min(self):
        if self.is_empty():
            return None
        return self._min(self.root)
        
    def _min(self, current):
        while current.left != None:
            current = current.left
        return current.data

    def find_max(self):
        if self.is_empty():
            return None
        return self._max(self.root)
        
    def _max(self, current):
        while current.right != None:
            current = current.right
        return current.data

    def is_empty(self):
        if self.root is None:
            return True
        return False
    
    #traversal
    def preorder(self):
        if self.root != None:
            self.recursive_preorder(self.root)
    
    def recursive_preorder(self, current):
        if current != None:
            print("->", current.data, end=" ")
            self.recursive_preorder(current.left)
            self.recursive_preorder(current.right)

    def inorder(self):
        if self.root != None:
            self.recursive_inorder(self.root)

    def recursive_inorder(self, current):
        if current != None:
            self.recursive_inorder(current.left)
            print("->", current.data, end=" ")
            self.recursive_inorder(current.right)
    
    def postorder(self):
        if self.root != None:
            self.recursive_postorder(self.root)

    def recursive_postorder(self, current):
        if current != None:
            self.recursive_postorder(current.left)
            self.recursive_postorder(current.right)
            print("->", current.data, end=" ")

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return
        print('Preorder: ', end='')
        self.preorder()
        print('\nInorder: ', end='')
        self.inorder()
        print('\nPostorder: ', end='')
        self.postorder()

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
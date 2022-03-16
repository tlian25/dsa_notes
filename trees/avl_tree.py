# Implementation of AVL tree

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)


class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, root, key):
        
        # Empty tree, so insert is a new node set to be root
        if not root:
            return TreeNode(key)
        # BST -> recursively
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update heights after insertion
        root.height = 1 + max(self.getHeight(root.left), 
                             self.getHeight(root.right))

        # Get Balance factor
        balance = self.getBalance(root)

        # If node is unbalances, then check 4 cases and rotate accordingly
        if abs(balance) <= 1:
            return root

        # Left heavy and key < left value
        elif balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        elif balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        elif balance < -1 and key > root.right.val:
            return self.rightRotate(root)

        elif balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)


    def getHeight(self, root):
        if not root: 
            return 0
        return root.height


    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)


    def printTree(self, root):
        if not root:
            print('# ', end="")
            return None

        print(f"{root} ", end = "")
        self.printTree(root.left)
        self.printTree(root.right)


    # Rotate node z's right child with node z
    # Right child moving left
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update Heights -> update z first because it's now the child node
        z.height = 1 + max(self.getHeight(z.left),
                            self.getHeight(z.right))

        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return new root -> previous right child
        return y


    # Rotate node z's left child with node z
    # Left child moving right
    def rightRotate(self, z):

        y = z.left
        T2 = y.right

        # Perform rotation
        y.right = z
        z.left = T2

        # Update Heights -> update z first because it's now the child node
        z.height = 1 + max(self.getHeight(z.left),
                            self.getHeight(z.right))
   
        y.height = 1 + max(self.getHeight(y.left),
                            self.getHeight(y.right))
   
        # Return new root -> previous left child
        return y 



### EXAMPLE

avl = AVLTree()
root = None

root = avl.insert(root, 10)
root = avl.insert(root, 20)
root = avl.insert(root, 30)
root = avl.insert(root, 40)
root = avl.insert(root, 50)
root = avl.insert(root, 25)

avl.printTree(root)


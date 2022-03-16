# Notes on constructing Trees from different representations

from typing import Optional, List

class TreeNode:
    def __init__(self, val:int=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)




# Construction from in-order traversal
# left -> root -> right
'''
            1
      2           3
  4       5     6     7
#   8   #   #  #  9  #  10
'''
inorder = [4, 2, 8, 5, 1, 6, 9, 3, 7, 10]

for n in inorder:
    exec(f'n{n} = TreeNode({n})')

root = n1
root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n4.right = n8
n3.left = n6
n3.right = n7
n6.right = n9
n7.right = n10


################ Searches #################



### Depth First Search

def dfs_iterative(root):
    ''' 
    use stack to track next right element to examine
    '''
    curr = root
    stack = []
    while curr or stack:

        # If node exists -> keep looking left
        # place right on stack to revisit/backtrack later
        if curr:
            print(f'{curr} -> ', end = '')
            stack.append(curr.right)
            curr = curr.left
        
        # Current is none so we look to stack for next item
        else:
            print('# -> ', end = '')
            curr = stack.pop()
    
    # Terminating Right none
    print('# -> ')


print('DFS Iterative')
dfs_iterative(root)


def dfs_recursive(root):

    if root is None:
        print('# -> ', end='')
    else:
        print(f'{root} -> ', end='')
        dfs_recursive(root.left)
        dfs_recursive(root.right)

print("DFS Recursive")
dfs_recursive(root)
print('')




### Breadth First Search

def bfs_iterative(root):
    '''
    Use a queue to track order
    '''
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if not curr:
            print('# -> ', end='')
            continue

        print(f'{curr} -> ', end = '')
        queue.append(curr.left)
        queue.append(curr.right)

    print('')


print("BFS Iterative")
bfs_iterative(root)




def bfs_recursive(nodes: List[TreeNode]):
    # Takes in a list of next nodes to look at

    if nodes == []:
        return 
    else:
        next = []
        for n in nodes:
            if n:
                print(f'{n} -> ', end='')
                next.append(n.left)
                next.append(n.right)
            else:
                print('# -> ', end='')


        bfs_recursive(next)


print("BFS Recursive")
bfs_recursive([root])
    





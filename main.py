# binary search tree node class 
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left_node = None
        self.right_node = None

root = TreeNode(20)
nodeA = TreeNode(12)
nodeB = TreeNode(29)
nodeC = TreeNode(7)
nodeD = TreeNode(15)
nodeE = TreeNode(21)
nodeF = TreeNode(32)

root.left_node = nodeA
root.right_node = nodeB
nodeA.left_node = nodeC
nodeA.right_node = nodeD
nodeB.left_node = nodeE
nodeB.right_node = nodeF

"""
            R(20)
     A(12)         B(29)
 C(7)   D(15)  E(21)   F(32)

"""

def search(node, target):
    if node is None: # if node no found
        return
    elif node.value == target: # if node is found 
        return node
    elif target < node.value: # if target is less than node value, search left subtree
        return search(node.left_node, target)
    else:
        return search(node.right_node, target) # search right subtree

result = search(root, 31)
if result:
    print(result.value)
else:
    print(result)

def insert(node, value):
    if node is None:
        return TreeNode(value)
    elif value < node.value: # if value less than node value, insert left subtree
        node.left = insert(node.left_node, value)
    elif value > node.value:
        node.right = insert(node.right_node, value) # if value more than node value, insert right subtree
    else:
        return node # if node already exist
    return node


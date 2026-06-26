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
def inOrderTraversal(node):
    if node is None:
        return
    inOrderTraversal(node.left_node)
    print(node.value)
    inOrderTraversal(node.right_node)

def delete(node, value):
    # remove the node from parent node
    # link the child nodes to parent node

    if node is None:
        return
    
    if value < node.value: # node in left subtree
        node.left_node = delete(node.left_node, value)
    elif value > node.value: # node in right subtree
        node.right_node = delete(node.right_node, value)
    else: # found node
        # if node has no child, or one child
        if node.left_node is None: # return right node if no left node
            return node.right_node
        elif node.right_node is None:
            return node.left_node # return left node if no right node
        else:
            node.data = node.right_node.data
            node.right_node = None
    return node 

delete(root, 15)
inOrderTraversal(root)
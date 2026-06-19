class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left_node = nodeA
root.right_node = nodeB
nodeA.left_node = nodeC
nodeA.right_node = nodeD
nodeB.left_node = nodeE
nodeB.right_node = nodeF
nodeF.left_node = nodeG

print("root.right.right.left.value:", root.right_node.right_node.left_node.value)
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: # method signature
        l1_node = l1
        l2_node = l2
        carry = 0
        head_node = None
        temp_node = None

        # if l1 or l2 have nodes, or if carry happens
        while l1_node or l2_node or carry:
            l1_val = 0
            l2_val = 0

            # extract l1 & l2 node values, and move pointer to next node nodes
            if l1_node:
                l1_val = l1_node.val
                l1_node = l1_node.next
            if l2_node:
                l2_val = l2_node.val
                l2_node = l2_node.next

            sum = l1_val + l2_val + carry 
            digit = sum % 10 # remainder
            carry = sum // 10 # integer division
            
            # create new using node sum
            new_node = ListNode(digit) # ListNode(7),  ListNode(0),  ListNode(8)

            # print(new_node.val) # [7, 0, 8] => head_node => 8 => 0 => 7 
            # head_node => 7 => 0 => 8, [8, 0, 7]

            if not head_node: #if linked list is empty
                temp_node = head_node = new_node # ListNode(7): temp_node & head_node=>7, 7.next=None
                print(f"id of temp_node: {id(temp_node)}, id of head_node: {id(head_node)}")
            else: #if linked list is not empty
                # ListNode(0): temp_node & head_node=>7, 7.next=>None. So temp_node.next = new_node => 7.next = new_node, temp_node & head_node=>7, 7.next=>0, 0.next=>None
                # ListNode(8): head_node=>7, 7.next=>(temp_node=>ListNode(0))0, 0.next=None. So temp_node.next = new_node => 0.next = new node, head_node=>7, 7.next=>(temp_node=>ListNode(0))0, 0.next=>8, 8.next=>None
                temp_node.next = new_node
                temp_node = new_node # ListNode(0): temp_node = 0 | ListNode(8): temp_node = 8
        return head_node

l1_a = ListNode(2) 
l1 = l1_a # l1=>2, .next=>None

l1_b = ListNode(4) 
l1_b.next = l1 # l1_b.next = l1 = l1_a
l1 = l1_b # l1=>4, .next=>2, .next=>None

l1_c = ListNode(3)
l1_c.next = l1 # l1_c.next = l1 = l1_b
l1 = l1_c # l1=>3, .next=>4, .next=>2, .next=>None

l2_a = ListNode(5)
l2 = l2_a
l2_b = ListNode(6)
l2_b.next = l2
l2 = l2_b
l2_c = ListNode(4)
l2_c.next = l2
l2 = l2_c

solution = Solution()
solution.addTwoNumbers(l1, l2)
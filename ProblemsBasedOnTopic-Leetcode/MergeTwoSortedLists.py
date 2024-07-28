"""
21. Merge Two Sorted Lists
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

-> The number of nodes in both lists is in the range [0, 50].
-> -100 <= Node.val <= 100
-> Both list1 and list2 are sorted in non-decreasing order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        elif list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    def createLinkedList(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def display(self, node=None):
        while node:
            print(node.val, end="-->")
            node = node.next
        print("Null")


s = Solution()
list1 = s.createLinkedList([1, 2, 4])
list2 = s.createLinkedList([1, 3, 4])
merged = s.mergeTwoLists(list1, list2)
s.display(merged)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Mergesorting a linked list
1. Use a fast/slow pointer approach to find middle of linked list
2. Disjoin the two halfs of the LL
3. Stitch two halfs together in sort order using merge function
4. r

'''


class Solution:
    # Method 2 - two pointer approach to split list in half then mergesort
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Traverse fast, slow until fast reached end. Then slow will be at midpoint
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Hold track of start of 2nd half of list
        start2ndHalf = slow.next
        # Break link from 1st half
        slow.next = None

        l, r = self.sortList(head), self.sortList(start2ndHalf)
        return self.merge(l, r)


    def merge(self, l, r):
        if not l or not r:
            return l or r

        root = p = ListNode(0)
        while l and r:
            # If left is smaller, append next left node
            if l.val < r.val:
                p.next = l
                l = l.next
            # If right is smaller, append next right node
            else:
                p.next = r
                r = r.next

            p = p.next

        # which every list remains 
        p.next = l or r
        return root.next


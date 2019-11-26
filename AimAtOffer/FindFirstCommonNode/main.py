# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        h1 = pHead1
        h2 = pHead2

        t1 = 0
        t2 = 0
        
        while(h1):
            t1 += 1
            h1 = h1.next
        while(h2):
            t2 += 1
            h2 = h2.next
        
        h1 = pHead1
        h2 = pHead2
        if(t1 >= t2):
            t = t1 - t2
            while(t):
                h1 = h1.next
                t -= 1
        else:
            t = t2 - t1
            while(t):
                h2 = h2.next
                t2 -= 1

        while((h1 != None) & (h2 != None)):
            if(h1 == h2):
                return h1
            h1 = h1.next
            h2 = h2.next
        return None
'''

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        h1 = pHead1
        h2 = pHead2
        while(h1 != h2):
            if(h1):
                h1 = h1.next
            else:
                h1 = pHead1
            if(h2):
                h2 = h2.next
            else:
                h2 = pHead2
        return h1

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    n1 = ListNode(6)
    n2 = ListNode(7)

    n1.next = n2
    n2.next = node3

    sol = Solution()
    n = sol.FindFirstCommonNode(node1, n1)
    print(n.val)

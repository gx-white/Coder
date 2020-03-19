# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    def __init__(self):
        self.x = 0
    def FindKthToTail(self, head, k):
        # write code here
        if(head == None):
            return None
        node = 0
        if(head.next == None):
            self.x = 1
        else:
            node = self.FindKthToTail(head.next, k)
            self.x = self.x + 1
        if(self.x == k):
            node = head
        if(node == 0):
            return None
        return node
'''
# 快慢指针的做法
class Solution:
    def __init__(self):
        self.x = 0
    def FindKthToTail(self, head, k):
        # write code here
        if(head == None):
            return None
        p1 = head
        p2 = head
        while(k > 0) & (p2 != None):
            p2 = p2.next
            k -= 1
        if(k != 0):
            return None
        while(p2 != None):
            p2 = p2.next
            p1 = p1.next
        return p1

        

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

    sol = Solution()
    print(sol.FindKthToTail(node1, 5))

        
            
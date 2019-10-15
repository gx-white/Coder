# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if(not pHead):
            return pHead
        if(pHead.next == None):
            return pHead
        if(pHead == None):
            return pHead
        
        tHead1 = ListNode(0)
        tHead2 = ListNode(0)
        temp = ListNode(0)

        tHead1.next = pHead
        tHead2.next = pHead.next

        pHead.next = None
        while(1):
            tHead1.next = tHead2.next.next
            tHead2.next.next = pHead
            if(tHead1.next.next == None):
                tHead1.next.next = tHead2.next
                return tHead1.next
            temp.next = tHead1.next.next
            pHead = tHead1.next
            pHead.next = tHead2.next
            tHead2 = temp
            if(tHead2.next.next == None):
                break
        return tHead2.next

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
    node = sol.ReverseList(1)
    while(node):
        print(node.val)
        node = node.next
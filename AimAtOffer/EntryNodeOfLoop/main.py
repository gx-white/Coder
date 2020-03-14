# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if(pHead == None):
            return None
        
        fast = pHead
        slow = pHead

        flag = 0
        while((slow != None) & (fast.next != None)):
                fast = fast.next.next
                slow = slow.next
                if(fast.val == slow.val):
                    flag = 1
                    break
        if(flag == 0):
            return None
        fast = pHead
        while(fast.val != slow.val):
            fast = fast.next
            slow = slow.next
        return fast
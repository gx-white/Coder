# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if(pHead == None):
            return pHead
        if(pHead.next == None):
            return pHead
        head = ListNode(1)
        head.next = pHead
        pre = head
        last = head.next
        while(last != None):
            if(last.next != None):
                if(last.next.val == last.val):
                    while(last.next.val == last.val):
                        last = last.next
                        if(last.next == None):
                            break
                    pre.next = last.next
                    last = last.next
                else:
                    pre = pre.next
                    last = last.next

            else:
                pre = pre.next
                last = last.next

        return head.next

        
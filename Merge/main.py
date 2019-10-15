# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if(not pHead1) or (not pHead2):
            return pHead1 or pHead2
        
        # 保证pHead的第一个是小的
        if(pHead1.val > pHead2.val):
            head = pHead2
            pHead2 = pHead1
            pHead1 = head
        
        head = pHead1
        while(pHead1.next != None):
            if(pHead2 != None):  
                left1 = pHead1
                right1 = pHead1.next
                left2 = pHead2
                right2 = pHead2
                flag = 0
                while((pHead2.val >= pHead1.val) & (pHead2.val <= pHead1.next.val)):
                    flag = 1
                    right2 = pHead2
                    pHead2 = pHead2.next
                    if(pHead2 == None):
                        break
                if(flag == 1):
                    left1.next = left2
                    right2.next = right1
                pHead1 = right1
            else:
                break
        if(pHead2 != None):
            pHead1.next = pHead2
        return head
'''
# 递归方式
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if(not pHead1) or (not pHead2):
            return pHead1 or pHead2
        
        if(pHead1.val <= pHead2.val):
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2

if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(2)
    node3 = ListNode(2)
    node4 = ListNode(2)
    node5 = ListNode(2)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    list1 = ListNode(1)
    list2 = ListNode(1)
    list3 = ListNode(1)
    list4 = ListNode(1)
    list5 = ListNode(1)

    list1.next = list2
    list2.next = list3
    list3.next = list4
    list4.next = list5

    sol = Solution()
    head = sol.Merge(node1, list1)
    while(head):
        print(head.val)
        head = head.next
                
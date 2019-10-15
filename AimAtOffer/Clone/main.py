# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
# 不太好看的写法
'''
class Solution:
    #RandomListNode
    def Clone(self, pHead):
        # write code here
        if(pHead == None):
            return None
        head = self.digui(pHead)

        cur_head = head
        while(cur_head):
            new = head
            while(new):
                if(pHead.random == None):
                    pHead = pHead.next
                    cur_head = cur_head.next
                    if(pHead == None):
                        break
                if(new.label == pHead.random.label):
                    cur_head.random = new
                    pHead = pHead.next
                    cur_head = cur_head.next
                    while(pHead.random == None):
                        pHead = pHead.next
                        cur_head = cur_head.next
                        if(pHead == None):
                            break
                    break
                new = new.next
        return head

    def digui(self, pHead):
        if(pHead.next == None):
            temp = RandomListNode(pHead.label)
            return temp
        head = RandomListNode(pHead.label)
        head.next = self.digui(pHead.next)
        return head
'''
# 反而耗时长
class Solution:
    #RandomListNode
    def Clone(self, pHead):
        # write code here
        if(pHead == None):
            return None
        head = self.digui(pHead)

        cur_head = head
        while(cur_head):
            new = head
            while(new):
                try:
                    if(new.label == pHead.random.label):
                        cur_head.random = new
                        pHead = pHead.next
                        cur_head = cur_head.next
                        break
                except:
                    while(pHead.random == None):
                        pHead = pHead.next
                        cur_head = cur_head.next
                        if(pHead == None):
                            break
                    break
                new = new.next
        return head

    def digui(self, pHead):
        if(pHead.next == None):
            temp = RandomListNode(pHead.label)
            return temp
        head = RandomListNode(pHead.label)
        head.next = self.digui(pHead.next)
        return head

if __name__ == "__main__":
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    n5 = RandomListNode(5)

    n1.next = n2
    n2.next = n3
    n2.random = n5
    n3.next = n4
    n3.random = n3
    n4.next = n5
    n4.random = n2

    sol = Solution()
    temp = sol.Clone(n1)
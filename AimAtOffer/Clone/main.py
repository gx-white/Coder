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
'''
class Solution:
    #RandomListNode
    def Clone(self, pHead):
        # write code here
        if(pHead == None):
            return None
        head = pHead
        # 完成将新节点插到老节点后面
        while(pHead):
            copy = RandomListNode(pHead.label)
            copy.next = pHead.next
            pHead.next = copy
            pHead = copy.next
        ###
        pHead = head
        while(pHead):
            if(pHead.random != None):
                pHead.next.random = pHead.random.next
            pHead = pHead.next.next
        
        pHead = head
        copy = pHead.next
        copy_head = copy
        while(copy.next):
            pHead.next = copy.next
            copy.next = pHead.next.next
            pHead = pHead.next
            copy = pHead.next
        pHead.next = None
        return copy_head
        


if __name__ == "__main__":
    n1 = RandomListNode(1)
    n2 = RandomListNode(2)
    n3 = RandomListNode(3)
    n4 = RandomListNode(4)
    n5 = RandomListNode(5)

    n1.next = n2
    n1.random = n3
    n2.next = n3
    n2.random = n5
    n3.next = n4
    n4.next = n5
    n4.random = n2

    sol = Solution()
    temp = sol.Clone(n1)
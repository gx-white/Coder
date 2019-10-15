# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        arr = []
        while(listNode != None):
            arr.append(listNode.val)
            listNode = listNode.next
        return arr[::-1]  # 逆序打印
        # [start:end:step]
'''
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.arr = []
    def printListFromTailToHead(self, listNode):
        # write code here
        if(listNode != None):
            self.printListFromTailToHead(listNode.next)  # 递归到尾，再添加
            self.arr.append(listNode.val)
        return self.arr

        
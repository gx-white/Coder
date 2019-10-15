# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        if(len(self.stack2) == 0):
            while(self.stack1):
                self.stack2.append(self.stack1.pop())
        if(len(self.stack2) == 0):  # 不需要这个判断也可以通过，最好判断一下
            return False            # IndexError: pop from empty list
        return self.stack2.pop()
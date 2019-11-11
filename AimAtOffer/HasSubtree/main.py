# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
# 这种写法不够直观，所以采用下面的方式，更直白一点，实际上是一样的
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if((pRoot2 == None) | (pRoot1 == None)):
            return False
        return self.isSubtree(pRoot1, pRoot2) | self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)
        
    
    def isSubtree(self, pRoot1, pRoot2):
        if(pRoot2 == None):
            return True
        if(pRoot1 == None):
            return False

        if(pRoot1.val == pRoot2.val):
            return self.isSubtree(pRoot1.left, pRoot2.left) & self.isSubtree(pRoot1.right, pRoot2.right)
        else:
            return False
'''
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if((pRoot2 == None) | (pRoot1 == None)):
            return False
        result = False
        if(pRoot1.val == pRoot2.val):
            # 如果这里直接return，则会导致无法完全遍历，遇到第一个相等的点之后就不管后面的了，很有可能有多个相等的点
            result = self.isSubtree(pRoot1.left, pRoot2.left) & self.isSubtree(pRoot1.right, pRoot2.right)
        if(not result):
            return self.HasSubtree(pRoot1.left, pRoot2) | self.HasSubtree(pRoot1.right, pRoot2)
        return result
    
    def isSubtree(self, pRoot1, pRoot2):
        if(pRoot2 == None):
            return True
        if(pRoot1 == None):
            return False

        if(pRoot1.val == pRoot2.val):
            return self.isSubtree(pRoot1.left, pRoot2.left) & self.isSubtree(pRoot1.right, pRoot2.right)
        else:
            return False
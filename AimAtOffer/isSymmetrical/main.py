#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
题目描述
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

思路：
左子树的左子树 == 右子树的左子树
左子树的右子树 == 右子树的左子树

我还是就记递归的做法吧。
'''
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if(pRoot == None):
            return True
        return self.digui(pRoot.left, pRoot.right)
    
    def digui(self, left, right):
        if((left != None) & (right != None)):
            return (left.val == right.val) & self.digui(left.left, right.right) & self.digui(left.right, right.left)
        elif((left == None) & (right == None)):
            return True
        return False
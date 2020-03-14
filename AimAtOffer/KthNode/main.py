# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

二叉搜索树是左<中<右，按照中序遍历来。
（要会解应用题啊！！）
'''
class Solution:
    def __init__(self):
        self.count = 0
        self.result = None
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if(k == 0):
            return None
        self.zhongxu(pRoot, k)
        return self.result
    
    def zhongxu(self, pRoot, k):
        if(pRoot == None):
            pass
        else:
            if(self.result == None):
                self.zhongxu(pRoot.left, k)
            self.count += 1
            if(self.count == k):
                self.result = pRoot
                return
            if(self.result == None):
                self.zhongxu(pRoot.right, k)
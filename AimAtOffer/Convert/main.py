# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
class Solution:
    def __init__(self):
        self.left_flag = False
        self.right_flag = False
    def Convert(self, pRootOfTree):
        # write code here
        if(pRootOfTree == None):
            return None

        return self.digui(pRootOfTree)[0]
        
    # 这个函数要返回当前节点作为根节点的二叉树的双向链表，
    # 返回值包含head，tail
    # 如果是向左子树递归，则
    # 如果是向右子树递归，则
    # 结束条件是找到了最小结构
    # 最小结构定义为：有左子树，则左子树没有子结点；有右子树，则右子树没有子结点
    def digui(self, pRootOfTree):
        head = pRootOfTree
        tail = pRootOfTree
        if(pRootOfTree.left):
            if((pRootOfTree.left.left == None) & (pRootOfTree.left.right == None)):  # 结束条件
                pRootOfTree.left.right = pRootOfTree
                head = pRootOfTree.left
            else:
                # 向左子树递归
                head, tail_temp = self.digui(pRootOfTree.left)
                pRootOfTree.left = tail_temp
                tail_temp.right = pRootOfTree
    
        if(pRootOfTree.right):
            if((pRootOfTree.right.left == None) & (pRootOfTree.right.right == None)):  # 结束条件
                pRootOfTree.right.left = pRootOfTree
                tail = pRootOfTree.right
            else:
                # 向右子树递归
                head_temp, tail = self.digui(pRootOfTree.right)
                pRootOfTree.right = head_temp
                head_temp.left = pRootOfTree
        return head, tail
'''
# 中序遍历多加了一个pre
class Solution:
    def __init__(self):
        self.pre = None
    def Convert(self, pRootOfTree):
        # write code here
        if(pRootOfTree == None):
            return None
        self.digui(pRootOfTree)
        while(self.pre.left):
            self.pre = self.pre.left
        return self.pre

    def digui(self, pRootOfTree):
        if(pRootOfTree == None):
            return 
        self.digui(pRootOfTree.left)
        pRootOfTree.left = self.pre
        if(self.pre):
            self.pre.right = pRootOfTree
        self.pre = pRootOfTree

        self.digui(pRootOfTree.right)

if __name__ == "__main__":
    n1 = TreeNode(12)
    n2 = TreeNode(5)
    n3 = TreeNode(2)
    n4 = TreeNode(9)
    n5 = TreeNode(18)
    n6 = TreeNode(15)
    n7 = TreeNode(19)
    n8 = TreeNode(17)
    n9 = TreeNode(16)
    n10 = TreeNode(8)

    n1.left = n2
    n1.right = n5
    n2.left = n3
    n2.right = n4
    n4.left = n10
    n5.left = n6
    n5.right = n7
    n6.right = n8
    n8.left = n9

    sol = Solution()
    a = sol.Convert(n1)
    print(1)
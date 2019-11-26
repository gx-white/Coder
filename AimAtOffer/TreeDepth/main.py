# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.num = 1   # 用来存储当前最深的深度
    def TreeDepth(self, pRoot):
        # write code here
        if(pRoot == None):
            return 0
        self.digui(pRoot, 1)
        return self.num

    def digui(self, pRoot, count):
        if((pRoot.left == None) & (pRoot.right == None)):
            if(self.num < count):
                self.num = count
        if(pRoot.left):
            self.digui(pRoot.left, count+1)
        if(pRoot.right):
            self.digui(pRoot.right, count+1)

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
    print(sol.TreeDepth(n1))
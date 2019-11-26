# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return (self.getDepth(pRoot) != -1)

    def getDepth(self, pRoot):
        if(pRoot == None):
            return 0
        left = self.getDepth(pRoot.left)
        if(left == -1):
            return -1
        right = self.getDepth(pRoot.right)
        if(right == -1):
            return -1
        return -1 if abs(left - right) > 1 else 1 + max(left, right)

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
    print(sol.IsBalanced_Solution(n1))

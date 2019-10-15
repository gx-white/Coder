# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        tinL = tin[:tin.index(pre[0])]
        tinR = tin[tin.index(pre[0])+1:]
        root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tinL)
        root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tinR)
        return root

if __name__ == "__main__":
    sol = Solution()
    sol.reConstructBinaryTree([1,2,4,7,3,5,6,8], [4,7,2,1,5,3,8,6])
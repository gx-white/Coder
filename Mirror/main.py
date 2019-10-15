# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if(root == None):
            return root
        if((root.left == None) & (root.right == None)):
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.Mirror(root.left) 
        self.Mirror(root.right)

        return root

if __name__ == "__main__":
    n1 = TreeNode(8)
    n2 = TreeNode(6)
    n3 = TreeNode(10)
    n4 = TreeNode(5)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(11)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    sol = Solution()
    sol.Mirror(n1)


        
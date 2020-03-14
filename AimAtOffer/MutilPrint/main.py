# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

这个就是上个题目说的层次遍历按层打印
'''
'''
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if(pRoot == None):
            return []

        result = []
        result.append([pRoot.val])
        node_list = [pRoot]
        while(1):
            temp_node_list = []
            current_layer = []
            while(node_list):
                if(node_list[0].left):
                    temp_node_list.append(node_list[0].left)
                    current_layer.append(node_list[0].left.val)
                if(node_list[0].right):
                    temp_node_list.append(node_list[0].right)
                    current_layer.append(node_list[0].right.val)
                node_list.pop(0)
            if(len(temp_node_list) == 0):
                break
            result.append(current_layer)
            node_list = temp_node_list
        return result
'''
# 递归方法
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def __init__(self):
        self.result = []
    def Print(self, pRoot):
        # write code here
        if(pRoot == None):
            return []
        self.align(pRoot, 1)
        return self.result
    def align(self, root, depth):
        if(root):
            if(len(self.result) < depth):
                self.result.append([])
            self.result[depth-1].append(root.val)
            if(root.left):
                self.align(root.left, depth+1)
            if(root.right):
                self.align(root.right, depth+1)
if __name__ == "__main__":
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(10)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(11)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5

    node3.left = node6
    node3.right = node7

    sol = Solution()
    print(sol.Print(node1))
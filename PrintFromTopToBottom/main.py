# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if(not root):
            return []
        arr = []
        arr.append(root.val)
        node_list = []
        root_list = [root]
        while(root_list):
            for each in root_list:
                if(each.left):
                    node_list.append(each.left)
                if(each.right):
                    node_list.append(each.right)
            root_list = []
            for each in node_list:
                arr.append(each.val)
                root_list.append(each)
            node_list = []
            '''
            尝试写成
            for each in node_list:
                arr.append(each.val)
            root_list = node_list
            但是这样程序运行时间更长了
            '''
        return arr
"""
# 以队列的形式来写，相当于把我上面的方法更加精简了
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if(not root):
            return []
        arr = []
        node_list = [root]
        while(node_list):
            if(node_list[0].left):
                node_list.append(node_list[0].left)
            if(node_list[0].right):
                node_list.append(node_list[0].right)
            arr.append(node_list.pop(0).val)
        return arr
if __name__ == "__main__":
    n1 = TreeNode(8)
    n2 = TreeNode(6)
    n3 = TreeNode(10)
    n4 = TreeNode(5)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(11)
    n8 = TreeNode(2)
    n9 = TreeNode(4)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9


    sol = Solution()
    print(sol.PrintFromTopToBottom(n1))
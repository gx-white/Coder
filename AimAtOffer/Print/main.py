# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
题目描述
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。

还是从层次遍历出发...昨天做的时候感觉要定义好几个数组，最终不想看了。
今天又重新看了一下层次遍历的代码。虽然做法不是很好，不过结果是好der

层次遍历打印/层次遍历分层打印
'''
class Solution:
    def Print(self, pRoot):
        # write code here
        if(pRoot == None):
            return []

        count = 0
        result = []
        result.append([pRoot.val])
        node_list = [pRoot]
        while(1):
            temp = []
            while(node_list):
                if(node_list[0].left):
                    temp.append(node_list[0].left)
                if(node_list[0].right):
                    temp.append(node_list[0].right)
                node_list.pop(0)
            if(len(temp) == 0):
                break
            table = []
            for each in temp:
                table.append(each.val)
            if((count % 2) == 1):
                result.append(table)
            else:
                result.append(table[::-1])
            node_list = temp
            count += 1
        return result

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
        
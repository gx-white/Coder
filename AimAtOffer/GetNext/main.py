#-*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

思路：
用了笨办法，但是也做对了很开心啊哈哈。不过我竟然写错了中序遍历...羞愧

正确做法是：如果当前节点有右节点，那么下一个节点就是右子树的最左边的节点
          如果当前节点没有右节点，那么下一个节点就是第一个以当前节点为左子树的父节点
'''
'''
# 笨办法
class Solution:
    def __init__(self):
        self.flag = 0
        self.result = 0
    def GetNext(self, pNode):
        # write code here
        # pNode应该是指其中的一个节点，self.next表示该节点的父节点
        if(pNode == None):
            return None

        pRoot = pNode
        while(pRoot.next != None):
            pRoot = pRoot.next

        self.bianli(pNode, pRoot)
        return self.result.val

    def bianli(self, pNode, pRoot):
        if(pRoot.left != None):
            self.bianli(pNode, pRoot.left)
        if(self.flag == 1):
            if(self.result == 0):
                self.result = pRoot
        if(pRoot == pNode):
            self.flag = 1
        if(pRoot.right != None):
            self.bianli(pNode, pRoot.right)
'''
class Solution:
    def __init__(self):
        self.flag = 0
        self.result = 0
    def GetNext(self, pNode):
        # write code here
        if(pNode == None):
            return None
        if(pNode.right != None):
            p = pNode.right
            while(p.left):
                p = p.left
            return p
        else:
            while(pNode.next):
                if(pNode.next.left == pNode):
                    return pNode.next
                pNode = pNode.next
            return None

if __name__ == "__main__":
    node1 = TreeLinkNode(1)
    node2 = TreeLinkNode(2)
    node3 = TreeLinkNode(3)
    node4 = TreeLinkNode(4)
    node5 = TreeLinkNode(5)

    node1.next = None
    node1.left = node2
    node1.right = node4

    node2.next = node1
    node2.left = node3

    node3.next = node2

    node4.next = node1
    node4.left = node5

    node5.next = node4

    sol = Solution()
    print(sol.GetNext(node1))
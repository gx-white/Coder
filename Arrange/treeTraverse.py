# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class treeTraverse:
    def __init__(self):
        self.result = []
    # 这里就写遍历打印输出吧
    def preorderTraverse(self, pRoot):
        if(pRoot == None):
            return
        self.result.append(pRoot.val)
        self.preorderTraverse(pRoot.left)
        self.preorderTraverse(pRoot.right)
        return self.result
    def inorderTraverse(self, pRoot):
        if(pRoot == None):
            return
        self.inorderTraverse(pRoot.left)
        self.result.append(pRoot.val)
        self.inorderTraverse(pRoot.right)
        return self.result
    def postorderTraverse(self, pRoot):
        if(pRoot == None):
            return
        self.postorderTraverse(pRoot.left)
        self.postorderTraverse(pRoot.right)
        self.result.append(pRoot.val)
        return self.result
    # 用队列去实现
    def levelorderTraverse(self, pRoot):
        if(pRoot == None):
            return []
        node_list = [pRoot]
        while(node_list):
            node_list.append(node_list[0].left) if node_list[0].left else 1
            node_list.append(node_list[0].right) if node_list[0].right else 1
            self.result.append(node_list.pop(0).val)
        return self.result
    # 按行打印
    # 可以再直接打印的基础上，储存当前层的数字
    # 这里写比较巧妙的递归方式
    def levelorderTraverseLine(self, pRoot, depth=None):
        if(pRoot == None):
            return []
        depth = 1 if not isinstance(depth, (int, float)) else depth

        if(len(self.result) < depth):
            self.result.append([])
        self.result[depth-1].append(pRoot.val)
        self.levelorderTraverseLine(pRoot.left, depth+1)
        self.levelorderTraverseLine(pRoot.right, depth+1)
        return self.result

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

    sol = treeTraverse()
    print(sol.postorderTraverse(n1))
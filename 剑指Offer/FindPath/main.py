# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.x = []
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if(root == None):
            return []
        if(expectNumber == 0):
            return []
        arr = []
        self.digui(root, expectNumber, arr)
        # 排序
        if(self.x):
            max_length = 0
            length = len(self.x)
            for i in range(0, length):
                max_length = len(self.x[i])
                index = i
                for j in range(i+1, length):
                    if(len(self.x[j]) > max_length):
                        max_length = len(self.x[j])
                        index = j
                if(i != index):
                    temp = self.x[i]
                    self.x[i] = self.x[index]
                    self.x[index] = temp
                    
        return self.x

    def digui(self, root, expectNumber, arr):
        if((expectNumber-root.val == 0) & (root.left == None) & (root.right == None)):
            arr.append(root.val)
            # 这里如果直接self.x.append(temp)是地址传递，导致之后这个值会随着不断的append/pop改变
            temp = []
            for each in arr:  
                temp.append(each)  
            self.x.append(temp) 
            # end
            return True
        arr.append(root.val)
        result = False
        if(root.left):
            result = self.digui(root.left, expectNumber-root.val, arr)
            arr.pop()
        if(root.right):
            result = self.digui(root.right, expectNumber-root.val, arr)
            arr.pop()
        return result

if __name__ == "__main__":
    n1 = TreeNode(8)
    n2 = TreeNode(6)
    n3 = TreeNode(10)
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(10)
    n8 = TreeNode(1)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n7.left = n8

    sol = Solution()
    print(sol.FindPath(n1, 29))
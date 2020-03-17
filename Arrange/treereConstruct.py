# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class treereConstruct:
    def reConstructPreoderInorder(self, pre, tin):
        if(len(pre) == 0):
            return None
        if(len(pre) == 1):
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        tinL = tin[:tin.index(pre[0])]
        tinR = tin[tin.index(pre[0])+1 :]    
        root.left = self.reConstructPreoderInorder(pre[1:tin.index(pre[0])+1], tinL)
        root.right = self.reConstructPreoderInorder(pre[tin.index(pre[0])+1:], tinR)
        return root
    def reConstructInoderPostorder(self, tin, post):
        if(len(tin) == 0):
            return None
        if(len(tin) == 1):
            return TreeNode(post[-1])
        
        root = TreeNode(post[-1])
        tinL = tin[:tin.index(post[-1])]
        tinR = tin[tin.index(post[-1])+1:]
        root.left = self.reConstructInoderPostorder(tinL, post[:len(tinL)])
        root.right = self.reConstructInoderPostorder(tinR, post[len(tinL):-1])
        return root

if __name__ == "__main__":
    sol = treereConstruct()
    root = sol.reConstructInoderPostorder([2, 5, 8, 9, 12, 15, 16, 17, 18, 19], [2, 8, 9, 5, 16, 17, 15, 19, 18, 12])
    print(1)
    # 先 [12, 5, 2, 9, 8, 18, 15, 17, 16, 19]  
    # 中 [2, 5, 8, 9, 12, 15, 16, 17, 18, 19]
    # 后 [2, 8, 9, 5, 16, 17, 15, 19, 18, 12]
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.x = []
        self.minimize = []
        self.top_index = 0
    def push(self, node):
        # write code here
        self.x.append(node)
        if(len(self.minimize) == 0):
            self.minimize.append(node)
        else:
            if(self.minimize[self.top_index] > node):
                self.top_index += 1
                self.minimize.append(node)
            else:
                self.minimize.append(self.minimize[self.top_index])
                self.top_index += 1
    def pop(self):
        # write code here
        self.x.pop()
        self.minimize.pop()
        self.top_index -= 1
    def top(self):
        # write code here
        pass
    def min(self):
        # write code here
        return self.minimize[self.top_index]

if __name__ == "__main__":
    sol = Solution()
    arr = []
    sol.push(3)
    arr.append(sol.min())
    sol.push(4)
    arr.append(sol.min())
    sol.push(2)
    arr.append(sol.min())
    sol.push(3)
    arr.append(sol.min())
    sol.pop()
    arr.append(sol.min())
    sol.pop()
    arr.append(sol.min())
    sol.pop()
    arr.append(sol.min())
    sol.push(0)
    arr.append(sol.min())
    print(arr)
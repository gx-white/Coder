# -*- coding:utf-8 -*-
'''
题目描述：
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

思路：
打算自己尝试一下递归。
做出来了，做的过程中思路还是很清晰的感觉。
这竟然是一种叫回溯的做法
'''
class Solution:
    def __init__(self):
        self.visit = []
        self.result = False
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(0, rows):
            self.visit.append([0 for j in range(0, cols)])
        index = 0
        temp = []
        for i in range(0, rows):
            temp.append([])
            for j in range(0, cols):
                temp[i].append(matrix[index])
                index += 1
        matrix = temp

        # 初始化 self.visit
        for i in range(0, rows):
            for j in range(0, cols):
                if(matrix[i][j] == path[0]):
                    # 执行递归去找
                    self.visit[i][j] = 1
                    if self.digui(matrix, i, j, path[1:], rows, cols):
                        return True
                    else:
                        for ii in range(0, rows):
                            for jj in range(0, cols):
                                self.visit[ii][jj] = 0
        return False
                
    def digui(self, matrix, i, j, path, rows, cols):
        if(path == ''):
            self.result = True
            return True
        
        if(i-1 >= 0):
            if(matrix[i-1][j] == path[0]) & (self.visit[i-1][j] != 1):
                self.visit[i-1][j] = 1
                if self.digui(matrix, i-1, j, path[1:], rows, cols):
                    return True
        if(i+1 <= rows-1):
            if(matrix[i+1][j] == path[0]) & (self.visit[i+1][j] != 1):
                self.visit[i+1][j] = 1
                if self.digui(matrix, i+1, j, path[1:], rows, cols):
                    return True
        if(j-1 >= 0):
            if(matrix[i][j-1] == path[0]) & (self.visit[i][j-1] != 1):
                self.visit[i][j-1] = 1
                if self.digui(matrix, i, j-1, path[1:], rows, cols):
                    return True
        if(j+1 <= cols-1):
            if(matrix[i][j+1] == path[0]) & (self.visit[i][j+1] != 1):
                self.visit[i][j+1] = 1
                if self.digui(matrix, i, j+1, path[1:], rows, cols):
                    return True
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.hasPath('ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS', 5, 8, 'SGGFIECVAASABCEHJIGQEMS'))
# -*- coding:utf-8 -*-
'''
题目描述
地上有一个m行和n列的方格。
一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

思路：
这个题跟上个题应该算是比较类似的吧。先按最多能够达到多少个格子来处理。
竟然做出来了...
这个题不是最远能走到哪个格子的意思，而是说有几个格子可以走。
'''
class Solution:
    def __init__(self):
        self.result = 0
        self.temp = 0
        self.visit = []
    def movingCount(self, threshold, rows, cols):
        # write code here
        for i in range(0, rows):
            self.visit.append([0 for j in range(0, cols)])
        self.visit[0][0] = 1
        self.digui(threshold, 0, 0, rows, cols)
        return self.result

    def digui(self, threshold, i, j, rows, cols):
        sum_i = 0
        temp_i = i
        while(temp_i > 0):
            sum_i += temp_i % 10
            temp_i = temp_i / 10
        sum_j = 0
        temp_j = j
        while(temp_j > 0):
            sum_j += temp_j % 10
            temp_j = temp_j / 10
        if(sum_i + sum_j > threshold):
            if(self.temp > self.result):
                self.result = self.temp
            return
        self.temp += 1
        if(i-1 >= 0):
            if(self.visit[i-1][j] != 1):
                self.visit[i-1][j] = 1
                self.digui(threshold, i-1, j, rows, cols)
        if(i+1 <= rows-1):
            if(self.visit[i+1][j] != 1):
                self.visit[i+1][j] = 1
                self.digui(threshold, i+1, j, rows, cols)
        if(j-1 >= 0):
            if(self.visit[i][j-1] != 1):
                self.visit[i][j-1] = 1
                self.digui(threshold, i, j-1, rows, cols)
        if(j+1 <= cols-1):
            if(self.visit[i][j+1] != 1):
                self.visit[i][j+1] = 1
                self.digui(threshold, i, j+1, rows, cols)
        
        if(j == cols-1) & (i == rows-1):
            if(self.temp > self.result):
                self.result = self.temp
            return
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.movingCount(5, 10, 10))
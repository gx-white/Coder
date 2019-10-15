# -*- coding:utf-8 -*-
'''
# 暴力
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for each in array:
            if(target in each):
                return True
            else:
                continue
'''
'''
# 左下/右上
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        line = len(array[0])
        if(row == 0):
            return False

        i = row-1
        j = 0
        while (i>=0) & (j<line):
            if(array[i][j] == target):
                return True
            elif(array[i][j] > target):
                i = i - 1
            else:
                j = j + 1
        return False
'''
# 二分法
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        for i in range(0, row):
            left = 0
            right = len(array[0])-1
            while(left <= right):
                mid = (left + right) / 2
                if(array[i][mid] == target):
                    return True
                elif(array[i][mid] > target):
                    right = mid - 1
                elif(array[i][mid] < target):
                    left = mid + 1

if __name__ == "__main__":
    # line = sys.stdin.readline().strip()
    sol = Solution()
    if sol.Find(7,[[1,2,8,9],[4,7,10,13]]):
        print('True')
    else:
        print('False')
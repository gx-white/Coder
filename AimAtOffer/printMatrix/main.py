# -*- coding:utf-8 -*-
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if(not matrix):
            return matrix
        row = len(matrix)
        if(row == 1):
            return matrix[0]
        line = len(matrix[0])
        return self.digui(matrix, 0, row, line)

    def digui(self, matrix, width, row, line):
        if((width * 2 >= len(matrix)) | (width * 2 >= len(matrix[0]))):
            return []
        arr = []
        if((width+1) * 2 > len(matrix)):   # 剩下单行
            return matrix[width][width:line-width]
        elif((width+1) * 2 > len(matrix[0])):   # 剩下单列
            for i in range(width, row-width):
                arr.append(matrix[i][width])
            return arr

        for i in range(width, line-width):
            arr.append(matrix[width][i])
        for i in range(width+1, row-width):
            arr.append(matrix[i][line-width-1])
        for i in range(line-width-2, width-1, -1):
            arr.append(matrix[row-width-1][i])
        for i in range(row-width-2, width, -1):
            arr.append(matrix[i][width])
        return arr+self.digui(matrix, width+1, row, line)
'''
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if(not matrix):
            return matrix
        row = len(matrix)
        if(row == 1):
            return matrix[0]

        line = len(matrix[0])
        return self.digui(matrix, 0, line-1, 0, row-1)
    
    def digui(self, matrix, left, right, top, bottom):
        if(left >= right):
            arr = []
            if(left == right):
                for i in range(top, bottom+1):
                    arr.append(matrix[i][left])
            return arr
        if(top >= bottom):
            arr = []
            if(top == bottom):
                for i in range(left, right+1):
                    arr.append(matrix[top][i])
            return arr
        arr = []
        for i in range(left, right+1):
            arr.append(matrix[top][i])
        for i in range(top+1, bottom+1):
            arr.append(matrix[i][right])
        for i in range(right-1, left-1, -1):
            arr.append(matrix[bottom][i])
        for i in range(bottom-1, top, -1):
            arr.append(matrix[i][left])
        return arr + self.digui(matrix, left+1,right-1,top+1,bottom-1)
'''
# 这样更写好理解记忆
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if(not matrix):
            return matrix
        rowEnd = len(matrix) - 1
        if(rowEnd == 0):
            return matrix[0]

        colEnd = len(matrix[0]) - 1
        rowBegin, colBegin = 0, 0
        result = []
        while(rowBegin <= rowEnd) & (colBegin <= colEnd):
            for i in range(colBegin, colEnd+1):
                result.append(matrix[rowBegin][i])
            rowBegin += 1
            for j in range(rowBegin, rowEnd+1):
                result.append(matrix[j][colEnd])
            colEnd -= 1
            if(rowBegin <= rowEnd):
                for i in range(colEnd, colBegin-1, -1):
                    result.append(matrix[rowEnd][i])
            rowEnd -= 1
            if(colBegin <= colEnd):
                for j in range(rowEnd, rowBegin-1, -1):
                    result.append(matrix[j][colBegin])
            colBegin += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.printMatrix([[1, 2],[3, 4]]))
# -*- coding:utf-8 -*-
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

if __name__ == "__main__":
    sol = Solution()
    print(sol.printMatrix([[1,2],[3,4],[5,6],[7,8],[9,10]]))
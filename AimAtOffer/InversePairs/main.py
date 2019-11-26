# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        self.mergeSort(data)
        return self.count
    def mergeSort(self, data):
        length = len(data)
        if(length < 2):
            return data

        mid = length / 2
        left, right = data[0:mid], data[mid:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):
        result = []
        while(left and right):
            if(left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                self.count += len(left)    # 累加
                self.count %= 1000000007   
        while(left):
            result.append(left.pop(0))
        while(right):
            result.append(right.pop(0))
        return result

'''
# 写一下归并排序的代码，便于之后理解这个题目的解法
class Solution:
    def mergeSort(self, data):
        length = len(data)
        if(length < 2):
            return data

        mid = length / 2
        left, right = data[0:mid], data[mid:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):
        result = []
        while(left and right):
            if(left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while(left):
            result.append(left.pop(0))
        while(right):
            result.append(right.pop(0))
        return result
'''
if __name__ == "__main__":
    sol = Solution()
    print(sol.InversePairs([7,1,2,3,4,5,0,6]))
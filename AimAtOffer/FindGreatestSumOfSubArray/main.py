# -*- coding:utf-8 -*-
# 暴力解法
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        length = len(array)
        if(length == 0):
            return 0
        max_sum = -10000

        for i in range(0, length):
            temp_sum = 0
            for j in range(i, length):
                temp_sum += array[j]
                if(temp_sum > max_sum):
                    max_sum = temp_sum
        return max_sum
'''
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        length = len(array)
        if(length == 0):
            return 0
        max_sum = array[0]
        temp_sum = array[0]

        for i in range(1, length):
            if(temp_sum < 0):
                temp_sum = array[i]
            else:
                temp_sum += array[i]
                
            if(temp_sum > max_sum):
                max_sum = temp_sum
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))
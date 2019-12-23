# -*- coding:utf-8 -*-
'''
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        if(length == 1):
            return 0
        elif(length == 2):
            if(array[0] + array[1] == tsum):
                return array[0], array[1]
        
        left = 0
        right = 1
        result = []
        while((left < right) & (left < length) & (right < length)):
            temp = array[left] + array[right]
            if(temp == tsum):
                result.append([array[left], array[right]])
                left += 1
                right = left + 1
            elif(temp < tsum):
                right += 1
            elif(temp > tsum):
                left += 1
                right = left + 1
        min_temp = 1000000
        return_a = 0
        return_b = 0
        if(len(result) == 0):
            return []
        for each in result:
            temp = each[0] * each[1]
            if(temp < min_temp):
                min_temp = temp
                return_a = each[0]
                return_b = each[1]
        return return_a, return_b
'''

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        if(length == 1):
            return 0
        elif(length == 2):
            if(array[0] + array[1] == tsum):
                return array[0], array[1]
        
        left = 0
        right = length - 1
        while(left < right):
            temp = array[left] + array[right]
            if(temp < tsum):
                left += 1
            elif(temp > tsum):
                right -= 1
            else:
                return array[left], array[right]
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.FindNumbersWithSum([1,2,3,4,5,6], 7))

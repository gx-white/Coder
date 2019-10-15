# -*- coding:utf-8 -*-
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if(length == 0):
            return 0
        for i in range(1, length):
            if(rotateArray[i] < rotateArray[i-1]):
                return rotateArray[i]
'''
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        left = 0
        right = length - 1

        while (left < right):
            if(rotateArray[left] < rotateArray[right]):  # 特殊情况，正好最左端指在了最小值上
                return rotateArray[left]
            mid = (left + right) / 2
            if(rotateArray[mid] > rotateArray[left]):
                left = mid + 1
            elif(rotateArray[mid] < rotateArray[right]):
                right = mid
            else:
                left = left + 1
        return rotateArray[left]
'''
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 中间数大于左边就往右递归
        # 中间数小于左边就往左递归
        length = len(rotateArray)
        if(length == 0):
            return 0
        if((rotateArray[0] < rotateArray[length-1]) | (length == 1)):
            return rotateArray[0]
        if(length == 2):
            return rotateArray[1]
        if(rotateArray[length/2] > rotateArray[0]):
            return self.minNumberInRotateArray(rotateArray[length/2+1:])
        else:
            return self.minNumberInRotateArray(rotateArray[0:length/2+1])
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if(number <= 1):
            return number
        temp = 1
        for i in range(2, number + 1):
            temp = temp * 2
        return temp
        
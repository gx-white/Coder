# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0
        for each in data:
            if(each == k):
                count += 1
            else:
                if(count > 0):
                    break
        return count
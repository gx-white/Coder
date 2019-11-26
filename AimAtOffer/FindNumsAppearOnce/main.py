# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        result = {}
        for each in array:
            try:
                result[each] += 1
            except:
                result[each] = 1

        save = []
        for each in result:
            if result[each] == 1:
                save.append(each)
        return save
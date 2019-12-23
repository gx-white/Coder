# -*- coding:utf-8 -*-
'''
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
'''
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        sub_array1 = []
        sub_array2 = []

        temp = 0
        for each in array:
            temp ^= each
        count = 0
        while(not (temp & 1)):
            count += 1
            temp = temp >> 1
        for each in array:
            temp = each >> count
            if(temp & 1):
                sub_array1.append(each)
            else:
                sub_array2.append(each)
        a = 0
        b = 0
        for each in sub_array1:
            a ^= each
        for each in sub_array2:
            b ^= each
        return [a, b]


if __name__ == "__main__":
    sol = Solution()
    print(sol.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))
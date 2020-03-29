# -*- coding:utf-8 -*-
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        arr_odd = []
        arr_even = []
        
        for each in array:
            if(each & 1):
                arr_odd.append(each)
            else:
                arr_even.append(each)
        return arr_odd + arr_even
'''
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        length = len(array)
        if(length == 1):
            return array
        return self.digui(array, length)
        
    def digui(self, array, length):
        if(length == 0):
            return 0
        if(array[length - 1] & 1):  # 是奇数
            i = length - 2
            count = 1
            while((array[i] & 1) & (i >= 0)):
                count = count + 1
                i = i - 1
            if(i == -1):
                return 0
            even = array[i]
            while(count > 0):
                array[i] = array[i+1]
                i = i + 1
                count = count - 1
            array[i] = even
            self.digui(array, length - 1)
        else:
            self.digui(array, length-1)
        
        return array
'''
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        length = len(array)
        if(length == 1):
            return array

        flag = 1
        while(flag):
            i = 0
            flag = 0
            for i in range(1, length):
                if((array[i] & 1) & (array[i-1] & 1 == 0)):  # 前偶后奇
                    temp = array[i]
                    array[i] = array[i-1]
                    array[i-1] = temp
                    flag = 1
        return array
'''
# 这样用了partition的思想，但是会改变原本的位置关系
class Solution:
    def reOrderArray(self, array):
        # write code here
        if not array:
            return array
        length = len(array)
        if(length == 1):
            return array

        i = 0
        j = length - 1
        while(i < j):
            while(array[i] % 2 == 1) & (i < j):
                i += 1
            while(array[j] % 2 == 0) & (i < j):
                j -= 1
            if(i < j):
                array[i], array[j] = array[j], array[i]
        return array
'''
if __name__ == "__main__":
    sol = Solution()
    print(sol.reOrderArray([1,3,5,7,2,4,6]))


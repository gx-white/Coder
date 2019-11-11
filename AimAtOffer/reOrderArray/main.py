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
if __name__ == "__main__":
    sol = Solution()
    print(sol.reOrderArray([2,1]))


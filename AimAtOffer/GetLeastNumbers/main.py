# -*- coding:utf-8 -*-
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if(length == 0):
            return []
        if(k > length):
            return []
        self.QuickSort(tinput,0, length-1)
        return tinput[0:k]

    def QuickSort(self, tinput, start, end):
        if(start >= end):
            return

        i = start
        j = end
        temp = tinput[start]
        while(i != j):
            while((tinput[j] >= temp) & (i < j)):
                j -= 1
            if(i < j):
                tinput[i] = tinput[j]
                i += 1
            while((tinput[i] < temp) & (i < j)):
                i += 1
            if(i < j):
                tinput[j] = tinput[i]
                j -= 1
        tinput[i] = temp
        self.QuickSort(tinput, start, i-1)
        self.QuickSort(tinput, i+1, end)
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if(k > length):
            return []
        for i in range(0, length):
            min_n = tinput[i]
            min_index = i
            for j in range(i+1, length):
                if(tinput[j] < min_n):
                    min_index = j
                    min_n = tinput[j]
            if(min_index != i):
                temp = tinput[i]
                tinput[i] = tinput[min_index]
                tinput[min_index] = temp
            if(i+1 >= k):
                break
        return tinput[0:k]

if __name__ == "__main__":
    sol = Solution()
    print(sol.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 7))
# -*- coding:utf-8 -*-
'''
# 我的方法
class Solution:
    def __init__(self):
        self.table = [1, 2, 3, 4, 5]
        self.base = [2, 3, 5]
    def GetUglyNumber_Solution(self, index):
        # write code here
        if(index == 0):
            return 0
        if(index < 5):
            return self.table[index-1]
        
        i = 5
        start = 0
        while(i < index):
            max_num = 1000000000
            flag = 0
            for j in range(start, len(self.table)):
                ## 加上这个判断，运行时间明显降低了很多
                if(self.table[j] * 5 < self.table[-1]):
                    continue
                ## 
                if(flag == 0):
                    t = j
                    flag = 1
                for each_base in self.base:
                    temp = self.table[j] * each_base
                    if((temp > self.table[-1]) & (temp < max_num)):
                        max_num = temp
                        break
            start = t
            self.table.append(max_num)
            i += 1
        return self.table[-1]
'''
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if(index < 7):
            return index
        t1 = 0
        t2 = 0
        t3 = 0
        arr = [1]
        i = 1
        while(i < index):
            newnum = min(arr[t1]*2, min(arr[t2]*3, arr[t3]*5))
            arr.append(newnum)
            if(newnum == arr[t1]*2):
                t1 += 1
            if(newnum == arr[t2]*3):
                t2 += 1
            if(newnum == arr[t3]*5):
                t3 += 1
            i += 1
        return arr[-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.GetUglyNumber_Solution(1500))




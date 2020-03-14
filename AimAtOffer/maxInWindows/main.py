# -*- coding:utf-8 -*-
'''
题目描述
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： 
{[2,3,4],2,6,2,5,1}， 
{2,[3,4,2],6,2,5,1}， 
{2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， 
{2,3,4,2,[6,2,5],1}， 
{2,3,4,2,6,[2,5,1]}。
'''
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        queues, res, i = [], [], 0
        while(size > 0) & (i < len(num)):
            if(len(queues) > 0): 
                if(i-size+1 > queues[0]):
                    queues.pop(0)
            if(len(queues) > 0): 
                while(len(queues) > 0) & (num[queues[-1]] < num[i]):
                    queues.pop()
                    if(len(queues) == 0):
                        break
            queues.append(i)   # 存储的是坐标，方便比较是否过期
            if(i >= size-1):
                res.append(num[queues[0]])
            i += 1
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxInWindows([10,14,12,11],1))
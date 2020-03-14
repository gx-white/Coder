# -*- coding:utf-8 -*-
'''
题目描述
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''
from heapq import *
# 感觉巧妙之处在于如何保证这两个堆的大小是一样的...
class Solution:
    def __init__(self):
        self.heaps = [], []
    def Insert(self, num):
        # write code here
        small, large = self.heaps   # heaps可以返回堆的最小值，也就是最小堆，要想建立最大堆，就需要取反
        heappush(small, -heappushpop(large, num))
        if(len(large) < len(small)):
            heappush(large, -heappop(small))

    def GetMedian(self):
        # write code here
        small, large = self.heaps
        if(len(large) > len(small)):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        self.mergeSortBottomToTop(data)
        return self.count
    # 换成 迭代写法 的归并排序就过了，虽然耗时还是很久
    def mergeSortBottomToTop(self, arr):
        length = len(arr)
        b = []
        a = arr
        seg = 1
        while(1):
            # for seg in range(1, length):
            for start in range(0, length, seg+seg):
                low = start
                mid = min(start+seg, length)
                high = min(start+seg+seg, length)

                start1, end1, start2, end2 = low, mid, mid, high
                while(start1 < end1) & (start2 < end2):
                    if(a[start1] <= a[start2]):
                        b.append(a[start1])
                        start1 += 1
                    else:
                        b.append(a[start2])
                        start2 += 1
                        self.count += end1 - start1
                        self.count %= 1000000007  
                while(start1 < end1):
                    b.append(a[start1])
                    start1 += 1
                while(start2 < end2):
                    b.append(a[start2])
                    start2 += 1
            a, b = b, []
            seg += seg
            if(seg >= length):
                break
        return a
    
    # 超时 75%
    def mergeSort(self, data):
        length = len(data)
        if(length < 2):
            return data

        mid = length / 2
        left, right = data[0:mid], data[mid:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):
        result = []
        while(left and right):
            if(left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
                self.count += len(left)    # 累加
                self.count %= 1000000007   
        while(left):
            result.append(left.pop(0))
        while(right):
            result.append(right.pop(0))
        return result
    
'''
# 写一下归并排序的代码，便于之后理解这个题目的解法
class Solution:
    def mergeSort(self, data):
        length = len(data)
        if(length < 2):
            return data

        mid = length / 2
        left, right = data[0:mid], data[mid:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, left, right):
        result = []
        while(left and right):
            if(left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while(left):
            result.append(left.pop(0))
        while(right):
            result.append(right.pop(0))
        return result
'''
if __name__ == "__main__":
    sol = Solution()
    print(sol.InversePairs([7,1,2,3,4,5,0,6]))
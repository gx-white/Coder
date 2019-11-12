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
'''
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if(length == 0):
            return []
        if(k > length):
            return []
        self.QuickSort(tinput,0, length-1, k)
        a = tinput[0:k]
        a.sort()
        return a
        
    
    def QuickSort(self, tinput, start, end, k):
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
        if(i > k-1):
            self.QuickSort(tinput, start, i-1, k)
        elif(i < k-1):
            self.QuickSort(tinput, i+1, end, k)
        else:
            return
'''
'''
# 堆排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        size = len(tinput)
        if(size == 0):
            return []
        if(k > size):
            return []
        for i in range(0, size):   # 每次选一个最大的出来，与最后一位交换
            self.maxHeapify(tinput, size-i)
            # 交换
            temp = tinput[0]
            tinput[0] = tinput[size-i-1]
            tinput[size-i-1] = temp
        return tinput[0:k]

    def maxHeapify(self, tinput, size):
        # 完成一次建堆
        for i in range((size-1)/2, -1, -1):
            self.heapify(tinput, i, size)
    # 建堆
    def heapify(self, tinput, currentRootNode, size):
        if(currentRootNode < size):
            left = currentRootNode * 2 + 1
            right = currentRootNode * 2 + 2

            max_index = currentRootNode

            if(left < size):
                if(tinput[left] > tinput[max_index]):
                    max_index = left
            if(right < size):
                if(tinput[right] > tinput[max_index]):
                    max_index = right

            if(max_index != currentRootNode):
                temp = tinput[max_index]
                tinput[max_index] = tinput[currentRootNode]
                tinput[currentRootNode] = temp
'''
# 基于堆排序
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        size = len(tinput)
        if(size == 0):
            return []
        if(k > size):
            return []
        if(k == 0):
            return []

        heap = tinput[0:k]
        self.maxHeapify(heap, k)
        for i in range(k, size):
            if(tinput[i] >= heap[0]):
                pass
            else:
                heap[0] = tinput[i]
                self.maxHeapify(heap, k)
        for i in range(0, k):
            self.maxHeapify(heap, k-i)

            temp = heap[0]
            heap[0] = heap[k-i-1]
            heap[k-i-1] = temp
        return heap


    def maxHeapify(self, tinput, size):
        # 完成一次建堆，堆大小为k
        for i in range((size-1)/2, -1, -1):
            self.heapify(tinput, i, size)

    # 建堆
    def heapify(self, tinput, currentRootNode, size):
        if(currentRootNode < size):
            left = currentRootNode * 2 + 1
            right = currentRootNode * 2 + 2

            max_index = currentRootNode

            if(left < size):
                if(tinput[left] > tinput[max_index]):
                    max_index = left
            if(right < size):
                if(tinput[right] > tinput[max_index]):
                    max_index = right

            if(max_index != currentRootNode):
                temp = tinput[max_index]
                tinput[max_index] = tinput[currentRootNode]
                tinput[currentRootNode] = temp
    


if __name__ == "__main__":
    sol = Solution()
    print(sol.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 8))
# -*- coding:utf-8 -*-
class Sort:
    def selectionSort(self, arr):
        length = len(arr)

        for i in range(0, length):
            max_index = i
            for j in range(i, length):
                if(arr[max_index] < arr[j]):
                   max_index = j
            if(max_index != i):
                arr[max_index], arr[i] = arr[i], arr[max_index]
        return arr

    def bubbleSort(self, arr):
        length = len(arr)

        for i in range(1, length):
            for j in range(0, length-i):
                if(arr[j] > arr[j+1]):
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        return arr

    # 前面n个是排好的，然后把第n+1个数插入到n个数中。
    def insertionSort(self, arr):
        length = len(arr)

        for i in range(1, length):      # 未排序数组部分，初始认为0是已经排序了的
            current_compare = i-1       # 当前要比较的下标
            while(current_compare >= 0) & (arr[current_compare] > arr[i]):
                arr[current_compare+1] = arr[current_compare]      # 在比较的过程中不断后移
                current_compare -= 1
            arr[current_compare] = arr[i]
        return arr
    
    '''
    归并排序的思路就是：
    1. 分割 2. 归并
    递归方式就是 自顶向下
    迭代方式就是 自底向上
    '''
    def mergeSortTopToBottom(self, arr):
        length = len(arr)

        mid = length / 2
        left, right = arr[0, mid], arr[mid, length]
        return self.merge(self.mergeSortTopToBottom(left), self.mergeSortTopToBottom(right))
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

    # 自底向上
    def mergeSortBottomToTop(self, arr):
        length = len(arr)
        b = []
        a = arr
        seg = 1
        while(1):
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
    def quickSort(self, arr, start=None, end=None):
        start = 0 if not isinstance(start, (int, float)) else start
        end = len(arr)-1 if not isinstance(end, (int, float)) else end

        if(start < end):
            partitionIndex = self.partition(arr, start, end)
            self.quickSort(arr, start, partitionIndex-1)
            self.quickSort(arr, partitionIndex+1, end)
        return arr
    def partition(self, arr, start, end):
        i = start
        j = end
        temp = arr[start]
        while(i != j):
            while(arr[j] >= temp) & (i < j):
                j -= 1
            if(i < j):
                arr[i] = arr[j]
                i += 1
            while(arr[i] < temp) & (i < j):
                i += 1
            if(i < j):
                arr[j] = arr[i]
                j -= 1
        arr[i] = temp
        return i   # 返回当前分组的中心

    def heapSort(self, arr):
        # write code here
        size = len(arr)
        if(size == 0):
            return []
        for i in range(0, size):   # 每次选一个最大的出来，与最后一位交换
            self.maxHeapify(arr, size-i)
            # 交换
            temp = arr[0]
            arr[0] = arr[size-i-1]
            arr[size-i-1] = temp
        return arr

    def maxHeapify(self, arr, size):
        # 完成一次建堆
        for i in range((size-1)/2, -1, -1):
            self.heapify(arr, i, size)
    # 建堆
    def heapify(self, arr, currentRootNode, size):
        if(currentRootNode < size):
            left = currentRootNode * 2 + 1
            right = currentRootNode * 2 + 2

            max_index = currentRootNode

            if(left < size):
                if(arr[left] > arr[max_index]):
                    max_index = left
            if(right < size):
                if(arr[right] > arr[max_index]):
                    max_index = right

            if(max_index != currentRootNode):
                temp = arr[max_index]
                arr[max_index] = arr[currentRootNode]
                arr[currentRootNode] = temp
if __name__ == "__main__":
    sol = Sort()
    print(sol.quickSort([4, 5, 3, 1, 0]))
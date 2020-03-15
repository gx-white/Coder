# -*- coding:utf-8 -*-
class Sort:
    def xuanze(self, arr):
        length = len(arr)

        for i in range(0, length):
            max_index = i
            for j in range(i, length):
                if(arr[max_index] < arr[j]):
                   max_index = j
            if(max_index != i):
                arr[max_index], arr[i] = arr[i], arr[max_index]
        return arr

    def maopao(self, arr):
        length = len(arr)

        for i in range(1, length):
            for j in range(0, length-i):
                if(arr[j] > arr[j+1]):
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        return arr
    def charu(self, arr):
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
    def mergeSort(self, arr):
        length = len(arr)

        mid = length / 2
        left, right = arr[0, mid], arr[mid, length]
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
if __name__ == "__main__":
    sol = Sort()
    print(sol.mergeSortBottomToTop([4, 5, 3, 1, 0]))
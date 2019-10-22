# -*- coding:utf-8 -*-
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        i = 0
        length = len(numbers)
        if(length == 1):
            return numbers[0]
        while(i < length):
            max_num = numbers[i]
            max_index = i
            j = i + 1
            while(j < length):
                if(numbers[j] > max_num):
                    max_num = numbers[j]
                    max_index = j
                j += 1
            if(max_index != i):
                temp = numbers[max_index]
                numbers[max_index] = numbers[i]
                numbers[i] = temp
            i += 1
        count = 0
        for i in range(0, length-1):
            if(numbers[i] == numbers[i+1]):
                count += 1
            else:
                if(count+1 > length / 2):
                    return numbers[i]
                count = 0
        return 0
'''
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        value = numbers[0]
        count = 1
        length = len(numbers)
        if(length == 1):
            return numbers[0]
        for i in range(1, length):
            if(numbers[i] == value):
                count += 1
            else:
                if(count == 0):
                    value = numbers[i]
                    count = 1
                    continue
                count -= 1
                
        count = 0
        for each in numbers:
            if(value == each):
                count += 1
        if(count > length/2):
            return value
        return 0
'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if(length == 1):
            return numbers[0]
        
        n = self.digui(numbers, 0, length-1, length/2)
        count = 0
        for each in numbers:
            if(each == n):
                count += 1
        if(count > length/2):
            return n
        return 0

        
    def digui(self, numbers, start, end, k):
        if(start == end):
            return numbers[start]
        temp = numbers[start]
        i = start
        j = end
        while(i != j):
            while((numbers[j] >= temp) & (i < j)):
                j -= 1
            if(i < j):
                numbers[i] = numbers[j]
                i += 1
            while((numbers[i] < temp) & (i < j)):
                i += 1
            if(i < j):
                numbers[j] = numbers[i]
                j -= 1
        numbers[i] = temp

        if(i < k):
            return self.digui(numbers, i+1, end, k)
        elif(i > k):
            return self.digui(numbers, start, i-1, k)
        else:
            return numbers[i]


if __name__ == "__main__":
    sol = Solution()
    print(sol.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))
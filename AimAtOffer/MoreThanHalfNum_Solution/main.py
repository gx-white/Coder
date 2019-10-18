# -*- coding:utf-8 -*-
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

if __name__ == "__main__":
    sol = Solution()
    print(sol.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))
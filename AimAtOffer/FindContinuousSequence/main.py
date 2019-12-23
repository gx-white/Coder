# -*- coding:utf-8 -*-
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if((tsum == 0) | (tsum == 1) | (tsum == 2)):
            return []
        start = 1
        end = tsum / 2 + 1 + 1
        result = []
        for i in range(start, end):
            number_sum = 0
            for j in range(i, end):
                number_sum += j
                if(number_sum == tsum):
                    result.append(range(i, j+1))
                elif(number_sum > tsum):
                    break
        return result
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if((tsum == 0) | (tsum == 1) | (tsum == 2)):
            return []
        left = 1
        right = 2
        result = []
        while(left < right):
            # na + n(n-1)d/2
            number_sum = (right - left + 1) * left + (right - left + 1) * (right - left) * 1.0 / 2
            if(number_sum > tsum):
                left += 1
            elif(number_sum < tsum):
                right += 1
            else:
                result.append(range(left, right+1))
                left += 1
        return result



if __name__ == "__main__":
    sol = Solution()
    print(sol.FindContinuousSequence(100))
# -*- coding:utf-8 -*-
'''
class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        B = []
        for i in range(0, length):
            B.append(1)
        for i in range(0, length):
            for j in range(0, length):
                if(j != i):
                    B[j] *= A[i]
        return B
'''
class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        B = []
        for i in range(0, length):
            B.append(1)
        for i in range(1, length):
            B[i] = B[i-1] * A[i-1]
        
        temp = 1
        for i in range(length-2,-1,-1):
            temp *= A[i+1]
            B[i] *= temp
        return B

if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply([1,2,3]))
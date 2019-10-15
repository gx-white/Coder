# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if(not sequence):
            return False
        return self.digui(sequence)
    def digui(self, sequence):
        if(not sequence):
            return True
        length = len(sequence)
        root = sequence[length-1]
        left = []
        right = []
        
        for i in range(0, length):
            if(sequence[i] < root):
                left.append(sequence[i])
            else:
                right = sequence[i:length-1]
                break
        for each in right:
            if(each < root):
                return False
        if((self.digui(left)==False) | (self.digui(right)==False)):
            return False
        return  True

if __name__ == "__main__":
    sol = Solution()
    print(sol.VerifySquenceOfBST([7,4,6,5]))
        
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if(number <= 2):
            return number
        
        temp1 = 1
        temp2 = 2
        count = 0
        i = 3
        while(i <= number):
            count = temp1 + temp2
            temp1 = temp2
            temp2 = count
            i = i + 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.rectCover(4))
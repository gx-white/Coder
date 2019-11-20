# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        if(length == 0):
            return 0
        count = 0
        for i in range(0, length):
            for j in range(i+1, length):
                if(data[j] < data[i]):
                    count += 1
            count = count % 1000000007
        
        return count
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.InversePairs([7,1,2,3,4,5,0,6]))
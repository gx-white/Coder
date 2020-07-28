import sys

max_r = 0

def digui(res, arr):
    global max_r
    n = len(arr)
    r = res
    current = arr[0][0]
    for i in range(0, n):
        if(current <= arr[i][0]):
            tmp = arr[i][1] - arr[i][0]
            r += arr[i][1] - arr[i][0]
            current = arr[i][1]
            if(max_r < r):
                max_r = r
        else:
            m = digui(r - tmp, arr[i:])
            if(m > max_r):
                max_r = m
    return r

if __name__ == "__main__":
    T = int(input())
    for i in range(0, T):
        global max_r
        n = int(input())
        table = []
        for j in range(0, n):
            table.append(map(int, sys.stdin.readline().strip().split()))
        
        table.sort()

        result = 0
        # current = table[0][0]

        digui(0, table)
        print(max_r)


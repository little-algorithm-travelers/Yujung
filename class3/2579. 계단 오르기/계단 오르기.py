import sys
input = sys.stdin.readline
arr = [0]
dp = []

l = int(input())
for _ in range(l):
    arr.append(int(input()))
if l ==1:
    print(arr[1])
else:    
    dp.append(arr[0])
    dp.append(max(arr[0]+arr[1],arr[1]))
    dp.append(max(arr[0]+arr[2],arr[1]+arr[2]))


    for i in range(3,l+1):
        dp.append(max(dp[i-2] + arr[i] , dp[i-3] + arr[i] + arr[i - 1]))

    print(dp.pop())
### 斐波那契数列，如果用递归 计算n=38时耗时11.5s
### 用动态规划，或按序增加 ，耗时0 S

class Solution:
    def Fibonacci(self, n):
        #write code here
        if n <= 1:
            return n
        first = 0
        second = 1
        third = 0
        for i in range(2,n+1):
            third = first + second
            first = second
            second = third
        return third

while  True:
    try:
        n = input() 
        s = Solution()
        print(s.Fibonacci(eval(n)))
    except:
        break
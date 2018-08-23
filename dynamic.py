### 斐波那契数列，如果用递归 计算n=38时耗时11.5s
### 用动态规划，或按序增加 ，耗时0 S
'''
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
'''
### 假设有几种硬币，如1、3、5，并且数量无限。请找出能够组成某个数目的找零所使用最少的硬币数。 
'''
class Solution:
    def __init__(self, money):
        self.mark = [0 for _ in range(money + 1)]
        print(self.dp(money))
    def dp(self, money):
        #write code here
        self.coin = 0
        if self.mark[money] != 0:
            self.coin = self.mark[money]
        elif money <= 0:
            if money == 0:
                self.coin = 0
            else:
                self.coin = float('inf')
        elif money > 0:
            self.coin = min(self.dp(money-1),self.dp(money-3),self.dp(money-5))+1
        self.mark[money] = self.coin
        return self.coin

while  True:
    try:
        n = input() 
        s = Solution(eval(n))
    except:
        break
'''
### 一个矩形区域被划分为N*M个小矩形格子，在格子(i,j)中有A[i][j]个苹果。
### 现在从左上角的格子(1,1)出发，要求每次只能向右走一步或向下走一步，最后到达(N,M)，
### 每经过一个格子就把其中的苹果全部拿走。请找出能拿到最多苹果数的路线

class Solution:
    def __init__(self):
        self.A = [[6,5,3,5],[3,1,3,1],[1,1,2,3]]
        self.n = len(self.A) - 1
        self.m = len(self.A[0]) - 1
        self.mark = [[0,0,0,0] for _ in range(3)]
        print(self.dp(self.n,self.m))
    def dp(self,n,m):
        print(1)
        #write code here
        self.num = 0
        if self.mark[n][m] != 0:
            self.num = self.mark[n][m]
        elif n < 0 or m < 0:
            self.num = 0
        elif n < 0 and m < 0:
            return self.num
        else:
            self.num = max(self.dp(n-1,m),self.dp(n,m-1))+self.A[n][m]
        self.mark[n][m] = self.num
        return self.num

while  True:
    try:
        s = Solution()
    except:
        break




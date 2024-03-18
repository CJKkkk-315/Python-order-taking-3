def check(n,c,w,v):
    dp=[[-1 for j in range(c+1)] for i in range(n+1)]
    for j in range(c+1):
        dp[0][j]=0
    for i in range(1,n+1):
        for j in range(1,c+1):
            dp[i][j]=dp[i-1][j]
            if j>=w[i-1] and dp[i][j]<dp[i-1][j-w[i-1]]+v[i-1]:
                dp[i][j]=dp[i-1][j-w[i-1]]+v[i-1]
    return dp
if __name__=='__main__':
    n=10 # 几本书
    c=20 # 多少天
    w=[2,2,6,5,4,7,8,8,6,10] # 每本书所需要的天数
    v=[6,3,5,4,6,8,5,6,9,10] # 每本书所产生的价值
    dp=check(n,c,w,v)
    print('最大价值为:', dp[n][c])


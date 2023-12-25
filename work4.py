def func(word1,word2):
    n1,n2 = len(word1),len(word2)
    #word1为行
    dp = [[0] * (n2+1) for m in range(n1+1)]
    #加1避免边界处理
    for j in range(1,n2+1):
        dp[0][j] = dp[0][j-1] + 1
    for i in range(1,n1+1):
        dp[i][0] = dp[i-1][0] + 1
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
    return dp[n1][n2]
word1,word2 = "horse","ros"
print(func(word1,word2))
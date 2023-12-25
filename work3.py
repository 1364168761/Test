def func(text1,text2):
    n1,n2 = len(text1),len(text2)
    dp = [[0] * (n2 + 1) for m in range(n1 + 1)]
    #错误初始化如下
    # dp = []
    # for m in range(n2+1):
    #     dp.append([0] * (n1+1))

    #将n1,n2加1是为了避免边界问题，如i或j等于0时
    for i in range(1,n1+1):
        for j in range(1,n2+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp[n1][n2]

text1 = "abcde"
text2 = "ace"
print(func(text1,text2))
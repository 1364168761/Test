def func(nums):
    n = len(nums)
    #[1]*1001:表示差值；行为nums下标，列为差值；d[0,1000]
    dp = [[1] * 1001 for _ in range(n)]
    ans = 0
    for i in range(1, n):
        for j in range(i):
            #加500：避免处理负数
            d = nums[i] - nums[j] + 500
            dp[i][d] = max(dp[i][d], dp[j][d] + 1)
            #记录max(已记录最长，新长度)
            ans = max(ans, dp[i][d])
    return ans

nums = [9,4,7,2,10]
print(func(nums))
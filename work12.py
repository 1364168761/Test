def backtrack(ans, digits, start, temp, info):
    # 递归结束条件,索引越界
    if start == len(digits):
        ans.append(temp) #找到底了，添加组合
    else:
        # 当前索引位置的数字
        digit = digits[start]
        # 拿到数字对应的字母字符串
        letters = info[digit]
        # 遍历字符串
        for letter in letters:
            # 拿到字符串中的字母
            temp += letter
            # 继续拿下一个数字对应的字母
            backtrack(ans, digits, start + 1, temp, info)
            # pop:把最后一个删除了，再找下一个加进去
            temp = temp[:-1]

# 示例调用
ans = []
digits = "27"
info = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
    }
backtrack(ans, digits, 0, '', info)
print(ans)





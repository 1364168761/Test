def bracket_generating (n) :
    answer = [] #所有有效组合

    #直接生成有效组合
    def backtrack (temp, left, right):
        if len(temp) == 2 * n: #检查是否以及生成n对括号
            answer.append(''.join(temp)) #将temp中的元素以''分开
            return
        #先生成左括号：最左边必须是左括号
        if left < n: #当左括号未生成完时，可以继续生成
            temp.append('(')
            backtrack(temp, left + 1, right)
            temp.pop() #回溯
        if right < left: # 只有当右括号比左括号少时，才能生成
            temp.append(')')
            backtrack(temp, left, right + 1)
            temp.pop()

    backtrack([], 0, 0)
    return answer

n = 3
print(bracket_generating(n))
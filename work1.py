

def LPS(s):
    def func(i,j):
        if i > j:
            return 0
        if i == j:
            return 1
        if s[i] == s[j]:
            return func(i + 1, j - 1) + 2
        return max(func(i + 1, j), func(i, j - 1))
    return func(0,len(s)-1)

s = "aaaba"
print(LPS(s))
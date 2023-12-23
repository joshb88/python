'''
you are given a string s. your task is to count the number of ways of splitting s into three non-empty parts a b and c 
(s = a + b + c) in such a way that a + b, b+c, and c+a are all different strings. 
+ refers to concatenation. write a function in python or r
'''

def solution(s):
    n = len(s)
    count = 0

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            a = s[:i]
            b = s[i:j]
            c = s[j:]

            # print(f"{a}\n{b}\n{c}\n")

            if a+c != b+c != c+a:
                count += 1

    return count

print(solution("xzxzx"))

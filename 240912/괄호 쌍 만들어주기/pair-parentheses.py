s = list(input())

open_pair = []
close_pair = []

# 여는 괄호 쌍을 찾아서 저장
for i in range(len(s) - 1):
    if s[i] == "(" and s[i + 1] == "(":
        open_pair.append(i)

# 닫는 괄호 쌍을 찾아서 저장
for i in range(len(s) - 1):
    if s[i] == ")" and s[i + 1] == ")":
        close_pair.append(i)

count = 0
j = 0

# 매칭 가능한 쌍을 계산
for i in open_pair:
    while j < len(close_pair) and close_pair[j] <= i:
        j += 1
    count += len(close_pair) - j

print(count)
s = list(input())

print(s) 
open_cnt = 0
close_cnt = 0

for i in range(len(s) - 1):
    if s[i] == "(" and s[i + 1] == "(":
        open_cnt += 1

for i in range(len(s) - 1, 0, -1):
    if s[i] == ")" and s[i - 1] ==")":
        close_cnt += 1

print(open_cnt * close_cnt)
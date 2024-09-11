s = input()

open_count = 0  # 여는 괄호 쌍의 개수
close_count = 0  # 닫는 괄호 쌍의 개수
result = 0

# 문자열을 순차적으로 탐색
for i in range(len(s) - 1):
    # 여는 괄호 쌍을 찾음
    if s[i] == '(' and s[i + 1] == '(':
        open_count += 1
    # 닫는 괄호 쌍을 찾음
    if s[i] == ')' and s[i + 1] == ')':
        result += open_count

print(result)
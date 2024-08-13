f = input().strip().split()
s = input().strip().split()
t = input().strip().split()

c1, tem1 = f[0], int(f[1])
c2, tem2 = s[0], int(s[1])
c3, tem3 = t[0], int(t[1])

# A로 분류되는 사람의 수를 저장할 변수
a_count = 0

# 첫 번째 사람 분류
if c1 == "Y" and tem1 >= 37:
    a_count += 1

# 두 번째 사람 분류
if c2 == "Y" and tem2 >= 37:
    a_count += 1

# 세 번째 사람 분류
if c3 == "Y" and tem3 >= 37:
    a_count += 1

# 위급상황 판단
if a_count >= 2:
    print("E")
else:
    print("N")
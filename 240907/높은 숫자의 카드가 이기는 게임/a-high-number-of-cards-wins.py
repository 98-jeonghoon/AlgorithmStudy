n = int(input())
A = []
B = []

# B의 카드 입력 받기
for _ in range(n):
    value = int(input())
    B.append(value)

# B를 set으로 변환하여 탐색 속도 개선
B_set = set(B)

# A의 카드 리스트 구하기 (B에 없는 카드들)
for i in range(1, n * 2 + 1):
    if i not in B_set:
        A.append(i)

# A와 B를 오름차순으로 정렬
A.sort()
B.sort()

A_pointer = 0
B_pointer = 0
answer = 0

# 두 포인터로 카드 비교
while A_pointer < n and B_pointer < n:
    if A[A_pointer] > B[B_pointer]:
        # A의 카드가 B의 카드보다 크면 A가 이김
        answer += 1
        B_pointer += 1
    # A의 카드가 B의 카드보다 작거나 같은 경우에도 A 카드는 소모됨
    A_pointer += 1

print(answer)
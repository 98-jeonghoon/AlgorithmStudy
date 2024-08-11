from collections import deque

arr = list(input())

answer = 1e9
# 쉬프트 하는 개수
for i in range(1, len(arr) + 1):
    copy_arr = arr[:]
    copy_arr = deque(copy_arr)
    # 쉬프트 하기
    for j in range(i):
        shift = copy_arr.popleft()
        copy_arr.append(shift)
    # Run-Length Encoding 진행
    encoding = ""
    cnt = 1
    while copy_arr:
        value = copy_arr.popleft()
        # 만약 배열이 존재하고
        if copy_arr:
            # 배열의 값이랑 첫번째 값이 일치할때,
            if copy_arr[0] == value:
                cnt += 1
            else:
                encoding += str(value) + str(cnt)
                cnt = 1
        else:
            encoding += str(value) + str(cnt)
            cnt = 1
    answer = min(answer, len(encoding))

print(answer)
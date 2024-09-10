def flip(arr, index):
    # index 위치를 기준으로 좌우를 포함해 반전
    arr[index] = 1 - arr[index]
    if index - 1 >= 0:
        arr[index - 1] = 1 - arr[index - 1]
    if index + 1 < len(arr):
        arr[index + 1] = 1 - arr[index + 1]

def min_clicks_to_make_all_ones(n, arr):
    click_count = 0
    
    for i in range(1, n):  # 첫 번째 칸은 제외하고 탐색
        if arr[i - 1] == 0:  # 왼쪽 칸이 0이면 현재 칸을 눌러야 함
            flip(arr, i)
            click_count += 1

    # 마지막으로 모든 칸이 1로 변환되었는지 확인
    if all(x == 1 for x in arr):
        return click_count
    else:
        return -1

n = int(input())
arr = list(map(int, input().split()))


result = min_clicks_to_make_all_ones(n, arr)
print(result)
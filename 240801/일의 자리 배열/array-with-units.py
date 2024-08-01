# arr=list(map(int,input().split()))
# a=[]
# for i in range(2,11):
#     a.append(arr[-1]+arr[-2])
# print(a)


arr = list(map(int, input().split()))

answer_arr = arr
for i in range(2, 10):
    answer_arr.append((arr[i - 2] + arr[i - 1]) % 10)
print(*answer_arr)
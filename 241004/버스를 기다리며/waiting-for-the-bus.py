import sys

N, M, C = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))
t.sort()
W_lo = 0
W_hi = t[-1] - t[0]

while W_lo < W_hi:
    W_mid = (W_lo + W_hi) // 2
    bus_count = 0
    i = 0
    N = len(t)
    while i < N:
        bus_count += 1
        start_time = t[i]
        bus_departure_time = start_time + W_mid
        bus_capacity = 0
        # 현재 버스에 사람 태우기
        while bus_capacity < C and i < N and t[i] <= bus_departure_time:
            i += 1
            bus_capacity += 1
    if bus_count <= M:
        W_hi = W_mid
    else:
        W_lo = W_mid + 1

print(W_lo)
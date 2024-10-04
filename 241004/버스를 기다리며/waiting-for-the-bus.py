def main():
    import sys
    import threading
    def solve():
        N, M, C = map(int, sys.stdin.readline().split())
        t = list(map(int, sys.stdin.readline().split()))
        t.sort()
        N = len(t)
        W_lo = 0
        W_hi = t[-1] - t[0]

        def check(W):
            bus_count = 0
            i = 0
            N = len(t)
            while i < N:
                bus_count += 1
                start_time = t[i]
                bus_departure_time = start_time + W
                bus_capacity = 0
                # Assign passengers to this bus
                while bus_capacity < C and i < N and t[i] <= bus_departure_time:
                    i += 1
                    bus_capacity +=1
            return bus_count <= M

        # Binary search for minimal W
        while W_lo < W_hi:
            W_mid = (W_lo + W_hi) // 2
            if check(W_mid):
                W_hi = W_mid
            else:
                W_lo = W_mid +1
        print(W_lo)

    threading.Thread(target=solve).start()
main()
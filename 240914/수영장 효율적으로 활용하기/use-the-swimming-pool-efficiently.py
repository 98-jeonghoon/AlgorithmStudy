def can_assign_lanes(T, n, m, max_time):
    lane_count = 1
    current_sum = 0
    
    for time in T:
        if current_sum + time > max_time:
            lane_count += 1
            current_sum = time
            if lane_count > m:
                return False
        else:
            current_sum += time
    
    return True

def find_min_max_lane_time(n, m, T):
    left = max(T)
    right = sum(T)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        if can_assign_lanes(T, n, m, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
            
    return answer


n, m = map(int, input().split())
T = list(map(int, input().split()))


print(find_min_max_lane_time(n, m, T))
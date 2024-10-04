def solution(jobs):
    import heapq

    # 작업들을 요청 시간에 따라 정렬
    jobs.sort(key=lambda x: x[0])

    heap = []
    current_time = 0
    total_waiting_time = 0
    i = 0
    jobs_len = len(jobs)
    processed_jobs = 0

    while processed_jobs < jobs_len:
        # 현재 시간까지 도착한 모든 작업을 힙에 추가
        while i < jobs_len and jobs[i][0] <= current_time:
            # 힙에 (소요 시간, 요청 시간)을 추가
            heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
            i += 1

        if heap:
            # 소요 시간이 가장 짧은 작업을 선택
            duration, request_time = heapq.heappop(heap)
            current_time += duration
            total_waiting_time += current_time - request_time
            processed_jobs += 1
        else:
            # 처리할 수 있는 작업이 없으면 현재 시간을 다음 작업의 요청 시간으로 이동
            if i < jobs_len:
                current_time = jobs[i][0]
            else:
                break

    average_waiting_time = total_waiting_time // jobs_len  # 소수점 이하 버림
    # print(average_waiting_time)
    return average_waiting_time
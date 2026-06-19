import heapq


def solution(jobs):
    indexed_jobs = [
        (request_time, duration, job_number)
        for job_number, (request_time, duration) in enumerate(jobs)
    ]

    indexed_jobs.sort()

    n = len(jobs)
    time = 0
    index = 0
    completed = 0
    total_turnaround = 0
    heap = []

    while completed < n:
        while index < n and indexed_jobs[index][0] <= time:
            request_time, duration, job_number = indexed_jobs[index]
            heapq.heappush(heap, (duration, request_time, job_number))
            index += 1

        if heap:
            duration, request_time, job_number = heapq.heappop(heap)

            time += duration
            total_turnaround += time - request_time
            completed += 1
        else:
            time = indexed_jobs[index][0]

    return total_turnaround // n
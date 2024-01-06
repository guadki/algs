# calculate minimum waiting time required for all queries to start
# for each query its waiting time is execution time of queries that were executed before that query
def minimum_waiting_time(queries: list[int]) -> int:
    waiting_times_sum = 0
    waiting_time = 0

    if len(queries) <= 1:
        return waiting_time

    queries.sort()

    for i in range(1, len(queries)):
        waiting_time += queries[i - 1]
        waiting_times_sum += waiting_time

    return waiting_times_sum


print(minimum_waiting_time([3, 2, 1, 2, 6]))

# Greedy Algorithm for Interval Partitioning


# Define the intervals (start_time, end_time) for each lecture
intervals = [
    (1, 3),
    (2, 5),
    (4, 6),
    (7, 8),
    (5, 9)
]

intervals.sort()
# print(intervals)
classroom_end_time = []
classroom_assignments = {}
num = 0
for interval in intervals:
    start,end = interval
    scheduled = False
    for i in range(num):
        if classroom_end_time[i] <= start:
            classroom_end_time[i] = end
            classroom_assignments[i].append(interval)  # Assign lecture
            scheduled = True
            break
    if not scheduled:
        classroom_assignments[num] = [interval]
        classroom_end_time.append(end)
        num += 1

for i in range(num):
    print(f"Classroom {i + 1}: {classroom_assignments[i]}")



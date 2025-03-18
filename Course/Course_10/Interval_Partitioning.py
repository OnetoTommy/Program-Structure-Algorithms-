# Greedy Algorithm for Interval Partitioning

# Define the intervals (start_time, end_time) for each lecture
intervals = [
    (1, 3),
    (2, 5),
    (4, 6),
    (7, 8),
    (5, 9)
]

# Sort intervals by their start time
intervals.sort()
# print(intervals)

# List to store end times of lectures assigned to classrooms
classroom_end_times = []
# Dictionary to store classrooms and their assigned lectures
classroom_assignments = {}

# Number of classrooms allocated
d = 0

# Process each lecture
for interval in intervals:
    start, end = interval
    scheduled = False

    # Try to find an existing classroom for the lecture
    for i in range(d):
        if classroom_end_times[i] <= start:
            # Schedule the lecture in this classroom
            classroom_end_times[i] = end  # Update the end time
            classroom_assignments[i].append(interval)  # Assign lecture
            scheduled = True
            break

    # If no existing classroom can accommodate the lecture, allocate a new classroom
    if not scheduled:
        classroom_end_times.append(end)  # New classroom with its end time
        classroom_assignments[d] = [interval]  # Store lecture in new classroom
        d += 1

# Print the classrooms and their assigned lectures
for i in range(d):
    print(f"Classroom {i + 1}: {classroom_assignments[i]}")

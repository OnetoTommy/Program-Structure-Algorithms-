# Step 1: Sort jobs by their finish time
def sort_jobs(jobs):
    # Sort jobs by finish time (second element of tuple)
    jobs.sort(key=lambda x: x[1])  # Jobs are represented as (start_time, finish_time, profit)
    return jobs


# Step 2: Find p(j) - the last job that doesn't conflict with job j
def find_p(j, jobs):
    # p(j) is the index of the last job that ends before job j starts
    for i in range(j - 1, -1, -1):
        if jobs[i][1] <= jobs[j][0]:
            return i  # Return the index of the non-conflicting job
    return -1  # If no such job exists, return -1


# Step 3: Weighted Interval Scheduling with Dynamic Programming
def weighted_interval_scheduling(jobs):
    # Step 1: Sort jobs by their finish time
    jobs = sort_jobs(jobs)

    # Number of jobs
    n = len(jobs)

    # Initialize dp array, where dp[i] will store the max profit considering first i jobs
    dp = [0] * n

    # Step 4: Dynamic programming computation
    for j in range(n):
        # Get the p(j) - the last job that does not conflict with job j
        p_j = find_p(j, jobs)

        # Recurrence relation: max of including job j or excluding it
        include_profit = jobs[j][2] + (dp[p_j] if p_j != -1 else 0)
        exclude_profit = dp[j - 1] if j > 0 else 0

        dp[j] = max(include_profit, exclude_profit)

    # The last value in dp array contains the maximum possible profit
    return dp[n - 1]


# Example usage:
# Each job is represented as (start_time, finish_time, profit)
jobs = [
    (1, 3, 5),  # Job 1: Starts at 1, finishes at 3, profit = 5
    (2, 5, 6),  # Job 2: Starts at 2, finishes at 5, profit = 6
    (4, 6, 5),  # Job 3: Starts at 4, finishes at 6, profit = 5
    (6, 7, 4),  # Job 4: Starts at 6, finishes at 7, profit = 4
    (5, 8, 11),  # Job 5: Starts at 5, finishes at 8, profit = 11
]

# Call the weighted interval scheduling function
max_profit = weighted_interval_scheduling(jobs)
print(f"Maximum Profit: {max_profit}")

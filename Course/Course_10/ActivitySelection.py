def recursive_activity_selector(s, f, k, n):
    # m is the index of the next possible compatible activity
    m = k + 1

    # Find the first compatible activity with the activity at index k
    while m <= n and s[m] < f[k]:
        m += 1

    # If there is a compatible activity
    if m <= n:
        # Select activity m and recursively find compatible activities
        return [m] + recursive_activity_selector(s, f, m, n)  # Include the current activity (k)
    else:
        # No compatible activities left
        return []  # Just return the current activity if no further activities can be selected

# Example usage
s = [1, 2, 3, 4, 5]  # Start times of activities
f = [2, 3, 4, 7, 6]  # Finish times of activities

# Call the recursive function starting from the first activity (index 0)
selected_activities = recursive_activity_selector(s, f, 0, len(s) - 1)
print("Selected activities:", selected_activities)

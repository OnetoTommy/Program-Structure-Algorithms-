def recursive_activity_selector(s, f, k, n):
    """
    s: list of start times (1-indexed, s[0] is dummy)
    f: list of finish times (1-indexed, f[0] is dummy)
    k: index of last selected activity
    n: total number of activities
    """
    m = k + 1
    print(m)
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [m] + recursive_activity_selector(s, f, m, n)
    else:
        return []



# Example usage:
# Add a dummy activity at index 0 so that s[0] = f[0] = 0
s = [0, 1, 3, 0, 5, 8, 5]   # Start times
f = [0, 2, 4, 6, 7, 9, 9]   # Finish times
n = len(s) - 1

selected_activities = recursive_activity_selector(s, f, 0, n)
print("Selected activities:", selected_activities)

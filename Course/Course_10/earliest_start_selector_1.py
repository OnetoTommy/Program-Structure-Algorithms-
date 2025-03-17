def earliest_start_selector(s, f):
    n = len(s)
    s = sorted(range(n), key=lambda i: s[i])
    selector = set()
    last_f_time = -1
    for i in s:
        if s[i] >= last_f_time:
            selector.add(s[i])
            last_f_time = f[i]
    return selector

    return selected




# Example Usage
s = [0, 1, 3, 0, 5, 8, 5, 6, 8, 12]  # Start times (sorted)
f = [0, 2, 4, 6, 7, 9, 9, 10, 11, 14]  # Finish times (sorted)

selected_activities = earliest_start_selector(s, f)
print("Selected Activities (Earliest Start):", selected_activities)

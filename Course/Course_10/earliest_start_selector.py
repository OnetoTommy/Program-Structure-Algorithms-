def earliest_start_selector(s, f):
    """
    Select activities based on the earliest start time (greedy)
    :param s: List of start times
    :param f: List of finish times
    :return: Set of selected activities
    """
    n = len(s)
    activities = sorted(range(n), key=lambda i: s[i])  # Sort by start time

    selected = set()
    last_finish_time = -1

    for i in activities:
        if s[i] >= last_finish_time:
            selected.add(i)
            last_finish_time = f[i]  # Update last selected activity's finish time

    return selected


# Example Usage
s = [0, 1, 3, 0, 5, 8, 5, 6, 8, 12]  # Start times (sorted)
f = [0, 2, 4, 6, 7, 9, 9, 10, 11, 14]  # Finish times (sorted)

selected_activities = earliest_start_selector(s, f)
print("Selected Activities (Earliest Start):", selected_activities)

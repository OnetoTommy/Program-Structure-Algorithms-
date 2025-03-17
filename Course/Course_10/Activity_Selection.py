def recursive_activity_selector(s, f, k, n):
    """
    :param s: List of activity start times
    :param f: List of activity finish times
    :param k: Index of the current subproblem
    :param n: Total number of activities
    :return: A set of selected activities that are mutually compatible
    """
    m = k + 1  # Move to the next activity
    # Find the first activity whose start time is >= finish time of the current activity
    while m <= n and s[m] < f[k]:
        m += 1

    if m <= n:
        # Include the current activity and recursively find more compatible activities
        return {m} | recursive_activity_selector(s, f, m, n)
    else:
        return set()  # Return an empty set if no more activities can be selected


# Example usage:
if __name__ == "__main__":
    s = [0, 1, 3, 0, 5, 8, 5, 6, 8, 12]  # Start times (sorted)
    f = [0, 2, 4, 6, 7, 9, 9, 10, 11, 14]  # Finish times (sorted)
    n = len(s) - 1  # Number of activities (ignoring index 0)

    selected_activities = recursive_activity_selector(s, f, 0, n)
    print("Selected activities:", selected_activities)

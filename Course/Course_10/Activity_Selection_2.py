def selection(s, f, k, n):
    # m = k+1
    # while m <= n and s[m] < f[k]:
    #     m += 1
    # if m <= n:
    #     return {m} | selection(s,f,m,n)
    # else:
    #     return set()
    dict = set()
    m = k + 1
    while m <= n:
        if s[m] >= f[k]:
            dict.add(m)
            k = m
            m = k+1
        else:
            m += 1
    return dict

# Example usage:
if __name__ == "__main__":
    s = [0, 1, 3, 0, 5, 8, 5, 6, 8, 12]  # Start times (sorted)
    f = [0, 2, 4, 6, 7, 9, 9, 10, 11, 14]  # Finish times (sorted)
    n = len(s) - 1  # Number of activities (ignoring index 0)

    selected_activities = selection(s, f, 0, n)
    print("Selected activities:", selected_activities)
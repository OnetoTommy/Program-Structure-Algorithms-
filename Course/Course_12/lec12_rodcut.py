def memoized_cut_rod(p, n):
    r = [-1] * (n+1) 
    return memoized_cut_rod_aux(p, n, r)

def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    elif q == -float("inf"):
        for i in range(1, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    print("%d : %d", n, r[n])
    return q

def bottom_up_cut_rod(p, n, debug = 0):
    r = [-1] * (n+1)
    s = [-1] * (n+1)
    r[0] = 0
    for i in range(1, n+1):
        q = -1
        for j in range(1, i+1):
            new_val = p[j] + r[i-j]
            if new_val > q:
                q = new_val
                if debug > 1:
                    print("i = %d j = %d r = %d q = %d"%(i, j, r[i-j], q))
                s[i] = j
        r[i] = q
        if debug > 0:
            print("%d : %d %d"%(i, r[i], s[i]))
    return r, s

def print_cut_rod(p, n, debug = 0):
    (r, s) = bottom_up_cut_rod(p, n, debug)
    print("%-4s : %-4s : %-5s"%("i", "r[i]", "s[i]"))
    print("---------------------")
    for i in range(1, n+1):
        #print(n)
        print("%-4d : %-4d : %-4d"%(i, r[i], s[i]))
        #n = n - s[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20]
debug = 0
print_cut_rod(p, len(p)-1, debug)
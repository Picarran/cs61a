# linear-time-intersection-of-sorted-list
# 3 4 6 7 9 10
# 1 3 5 7 8
# n^2 --> n

def fast_overlap(s,t):
    """Return the overlap between sorted S and sorted T.

    >>> fast_overlap([3,4,6,7,9,10],[1,3,5,7,8])
    2
    """
    i,j,cnt = 0,0,0
    while i<len(s) and j<len(t):
        if s[i]==t[j]:
            cnt,i,j = cnt+1,i+1,j+1
        elif s[i]<t[j]:
            i+=1
        else:
            j+=1
    return cnt
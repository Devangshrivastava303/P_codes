def max_good_subarray_sum():
    n=int(input())
    k=int(input())
    A = list(map(int, input().split()))

    from collections import defaultdict
    count = defaultdict(int)   
    distinct = 0
    window_sum = 0
    max_sum = 0               
    l = 0

    for r in range(n):
        if count[A[r]] == 0:
            distinct += 1
        count[A[r]] += 1
        window_sum += A[r]


        while distinct > k:
            count[A[l]] -= 1
            if count[A[l]] == 0:
                distinct -= 1
            window_sum -= A[l]
            l += 1
        max_sum = max(max_sum, window_sum)

    print(max_sum)
    return max_sum

max_good_subarray_sum()
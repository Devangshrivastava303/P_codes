import sys

def solve(n, k, s):
    if n < 2 * k:
        return -1
    
    INF = float('inf')
    best = INF
    for a in range(k, n - k + 1):
        b = n - a
        dp = [INF] * (a + 1)
        dp[0] = 0
        
        for i in range(n):  
            ndp = [INF] * (a + 1)
            ch = s[i]
            for r in range(0, min(i, a) + 1):
                if dp[r] == INF:
                    continue
                l_so_far = i - r 

                if r >= k:
                    cost = 0 if ch == 'L' else 1
                    if dp[r] + cost < ndp[r]:
                        ndp[r] = dp[r] + cost
            
            dp = ndp
        
        if dp[a] < best:
            best = dp[a]
    
    return best if best != INF else -1


def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    for _ in range(t):
        n, k = int(input_data[idx]), int(input_data[idx+1]); idx += 2
        s = input_data[idx]; idx += 1
        results.append(str(solve(n, k, s)))
    print('\n'.join(results))

if __name__ == "__main__":
    main()
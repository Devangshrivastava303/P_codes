# PYTHON DSA CHEATSHEET

## Built-in Data Structures

### List
arr = [1, 2, 3]
arr.append(4)        # O(1)
arr.pop()            # O(1)
arr.pop(0)           # O(n)
arr.insert(0, 5)     # O(n)
arr.sort()           # O(n log n)
arr.reverse()        # O(n)
arr.index(val)       # O(n)
val in arr           # O(n)

### Set
s = set()
s.add(val)           # O(1)
s.remove(val)        # O(1)
val in s             # O(1)

### Dictionary
d = {}
d[key] = val         # O(1)
d.get(key, default)  # O(1)
key in d             # O(1)
d.keys() / d.values()

### Collections
from collections import deque, Counter, defaultdict

# Deque (queue/deque)
q = deque()
q.append(val)        # O(1)
q.appendleft(val)    # O(1)
q.pop()              # O(1)
q.popleft()          # O(1)

# Counter
c = Counter(arr)     # Frequency count
c.most_common(k)

# DefaultDict
d = defaultdict(int)
d = defaultdict(list)

## Dynamic Programming (Progressive)

### General DP Approach
1. **Identify**: Problem asks "count ways", "max/min value", "can reach/achieve"
2. **Subproblems**: What's the decision at each step?
3. **Recurrence**: How does dp[i] relate to dp[i-1], dp[i-2], ...?
4. **Base cases**: dp[0], dp[1] — what's the smallest input?
5. **Iterate**: Fill table bottom-up OR recurse + memoize

### Climbing Stairs (LC 70) — 1D DP Intro
# Ways to climb n stairs taking 1 or 2 steps at a time
# dp[i] = dp[i-1] + dp[i-2]  (same as Fibonacci)
dp = [0] * (n + 1)
dp[0], dp[1] = 1, 1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]
return dp[n]

# Space optimized (two variables instead of array)
prev2, prev1 = 1, 1
for i in range(2, n + 1):
    curr = prev1 + prev2
    prev2, prev1 = prev1, curr
return prev1

### House Robber (LC 198) — Decision DP
# Max money robbing non-adjacent houses
# dp[i] = max(rob house i, skip house i)
dp = [0] * len(nums)
dp[0] = nums[0]
dp[1] = max(nums[0], nums[1])
for i in range(2, len(nums)):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])
return dp[-1]

# Space optimized
rob_prev2 = nums[0]
rob_prev1 = max(nums[0], nums[1])
for i in range(2, len(nums)):
    curr = max(rob_prev1, rob_prev2 + nums[i])
    rob_prev2, rob_prev1 = rob_prev1, curr
return rob_prev1

### House Robber 2 (LC 213) — Circular Array Trick
# Houses in a circle: house 0 and house n-1 are neighbors.
# Only that one pair is broken → try both sides of the break.
# Reuse the linear rob() on two windows, take the max.
# Edge cases FIRST: n==0 → 0, n==1 → nums[0], n==2 → max(nums)
def rob_range(nums, left, right):   # linear rob on nums[left..right-1]
    # same recurrence as HR1, using nums[left], nums[left+1]...
    dp0 = nums[left]
    if right - left == 1:
        return dp0
    dp1 = max(nums[left], nums[left + 1])
    if right - left == 2:
        return dp1
    for i in range(left + 2, right):
        dp0, dp1 = dp1, max(dp1, dp0 + nums[i])
    return dp1

answer = max(rob_range(nums, 0, n - 1),   # exclude last house
             rob_range(nums, 1, n))        # exclude first house

### Coin Change (LC 322) — 1D Min/Max DP
# Minimum coins to make amount
dp = [float('inf')] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
return dp[amount] if dp[amount] != float('inf') else -1

### LCS (LC 1143) — 2D DP
# Longest common subsequence length
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
return dp[len(s)][len(t)]

### 0/1 Knapsack — Classic 2D DP
# Max value with weight capacity W
dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, W + 1):
        if weights[i-1] <= w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
        else:
            dp[i][w] = dp[i-1][w]
return dp[n][W]

### DP Pattern Quick Reference
| Pattern | Recurrence | Example |
|---------|-----------|---------|
| Fibonacci | dp[i] = dp[i-1] + dp[i-2] | Climbing Stairs |
| Decision | dp[i] = max(dp[i-1], dp[i-2] + val[i]) | House Robber |
| Min Coins | dp[i] = min(dp[i], dp[i-coin] + 1) | Coin Change |
| 2D Match | if match: dp[i][j] = dp[i-1][j-1]+1 else: max(...) | LCS |
| Knapsack | max(dp[i-1][w], dp[i-1][w-wt] + val) | 0/1 Knapsack |
| Partition | dp[i] = sum(dp[i-1]...dp[i-m]) | Phone Keypad |

## Algorithm Templates

### Kadane's Algorithm (Maximum Subarray)
# Track running sum. If it drops below 0, reset.
# Edge: all negative nums → return max(num) not 0
max_sum = nums[0]
curr_sum = 0
for num in nums:
    curr_sum = max(num, curr_sum + num)   # extend or start fresh
    max_sum = max(max_sum, curr_sum)
return max_sum

### Binary Search
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

### BFS
from collections import deque
def bfs(graph, start):
    visited = set([start])
    q = deque([start])
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

### Connected Components (Transitive Relation → BFS)
# Signal: "if A relates B, and B relates C, then A relates C" → equivalence
# relation → groups = connected components. Answer = max component size
# (transitive closure makes every component a clique → each member needs
# its own slot/class).
# Build adjacency BOTH directions ("vice versa" line people forget!):
adj = [[] for _ in range(n + 1)]   # index = person 1..n
for i in range(m):
    x, y = a[i], b[i]
    adj[x].append(y)               # x likes y
    adj[y].append(x)               # y likes x — forget this = wrong groups

visited = [False] * (n + 1)        # checklist indexed by person number
max_group = 0
for person in range(1, n + 1):
    if not visited[person]:        # NOT "if person not in visited" (always True)
        q = deque([person])
        visited[person] = True
        group_size = 0
        while q:
            curr = q.popleft()
            group_size += 1
            for friend in adj[curr]:
                if not visited[friend]:
                    visited[friend] = True
                    q.append(friend)
        max_group = max(max_group, group_size)

### DFS (Recursive)
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

### Tree Traversals
def inorder(node):
    if not node: return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def preorder(node):
    if not node: return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

### Sliding Window

# Fixed size (k known)
# Expand right. When window hits size k, process, shrink left.
window = deque()
for r in range(len(arr)):
    window.append(arr[r])
    if len(window) == k:
        # process window
        window.popleft()

# Variable size (condition based, e.g. "sum ≤ target")
# Expand right. While condition violated, shrink left.
l = 0
for r in range(len(arr)):
    # add arr[r] to window state
    while condition_violated:
        # remove arr[l] from window state
        l += 1
    # process valid window

# Longest Substring Without Repeating (LC 3)
# Set tracks chars in current window. Duplicate → shrink left until removed.
l = 0
max_len = 0
chars = set()
for r in range(len(s)):
    while s[r] in chars:
        chars.remove(s[l])
        l += 1
    chars.add(s[r])
    max_len = max(max_len, r - l + 1)

### Two Pointers

# From ends (Container With Most Water, 3Sum, Rain Water)
l, r = 0, len(arr) - 1
while l < r:
    # process arr[l], arr[r]
    if condition:
        l += 1
    else:
        r -= 1

# 3Sum (LC 15): sort first, then fixed i + two-pointer j,k
# Skip duplicates after each pointer move

# Trapping Rain Water (LC 42):
# left_max, right_max. Process the shorter side.
# water += left_max - height[l] (or right_max - height[r])

### Longest Consecutive Sequence (LC 128)
# Set of numbers. Only start counting from numbers with no predecessor.
sett = set(nums)
longest = 0
for num in sett:
    if num - 1 not in sett:        # start of a sequence
        length = 1
        curr = num + 1
        while curr in sett:
            length += 1
            curr += 1
        longest = max(longest, length)

### Group Anagrams (LC 49)
# Sorted string as key. Same chars → same key → same group.
valid = {}
for word in strs:
    key = ''.join(sorted(word))
    if key not in valid:
        valid[key] = []
    valid[key].append(word)
return list(valid.values())

### Palindrome from Frequency (Smallest Palindromic Rearrangement)
# Build left half from freq//2. Middle = first char with odd count.
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

left = []
for i in range(26):
    ch = chr(ord('a') + i)
    if ch in freq:
        for _ in range(freq[ch] // 2):
            left.append(ch)

middle = ''
if len(s) % 2 == 1:
    for i in range(26):
        ch = chr(ord('a') + i)
        if ch in freq and freq[ch] % 2 == 1:
            middle = ch
            break

right = list(reversed(left))
return ''.join(left) + middle + ''.join(right)

### Next Greater Element (Monotonic Stack)
# Traverse right to left. Maintain decreasing stack.
result = [-1] * len(nums)
stack = []
for i in range(len(nums) - 1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1]
    stack.append(nums[i])

### Coin Change (Minimum Coins) — DP Bottom-Up
dp = [float('inf')] * (amount + 1)
dp[0] = 0
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
return dp[amount] if dp[amount] != float('inf') else -1

### LCS (Longest Common Subsequence) — 2D DP
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    for j in range(1, len(t) + 1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
return dp[len(s)][len(t)]

### Number of Islands (BFS/DFS on Grid)
def numIslands(grid):
    if not grid: return 0
    rows, cols = len(grid), len(grid[0])
    count = 0
    def bfs(r, c):
        q = deque([(r, c)])
        grid[r][c] = '0'
        while q:
            row, col = q.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    q.append((nr, nc))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                count += 1
    return count

### Wildcard Matching — Greedy Backward (star_pos + match_pos)
i, j = len(s)-1, len(p)-1
star_pos = match_pos = -1
while i >= 0:
    if j >= 0 and (p[j] == s[i] or p[j] == '?'):
        i -= 1; j -= 1
    elif j >= 0 and p[j] == '*':
        star_pos = j; match_pos = i; j -= 1
    elif star_pos != -1:
        j = star_pos - 1; match_pos -= 1; i = match_pos
    else:
        return False
while j >= 0 and p[j] == '*': j -= 1
return j < 0

### Frequency Map Sliding Window (Beauty problem)
# Instead of sorting each window, maintain freq dict.
# Count cumulative frequencies to find xth smallest.
freq = defaultdict(int)
# Add nums[r], remove nums[l] on each slide
# For xth: iterate sorted keys, accumulate count until >= x

### Phone Keypad DP (Composition DP)
# For each run of length L with max group size m:
# dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-m]
# Optimize: sliding window sum instead of inner loop
dp = [0] * (L + 1)
dp[0] = 1
window_sum = 0
for i in range(1, L + 1):
    window_sum = (window_sum + dp[i-1]) % MOD
    if i > m:
        window_sum = (window_sum - dp[i-m-1] + MOD) % MOD
    dp[i] = window_sum
# Total = product of dp[L] for all runs % MOD

### 3D DP for LCS with K Replacements
dp[i][j][r] = longest using S[0..i-1], T[0..j-1], ≤ r replacements
if s[i-1] == t[j-1]:
    take = 1 + dp[i-1][j-1][r]
elif r > 0:
    take = 1 + dp[i-1][j-1][r-1]
else:
    take = -inf
skip = max(dp[i-1][j][r], dp[i][j-1][r])
dp[i][j][r] = max(take, skip)

## Greedy Sub-Patterns (don't lump them together!)

| Signal | Sub-pattern | Tool |
|---|---|---|
| Time intervals overlap ("arrives before another departs") | Sorted sweep | sort + two pointers, count max overlap |
| Fit items into fixed capacity ("each car holds at most 4") | Counting + pairing | count frequencies, pair big-with-small |
| Intervals that can merge | Merge intervals | sort by start, extend end |

### Counting + Pairing (Taxi problem)
# Items of sizes 1..4 must share containers of capacity 4. Groups can't split.
# NEVER pack in array order — order-based packing wastes seats (2+1=3 cab
# leaves a seat that a 2 could have used). Count inventory, pair by class:
count = [0] * 5            # index = size
for size in s:
    count[size] += 1

cabs = 0
cabs += count[4]                                # 4s alone, no sharing
cabs += count[3]                                # each 3 its own cab...
count[1] = max(0, count[1] - count[3])          # ...but grabs one 1 (free seat)
cabs += count[2] // 2                           # two 2s share one cab
if count[2] % 2 == 1:                           # lone 2 left
    cabs += 1
    count[1] = max(0, count[1] - 2)             # takes up to two 1s
cabs += (count[1] + 3) // 4                     # leftover 1s: 4 per cab, round up

## Time Complexities

| Operation | List | Set | Dict | Deque |
| Access | O(1) | - | O(1) | O(1) |
| Search | O(n) | O(1) | O(1)* | O(n) |
| Insert | O(n) | O(1) | O(1) | O(1) |
| Delete | O(n) | O(1) | O(1) | O(1) |
*dict search by key only

## Recursion Pattern
def recursion(state):
    if base_condition:
        return base_value
    result = modify(state)
    return recursion(result)

## Backtracking Template
def backtrack(state):
    if goal_reached(state):
        record_solution(state)
        return
    for choice in choices(state):
        make_choice(state, choice)
        backtrack(state)
        undo_choice(state, choice)

## Common Edge Cases Checklist
- Empty input
- Single element
- All same values
- Negative numbers
- All negative (Kadane's issue)
- Duplicates
- Already sorted
- Large input (overflow, TLE)
- First element missing from dict (KeyError — use dict.get())
- Off-by-one in ranges (range(n) vs range(n-1))
- n=0 or n=1

When you have two arrays and one is a subset/permutation of relevant values from the other, think hashmap immediately.

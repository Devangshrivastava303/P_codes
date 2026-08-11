from collections import deque


def minClassesRequired(n: int, m: int, a: list[int], b: list[int]) -> int:
    adj = {i: [] for i in range(1, n + 1)}
    for i in range(m):
        u, v = a[i], b[i]
        adj[u].append(v)
        adj[v].append(u)

    visited = set()
    classes = 0
    for person in range(1, n + 1):
        if person in visited:
            continue
        classes += 1
        queue = deque([person])
        visited.add(person)
        while queue:
            current = queue.popleft()
            for neighbor in adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return classes


print(minClassesRequired(7,4,[1,2,3,4],[2,3,4,5]))  
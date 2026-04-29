def findPaths(m, n, N, i, j):
    dp = [[0] * n for _ in range(m)]
    dp[i][j] = 1
    count = 0

    for step in range(N):
        temp = [[0] * n for _ in range(m)]
        for x in range(m):
            for y in range(n):
                if dp[x][y] > 0:
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n:
                            temp[nx][ny] += dp[x][y]
                        else:
                            count += dp[x][y]
        dp = temp

    return count

print(findPaths(2, 2, 2, 0, 0))
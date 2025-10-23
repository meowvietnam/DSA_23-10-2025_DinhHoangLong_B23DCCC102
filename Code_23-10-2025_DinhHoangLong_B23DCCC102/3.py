def solution(N, M, area, C):
    grid = [[0]*N for _ in range(N)]
    for a in area:
        r1, c1, r2, c2, color = a
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if grid[i][j] == 0:
                    grid[i][j] = color
                elif grid[i][j] != color:
                    grid[i][j] = 3
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == C:
                count += 1
    return count

print(solution(10, 2, [[1,1,5,4,1],[2,3,6,6,1]], 3))  

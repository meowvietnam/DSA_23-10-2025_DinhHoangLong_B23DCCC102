def solution(watering_can, N, M):
    v = [[0] * N for _ in range(N)]
    for y, x, w in watering_can:
        for c in range(max(0, x - w), min(N - 1, x + w) + 1):
            v[y][c] = 1
        for r in range(max(0, y - w), min(N - 1, y + w) + 1):
            v[r][x] = 1
    k = 0
    for r in range(N):
        for c in range(N):
            if v[r][c] == 0:
                k += 1
    return k

print(solution([[2,2,2],[0,0,1]], 5, 2))
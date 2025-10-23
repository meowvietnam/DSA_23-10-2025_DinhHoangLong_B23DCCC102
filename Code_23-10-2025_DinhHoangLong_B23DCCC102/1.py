def solution(arr, M):
    N = len(arr)
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    total = 0
    for i in range(M, N, M):
        total += arr[i]
    return total

arr = [4, 2, 1, 3, 9, 5, 6]
M = 3
print(solution(arr, M))
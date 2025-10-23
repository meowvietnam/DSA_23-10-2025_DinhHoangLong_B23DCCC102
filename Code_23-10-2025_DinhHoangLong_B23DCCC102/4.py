def solution(arr, N, M):
    max_sum = 0
    min_sum = float('inf')
    for i in range(N - M + 1):
        s = sum(arr[i:i+M])
        if s > max_sum:
            max_sum = s
        if s < min_sum:
            min_sum = s
    return max_sum - min_sum

print(solution([3,1,1,4,5,9], 6, 3))
print(solution([3,1,1,4,5,9], 6, 2))  
print(solution([1,2,3,4,5,6], 6, 4))
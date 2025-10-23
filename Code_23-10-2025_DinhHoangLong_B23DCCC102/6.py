def solution(arr, N):
    count = {}
    for x in arr:
        count[x] = count.get(x, 0) + 1
    max_vote = max(count.values())
    candidates = [k for k, v in count.items() if v == max_vote]
    return max(candidates)

print(solution([1,2,3,4,4,5,6,7,7,8,9,9,9,9,10], 15))
print(solution([1,1,4,4,8,8,9,9,9,4,4,4,5,3,2,1,2,4,8,7], 24))
print(solution([3,3,3,3,3,3,9,9,9,9,11,11,11,11,11,11,11,11,11,11], 20))







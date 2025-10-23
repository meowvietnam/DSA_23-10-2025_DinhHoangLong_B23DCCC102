import math

def solution(arr, N):
    return max(math.gcd(a, b) for a, b in arr)

print(solution([[15,20],[36,48],[12,7],[121,44],[39,65]], 5))
print(solution([[356,78],[154,122],[38,190],[44,188],[365,245]], 5))







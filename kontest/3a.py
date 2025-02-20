n, k = map(int, input().split())
nums = list(map(int, input().split()))

result = nums[:k]
result.sort()
for num in nums[k:]:
    if num < result[-1]:
        result[-1] = num
        result.sort()
print(*result)


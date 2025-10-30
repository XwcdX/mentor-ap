def power_set(nums):
    result = []
    nums.sort()

    def backtrack(start, path):
        if path not in result:
            result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    result.sort(key=lambda x: (len(x), x))
    return result

print(power_set([1,2,3]))


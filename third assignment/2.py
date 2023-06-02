def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for a in range(n - 3):
        if a > 0 and nums[a] == nums[a-1]:
            continue

        for b in range(a + 1, n - 2):
            if b > a + 1 and nums[b] == nums[b-1]:
                continue

            left = b + 1
            right = n - 1

            while left < right:
                sum = nums[a] + nums[b] + nums[left] + nums[right]

                if sum == target:
                    result.append([nums[a], nums[b], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1

    return result



value=fourSum(nums = [1,0,-1,0,-2,2], target = 0)
print(value)
# NOW it's a "room"
def containsNearbyDuplicate(nums, k):
    map = {}
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                diff = abs(i - j)
                if diff <= k:
                    return True

    return False


result = containsNearbyDuplicate([1, 2, 3, 1], 3)
print(result)
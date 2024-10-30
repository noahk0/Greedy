def maxSubArray(self, nums: List[int]) -> int:
    sub = largest = nums[0]

    for num in nums[1:]:
        if sub > 0:
            sub += num
        else:
            sub = num
                
        largest = max(sub, largest)

    return largest

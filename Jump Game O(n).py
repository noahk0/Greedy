def canJump(self, nums: List[int]) -> bool:
    reach = nums[0]

    for i in range(len(nums)):
        if len(nums) <= reach + 1:
            return True

        if reach < i:
            return False

        reach = max(reach, i + nums[i])

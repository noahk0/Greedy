def jump(self, nums: List[int]) -> int:
    l = jump = 0
    r, nums = 1, [i + nums[i] for i in range(len(nums) - 1)]

    while r <= len(nums):
        jump += 1
        l, r = r, max(nums[l : r]) + 1

    return jump

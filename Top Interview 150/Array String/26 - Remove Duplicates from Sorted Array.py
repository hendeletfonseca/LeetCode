class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setNum = set(nums)
        nums.clear()
        nums.extend(setNum)
        nums.sort()
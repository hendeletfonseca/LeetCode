class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        setList = set(nums)
        size = len(nums)
        for n in setList:
            if (nums.count(n) > size / 2):
                return n
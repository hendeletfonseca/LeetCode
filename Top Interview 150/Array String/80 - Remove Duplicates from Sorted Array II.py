class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        setList = set(nums)
        for num in setList:
            while (nums.count(num) > 2):
                nums.remove(num)
        return len(nums)
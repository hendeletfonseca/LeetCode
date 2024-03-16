class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)
        for _ in range(n):
            removed = nums.pop()
            nums.insert(0,removed)
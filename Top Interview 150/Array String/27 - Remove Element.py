class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = nums.count(val)
        while (size != 0):
            nums.remove(val)
            size -= 1
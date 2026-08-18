class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hasdup = Counter(nums)
        if max(hasdup.values())>=2:
            return True
        else:
            return False
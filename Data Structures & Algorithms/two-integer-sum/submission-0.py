class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        diff = 0
        index = 0
        for num in nums:
            diff = target - num
            if diff in seen:
                return [seen[diff],index]
            else:
                seen[num]=index
            index +=1


        
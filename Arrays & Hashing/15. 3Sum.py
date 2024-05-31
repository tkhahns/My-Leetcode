class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            pair = self.twoSum(nums, i+1, target)
            for p in pair:
                out.append([nums[i]] + p)
        return out
    
    def twoSum(self, nums: List[int], start: int, target: int) -> List[int]:
        out = []
        a = start
        b = len(nums) - 1
        while a < b:
            if nums[a] + nums[b] == target:
                out.append([nums[a], nums[b]])
                while a < b and nums[a] == nums[a+1]:
                    a += 1
                while a < b and nums[b] == nums[b-1]:
                    b -= 1
                a += 1
                b -= 1
            elif nums[a] + nums[b] > target:
                b -= 1
            else:
                a += 1
        return out

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict = {}
        j = 0
        for i in nums:
            comp = target - i
            if comp in dict.values():
                return [list(dict.keys())[list(dict.values()).index(comp)], j]
            dict[j] = i
            j += 1

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = []
        sum = nums[0]
        res.append(sum)
        for i in range(1, len(nums)):
            sum += nums[i]
            res.append(sum)
        return res

sol = Solution()
print(sol.runningSum([3, 1, 2, 10, 1]))
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
            max = 0
            for i in accounts:
                res = sum(i)
                if max < res: max = res
            return max


sol = Solution()
print(sol.maximumWealth([[3, 1, 2, 10, 1], [3, 1, 2, 1099, 1], [3, 111, 2, 10, 1]]))
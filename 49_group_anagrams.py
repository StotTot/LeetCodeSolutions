from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for i in strs:
            count = [0] * 26
            
            for c in i:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(i)

        return res.values()


sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
from collections import defaultdict
class Solution:
    def topKFrequentSlow(self, nums: list[int], k: int) -> list[int]:
        res = []
        if len(nums) == 1:
            return [nums[0]]
        dict = defaultdict(int)
        for i in range(len(nums)):
            dict[nums[i]] += 1
        for j in range(k):
            x = max(dict, key = dict.get)
            res.append(x)
            del dict[x]
        return res

    # Reference for linear solution @ NeetCode @ https://www.youtube.com/watch?v=YPTqKIgVk-k
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        
        # Count the occurences of each value in the given list
        for i in range(len(nums)):
            count[nums[i]] += 1
        # Bucket sort the the values by their occurences.
        # ie:   0      1      2   3   4    5   6   7   8
        #     [[], [21, 3], [2], [], [1], [], [], [], []]
        for i, j in count.items():
            freq[j].append(i)
        
        res = []
        print(count)
        print(freq)
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

sol = Solution()

print(sol.topKFrequentSlow([2, 21, 1, 1, 2, 3, 1, 1], 2))
print(sol.topKFrequent([2, 21, 1, 1, 2, 3, 1, 1], 2))
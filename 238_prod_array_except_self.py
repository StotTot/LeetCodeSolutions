import numpy as np
class Solution:
    def productExceptSelfSlow(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(0, len(nums)):
            temp = nums.copy()
            del temp[i]
            res.append(int(np.product(temp)))
            temp = nums
        return res
    
    # Time limit still exceeded?
    def productExceptSelfStillSlow(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))
        for i in range(len(nums)):
            if i == 0:
                res.append(int(np.product(nums[1:])))
            elif i == len(nums) - 1:
                res.append(int(np.product(nums[:i])))
            else:
                res.append(int(np.product(nums[:i])) * int(np.product(nums[i + 1:])))
        return res
    
    # Please work
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))
        tail = 1

        for i in range(len(nums)):
            res[i] = tail
            tail *= nums[i]
        
        head = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= head
            head *= nums[i]

        return res
    
sol = Solution()

print(sol.productExceptSelfSlow([1, 2, 3, 4]))

print(sol.productExceptSelf([1, 2, 3, 4]))
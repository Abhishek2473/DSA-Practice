class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        c=0
        for i in nums:
            if i:
                prod*=i
            else:
                c+=1
        if c>1:
            return [0]*len(nums)
        res=[0]*len(nums)
        for i in range(len(nums)):
            if c:
                res[i]=0 if nums[i] else prod
            else:
                res[i]=prod//nums[i]
        return res



        
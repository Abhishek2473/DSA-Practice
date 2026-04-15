class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]==-1*a:
                    res.append([nums[l],nums[r],a])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
                elif nums[l]+nums[r]<-1*a:
                    l+=1
                else:
                    r-=1
        return res

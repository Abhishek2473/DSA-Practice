class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        longest=0
        for i in nums:
            if i-1 not in hs:
                c=1
                while i+c in hs:
                    c+=1
                longest=max(c,longest)
        return longest
        
import typing.List
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l = length(nums)
        lp = l/2
        for i in range(l/2):
            a = nums[i]
            b = nums[i+1]
            for j in range(a):
                outlist.append(b)

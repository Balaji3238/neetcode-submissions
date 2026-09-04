class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        maxx=0
        for i in nums:
            if i==0:
                cnt=0
            else:
                cnt=cnt+1
                maxx=max(maxx,cnt)
        return maxx
class Solution:
    def maximumWealth(self, acc: List[List[int]]) -> int:
        sam=0
        for i in range(len(acc)):
            m=sum(acc[i])
            sam=max(sam,m)
        return sam
s = Solution()
accounts = [[1,5],[7,3],[3,5]]
s.maximumWealth(accounts)

class Solution(object):
    def numberOfSteps(self, num):
        count =0 
        while num > 0:
            count += 1
            if num % 2 ==0:
                num = num / 2
            else:
                num = num - 1 
        return count
s = Solution()

print(s.numberOfSteps(8))
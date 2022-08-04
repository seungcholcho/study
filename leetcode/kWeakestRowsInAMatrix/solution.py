class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        indexed_list=[]
        count = 0
        for x in mat:
            sum = 0
            for y in x:
                sum += y

            indexed_list.append([count,sum])
            count += 1


        indexed_list.sort(key = lambda x:(x[1],x[0]))
        solution = []

        for i in range(k):
            solution.append(indexed_list[i][0])

        return solution


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

solution = Solution()

solution.kWeakestRows(mat, 3)

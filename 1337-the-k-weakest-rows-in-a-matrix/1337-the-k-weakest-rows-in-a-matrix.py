class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])
        
        mList= []
        for i in range(rows):
            count = 0
            for person in mat[i]:
                if person == 0:
                    break
                else:
                    count += 1
            mList.append((count, i))
        mList.sort()
        result = []
        for i in range(k):
            result.append(mList[i][1])
        return result
                
        
        
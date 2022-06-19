
class Node:
    def __init__(self):
        self.children = [-1] * 26

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        start = 0
        wordSoFar = ""
        results = []
        for i in searchWord:
            temp = []
            wordSoFar += i
            loop_starter = start
            is_broke = False
            for j in range(loop_starter, len(products)):
                if self.starts_with(products[j], wordSoFar):
                    temp.append(products[j])
                    for k in range(2):
                        m = j + k + 1
                        if m < len(products) and self.starts_with(products[m], wordSoFar):
                            temp.append(products[m])
                        else:
                            break
                    results.append(temp)
                    is_broke = True
                    break
                else:
                    start += 1
            if not is_broke:
                results.append([])
        return results
                
    def starts_with(self, target, prefix):
        if len(prefix) > len(target):
            return False
        for i in range(len(prefix)):
            if target[i] != prefix[i]:
                return False
        return True
            
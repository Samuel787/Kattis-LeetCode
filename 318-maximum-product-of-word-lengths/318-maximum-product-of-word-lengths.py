class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def custom_comp(w1, w2):
            if len(w1) > len(w2):
                return -1
            else:
                return 1
            
        words.sort(cmp=custom_comp)
        # print(words)
        dict_list = []
        for word in words:
            curr_dict = {}
            for i in word:
                curr_dict[i] = 1
            curr_dict["length"] = len(word)
            dict_list.append(curr_dict)
        
        max_product = 0
        for i in range(0, len(dict_list), 1):
            curr_dict = dict_list[i]
            for j in range(i + 1, len(dict_list), 1):
                comp_dict = dict_list[j]
                contains_letter = False
                for key in curr_dict:
                    if key in comp_dict and key != "length":
                        # print("common letter in " + words[i] + " and " + words[j] + " is " + key)
                        contains_letter = True
                        break
                if not contains_letter:
                    # print("The solution is " + words[i] + " and " + words[j])
                    max_product = max(max_product, curr_dict["length"] * comp_dict["length"])
        return max_product
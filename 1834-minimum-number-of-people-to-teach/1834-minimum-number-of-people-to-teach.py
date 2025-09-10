class Solution(object):
    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        problemSet = set()

        for friends in friendships:
            languageSet = set(languages[friends[0] - 1])
            speaks = False
            for language in languages[friends[1] - 1]:
                if language in languageSet:
                    speaks = True
                    break
            if not speaks:
                problemSet.add(friends[0])
                problemSet.add(friends[1])
        
        maxCount = 0
        languageMap = {}
        for friend in problemSet:
            for language in languages[friend - 1]:
                if language not in languageMap:
                    languageMap[language] = []
                languageMap[language].append(friend)
                maxCount = max(maxCount, len(languageMap[language]))
            
        return len(problemSet) - maxCount
        
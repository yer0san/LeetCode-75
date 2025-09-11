# difficulty : medium
# there was a better way to impletent this idea using Counter imported from collections or maybe using defaultdict(int)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        d1 = dict()
        d2 = dict()
        
        for i in range(len(word1)):
            if word1[i] in d1:
                d1[word1[i]] += 1
            else:
                d1[word1[i]] = 1
            
            if word2[i] in d2:
                d2[word2[i]] += 1
            else:
                d2[word2[i]] = 1
        d1_view = d1.values()
        l1 = list(d1_view)
        d2_view = d2.values()
        l2 = list(d2_view)

        l1.sort()
        l2.sort()

        return l1 == l2 and set(word1) == set(word2)

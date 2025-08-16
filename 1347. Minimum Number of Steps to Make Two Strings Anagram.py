class Solution(object):
    def minSteps(self, s, t):
        hash_map = {}
        hash_map1 = {}
        count = 0
        for i in range(len(s)):
            hash_map[s[i]] = hash_map.get(s[i], 0) + 1
        for j in range(len(t)):
            hash_map1[t[j]] = hash_map1.get(t[j], 0) + 1

        for i in hash_map:
            if hash_map[i] > hash_map1.get(i, 0):
                count += hash_map[i] - hash_map1.get(i, 0)

        return count
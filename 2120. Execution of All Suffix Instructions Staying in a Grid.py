class Solution(object):
    def executeInstructions(self, n, startPos, s):
        result = []
        direction_map = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}
        for i in range(len(s)):
            row,col = startPos
            count = 0
            for j in range(i ,len(s)):
                (dr, dc) = direction_map[s[j]]
                row += dr
                col += dc
                if row < 0 or row >= n or col < 0 or col >= n:
                    break
                count += 1
            result.append(count)
        return result
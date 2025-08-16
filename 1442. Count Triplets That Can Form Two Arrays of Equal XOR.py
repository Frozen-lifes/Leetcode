class Solution(object):
    def countTriplets(self, arr):
        count = 0
        a=0
        b = 0
        for i in range(len(arr)):
            a ^= arr[i]
            b ^= arr[i]
        for j in range(len(arr)):
            for k in range(len(arr)):
                if a == b:
                    count += (i -k)

        return count
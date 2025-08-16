class Solution(object):
    def rearrangeArray(self, nums):
        res = []
        list1 = []
        list2 = []
        for i in range(len(nums)):
            if nums[i] > 0:
                list1.append(nums[i])
            if nums[i] < 0:
                list2.append(nums[i])
        for i in range(len(list1)):
            res.append(list1[i])
            res.append(list2[i])
        return res


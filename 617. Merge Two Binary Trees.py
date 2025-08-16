class Solution(object):
    def mergeTrees(self, root1, root2):

        if root1 and root2:
            value = TreeNode(root1.val + root2.val)
            value.left = self.mergeTrees(root1.left, root2.left)
            value.right = self.mergeTrees(root1.right, root2.right)
            return value
        else:
            return root1 or root2
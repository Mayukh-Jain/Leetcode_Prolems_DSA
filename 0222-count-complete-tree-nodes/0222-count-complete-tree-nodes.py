# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        lh=0
        rh=0
        curr=root
        while curr:
            curr=curr.left
            lh+=1
        curr=root
        while curr:
            curr=curr.right
            rh+=1
        if lh==rh: return 2**lh-1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
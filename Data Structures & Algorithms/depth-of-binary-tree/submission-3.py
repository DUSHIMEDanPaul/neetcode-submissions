# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=0
        q=[[root,1]]
        while q:
            node,depth =q.pop()
            if node:
                res=max(res,depth)
                q.append([node.left,depth+1])
                q.append([node.right,depth+1])
        return res
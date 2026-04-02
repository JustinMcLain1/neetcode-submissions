# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_node=[]
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level_node.append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            result.append(level_node)
        return result
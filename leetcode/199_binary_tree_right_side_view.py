from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        levelQueue: List[TreeNode] = []
        result = []
        levelQueue.append(root)
        temproraryRoot = root
        while len(levelQueue) > 0:
            # we need to preserve the length of the levelQueue to traversal though this queue
            queueLength = len(levelQueue)
            for i in range(queueLength):
                node = levelQueue.pop(0)
                if i == queueLength - 1:
                    result.append(node.val)
                if node.left:
                    levelQueue.append(node.left)
                if node.right:
                    levelQueue.append(node.right)
        return result
                
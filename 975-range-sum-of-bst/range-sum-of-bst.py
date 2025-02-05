class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            # If the current node's value is greater than the high value,
            # explore the left subtree only, because all values in the right subtree
            # will also be greater than 'high' and thus out of the required range.
            if node.val > high:
                return dfs(node.left)

            # If the current node's value is less than the low value,
            # explore the right subtree only, because all values in the left subtree
            # will be less than 'low' and thus out of the required range.
            elif node.val < low:
                return dfs(node.right)

            # If the current node's value is within the range,
            # continue the search in both directions.
            else:
                return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)

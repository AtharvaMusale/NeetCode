# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root):
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
            if node:
                cols[i].append(node.val)
                queue += (node.left, i - 1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]
    # def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

    #     hashmap = collections.defaultdict(list)
    #     queue = deque([(root,0)])

    #     while queue:
    #         node, col = queue.popleft()

    #         if node is not None:
    #             hashmap[col].append(node.val)
    #             queue.append((node.left,col-1))
    #             queue.append((node.right,col+1))
        
    #     return [hashmap[x] for x in sorted(hashmap.keys())]
        
            


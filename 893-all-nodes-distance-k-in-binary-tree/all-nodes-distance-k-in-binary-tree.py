# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Node: [list of neighbours]

        graph = collections.defaultdict(list)
        q = deque([root])

        while q:
            node = q.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)

        res = []
        visit = set([target])
        q = deque([(target,0)])
        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visit:
                        q.append((edge, dist+1))
                        visit.add(edge)
        
        return res



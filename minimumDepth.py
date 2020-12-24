from collections import deque


def minDepth(self, root) -> int:
    if not root:
        return 0

    q = deque([(root, 1)])

    while q:
        node, depth = q.popleft()

        if not node.left and not node.right:
            return depth

        for child in [node.left, node.right]:
            if not child:
                continue
            q.append((child, depth+1))

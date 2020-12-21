from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):

        d = defaultdict(list)  # directed graph
        nodes = set()  # nodes
        in_deg = {}
        s = set()

        # Make Directed Graph and maintain a unique list of nodes
        for c, pre in prerequisites:
            d[pre].append(c)  # di-graph

            nodes.add(pre)
            nodes.add(c)

        # Keep Track of how many adjacent nodes each node has
        for c, pre in prerequisites:
            if c in in_deg:
                in_deg[c] += 1
            else:
                in_deg[c] = 1

        # if a course or pre requisite has 0 prereqs add to stack (set makes it unique)
        for c, pre in prerequisites:
            if c not in in_deg:
                s.add(c)
            if pre not in in_deg:
                s.add(pre)

        # add courses with no prerequisites into stack
        for i in range(numCourses):
            if i not in in_deg:
                s.add(i)

        # Convert set -> list/array/stack
        stack = list(s)

        # Response List and Visited set
        res = []
        visited = set()

        # DFS
        while stack:
            node = stack.pop()  # Get node
            res.append(node)  # Add to response
            visited.add(node)  # Add to visited

            for nei in d[node]:  # Check each adjacent node
                if nei not in visited:  # If not visited reduce that node's its in_deg by 1
                    in_deg[nei] -= 1

                    if in_deg[nei] == 0:  # No Prereq's left add to stack
                        stack.append(nei)

        if len(res) == numCourses:  # if all classes are taken its Possible
            return res
        else:
            return []  # else return not possible

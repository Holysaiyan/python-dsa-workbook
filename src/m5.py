"""Module 5: Trees, heaps and graphs."""

MODULE = {"id": "trees-graphs", "title": "Trees, heaps and graphs"}

LESSONS = []

# ---------------------------------------------------------------- trees
LESSONS.append({
    "id": "trees",
    "title": "Trees and traversals",
    "minutes": 30,
    "tags": [],
    "summary": "A tree is a hierarchy of nodes with one root. Binary trees, where each node has at most two children, are an interview staple, and recursion makes them short to write.",
    "blocks": [
        ("p", "A <b>tree</b> has a <b>root</b> node at the top. Each node can have <b>children</b>; a node with none is a <b>leaf</b>. The <b>height</b> is the number of levels. In a <b>binary tree</b> each node has at most a left and a right child."),
        ("diagram", "tree"),
        ("code", """class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#        8
#       / \\
#      3   10
#     / \\    \\
#    1   6    14
root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14)))

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def count(node):
    if node is None:
        return 0
    return 1 + count(node.left) + count(node.right)

print(height(root), count(root))"""),
        ("h", "Depth-first traversals"),
        ("p", "The three orders differ only in when you visit the node itself relative to its children."),
        ("table", ["Order", "Visit sequence", "Common use"], [
            ["Pre-order", "node, left, right", "Copying a tree, printing a folder structure"],
            ["In-order", "left, node, right", "Gives a binary search tree in sorted order"],
            ["Post-order", "left, right, node", "Deleting a tree, totals that need children first"],
        ]),
        ("code", """class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14)))

def inorder(node, out):
    if node:
        inorder(node.left, out)
        out.append(node.val)
        inorder(node.right, out)
    return out

def preorder(node, out):
    if node:
        out.append(node.val)
        preorder(node.left, out)
        preorder(node.right, out)
    return out

print(inorder(root, []))
print(preorder(root, []))"""),
        ("h", "Breadth-first: level by level"),
        ("p", "Use a queue. Take a node from the front, record it, and add its children to the back."),
        ("code", """from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14)))

def levels(root):
    if not root:
        return []
    result, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result

print(levels(root))"""),
        ("h", "Binary search trees"),
        ("p", "In a <b>binary search tree</b> (BST), everything in a node's left subtree is smaller than it and everything on the right is larger. Searching follows one path down: O(h), which is O(log n) when the tree is balanced and O(n) when it degenerates into a chain."),
        ("code", """class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(node, val):
    if node is None:
        return TreeNode(val)
    if val < node.val:
        node.left = insert(node.left, val)
    else:
        node.right = insert(node.right, val)
    return node

def contains(node, val):
    while node:
        if val == node.val:
            return True
        node = node.left if val < node.val else node.right
    return False

root = None
for v in [8, 3, 10, 1, 6, 14]:
    root = insert(root, v)
print(contains(root, 6), contains(root, 7))"""),
    ],
    "mistakes": [
        "Forgetting the <code>None</code> base case for an empty subtree.",
        "Assuming a BST is balanced: a sorted insert order produces a chain.",
        "Mixing up height (levels) and number of nodes.",
    ],
    "practice": {
        "title": "Sum of the leaves",
        "prompt": "<p>A <code>TreeNode</code> class is provided. Write <code>leaf_sum(root)</code>, which returns the sum of the values of all <b>leaves</b> (nodes with no children). An empty tree returns 0.</p><p>The checker builds trees from level-order lists such as <code>[8, 3, 10, 1, 6, None, 14]</code>, where <code>None</code> is a missing child. That tree's leaves are 1, 6 and 14, so the answer is 21.</p>",
        "func": "leaf_sum",
        "starter": "class TreeNode:\n    def __init__(self, val, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef leaf_sum(root):\n    pass\n",
        "wrapper": """def __call(values):
    from collections import deque as __dq
    if not values or values[0] is None:
        return leaf_sum(None)
    root = TreeNode(values[0])
    q = __dq([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i]); q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i]); q.append(node.right)
        i += 1
    return leaf_sum(root)
""",
        "tests": [
            ("given example", [[8, 3, 10, 1, 6, None, 14]], False),
            ("single node is a leaf", [[5]], False),
            ("empty tree", [[]], True),
            ("left chain", [[1, 2, None, 3]], True),
            ("negative leaves", [[0, -4, 9]], True),
        ],
        "hints": [
            "Recursion with three cases: an empty node, a leaf, and a node with children.",
            "A leaf has <code>node.left is None and node.right is None</code>. For any other node, return the leaf sums of its two subtrees added together.",
        ],
        "solution": """class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def leaf_sum(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return root.val
    return leaf_sum(root.left) + leaf_sum(root.right)
""",
        "explain": "Each node is visited once: <b>O(n)</b> time. The recursion is as deep as the tree: <b>O(h)</b> space.",
    },
    "related": [("LeetCode: Maximum Depth of Binary Tree", "https://leetcode.com/problems/maximum-depth-of-binary-tree/")],
})

# ---------------------------------------------------------------- heaps
LESSONS.append({
    "id": "heaps",
    "title": "Heaps and priority queues",
    "minutes": 20,
    "tags": [],
    "summary": "A heap always gives you its smallest item in O(1) and adds or removes in O(log n). Use it for 'the k largest', 'the next most urgent', and shortest paths.",
    "blocks": [
        ("p", "A <b>min-heap</b> is a tree stored in a list where every parent is smaller than or equal to its children, so the smallest item is always at position 0. Python's <code>heapq</code> module keeps a plain list in heap order."),
        ("code", """import heapq

h = []
for x in [5, 1, 8, 3, 2]:
    heapq.heappush(h, x)
print(h[0])                 # smallest, O(1)
print(heapq.heappop(h))     # remove smallest, O(log n)
print(heapq.heappop(h))

nums = [9, 4, 7, 1]
heapq.heapify(nums)         # O(n), in place
print(nums[0])"""),
        ("table", ["Operation", "Code", "Cost"], [
            ["Peek smallest", "<code>h[0]</code>", "O(1)"],
            ["Push", "<code>heapq.heappush(h, x)</code>", "O(log n)"],
            ["Pop smallest", "<code>heapq.heappop(h)</code>", "O(log n)"],
            ["Build from a list", "<code>heapq.heapify(lst)</code>", "O(n)"],
        ]),
        ("h", "Priority queues with tuples"),
        ("p", "Push <code>(priority, item)</code> tuples. Tuples compare by their first element, so the lowest priority number comes out first. For a max-heap, push negated numbers."),
        ("code", """import heapq

jobs = []
heapq.heappush(jobs, (2, "repaint hallway"))
heapq.heappush(jobs, (1, "gas leak"))
heapq.heappush(jobs, (3, "replace bulb"))
while jobs:
    priority, job = heapq.heappop(jobs)
    print(priority, job)

# Max-heap trick: negate
scores = [40, 75, 62]
mx = [-s for s in scores]
heapq.heapify(mx)
print(-heapq.heappop(mx))"""),
        ("h", "Pattern: the k largest"),
        ("p", "Keep a min-heap of size k. When it grows beyond k, pop the smallest. What remains are the k largest, in O(n log k)."),
        ("code", """import heapq

def k_largest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)
    return sorted(h, reverse=True)

print(k_largest([3, 2, 1, 5, 6, 4], 2))
print(heapq.nlargest(2, [3, 2, 1, 5, 6, 4]))   # built-in shortcut"""),
    ],
    "mistakes": [
        "Expecting a heap list to be fully sorted. Only position 0 is guaranteed.",
        "Forgetting Python only has a min-heap. Negate numbers for a max-heap.",
        "Pushing tuples whose second items cannot be compared when priorities tie. Add a counter as a tie-breaker.",
    ],
    "practice": {
        "title": "Kth most expensive repair",
        "prompt": "<p>Write <code>kth_largest(costs, k)</code>. Return the k-th largest value in <code>costs</code> (duplicates count separately). You can assume <code>1 &lt;= k &lt;= len(costs)</code>. Try a heap of size k rather than sorting.</p><p>Example: <code>kth_largest([3, 2, 1, 5, 6, 4], 2)</code> returns <code>5</code>.</p>",
        "func": "kth_largest",
        "starter": "import heapq\n\ndef kth_largest(costs, k):\n    pass\n",
        "tests": [
            ("given example", [[3, 2, 1, 5, 6, 4], 2], False),
            ("k is 1", [[7, 9, 2], 1], False),
            ("duplicates count", [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], True),
            ("single item", [[42], 1], True),
            ("k equals length", [[5, 1, 9], 3], True),
            ("negatives", [[-1, -5, -3], 2], True),
        ],
        "hints": [
            "Keep a min-heap of the k largest values seen so far.",
            "After the loop, the smallest of those k values, <code>h[0]</code>, is the answer.",
        ],
        "solution": """import heapq

def kth_largest(costs, k):
    h = []
    for c in costs:
        heapq.heappush(h, c)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
""",
        "explain": "n pushes and pops on a heap of size k: <b>O(n log k)</b> time and <b>O(k)</b> space. Sorting would be O(n log n).",
    },
    "related": [("LeetCode: Kth Largest Element in an Array", "https://leetcode.com/problems/kth-largest-element-in-an-array/")],
})

# ---------------------------------------------------------------- graphs
LESSONS.append({
    "id": "graphs",
    "title": "Graphs, BFS and DFS",
    "minutes": 35,
    "tags": ["Lloyds"],
    "summary": "A graph is a set of points joined by connections. Breadth-first search finds shortest hop counts; depth-first search explores everything reachable. Lloyds lists a graph task.",
    "blocks": [
        ("p", "A <b>graph</b> has <b>vertices</b> (nodes, points) and <b>edges</b> (connections). Edges can be <b>undirected</b> (a two-way road) or <b>directed</b> (a one-way street), and can carry <b>weights</b> such as distance."),
        ("h", "Storing a graph: the adjacency list"),
        ("p", "Map each vertex to a list of its neighbours. Build it from an edge list with a <code>defaultdict(list)</code>."),
        ("code", """from collections import defaultdict

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)     # leave this out for a directed graph
print(dict(graph))"""),
        ("diagram", "graph"),
        ("h", "Breadth-first search (BFS)"),
        ("p", "BFS explores in rings: all vertices 1 hop away, then 2 hops, and so on. It uses a queue and a <code>visited</code> set. In an unweighted graph, the first time BFS reaches a vertex is by a shortest path."),
        ("code", """from collections import deque, defaultdict

edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

def hops_from(start):
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if nxt not in dist:          # dist doubles as visited
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    return dist

print(hops_from("A"))"""),
        ("h", "Depth-first search (DFS)"),
        ("p", "DFS goes as deep as possible along one route before backtracking. Use it for 'is there any path', counting connected groups, and detecting cycles. Write it with recursion or with an explicit stack."),
        ("code", """from collections import defaultdict

edges = [(1, 2), (2, 3), (4, 5)]
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)
nodes = [1, 2, 3, 4, 5, 6]

def count_groups():
    seen = set()
    groups = 0
    for start in nodes:
        if start in seen:
            continue
        groups += 1
        stack = [start]
        seen.add(start)
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
    return groups

print(count_groups())     # {1,2,3}, {4,5}, {6}"""),
        ("h", "Grids are graphs too"),
        ("p", "In a grid, each cell is a vertex and its up, down, left and right neighbours are edges. Check bounds before stepping."),
        ("code", """from collections import deque

grid = ["..#.",
        ".##.",
        "...."]
rows, cols = len(grid), len(grid[0])

def shortest(start, goal):
    q = deque([(start, 0)])
    seen = {start}
    while q:
        (r, c), d = q.popleft()
        if (r, c) == goal:
            return d
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "." and (nr, nc) not in seen:
                seen.add((nr, nc))
                q.append(((nr, nc), d + 1))
    return -1

print(shortest((0, 0), (0, 3)))"""),
        ("h", "Weighted graphs: Dijkstra's algorithm"),
        ("p", "When edges have different weights, BFS no longer gives shortest distances. Dijkstra's algorithm replaces the queue with a heap, always expanding the closest unfinished vertex. O((V + E) log V)."),
        ("code", """import heapq

graph = {"A": [("B", 4), ("C", 1)], "B": [("D", 1)], "C": [("B", 2), ("D", 5)], "D": []}

def dijkstra(start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue                  # stale entry
        for nxt, w in graph[node]:
            nd = d + w
            if nd < dist.get(nxt, float("inf")):
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist

print(dijkstra("A"))"""),
        ("table", ["Question", "Use", "Cost"], [
            ["Fewest hops, unweighted", "BFS", "O(V + E)"],
            ["Is B reachable from A?", "BFS or DFS", "O(V + E)"],
            ["How many separate groups?", "DFS or BFS from each unvisited vertex", "O(V + E)"],
            ["Shortest distance, weighted (no negatives)", "Dijkstra", "O((V + E) log V)"],
        ]),
    ],
    "mistakes": [
        "Forgetting the <code>visited</code> set, so a cycle loops forever.",
        "Marking a vertex visited when you pop it instead of when you push it, which queues it many times.",
        "Adding only one direction of an undirected edge.",
        "Forgetting isolated vertices that have no edges at all.",
        "Using BFS for weighted shortest paths.",
    ],
    "practice": {
        "title": "Fewest transfers between stations",
        "prompt": "<p>Write <code>fewest_hops(edges, start, goal)</code>. <code>edges</code> is a list of two-way connections <code>[a, b]</code> between stations. Return the fewest connections needed to travel from <code>start</code> to <code>goal</code>, or <code>-1</code> if it cannot be reached. Travelling from a station to itself takes 0.</p><p>Example: with edges <code>[['A','B'], ['B','C'], ['A','D'], ['D','C'], ['C','E']]</code>, <code>fewest_hops(edges, 'A', 'E')</code> returns <code>3</code>.</p>",
        "func": "fewest_hops",
        "starter": "from collections import deque, defaultdict\n\ndef fewest_hops(edges, start, goal):\n    pass\n",
        "tests": [
            ("given example", [[["A", "B"], ["B", "C"], ["A", "D"], ["D", "C"], ["C", "E"]], "A", "E"], False),
            ("direct link", [[["A", "B"]], "A", "B"], False),
            ("same station", [[["A", "B"]], "A", "A"], True),
            ("unreachable", [[["A", "B"], ["C", "D"]], "A", "D"], True),
            ("station with no edges", [[], "X", "Y"], True),
            ("cycle", [[["A", "B"], ["B", "C"], ["C", "A"], ["C", "D"]], "A", "D"], True),
        ],
        "hints": [
            "Build an adjacency list first, adding both directions.",
            "BFS from <code>start</code> with a <code>dist</code> dictionary. Return <code>dist[goal]</code> as soon as you reach it, or -1 when the queue empties.",
        ],
        "solution": """from collections import deque, defaultdict

def fewest_hops(edges, start, goal):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    dist = {start: 0}
    q = deque([start])
    while q:
        node = q.popleft()
        if node == goal:
            return dist[node]
        for nxt in graph[node]:
            if nxt not in dist:
                dist[nxt] = dist[node] + 1
                q.append(nxt)
    return -1
""",
        "explain": "Building the graph is O(E); BFS visits each vertex and edge once: <b>O(V + E)</b> time and <b>O(V + E)</b> space.",
    },
    "related": [("LeetCode: Number of Islands", "https://leetcode.com/problems/number-of-islands/")],
})

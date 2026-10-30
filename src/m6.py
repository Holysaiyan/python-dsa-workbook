"""Module 6: Problem-solving strategies."""

MODULE = {"id": "strategies", "title": "Problem-solving strategies"}

LESSONS = []

# ---------------------------------------------------------------- greedy
LESSONS.append({
    "id": "greedy",
    "title": "Greedy algorithms",
    "minutes": 20,
    "tags": [],
    "summary": "A greedy algorithm makes the locally best choice at every step and never reconsiders. It is fast and simple, but only correct for problems with the right structure.",
    "blocks": [
        ("p", "A <b>greedy</b> algorithm builds an answer one decision at a time, always taking whatever looks best right now. When that works it is usually the simplest O(n) or O(n log n) solution. When it does not work, it gives confidently wrong answers, so test it on small cases."),
        ("h", "Example that works: scheduling the most meetings"),
        ("p", "To fit the most non-overlapping meetings into one room, always pick the meeting that <b>finishes earliest</b>. Finishing early leaves the most room for the rest."),
        ("code", """def most_meetings(meetings):
    count = 0
    free_from = float("-inf")
    for start, end in sorted(meetings, key=lambda m: m[1]):
        if start >= free_from:
            count += 1
            free_from = end
    return count

print(most_meetings([(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]))"""),
        ("h", "Example where greedy fails"),
        ("p", "Making change with the fewest coins: always taking the biggest coin works for UK coins, but fails for unusual sets. With coins 1, 3 and 4, greedy pays 6 as 4 + 1 + 1 (three coins) when 3 + 3 (two coins) is better. That problem needs dynamic programming (next lesson)."),
        ("code", """def greedy_change(amount, coins):
    used = []
    for c in sorted(coins, reverse=True):
        while amount >= c:
            amount -= c
            used.append(c)
    return used

print(greedy_change(6, [1, 3, 4]))    # 3 coins: not optimal
print(greedy_change(68, [1, 2, 5, 10, 20, 50]))"""),
        ("tip", "Before trusting a greedy idea, try to break it with a tiny counter-example. If you cannot, and the choice never needs undoing, greedy is probably right."),
    ],
    "mistakes": [
        "Assuming greedy works without testing a counter-example.",
        "Sorting by the wrong key, such as start time instead of end time for meetings.",
        "Forgetting that sorting makes a greedy solution O(n log n).",
    ],
    "practice": {
        "title": "Minimum rooms needed",
        "prompt": "<p>Write <code>rooms_needed(bookings)</code>. Each booking is <code>[start, end]</code>, occupying a room from <code>start</code> up to but not including <code>end</code>. Return the minimum number of rooms so that no two overlapping bookings share a room.</p><p>Example: <code>rooms_needed([[9, 11], [10, 12], [11, 13]])</code> returns <code>2</code> (the first ends exactly when the third starts, so they can share).</p>",
        "func": "rooms_needed",
        "starter": "import heapq\n\ndef rooms_needed(bookings):\n    pass\n",
        "tests": [
            ("given example", [[[9, 11], [10, 12], [11, 13]]], False),
            ("no overlap", [[[1, 2], [3, 4]]], False),
            ("empty", [[]], True),
            ("all overlap", [[[1, 10], [2, 9], [3, 8]]], True),
            ("touching ends share", [[[1, 2], [2, 3], [3, 4]]], True),
            ("unsorted input", [[[5, 8], [1, 6], [2, 3]]], True),
        ],
        "hints": [
            "Sort bookings by start time. Keep a min-heap of end times for rooms in use.",
            "For each booking, if the earliest-ending room is free by its start (<code>h[0] &lt;= start</code>), reuse it with <code>heappop</code>. Push the new end. The answer is the largest heap size reached.",
        ],
        "solution": """import heapq

def rooms_needed(bookings):
    ends = []
    best = 0
    for start, end in sorted(bookings):
        if ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
        best = max(best, len(ends))
    return best
""",
        "explain": "Sorting is O(n log n) and each heap operation O(log n): <b>O(n log n)</b> time and <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- DP
LESSONS.append({
    "id": "dynamic-programming",
    "title": "Dynamic programming",
    "minutes": 35,
    "tags": [],
    "summary": "Dynamic programming solves a problem by combining answers to smaller overlapping sub-problems, computing each one only once.",
    "blocks": [
        ("p", "Use <b>dynamic programming</b> (DP) when a problem can be answered from answers to smaller versions of itself, and those smaller versions repeat. The work is mostly in defining the right sub-problem."),
        ("h", "The four questions"),
        ("steps", [
            "<b>State:</b> what does <code>dp[i]</code> mean, in one sentence?",
            "<b>Base case:</b> which values do you know without calculating?",
            "<b>Transition:</b> how is <code>dp[i]</code> built from smaller states?",
            "<b>Answer:</b> which state holds the final answer?",
        ]),
        ("h", "Example: climbing stairs"),
        ("p", "You can climb 1 or 2 steps at a time. How many different ways reach step n? To reach step i, your last move came from step i - 1 or step i - 2, so <code>ways[i] = ways[i - 1] + ways[i - 2]</code>."),
        ("code", """def climb(n):
    if n <= 1:
        return 1
    ways = [0] * (n + 1)
    ways[0], ways[1] = 1, 1          # base cases
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]

print([climb(n) for n in range(1, 8)])"""),
        ("h", "Example: fewest coins"),
        ("p", "State: <code>dp[a]</code> is the fewest coins making amount a. Base: <code>dp[0] = 0</code>. Transition: try every coin c as the last coin, so <code>dp[a] = 1 + min(dp[a - c])</code>. This fixes the greedy failure from the last lesson."),
        ("code", """def fewest_coins(amount, coins):
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1

print(fewest_coins(6, [1, 3, 4]))
print(fewest_coins(7, [2, 4]))"""),
        ("h", "Top-down and bottom-up"),
        ("table", ["Style", "How", "Feels like"], [
            ["Top-down (memoisation)", "Recursive function plus a cache dictionary", "Natural to write from the recurrence"],
            ["Bottom-up (tabulation)", "Fill a list from the base cases upwards", "No recursion limit, often less memory"],
        ]),
        ("code", """from functools import lru_cache

@lru_cache(maxsize=None)
def climb_top_down(n):
    if n <= 1:
        return 1
    return climb_top_down(n - 1) + climb_top_down(n - 2)

print(climb_top_down(30))"""),
        ("tip", "Words like 'number of ways', 'minimum cost', 'maximum total' and 'can you reach' over choices that build on each other often signal DP."),
    ],
    "mistakes": [
        "Starting to code before writing the state in one sentence.",
        "Wrong or missing base cases.",
        "Filling the table in an order where a state is used before it is computed.",
        "Using greedy where choices interact.",
    ],
    "practice": {
        "title": "Non-adjacent shifts",
        "prompt": "<p>Write <code>best_shifts(pay)</code>. <code>pay[i]</code> is what shift i pays. You cannot work two shifts next to each other. Return the largest total you can earn. An empty list returns 0.</p><p>Example: <code>best_shifts([2, 7, 9, 3, 1])</code> returns <code>12</code> (shifts 0, 2 and 4: 2 + 9 + 1).</p>",
        "func": "best_shifts",
        "starter": "def best_shifts(pay):\n    pass\n",
        "tests": [
            ("given example", [[2, 7, 9, 3, 1]], False),
            ("two shifts", [[5, 9]], False),
            ("empty", [[]], True),
            ("single shift", [[4]], True),
            ("skip two in a row", [[2, 1, 1, 9]], True),
            ("all equal", [[3, 3, 3, 3, 3]], True),
        ],
        "hints": [
            "State: <code>best[i]</code> is the most you can earn from shifts 0 to i.",
            "At shift i you either skip it (<code>best[i - 1]</code>) or take it (<code>pay[i] + best[i - 2]</code>). Two variables are enough.",
        ],
        "solution": """def best_shifts(pay):
    take_prev2, best_prev = 0, 0
    for p in pay:
        take_prev2, best_prev = best_prev, max(best_prev, take_prev2 + p)
    return best_prev
""",
        "explain": "One pass with two variables: <b>O(n)</b> time and <b>O(1)</b> space. This is the LeetCode problem House Robber.",
    },
    "related": [("LeetCode: Climbing Stairs", "https://leetcode.com/problems/climbing-stairs/"), ("LeetCode: House Robber", "https://leetcode.com/problems/house-robber/")],
})

# ---------------------------------------------------------------- patterns
LESSONS.append({
    "id": "pattern-guide",
    "title": "Pattern recognition guide",
    "minutes": 10,
    "tags": ["Accenture", "Lloyds"],
    "summary": "A one-page reference linking the words in a problem to the technique that usually solves it. Review it before every assessment.",
    "blocks": [
        ("p", "Read the problem, underline its key phrases, and match them below. Then use the six-step routine from the first lesson."),
        ("table", ["Signal in the problem", "Try", "Typical cost", "Lesson"], [
            ["'seen before', 'duplicate', 'already', 'contains'", "Set", "O(n)", "<a href='#sets'>Hash sets</a>"],
            ["'count', 'most frequent', 'anagram', 'group by'", "Dictionary, Counter", "O(n)", "<a href='#dictionaries'>Hash maps</a>"],
            ["'pair that sums to', return positions", "Dictionary of value to position", "O(n)", "<a href='#dictionaries'>Hash maps</a>"],
            ["Sorted input, 'pair', 'palindrome', 'in place'", "Two pointers", "O(n)", "<a href='#two-pointers'>Two pointers</a>"],
            ["'consecutive', 'subarray', 'substring', 'k days in a row'", "Sliding window", "O(n)", "<a href='#sliding-window'>Sliding window</a>"],
            ["'sum between i and j', many range questions", "Prefix sums", "O(n + q)", "<a href='#prefix-sums'>Prefix sums</a>"],
            ["'matching brackets', 'undo', 'most recent', nesting", "Stack", "O(n)", "<a href='#stacks'>Stacks</a>"],
            ["'in arrival order', 'last k seconds'", "Queue (deque)", "O(n)", "<a href='#queues'>Queues</a>"],
            ["Sorted data, 'find position', 'smallest value that works'", "Binary search", "O(log n)", "<a href='#binary-search'>Binary search</a>"],
            ["'k largest', 'next most urgent', 'merge sorted'", "Heap", "O(n log k)", "<a href='#heaps'>Heaps</a>"],
            ["'shortest path', 'fewest steps', grid of cells", "BFS", "O(V + E)", "<a href='#graphs'>Graphs</a>"],
            ["'connected', 'reachable', 'number of groups'", "DFS or BFS", "O(V + E)", "<a href='#graphs'>Graphs</a>"],
            ["Hierarchy, folders, nested lists", "Recursion", "O(n)", "<a href='#recursion'>Recursion</a>"],
            ["'number of ways', 'minimum cost', 'maximum total' over choices", "Dynamic programming", "Varies", "<a href='#dynamic-programming'>Dynamic programming</a>"],
            ["'schedule the most', 'fewest rooms'", "Greedy after sorting", "O(n log n)", "<a href='#greedy'>Greedy</a>"],
        ]),
        ("h", "What the input size tells you"),
        ("p", "If a problem states its limits, they hint at the complexity the setter expects."),
        ("table", ["Largest n", "Aim for"], [
            ["Up to about 20", "O(2<sup>n</sup>) may be fine: try every combination"],
            ["Up to about 1,000", "O(n&sup2;) is usually fine"],
            ["Up to about 100,000", "O(n log n) or O(n)"],
            ["A million or more", "O(n) or O(log n)"],
        ]),
        ("h", "Before you submit"),
        ("steps", [
            "Run the given example.",
            "Run an empty input and a single item.",
            "Run duplicates, negatives or all-equal values if they are allowed.",
            "Check the return type: list, number, string, <code>True</code>/<code>False</code>, or <code>-1</code>.",
            "Write the complexity in a comment.",
        ]),
    ],
    "mistakes": [],
    "practice": None,
})

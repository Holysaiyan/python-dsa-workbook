"""Module 3: Array techniques."""

MODULE = {"id": "techniques", "title": "Array techniques"}

LESSONS = []

# ---------------------------------------------------------------- two pointers
LESSONS.append({
    "id": "two-pointers",
    "title": "Two pointers",
    "minutes": 20,
    "tags": ["Accenture"],
    "summary": "Two indices moving through a list, often from opposite ends or at different speeds, turn many O(n squared) pair searches into a single O(n) pass.",
    "blocks": [
        ("p", "Instead of checking every pair with nested loops, keep two positions, <code>left</code> and <code>right</code>, and move them according to a rule. Each step moves at least one pointer, so the whole scan is O(n)."),
        ("h", "Shape 1: opposite ends"),
        ("p", "Start one pointer at each end and walk them towards each other. This suits palindromes, reversing in place, and pair sums on a <b>sorted</b> list."),
        ("code", """def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(is_palindrome("level"), is_palindrome("levels"), is_palindrome(""))"""),
        ("p", "On a sorted list, if the pair sum is too small, move <code>left</code> right to make it bigger. If it is too big, move <code>right</code> left."),
        ("code", """def pair_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1
        else:
            right -= 1
    return []

print(pair_sum_sorted([1, 3, 4, 6, 9], 10))"""),
        ("h", "Shape 2: reader and writer"),
        ("p", "Both pointers move left to right. The reader looks at every item; the writer marks where the next kept item goes. This edits a list in place with O(1) extra space."),
        ("code", """def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
    return nums

print(move_zeroes([0, 1, 0, 3, 12]))"""),
        ("tip", "Python swaps without a temporary variable: <code>a, b = b, a</code>."),
    ],
    "mistakes": [
        "Using opposite-end pointers on an unsorted list for a pair sum. Sort first, or use a set.",
        "Writing <code>while left &lt;= right</code> when the middle item should not pair with itself.",
        "Forgetting to move a pointer in some branch, which loops forever.",
    ],
    "practice": {
        "title": "Valid palindrome, ignoring punctuation",
        "prompt": "<p>Write <code>is_clean_palindrome(s)</code>. Ignore everything except letters and digits, and ignore case. Return <code>True</code> if what remains reads the same both ways. An empty result counts as a palindrome.</p><p>Example: <code>'A man, a plan, a canal: Panama'</code> returns <code>True</code>.</p>",
        "func": "is_clean_palindrome",
        "starter": "def is_clean_palindrome(s):\n    pass\n",
        "tests": [
            ("given example", ["A man, a plan, a canal: Panama"], False),
            ("not a palindrome", ["race a car"], False),
            ("empty string", [""], True),
            ("only punctuation", [".,!"], True),
            ("digits count", ["0P"], True),
            ("mixed case", ["Abba"], True),
        ],
        "hints": [
            "<code>ch.isalnum()</code> tells you whether a character is a letter or digit. <code>ch.lower()</code> ignores case.",
            "Either build a cleaned string and compare it with its reverse, or move two pointers inward, skipping anything that is not alphanumeric.",
        ],
        "solution": """def is_clean_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True
""",
        "explain": "Each character is visited at most once: <b>O(n)</b> time and <b>O(1)</b> extra space. Building a cleaned copy also works in O(n) time but uses O(n) space.",
    },
    "related": [("LeetCode: Valid Palindrome", "https://leetcode.com/problems/valid-palindrome/"), ("LeetCode: Move Zeroes", "https://leetcode.com/problems/move-zeroes/")],
})

# ---------------------------------------------------------------- sliding window
LESSONS.append({
    "id": "sliding-window",
    "title": "Sliding window",
    "minutes": 25,
    "tags": ["Accenture"],
    "summary": "A window is a run of consecutive items. Slide it along, updating a running total or set as items enter and leave, instead of recomputing from scratch.",
    "blocks": [
        ("p", "Problems that mention <b>consecutive</b>, <b>contiguous</b>, <b>subarray</b>, <b>substring</b> or <b>a run of k days</b> are usually sliding window problems."),
        ("h", "Fixed-size window"),
        ("p", "Recomputing the sum of every window of size k costs O(n &times; k). Instead, add the item entering the window and subtract the one leaving it: O(1) per step, O(n) overall."),
        ("code", """def best_window(nums, k):
    if k <= 0 or k > len(nums):
        return 0
    window = sum(nums[:k])          # first window
    best = window
    for i in range(k, len(nums)):
        window += nums[i]           # item entering
        window -= nums[i - k]       # item leaving
        best = max(best, window)
    return best

print(best_window([4, 2, 7, 1, 8, 3], 2))
print(best_window([4, 2, 7, 1, 8, 3], 3))"""),
        ("h", "Variable-size window"),
        ("p", "Grow the window by moving <code>right</code>. When the window breaks a rule, shrink it by moving <code>left</code> until it is valid again. Both pointers only move forwards, so it is O(n)."),
        ("code", """def longest_unique(s):
    seen = set()
    left = 0
    best = 0
    for right in range(len(s)):
        while s[right] in seen:      # rule broken: duplicate
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        best = max(best, right - left + 1)
    return best

print(longest_unique("abcabcbb"), longest_unique("bbbb"), longest_unique(""))"""),
        ("table", ["Window type", "When", "Moves"], [
            ["Fixed size k", "'any k consecutive days'", "Both ends move together"],
            ["Variable, longest valid", "'longest substring without...'", "Right grows, left shrinks when invalid"],
            ["Variable, shortest valid", "'smallest run with sum at least...'", "Right grows until valid, then left shrinks while still valid"],
        ]),
        ("tip", "The window from <code>left</code> to <code>right</code> inclusive has length <code>right - left + 1</code>."),
    ],
    "mistakes": [
        "Recomputing <code>sum(nums[i:i+k])</code> every step, which is O(n &times; k).",
        "Off-by-one in the window length.",
        "Forgetting the edge cases: k bigger than the list, k of zero, empty input.",
    ],
    "practice": {
        "title": "Busiest stretch",
        "prompt": "<p>Write <code>busiest_stretch(occupancy, k)</code>. Return the largest total over any <code>k</code> consecutive days. If <code>k</code> is larger than the list, or <code>k</code> is 0 or negative, return <code>0</code>. Aim for O(n).</p><p>Example: <code>busiest_stretch([4, 2, 7, 1, 8, 3], 2)</code> returns <code>11</code>.</p>",
        "func": "busiest_stretch",
        "starter": "def busiest_stretch(occupancy, k):\n    pass\n",
        "tests": [
            ("given example", [[4, 2, 7, 1, 8, 3], 2], False),
            ("whole list", [[1, 2, 3], 3], False),
            ("k too big", [[1, 2], 3], True),
            ("k is zero", [[5, 6], 0], True),
            ("negative k", [[5, 6], -1], True),
            ("zeros", [[0, 0, 0], 2], True),
            ("k of one", [[3, 9, 2], 1], True),
            ("long list", [{"__py__": "list(range(5000))"}, 100], True),
        ],
        "hints": [
            "Handle the invalid k cases first and return 0.",
            "Sum the first k items. Then for each next item, add it and subtract the one k places back, tracking the best.",
        ],
        "solution": """def busiest_stretch(occupancy, k):
    if k <= 0 or k > len(occupancy):
        return 0
    window = sum(occupancy[:k])
    best = window
    for i in range(k, len(occupancy)):
        window += occupancy[i] - occupancy[i - k]
        if window > best:
            best = window
    return best
""",
        "explain": "The first sum is O(k) and each slide is O(1): <b>O(n)</b> time and <b>O(1)</b> extra space.",
    },
    "related": [("LeetCode: Maximum Average Subarray I", "https://leetcode.com/problems/maximum-average-subarray-i/"), ("LeetCode: Longest Substring Without Repeating Characters", "https://leetcode.com/problems/longest-substring-without-repeating-characters/")],
})

# ---------------------------------------------------------------- prefix sums
LESSONS.append({
    "id": "prefix-sums",
    "title": "Prefix sums",
    "minutes": 15,
    "tags": ["Accenture"],
    "summary": "Precompute running totals once, then answer any 'sum between positions i and j' question in O(1).",
    "blocks": [
        ("p", "A <b>prefix sum</b> list stores the total of everything before each position. With one extra 0 at the front, the sum of positions <code>i</code> to <code>j</code> inclusive is <code>prefix[j + 1] - prefix[i]</code>."),
        ("code", """nums = [3, 1, 4, 1, 5]
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
print(prefix)

def range_sum(i, j):            # inclusive
    return prefix[j + 1] - prefix[i]

print(range_sum(1, 3))          # 1 + 4 + 1
print(range_sum(0, 4))          # everything"""),
        ("p", "Building it is O(n) once. Each query is then O(1), so q queries cost O(n + q) instead of O(n &times; q)."),
        ("h", "Pattern: balance point"),
        ("p", "Many questions compare the total on the left with the total on the right. Track the left total as you go, and get the right total as <code>total - left - current</code>."),
        ("code", """def pivot_index(nums):
    total = sum(nums)
    left = 0
    for i, x in enumerate(nums):
        if left == total - left - x:
            return i
        left += x
    return -1

print(pivot_index([1, 7, 3, 6, 5, 6]), pivot_index([1, 2, 3]))"""),
        ("h", "Pattern: count runs with a given sum"),
        ("p", "Combine prefix sums with a dictionary: a run ending here sums to k exactly when an earlier prefix equalled <code>current - k</code>."),
        ("code", """def count_runs(nums, k):
    seen = {0: 1}           # prefix value -> times seen
    current = 0
    count = 0
    for x in nums:
        current += x
        count += seen.get(current - k, 0)
        seen[current] = seen.get(current, 0) + 1
    return count

print(count_runs([1, 1, 1], 2), count_runs([1, 2, 3], 3))"""),
    ],
    "mistakes": [
        "Forgetting the leading 0, which breaks queries starting at position 0.",
        "Mixing up inclusive and exclusive ends: <code>prefix[j + 1] - prefix[i]</code> includes j.",
        "Using a sliding window when numbers can be negative. Prefix sums with a dictionary handle negatives.",
    ],
    "practice": {
        "title": "Balanced budget day",
        "prompt": "<p>Write <code>balance_day(spend)</code>. Return the first position where the total spent <b>before</b> that day equals the total spent <b>after</b> it. Return <code>-1</code> if there is none. Aim for O(n).</p><p>Example: <code>balance_day([1, 7, 3, 6, 5, 6])</code> returns <code>3</code> (1 + 7 + 3 = 11 = 5 + 6).</p>",
        "func": "balance_day",
        "starter": "def balance_day(spend):\n    pass\n",
        "tests": [
            ("given example", [[1, 7, 3, 6, 5, 6]], False),
            ("no balance point", [[1, 2, 3]], False),
            ("first day balances", [[2, 1, -1]], True),
            ("single day", [[5]], True),
            ("empty", [[]], True),
            ("zeros: first wins", [[0, 0, 0]], True),
        ],
        "hints": [
            "Compute the total once. Walk left to right keeping the running total of days before the current one.",
            "Right side = total minus left minus the current day.",
        ],
        "solution": """def balance_day(spend):
    total = sum(spend)
    left = 0
    for i, x in enumerate(spend):
        if left == total - left - x:
            return i
        left += x
    return -1
""",
        "explain": "One pass for the total, one pass to check: <b>O(n)</b> time and <b>O(1)</b> space.",
    },
    "related": [("LeetCode: Find Pivot Index", "https://leetcode.com/problems/find-pivot-index/"), ("LeetCode: Subarray Sum Equals K", "https://leetcode.com/problems/subarray-sum-equals-k/")],
})

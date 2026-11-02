"""Easy, Medium and Hard ladders for Foundations, Trees/Heaps/Graphs and Strategies lessons.

Same format as ladder.py. Tree problems use a wrapper that builds the tree from a level-order list (None = no node).
"""

def S(code): return code.strip("\n") + "\n"

def tree_wrapper(func):
    return f'''def __call(values):
    from collections import deque as __dq
    if not values or values[0] is None:
        return {func}(None)
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
    return {func}(root)
'''

TREE_NODE = '''class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''

LADDER_C = {}

# ================================================================ how-to-solve
FIRST_OVER = S('''
def first_over(temps, limit):
    for i, t in enumerate(temps):
        if t > limit:
            return i              # first one: stop now
    return -1                     # none found
''')
MAX_POS = S('''
def positions_of_max(nums):
    if not nums:
        return []
    top = max(nums)
    result = []
    for i, x in enumerate(nums):
        if x == top:
            result.append(i)
    return result
''')
SECOND = S('''
def second_largest(nums):
    first = second = None
    for x in nums:
        if first is None or x > first:
            first, second = x, first
        elif x != first and (second is None or x > second):
            second = x
    return second
''')
LADDER_C["how-to-solve"] = [
 dict(level="Easy", title="First reading over the limit", func="first_over",
      prompt="<p>Write <code>first_over(temps, limit)</code>. Return the position of the <b>first</b> reading strictly above <code>limit</code>, or <code>-1</code> if there is none.</p><p>Example: <code>first_over([18, 21, 25, 30], 22)</code> returns <code>2</code>.</p>",
      starter="def first_over(temps, limit):\n    pass\n",
      tests=[("given example", [[18, 21, 25, 30], 22], False), ("none over", [[1, 2, 3], 5], False), ("empty", [[], 0], True), ("equal is not over", [[5, 5, 6], 5], True), ("first item", [[9, 1], 3], True), ("100,000 readings", [{"__py__": "[0] * 99999 + [1]"}, 0], True)],
      hints=["'First' means return inside the loop as soon as you find one.", "Use <code>enumerate</code> for the position, and <code>return -1</code> after the loop."],
      solution=FIRST_OVER, explain="Stops at the first match, at worst one pass: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("How to solve, easy. The first reading over the limit. First! That word decides everything.", [("b", "first_over([18, 21, 25, 30], 22) is 2")]),
           ("First one means return inside the loop, the moment you find it.", [("clear",), ("code", FIRST_OVER.splitlines()), ("hl", [1, 2, 3])]),
           ("Enumerate gives the position and the value together. We return the position.", [("hl", [1])]),
           ("Nothing found after the whole loop? Minus one, exactly what the task asked for.", [("hl", [4]), ("cap", "First match? Return inside the loop.")])]),
 dict(level="Medium", title="Every position of the maximum", func="positions_of_max",
      prompt="<p>Write <code>positions_of_max(nums)</code>. Return a list of <b>all</b> positions where the largest value appears, in order. An empty list gives <code>[]</code>.</p><p>Example: <code>positions_of_max([3, 7, 2, 7])</code> returns <code>[1, 3]</code>.</p>",
      starter="def positions_of_max(nums):\n    pass\n",
      tests=[("given example", [[3, 7, 2, 7]], False), ("single max", [[1, 9, 4]], False), ("empty", [[]], True), ("all equal", [[2, 2, 2]], True), ("negatives", [[-5, -1, -3]], True), ("100,000 values", [{"__py__": "[i % 1000 for i in range(100000)]"}], True)],
      hints=["Two steps: find the max, then collect every position that equals it.", "Handle the empty list first, because <code>max([])</code> crashes."],
      solution=MAX_POS, explain="Two passes: <b>O(n)</b> time. The result can hold up to n positions: <b>O(n)</b> space at worst.",
      vid=[("How to solve, medium. Every position of the maximum. All of them, not just the first.", [("b", "[3, 7, 2, 7] gives [1, 3]")]),
           ("Edge case first. An empty list would crash max. Return an empty list straight away.", [("clear",), ("code", MAX_POS.splitlines()), ("hl", [1, 2])]),
           ("Find the top value once.", [("hl", [3])]),
           ("Then the 'all matches' skeleton: a result list, a loop, and return after the loop.", [("hl", [4, 5, 6, 7, 8])]),
           ("Two passes, still O of n. Edges first, then the skeleton. That's how winners work.", [("cap", "All matches? Collect, return after the loop.")])]),
 dict(level="Hard", title="Second largest distinct value", func="second_largest",
      prompt="<p>Write <code>second_largest(nums)</code>. Return the second largest <b>distinct</b> value, or <code>None</code> if there is not one. Do it in one pass without sorting.</p><p>Example: <code>second_largest([4, 9, 9, 7])</code> returns <code>7</code>.</p>",
      starter="def second_largest(nums):\n    pass\n",
      tests=[("given example", [[4, 9, 9, 7]], False), ("two values", [[1, 2]], False), ("all equal", [[5, 5, 5]], True), ("empty", [[]], True), ("negatives", [[-2, -8, -5]], True), ("max comes last", [[1, 2, 3, 10]], True), ("100,000 values", [{"__py__": "list(range(100000))"}], True)],
      hints=["Track two values, <code>first</code> and <code>second</code>, starting as <code>None</code>.", "A new biggest pushes the old first down to second. A value equal to first must be ignored."],
      solution=SECOND, explain="One pass with two variables: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("How to solve, hard. Second largest distinct value, one pass, no sorting.", [("b", "[4, 9, 9, 7] gives 7, not 9")]),
           ("Before coding, the edges: all equal, empty, only one value. Each one means None.", [("b", "Edges: [], [5, 5, 5], one value: None")]),
           ("Keep two trackers, first and second, both starting at None. Not zero: negatives would break it.", [("clear",), ("code", SECOND.splitlines()), ("hl", [1])]),
           ("A new biggest? The old first slides down to second.", [("hl", [3, 4])]),
           ("Otherwise, if it's different from first and beats second, it becomes second. Duplicates of the max are ignored.", [("hl", [5, 6])]),
           ("One pass. O of n, O of 1 space. Edge cases handled. That's interview gold.", [("cap", "Two trackers, start at None, ignore duplicates.")])]),
]

# ================================================================ big-o-time
HAS_COMMON = S('''
def has_common(a, b):
    seen = set(a)                 # O(n) once
    for x in b:
        if x in seen:             # O(1) each
            return True
    return False
''')
PAIRS = S('''
def count_pairs(nums, target):
    seen = {}                     # value -> how many so far
    count = 0
    for x in nums:
        count += seen.get(target - x, 0)
        seen[x] = seen.get(x, 0) + 1
    return count
''')
SUBARR = S('''
def subarrays_summing_to(nums, k):
    seen = {0: 1}                 # prefix total -> times seen
    total = 0
    count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
''')
LADDER_C["big-o-time"] = [
 dict(level="Easy", title="Any shared value?", func="has_common",
      prompt="<p>Write <code>has_common(a, b)</code>. Return <code>True</code> if any value appears in both lists. Aim for O(n + m), not a loop inside a loop.</p><p>Example: <code>has_common([1, 4, 9], [3, 9])</code> returns <code>True</code>.</p>",
      starter="def has_common(a, b):\n    pass\n",
      tests=[("given example", [[1, 4, 9], [3, 9]], False), ("nothing shared", [[1, 2], [3, 4]], False), ("one empty", [[], [1]], True), ("both empty", [[], []], True), ("strings", [["x", "y"], ["y"]], True), ("100,000 each, no overlap", [{"__py__": "list(range(100000))"}, {"__py__": "list(range(100000, 200000))"}], True)],
      hints=["A nested loop is O(n × m). Turn one list into a set first.", "Then one loop over the other list with an O(1) <code>in</code> check."],
      solution=HAS_COMMON, explain="Building the set is O(n), checking b is O(m): <b>O(n + m)</b> time, <b>O(n)</b> space.",
      vid=[("Big O, easy. Is there any shared value between two lists?", [("b", "[1, 4, 9] and [3, 9]: True")]),
           ("A loop inside a loop is O of n times m. A hundred thousand each? Ten billion checks. Terrible.", [("b", "Nested loops: O(n × m)")]),
           ("Build a set from one list. That's O of n, once.", [("clear",), ("code", HAS_COMMON.splitlines()), ("hl", [1])]),
           ("Then each check is O of 1. So the whole thing is O of n plus m. Massive upgrade.", [("hl", [2, 3, 4, 5]), ("cap", "Nested search? Swap the inner loop for a set.")])]),
 dict(level="Medium", title="Count pairs that add to a target", func="count_pairs",
      prompt="<p>Write <code>count_pairs(nums, target)</code>. Count the pairs of positions <code>i &lt; j</code> with <code>nums[i] + nums[j] == target</code>. Aim for O(n).</p><p>Example: <code>count_pairs([1, 5, 3, 3, 3], 6)</code> returns <code>4</code> (1 + 5, and three ways to pair the 3s).</p>",
      starter="def count_pairs(nums, target):\n    pass\n",
      tests=[("given example", [[1, 5, 3, 3, 3], 6], False), ("no pairs", [[1, 2, 3], 10], False), ("empty", [[], 4], True), ("all the same", [[2, 2, 2, 2], 4], True), ("negatives", [[-1, 7, 4, 2], 6], True), ("100,000 ones", [{"__py__": "[1] * 100000"}, 2], True)],
      hints=["For each number, how many earlier numbers are its partner, <code>target - x</code>?", "Keep a dict counting values seen so far. Add <code>seen.get(target - x, 0)</code> before you record x."],
      solution=PAIRS, explain="One pass with O(1) dict work: <b>O(n)</b> time, <b>O(n)</b> space. Two loops would be O(n²).",
      vid=[("Big O, medium. Count every pair that adds to the target.", [("b", "[1, 5, 3, 3, 3], target 6: 4 pairs")]),
           ("Checking every pair is O of n squared. A hundred thousand items? Five billion pairs. No way.", [("b", "Every pair: O(n²)")]),
           ("Flip it. For each number, how many earlier numbers are its partner? Count them with a dictionary.", [("clear",), ("code", PAIRS.splitlines()), ("hl", [1])]),
           ("Add the partners already seen, then record this number. Look, then store.", [("hl", [4, 5])]),
           ("One pass, O of n. That's the dictionary turning n squared into n. Beautiful.", [("cap", "Counting pairs? Count partners seen so far.")])]),
 dict(level="Hard", title="Stretches that add up to k", func="subarrays_summing_to",
      prompt="<p>Write <code>subarrays_summing_to(nums, k)</code>. Count the runs of consecutive values whose total is exactly <code>k</code>. Values can be negative. Aim for O(n).</p><p>Example: <code>subarrays_summing_to([1, 2, 3], 3)</code> returns <code>2</code> ([1, 2] and [3]).</p>",
      starter="def subarrays_summing_to(nums, k):\n    pass\n",
      tests=[("given example", [[1, 2, 3], 3], False), ("repeated ones", [[1, 1, 1], 2], False), ("empty", [[], 0], True), ("negatives", [[3, -3, 3], 3], True), ("zero target", [[0, 0, 0], 0], True), ("100,000 values", [{"__py__": "[1, -1] * 50000"}, 0], True)],
      hints=["A run from i to j totals <code>prefix[j] - prefix[i]</code>. You want that to equal k.", "Keep a dict of how many times each running total has appeared. Start it with <code>{0: 1}</code>."],
      solution=SUBARR, explain="One pass with O(1) dict work: <b>O(n)</b> time, <b>O(n)</b> space. Checking every run would be O(n²).",
      vid=[("Big O, hard. Count the stretches that add up to k. Negatives allowed, so no sliding window.", [("b", "[1, 2, 3], k = 3: [1, 2] and [3], so 2")]),
           ("Every start and end is O of n squared. Here's the trick: running totals.", [("clear",), ("code", SUBARR.splitlines()), ("hl", [2, 5])]),
           ("A stretch ending here adds to k if an earlier running total was this total minus k.", [("hl", [6])]),
           ("So count how often each total has appeared. Start with zero seen once, for stretches that begin at the start.", [("hl", [1, 7])]),
           ("One pass, O of n. Prefix sums plus a dictionary. That's a top tier move. You own it now.", [("cap", "Earlier total = total - k? That's a stretch.")])]),
]

# ================================================================ big-o-space
REVERSE = S('''
def reverse_in_place(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums
''')
ZEROS = S('''
def move_zeros(nums):
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums
''')
MISSING = S('''
def find_missing(nums):
    n = len(nums)
    expected = n * (n + 1) // 2   # 0 + 1 + ... + n
    return expected - sum(nums)
''')
LADDER_C["big-o-space"] = [
 dict(level="Easy", title="Reverse without a copy", func="reverse_in_place",
      prompt="<p>Write <code>reverse_in_place(nums)</code>. Reverse the list <b>in place</b> by swapping, using O(1) extra space (no slicing, no <code>reversed</code>), and return it.</p><p>Example: <code>[1, 2, 3, 4]</code> becomes <code>[4, 3, 2, 1]</code>.</p>",
      starter="def reverse_in_place(nums):\n    pass\n",
      tests=[("given example", [[1, 2, 3, 4]], False), ("odd length", [[1, 2, 3]], False), ("empty", [[]], True), ("one item", [[7]], True), ("strings", [["a", "b"]], True), ("300 values", [{"__py__": "list(range(300))"}], True)],
      hints=["One pointer at each end. Swap, then move both inwards.", "Python swaps in one line: <code>a[i], a[j] = a[j], a[i]</code>."],
      solution=REVERSE, explain="n/2 swaps: <b>O(n)</b> time. Only two pointers: <b>O(1)</b> extra space.",
      vid=[("Big O space, easy. Reverse a list without making a copy.", [("b", "[1, 2, 3, 4] becomes [4, 3, 2, 1], O(1) extra space")]),
           ("A slice like nums backwards makes a whole new list. That's O of n extra memory.", [("b", "nums[::-1] copies: O(n) space")]),
           ("Instead, two pointers. Swap the ends.", [("clear",), ("code", REVERSE.splitlines()), ("hl", [1, 3])]),
           ("Move inward and repeat until they meet. Two variables. O of 1 space. Lean and mean.", [("hl", [2, 4, 5]), ("cap", "In place = swap, don't copy.")])]),
 dict(level="Medium", title="Move the zeros to the end", func="move_zeros",
      prompt="<p>Write <code>move_zeros(nums)</code>. Move every 0 to the end <b>in place</b>, keeping the other values in their original order, and return the list. Use O(1) extra space.</p><p>Example: <code>[0, 1, 0, 3, 12]</code> becomes <code>[1, 3, 12, 0, 0]</code>.</p>",
      starter="def move_zeros(nums):\n    pass\n",
      tests=[("given example", [[0, 1, 0, 3, 12]], False), ("no zeros", [[1, 2]], False), ("all zeros", [[0, 0]], True), ("empty", [[]], True), ("zero at the end", [[4, 0]], True), ("300 values", [{"__py__": "[i % 3 for i in range(300)]"}], True)],
      hints=["Keep a 'write' position. Copy each non-zero value to it and move it on.", "After the loop, fill everything from <code>write</code> to the end with zeros."],
      solution=ZEROS, explain="Two passes over the list: <b>O(n)</b> time. One write pointer: <b>O(1)</b> extra space.",
      vid=[("Big O space, medium. Move the zeros to the end, same list, order kept.", [("b", "[0, 1, 0, 3, 12] becomes [1, 3, 12, 0, 0]")]),
           ("Building a new list is easy, but that's O of n extra space. We want O of 1.", [("clear",), ("code", ZEROS.splitlines()), ("hl", [1])]),
           ("A write pointer marks where the next non-zero goes. Copy it there and move on.", [("hl", [2, 3, 4, 5])]),
           ("Then fill the rest with zeros. Same list, order kept, constant extra memory.", [("hl", [6, 7]), ("cap", "Write pointer: keep the good ones at the front.")])]),
 dict(level="Hard", title="The missing number", func="find_missing",
      prompt="<p>Write <code>find_missing(nums)</code>. <code>nums</code> holds every whole number from 0 to n except one, in any order (so it has n values). Return the missing one using O(1) extra space: no sets, no sorting a copy.</p><p>Example: <code>find_missing([3, 0, 1])</code> returns <code>2</code>.</p>",
      starter="def find_missing(nums):\n    pass\n",
      tests=[("given example", [[3, 0, 1]], False), ("missing zero", [[1, 2]], False), ("missing the top", [[0, 1, 2]], True), ("one value", [[0]], True), ("empty", [[]], True), ("1,000,000 values", [{"__py__": "[i for i in range(1000001) if i != 777777]"}], True)],
      hints=["What should 0 + 1 + ... + n add up to?", "<code>n * (n + 1) // 2</code> minus the actual sum is the missing number."],
      solution=MISSING, explain="One pass to sum: <b>O(n)</b> time. A couple of numbers: <b>O(1)</b> space.",
      vid=[("Big O space, hard. Numbers zero to n, one missing. Find it with constant memory.", [("b", "[3, 0, 1]: 2 is missing")]),
           ("A set would work, but that's O of n memory. Think maths instead.", [("b", "Set of seen numbers: O(n) space")]),
           ("Zero to n should add up to n times n plus one, over two. Gauss did this as a schoolboy.", [("clear",), ("code", MISSING.splitlines()), ("hl", [2])]),
           ("Subtract the real total. What's left is the missing number. O of n time, O of 1 space. Genius.", [("hl", [3]), ("cap", "Expected total - actual total = missing.")])]),
]

# ================================================================ python-toolkit
FIRST_INDEX = S('''
def first_index(names):
    where = {}
    for i, name in enumerate(names):
        if name not in where:
            where[name] = i
    return where
''')
TOPK = S('''
from collections import Counter

def top_k_words(words, k):
    counts = Counter(words)
    ranked = sorted(counts, key=lambda w: (-counts[w], w))
    return ranked[:k]
''')
MERGE = S('''
def merge_bookings(slots):
    merged = []
    for start, end in sorted(slots):
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
''')
LADDER_C["python-toolkit"] = [
 dict(level="Easy", title="Where does each name first appear?", func="first_index",
      prompt="<p>Write <code>first_index(names)</code>. Return a dict mapping each name to the position where it <b>first</b> appears. Use <code>enumerate</code>.</p><p>Example: <code>[\"Ana\", \"Ben\", \"Ana\"]</code> gives <code>{\"Ana\": 0, \"Ben\": 1}</code>.</p>",
      starter="def first_index(names):\n    pass\n",
      tests=[("given example", [["Ana", "Ben", "Ana"]], False), ("all different", [["X", "Y", "Z"]], False), ("empty", [[]], True), ("all the same", [["Q", "Q", "Q"]], True), ("repeat after a gap", [["a", "b", "c", "a"]], True)],
      hints=["<code>for i, name in enumerate(names):</code> gives position and value.", "Only store a name the first time: <code>if name not in where</code>."],
      solution=FIRST_INDEX, explain="One pass with O(1) dict checks: <b>O(n)</b> time, <b>O(k)</b> space for k names.",
      vid=[("Python toolkit, easy. Where does each name first appear?", [("b", "['Ana', 'Ben', 'Ana'] gives {'Ana': 0, 'Ben': 1}")]),
           ("Enumerate hands you the position and the name together. Position zero, Ana. Position one, Ben.", [("clear",), ("code", FIRST_INDEX.splitlines()), ("hl", [2])]),
           ("Only store a name if it's not in the dictionary yet. That keeps the first position.", [("hl", [3, 4])]),
           ("No range of len, no counters. Clean Python. Interviewers love clean.", [("cap", "Need the position? enumerate.")])]),
 dict(level="Medium", title="Most common words", func="top_k_words",
      prompt="<p>Write <code>top_k_words(words, k)</code>. Return the <code>k</code> most common words, most frequent first. Break ties alphabetically. Use <code>Counter</code> and <code>sorted</code> with a key.</p><p>Example: <code>top_k_words([\"b\", \"a\", \"b\", \"c\", \"a\", \"b\"], 2)</code> returns <code>[\"b\", \"a\"]</code>.</p>",
      starter="from collections import Counter\n\ndef top_k_words(words, k):\n    pass\n",
      tests=[("given example", [["b", "a", "b", "c", "a", "b"], 2], False), ("tie broken A to Z", [["pear", "fig", "apple"], 2], False), ("k bigger than words", [["x"], 3], True), ("empty", [[], 2], True), ("k is zero", [["a"], 0], True), ("100,000 words", [{"__py__": "[f'w{i % 30}' for i in range(100000)]"}, 3], True)],
      hints=["<code>Counter(words)</code> counts for you.", "<code>sorted(counts, key=lambda w: (-counts[w], w))[:k]</code>: minus for most first, then the word for ties."],
      solution=TOPK, explain="Counting is O(n); sorting the d distinct words is O(d log d): <b>O(n log n)</b> at worst. Space <b>O(d)</b>.",
      vid=[("Python toolkit, medium. The k most common words, ties alphabetical.", [("b", "['b','a','b','c','a','b'], k = 2: ['b', 'a']")]),
           ("Counter does the counting in one line. Don't write it by hand.", [("clear",), ("code", TOPK.splitlines()), ("hl", [0, 3])]),
           ("Sort the words with a key. Minus the count puts the biggest first. Then the word itself breaks ties.", [("hl", [4])]),
           ("Slice the first k. Three lines, and every tie handled. Tremendous toolkit.", [("hl", [5]), ("cap", "Rank by two things? Key returns a tuple.")])]),
 dict(level="Hard", title="Merge overlapping bookings", func="merge_bookings",
      prompt="<p>Write <code>merge_bookings(slots)</code>. Each slot is <code>[start, end]</code>, in any order. Merge slots that overlap or touch, and return the merged list sorted by start.</p><p>Example: <code>[[1, 3], [8, 10], [2, 6]]</code> gives <code>[[1, 6], [8, 10]]</code>.</p>",
      starter="def merge_bookings(slots):\n    pass\n",
      tests=[("given example", [[[1, 3], [8, 10], [2, 6]]], False), ("touching", [[[1, 4], [4, 5]]], False), ("empty", [[]], True), ("one inside another", [[[1, 10], [2, 3]]], True), ("no overlaps", [[[5, 6], [1, 2]]], True), ("chain", [[[3, 4], [1, 2], [2, 3]]], True)],
      hints=["Sort by start first: <code>sorted(slots)</code> does that for lists of pairs.", "Compare each slot with the last merged one. If it starts before that one ends, stretch the end with <code>max</code>; otherwise add it."],
      solution=MERGE, explain="Sorting is O(n log n), the merge is one pass: <b>O(n log n)</b> time, <b>O(n)</b> space for the result.",
      vid=[("Python toolkit, hard. Merge overlapping bookings.", [("b", "[[1, 3], [8, 10], [2, 6]] gives [[1, 6], [8, 10]]")]),
           ("Step one: sort by start. Sorted on a list of pairs does it for free.", [("clear",), ("code", MERGE.splitlines()), ("hl", [2])]),
           ("Starts before the last merged booking ends? Overlap. Stretch the end with max, in case one sits inside another.", [("hl", [3, 4])]),
           ("Otherwise it's a new booking. Append it.", [("hl", [5, 6])]),
           ("Sort, then one pass. O of n log n. This exact pattern shows up in calendar and scheduling questions everywhere.", [("cap", "Intervals? Sort by start, then merge.")])]),
]

# ================================================================ trees
HEIGHT = S(TREE_NODE + '''
def tree_height(root):
    if root is None:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))
''')
LEVELS = S(TREE_NODE + '''
from collections import deque

def level_sums(root):
    if root is None:
        return []
    sums = []
    q = deque([root])
    while q:
        total = 0
        for _ in range(len(q)):          # one whole level
            node = q.popleft()
            total += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        sums.append(total)
    return sums
''')
ISBST = S(TREE_NODE + '''
def is_bst(root, low=None, high=None):
    if root is None:
        return True
    if low is not None and root.val <= low:
        return False
    if high is not None and root.val >= high:
        return False
    return (is_bst(root.left, low, root.val) and
            is_bst(root.right, root.val, high))
''')
def body(code): return [l for l in code.splitlines() if l][len(TREE_NODE.strip().splitlines()):]
LADDER_C["trees"] = [
 dict(level="Easy", title="How tall is the tree?", func="tree_height",
      prompt="<p>A <code>TreeNode</code> class is provided. Write <code>tree_height(root)</code>: the number of nodes on the longest path from the root down to a leaf. An empty tree has height 0. The checker builds the tree from a level-order list (<code>None</code> means no node).</p><p>Example: <code>[3, 9, 20, None, None, 15, 7]</code> has height <code>3</code>.</p>",
      starter=TREE_NODE + "\ndef tree_height(root):\n    pass\n", wrapper=tree_wrapper("tree_height"),
      tests=[("given example", [[3, 9, 20, None, None, 15, 7]], False), ("single node", [[1]], False), ("empty", [[]], True), ("leaning left", [[1, 2, None, 3, None, 4]], True), ("full tree", [[1, 2, 3, 4, 5, 6, 7]], True)],
      hints=["Base case: an empty tree has height 0.", "Otherwise it is 1 + the taller of the two subtrees."],
      solution=HEIGHT, explain="Each node is visited once: <b>O(n)</b> time. The recursion goes as deep as the tree: <b>O(h)</b> space.",
      vid=[("Trees, easy. How tall is the tree? Count nodes on the longest path down.", [("b", "[3, 9, 20, None, None, 15, 7]: height 3")]),
           ("Tree problem? Ask: what do I do at one node, and what do I ask my children?", [("clear",), ("code", body(HEIGHT)), ("hl", [1, 2])]),
           ("Base case. Empty tree, height zero.", [("hl", [1, 2])]),
           ("Otherwise, one for me, plus the taller of my two children. That's it. Recursion does the rest.", [("hl", [3]), ("cap", "1 + max(left, right)")])]),
 dict(level="Medium", title="Total for each level", func="level_sums",
      prompt="<p>A <code>TreeNode</code> class is provided. Write <code>level_sums(root)</code>: a list of the total of the values on each level, top to bottom. Empty tree gives <code>[]</code>.</p><p>Example: <code>[3, 9, 20, None, None, 15, 7]</code> gives <code>[3, 29, 22]</code>.</p>",
      starter=TREE_NODE + "\nfrom collections import deque\n\ndef level_sums(root):\n    pass\n", wrapper=tree_wrapper("level_sums"),
      tests=[("given example", [[3, 9, 20, None, None, 15, 7]], False), ("single node", [[5]], False), ("empty", [[]], True), ("negatives", [[1, -2, -3]], True), ("lopsided", [[1, 2, None, 3, None, 4]], True)],
      hints=["Breadth-first: a queue, starting with the root.", "At the start of each round, <code>len(q)</code> is exactly the number of nodes on this level. Process that many."],
      solution=LEVELS, explain="Each node is queued and removed once: <b>O(n)</b> time, <b>O(w)</b> space for the widest level.",
      vid=[("Trees, medium. Add up each level, top to bottom.", [("b", "[3, 9, 20, None, None, 15, 7] gives [3, 29, 22]")]),
           ("Level by level means breadth first search. A queue.", [("clear",), ("code", body(LEVELS)), ("hl", [5, 6])]),
           ("The trick: at the start of each round, the queue holds exactly one level. Process that many nodes.", [("hl", [7, 8, 9])]),
           ("Add each value, and queue its children for the next level.", [("hl", [10, 11, 12])]),
           ("One total per level. O of n. Breadth first, in a nutshell.", [("hl", [13]), ("cap", "Level by level? Queue, and len(q) per round.")])]),
 dict(level="Hard", title="Is it a valid search tree?", func="is_bst",
      prompt="<p>A <code>TreeNode</code> class is provided. Write <code>is_bst(root)</code>. Return <code>True</code> if every node is strictly greater than everything in its left subtree and strictly less than everything in its right subtree. An empty tree is valid.</p><p>Example: <code>[5, 1, 8, None, None, 4, 9]</code> is <b>not</b> valid: 4 is in 5's right subtree.</p>",
      starter=TREE_NODE + "\ndef is_bst(root):\n    pass\n", wrapper=tree_wrapper("is_bst"),
      tests=[("deep violation", [[5, 1, 8, None, None, 4, 9]], False), ("valid", [[2, 1, 3]], False), ("empty", [[]], True), ("duplicate value", [[2, 2]], True), ("valid bigger tree", [[8, 3, 10, 1, 6, None, 14]], True), ("right child too small", [[5, None, 4]], True)],
      hints=["Checking only a node and its children misses deep problems. Pass down the allowed range.", "Going left, the node's value becomes the new upper bound; going right, it becomes the new lower bound."],
      solution=ISBST, explain="Each node is checked once: <b>O(n)</b> time, <b>O(h)</b> recursion space.",
      vid=[("Trees, hard. Is it a valid binary search tree? Watch the trap.", [("b", "[5, 1, 8, None, None, 4, 9]: 4 is right of 5. Invalid!")]),
           ("Checking each node against its own children isn't enough. Four is fine next to eight, but it's on five's right.", [("b", "Local checks miss deep problems")]),
           ("So pass down a range: the lowest and highest a node is allowed to be.", [("clear",), ("code", body(ISBST)), ("hl", [0, 3, 4, 5, 6])]),
           ("Going left, my value becomes the ceiling. Going right, it becomes the floor.", [("hl", [7, 8])]),
           ("Every node checked once. O of n. Explain the range idea out loud and they'll be impressed. Believe me.", [("cap", "Pass the allowed range down.")])]),
]

# ================================================================ heaps
SMALLEST = S('''
import heapq

def smallest_k(nums, k):
    heap = list(nums)
    heapq.heapify(heap)               # O(n)
    return [heapq.heappop(heap) for _ in range(min(k, len(heap)))]
''')
MERGEL = S('''
import heapq

def merge_sorted(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    out = []
    while heap:
        val, i, j = heapq.heappop(heap)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out
''')
ROPES = S('''
import heapq

def join_ropes(lengths):
    heap = list(lengths)
    heapq.heapify(heap)
    cost = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        cost += a + b
        heapq.heappush(heap, a + b)
    return cost
''')
LADDER_C["heaps"] = [
 dict(level="Easy", title="The k smallest values", func="smallest_k",
      prompt="<p>Write <code>smallest_k(nums, k)</code>. Return the <code>k</code> smallest values in increasing order (all of them if there are fewer than k). Use <code>heapq</code>.</p><p>Example: <code>smallest_k([7, 2, 9, 4, 1], 3)</code> returns <code>[1, 2, 4]</code>.</p>",
      starter="import heapq\n\ndef smallest_k(nums, k):\n    pass\n",
      tests=[("given example", [[7, 2, 9, 4, 1], 3], False), ("k is 1", [[5, 3], 1], False), ("k bigger than list", [[2, 1], 5], True), ("empty", [[], 2], True), ("duplicates", [[3, 1, 1, 2], 2], True), ("100,000 values", [{"__py__": "list(range(100000, 0, -1))"}, 5], True)],
      hints=["<code>heapq.heapify(heap)</code> turns a list into a heap in O(n).", "Pop <code>min(k, len(heap))</code> times; each pop gives the next smallest."],
      solution=SMALLEST, explain="Heapify is O(n), then k pops at O(log n): <b>O(n + k log n)</b> time, <b>O(n)</b> space for the copy.",
      vid=[("Heaps, easy. The k smallest values, in order.", [("b", "[7, 2, 9, 4, 1], k = 3: [1, 2, 4]")]),
           ("Heapify turns the list into a heap in O of n. Faster than sorting everything.", [("clear",), ("code", SMALLEST.splitlines()), ("hl", [3, 4])]),
           ("Then pop k times. Every pop hands you the next smallest.", [("hl", [5])]),
           ("Min of k and the length stops you popping an empty heap. No crash. Smart.", [("cap", "Smallest few? Heapify, then pop k.")])]),
 dict(level="Medium", title="Merge sorted lists", func="merge_sorted",
      prompt="<p>Write <code>merge_sorted(lists)</code>. Each inner list is already sorted. Return one sorted list of everything. Use a heap of the current front of each list.</p><p>Example: <code>[[1, 4], [2, 3, 9], []]</code> gives <code>[1, 2, 3, 4, 9]</code>.</p>",
      starter="import heapq\n\ndef merge_sorted(lists):\n    pass\n",
      tests=[("given example", [[[1, 4], [2, 3, 9], []]], False), ("two lists", [[[1, 3], [2]]], False), ("no lists", [[]], True), ("all empty", [[[], []]], True), ("duplicates", [[[1, 1], [1]]], True), ("100 lists of 3", [{"__py__": "[[i, i + 100, i + 200] for i in range(100)]"}], True)],
      hints=["Push (value, list number, position) for the first item of each list.", "Pop the smallest, then push the next item from the same list."],
      solution=MERGEL, explain="Each of the N values is pushed and popped once, with at most k items in the heap: <b>O(N log k)</b> time, <b>O(k)</b> heap space.",
      vid=[("Heaps, medium. Merge several sorted lists into one.", [("b", "[[1, 4], [2, 3, 9], []] gives [1, 2, 3, 4, 9]")]),
           ("The next value out is always the smallest front of some list. Smallest of a few? That's a heap.", [("clear",), ("code", MERGEL.splitlines()), ("hl", [3, 4])]),
           ("The heap holds tuples: value, which list, which position. The value comes first, so it decides the order.", [("hl", [3])]),
           ("Pop the smallest, add it to the answer, then push the next item from the same list.", [("hl", [7, 8, 9, 10])]),
           ("N values, heap size k. O of N log k. That's how big data systems merge sorted files. Powerful.", [("cap", "k sorted sources? Heap of the fronts.")])]),
 dict(level="Hard", title="Cheapest way to join ropes", func="join_ropes",
      prompt="<p>Write <code>join_ropes(lengths)</code>. Joining two ropes costs the sum of their lengths, and makes one rope of that length. Join all ropes into one at the lowest total cost and return that cost. One rope or none costs 0.</p><p>Example: <code>join_ropes([4, 3, 2, 6])</code> returns <code>29</code>.</p>",
      starter="import heapq\n\ndef join_ropes(lengths):\n    pass\n",
      tests=[("given example", [[4, 3, 2, 6]], False), ("two ropes", [[5, 5]], False), ("one rope", [[7]], True), ("none", [[]], True), ("equal ropes", [[1, 1, 1, 1]], True), ("10,000 ropes", [{"__py__": "[1] * 10000"}], True)],
      hints=["Always join the two shortest ropes: long ropes should be added as few times as possible.", "Use a heap: pop two, add their sum to the cost, push the joined rope back."],
      solution=ROPES, explain="n - 1 joins, each a few O(log n) heap operations: <b>O(n log n)</b> time, <b>O(n)</b> space.",
      vid=[("Heaps, hard. The cheapest way to join ropes. Each join costs the two lengths added.", [("b", "[4, 3, 2, 6]: best total cost 29")]),
           ("Key insight: a rope's length is paid again every time it's joined. So join the shortest ones first.", [("b", "Always join the two shortest")]),
           ("Shortest two, again and again, as new ropes appear? A heap.", [("clear",), ("code", ROPES.splitlines()), ("hl", [3, 4])]),
           ("Pop two, pay their sum, push the joined rope back in.", [("hl", [6, 7, 8, 9, 10])]),
           ("Greedy choice, heap engine. O of n log n. The same idea builds Huffman codes for compression. Huge.", [("cap", "Repeatedly take the two smallest: heap.")])]),
]

# ================================================================ graphs
REACH = S('''
def count_reachable(graph, start):
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return len(seen)
''')
COMPONENTS = S('''
def count_groups(n, edges):
    graph = {i: [] for i in range(n)}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen = set()
    groups = 0
    for start in range(n):
        if start in seen:
            continue
        groups += 1                     # a new group
        seen.add(start)
        stack = [start]
        while stack:
            for nxt in graph[stack.pop()]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
    return groups
''')
DIJKSTRA = S('''
import heapq

def shortest_route(n, roads, start, end):
    graph = {i: [] for i in range(n)}
    for a, b, d in roads:
        graph[a].append((b, d))
        graph[b].append((a, d))
    best = {start: 0}
    heap = [(0, start)]
    while heap:
        dist, node = heapq.heappop(heap)
        if node == end:
            return dist
        if dist > best[node]:
            continue                    # stale entry
        for nxt, d in graph[node]:
            if dist + d < best.get(nxt, float("inf")):
                best[nxt] = dist + d
                heapq.heappush(heap, (dist + d, nxt))
    return -1
''')
LADDER_C["graphs"] = [
 dict(level="Easy", title="How many places can you reach?", func="count_reachable",
      prompt="<p>Write <code>count_reachable(graph, start)</code>. <code>graph</code> maps each place to a list of places you can go to next (one way). Return how many places you can reach from <code>start</code>, counting <code>start</code>.</p><p>Example: <code>{\"A\": [\"B\"], \"B\": [\"C\"], \"C\": [], \"D\": [\"A\"]}</code> from <code>\"A\"</code> gives <code>3</code>.</p>",
      starter="def count_reachable(graph, start):\n    pass\n",
      tests=[("given example", [{"A": ["B"], "B": ["C"], "C": [], "D": ["A"]}, "A"], False), ("cycle", [{"A": ["B"], "B": ["A"]}, "A"], False), ("alone", [{"A": []}, "A"], True), ("start not listed", [{"B": ["C"]}, "A"], True), ("branching", [{"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}, "A"], True), ("long chain", [{"__py__": "{str(i): [str(i + 1)] for i in range(20000)}"}, "0"], True)],
      hints=["Depth-first with a stack (or breadth-first with a queue), plus a seen set.", "Use <code>graph.get(node, [])</code> in case a place has no entry."],
      solution=REACH, explain="Each place and each link is handled once: <b>O(V + E)</b> time, <b>O(V)</b> space.",
      vid=[("Graphs, easy. How many places can you reach from the start?", [("b", "A to B to C: 3 places, D can't be reached")]),
           ("Explore and remember where you've been. A stack and a seen set.", [("clear",), ("code", REACH.splitlines()), ("hl", [1, 2])]),
           ("Take a place, look at every next place. New? Mark it seen and explore it later.", [("hl", [4, 5, 6, 7, 8])]),
           ("The seen set is what stops you looping forever in a cycle. Never forget it.", [("hl", [6]), ("b", "Cycles: the seen set saves you")]),
           ("Everything seen is reachable. O of V plus E. Depth first, done.", [("hl", [9]), ("cap", "Reachable? DFS with a seen set.")])]),
 dict(level="Medium", title="How many separate groups?", func="count_groups",
      prompt="<p>Write <code>count_groups(n, edges)</code>. People are numbered 0 to n - 1. Each edge <code>[a, b]</code> means a and b know each other (both ways). Return how many separate friendship groups there are; someone with no links is a group of one.</p><p>Example: <code>count_groups(5, [[0, 1], [1, 2], [3, 4]])</code> returns <code>2</code>.</p>",
      starter="def count_groups(n, edges):\n    pass\n",
      tests=[("given example", [5, [[0, 1], [1, 2], [3, 4]]], False), ("everyone alone", [3, []], False), ("nobody", [0, []], True), ("all connected", [4, [[0, 1], [1, 2], [2, 3]]], True), ("cycle and a loner", [4, [[0, 1], [1, 2], [2, 0]]], True), ("20,000 pairs", [20000, {"__py__": "[[i, i + 1] for i in range(0, 20000, 2)]"}], True)],
      hints=["Build an adjacency dict from the edges, adding both directions.", "Loop over every person. If they are not seen yet, that is a new group: explore everyone they connect to."],
      solution=COMPONENTS, explain="Building the graph and exploring it touch each person and edge a constant number of times: <b>O(V + E)</b> time, <b>O(V + E)</b> space.",
      vid=[("Graphs, medium. How many separate groups of friends?", [("b", "5 people, links 0-1, 1-2, 3-4: 2 groups")]),
           ("First, build the graph. Friendship goes both ways, so add both directions.", [("clear",), ("code", COMPONENTS.splitlines()), ("hl", [1, 2, 3, 4])]),
           ("Now loop over everyone. Already seen? Skip them. Not seen? That's a brand new group.", [("hl", [7, 8, 9, 10])]),
           ("Then flood the whole group with a depth first search, marking everyone seen.", [("hl", [11, 12, 13, 14, 15, 16, 17])]),
           ("Every person and link once. O of V plus E. This is counting islands, networks, clusters. Everywhere.", [("cap", "Unseen person = new group, then flood it.")])]),
 dict(level="Hard", title="Shortest road distance", func="shortest_route",
      prompt="<p>Write <code>shortest_route(n, roads, start, end)</code>. Towns are 0 to n - 1. Each road <code>[a, b, d]</code> joins a and b both ways with length d (positive). Return the shortest total distance from start to end, or <code>-1</code> if you cannot get there.</p><p>Example: <code>shortest_route(4, [[0, 1, 5], [0, 2, 1], [2, 1, 2], [1, 3, 1]], 0, 3)</code> returns <code>4</code>.</p>",
      starter="import heapq\n\ndef shortest_route(n, roads, start, end):\n    pass\n",
      tests=[("given example", [4, [[0, 1, 5], [0, 2, 1], [2, 1, 2], [1, 3, 1]], 0, 3], False), ("unreachable", [3, [[0, 1, 4]], 0, 2], False), ("start is end", [2, [[0, 1, 3]], 1, 1], True), ("direct is longer", [3, [[0, 2, 10], [0, 1, 3], [1, 2, 3]], 0, 2], True), ("one road", [2, [[0, 1, 7]], 1, 0], True), ("5,000 towns in a line", [5000, {"__py__": "[[i, i + 1, 2] for i in range(4999)]"}, 0, 4999], True)],
      hints=["Fewest roads is BFS; shortest distance with lengths is Dijkstra: a heap of (distance so far, town).", "Pop the closest town. If it is the end, you are done. Otherwise try every road out; push any town you reached more cheaply than before."],
      solution=DIJKSTRA, explain="Each road can cause one heap push: <b>O((V + E) log V)</b> time, <b>O(V + E)</b> space.",
      vid=[("Graphs, hard. Shortest road distance, with road lengths. BFS isn't enough any more.", [("b", "0 to 2 to 1 to 3: 1 + 2 + 1 = 4, beats the direct 5")]),
           ("Lengths mean Dijkstra. Always expand the closest town not yet finished. Closest? That's a heap.", [("clear",), ("code", DIJKSTRA.splitlines()), ("hl", [7, 8, 9, 10])]),
           ("Pop the closest. If it's the destination, that distance is final. Return it.", [("hl", [10, 11, 12])]),
           ("Skip stale entries: if we already found a shorter way, ignore this one.", [("hl", [13, 14])]),
           ("Try every road out. Found a cheaper way to a town? Record it and push it. That's Dijkstra. Satnavs run on it.", [("hl", [15, 16, 17, 18]), ("cap", "Weighted shortest path: Dijkstra with a heap.")])]),
]

# ================================================================ greedy
COINS = S('''
def fewest_uk_coins(pence):
    count = 0
    for coin in [200, 100, 50, 20, 10, 5, 2, 1]:
        count += pence // coin          # as many as fit
        pence %= coin
    return count
''')
TALKS = S('''
def max_talks(talks):
    count = 0
    free_at = float("-inf")
    for start, end in sorted(talks, key=lambda t: t[1]):
        if start >= free_at:            # fits after the last one
            count += 1
            free_at = end
    return count
''')
JUMP = S('''
def can_reach_end(jumps):
    furthest = 0
    for i, j in enumerate(jumps):
        if i > furthest:
            return False                # stuck before here
        furthest = max(furthest, i + j)
    return True
''')
LADDER_C["greedy"] = [
 dict(level="Easy", title="Fewest UK coins", func="fewest_uk_coins",
      prompt="<p>Write <code>fewest_uk_coins(pence)</code>. Using UK coins (£2, £1, 50p, 20p, 10p, 5p, 2p, 1p), return the fewest coins that make <code>pence</code> exactly.</p><p>Example: <code>fewest_uk_coins(37)</code> returns <code>4</code> (20p + 10p + 5p + 2p).</p>",
      starter="def fewest_uk_coins(pence):\n    pass\n",
      tests=[("small amount", [37], False), ("exactly £1", [100], False), ("zero", [0], True), ("one penny", [1], True), ("big amount", [9999], True), ("odd one", [288], True)],
      hints=["UK coins are designed so the greedy choice works: always take the biggest coin that fits.", "<code>count += pence // coin</code>, then <code>pence %= coin</code>."],
      solution=COINS, explain="A fixed 8 coins, whatever the amount: <b>O(1)</b> time and space.",
      vid=[("Greedy, easy. The fewest UK coins for an amount.", [("b", "37p: 20 + 10 + 5 + 2 = 4 coins")]),
           ("Greedy means take the best-looking choice now: the biggest coin that fits.", [("clear",), ("code", COINS.splitlines()), ("hl", [2])]),
           ("Floor division says how many of that coin fit. The remainder carries on to smaller coins.", [("hl", [3, 4])]),
           ("For UK coins, greedy is always right. For weird coins, like one, three and four, it isn't. Always check.", [("cap", "Biggest coin that fits, then the rest.")])]),
 dict(level="Medium", title="Most talks you can attend", func="max_talks",
      prompt="<p>Write <code>max_talks(talks)</code>. Each talk is <code>[start, end]</code>. You can attend one talk at a time; a talk can start exactly when the previous one ends. Return the most talks you can attend.</p><p>Example: <code>[[1, 4], [3, 5], [0, 6], [5, 7], [8, 9]]</code> gives <code>3</code>.</p>",
      starter="def max_talks(talks):\n    pass\n",
      tests=[("given example", [[[1, 4], [3, 5], [0, 6], [5, 7], [8, 9]]], False), ("touching", [[[1, 2], [2, 3], [3, 4]]], False), ("empty", [[]], True), ("all overlap", [[[1, 10], [2, 9], [3, 8]]], True), ("long one first", [[[0, 100], [1, 2], [3, 4]]], True), ("10,000 talks", [{"__py__": "[[i, i + 1] for i in range(10000)]"}], True)],
      hints=["Sort by <b>end</b> time, not start time.", "Take a talk whenever it starts at or after the end of the last one you took."],
      solution=TALKS, explain="Sorting dominates: <b>O(n log n)</b> time, <b>O(n)</b> space for the sorted copy.",
      vid=[("Greedy, medium. The most talks you can attend, one at a time.", [("b", "Best for the example: 3 talks")]),
           ("The winning rule: always pick the talk that finishes first. It leaves the most time for everything else.", [("clear",), ("code", TALKS.splitlines()), ("hl", [3])]),
           ("Sort by end time. Then walk through, taking any talk that starts after you're free.", [("hl", [4, 5, 6])]),
           ("Sorting by start time fails: one long talk can block everything. Earliest finish wins. Every time.", [("cap", "Most things in a schedule? Sort by end time.")])]),
 dict(level="Hard", title="Can you reach the end?", func="can_reach_end",
      prompt="<p>Write <code>can_reach_end(jumps)</code>. You start at position 0. <code>jumps[i]</code> is the furthest you can jump forward from position i. Return <code>True</code> if you can reach the last position.</p><p>Example: <code>[2, 3, 1, 1, 4]</code> is True; <code>[3, 2, 1, 0, 4]</code> is False.</p>",
      starter="def can_reach_end(jumps):\n    pass\n",
      tests=[("reachable", [[2, 3, 1, 1, 4]], False), ("stuck on a zero", [[3, 2, 1, 0, 4]], False), ("one position", [[0]], True), ("zero at the start", [[0, 1]], True), ("big first jump", [[10, 0, 0, 0]], True), ("100,000 ones", [{"__py__": "[1] * 100000"}], True)],
      hints=["Track the furthest position you can reach so far.", "Walk left to right. If your position is beyond the furthest reachable, you are stuck."],
      solution=JUMP, explain="One pass with one variable: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Greedy, hard. Can you jump all the way to the end?", [("b", "[2, 3, 1, 1, 4] True, [3, 2, 1, 0, 4] False")]),
           ("Trying every jump path explodes. Greedy keeps just one number: the furthest you can reach.", [("clear",), ("code", JUMP.splitlines()), ("hl", [1])]),
           ("Walk forward. If you're standing somewhere past the furthest reachable, you never got here. Stuck.", [("hl", [3, 4])]),
           ("Otherwise, stretch the furthest reach with this jump.", [("hl", [5])]),
           ("One pass, one variable, O of n. From exponential to linear. That's greedy at its best.", [("cap", "Track the furthest reach.")])]),
]

# ================================================================ dynamic programming
WAYS = S('''
def climb_ways(n):
    a, b = 1, 1                     # ways to reach step 0, step 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b if n >= 1 else 1
''')
CHANGE = S('''
def fewest_coins(coins, amount):
    INF = float("inf")
    best = [0] + [INF] * amount     # best[x] = coins for x
    for x in range(1, amount + 1):
        for c in coins:
            if c <= x and best[x - c] + 1 < best[x]:
                best[x] = best[x - c] + 1
    return best[amount] if best[amount] != INF else -1
''')
LCS = S('''
def common_subsequence(a, b):
    prev = [0] * (len(b) + 1)
    for ch in a:
        cur = [0]
        for j, other in enumerate(b):
            if ch == other:
                cur.append(prev[j] + 1)
            else:
                cur.append(max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]
''')
LADDER_C["dynamic-programming"] = [
 dict(level="Easy", title="Ways up the stairs", func="climb_ways",
      prompt="<p>Write <code>climb_ways(n)</code>. You climb n steps, taking 1 or 2 at a time. Return how many different ways there are. <code>climb_ways(0)</code> is 1 (do nothing).</p><p>Example: <code>climb_ways(4)</code> returns <code>5</code>.</p>",
      starter="def climb_ways(n):\n    pass\n",
      tests=[("given example", [4], False), ("one step", [1], False), ("zero", [0], True), ("two steps", [2], True), ("ten", [10], True), ("forty", [40], True)],
      hints=["The last move was 1 step or 2 steps, so ways(n) = ways(n - 1) + ways(n - 2).", "Keep just the last two answers and build up. No recursion needed."],
      solution=WAYS, explain="One loop up to n: <b>O(n)</b> time, two variables: <b>O(1)</b> space.",
      vid=[("Dynamic programming, easy. How many ways up n stairs, one or two steps at a time?", [("b", "climb_ways(4) is 5")]),
           ("Think about the last move. It was one step, or two. So ways of n is ways of n minus one, plus ways of n minus two.", [("b", "ways(n) = ways(n - 1) + ways(n - 2)")]),
           ("Plain recursion recomputes the same answers again and again. Exponential. Disaster.", [("clear",), ("code", WAYS.splitlines()), ("hl", [1])]),
           ("Instead, build up from the bottom, keeping only the last two answers.", [("hl", [2, 3])]),
           ("O of n time, O of 1 space. Ninety steps, instant. That's dynamic programming.", [("hl", [4]), ("cap", "Last move was 1 or 2: add the two.")])]),
 dict(level="Medium", title="Fewest coins for any coin set", func="fewest_coins",
      prompt="<p>Write <code>fewest_coins(coins, amount)</code>. Return the fewest coins (unlimited of each) that make <code>amount</code> exactly, or <code>-1</code> if impossible. Greedy does not always work here.</p><p>Example: <code>fewest_coins([1, 3, 4], 6)</code> returns <code>2</code> (3 + 3).</p>",
      starter="def fewest_coins(coins, amount):\n    pass\n",
      tests=[("greedy fails", [[1, 3, 4], 6], False), ("impossible", [[2], 3], False), ("zero amount", [[1], 0], True), ("one coin type", [[5], 15], True), ("UK style", [[1, 2, 5, 10, 20, 50], 88], True), ("bigger amount", [[7, 11, 13], 2000], True)],
      hints=["best[x] = the fewest coins to make x. best[0] = 0.", "For each x, try every coin c: <code>best[x - c] + 1</code>."],
      solution=CHANGE, explain="For each amount up to A, try each of k coins: <b>O(A × k)</b> time, <b>O(A)</b> space.",
      vid=[("Dynamic programming, medium. Fewest coins, for any set of coins.", [("b", "Coins 1, 3, 4, make 6: 3 + 3 = 2 coins")]),
           ("Greedy grabs 4, then 1, then 1. Three coins. Wrong! We need to try options properly.", [("b", "Greedy: 4 + 1 + 1 = 3 coins. Wrong.")]),
           ("Build a table. Best of x is the fewest coins to make x. Zero needs zero coins.", [("clear",), ("code", CHANGE.splitlines()), ("hl", [2])]),
           ("For each amount, try every coin as the last coin used: best of x minus that coin, plus one. Keep the smallest.", [("hl", [3, 4, 5, 6])]),
           ("Every small answer is solved once and reused. O of amount times coins. That's the DP promise.", [("hl", [7]), ("cap", "Try each option for the last move, reuse smaller answers.")])]),
 dict(level="Hard", title="Longest shared subsequence", func="common_subsequence",
      prompt="<p>Write <code>common_subsequence(a, b)</code>. Return the length of the longest sequence of characters that appears in both strings in the same order (not necessarily next to each other).</p><p>Example: <code>common_subsequence(\"abcde\", \"ace\")</code> returns <code>3</code>.</p>",
      starter="def common_subsequence(a, b):\n    pass\n",
      tests=[("given example", ["abcde", "ace"], False), ("nothing shared", ["abc", "xyz"], False), ("one empty", ["", "abc"], True), ("identical", ["kayak", "kayak"], True), ("order matters", ["abc", "cba"], True), ("300 characters each", [{"__py__": "'ab' * 150"}, {"__py__": "'ba' * 150"}], True)],
      hints=["Compare the strings character by character in a grid: rows for a, columns for b.", "Match: diagonal + 1. No match: the better of left and up. Keep only the previous row to save space."],
      solution=LCS, explain="One cell per pair of characters: <b>O(n × m)</b> time, <b>O(m)</b> space with one row kept.",
      vid=[("Dynamic programming, hard. The longest subsequence two strings share, in order.", [("b", "'abcde' and 'ace' share 'ace': length 3")]),
           ("Picture a grid: one string down the side, the other across the top. Each cell answers: best so far for these two prefixes.", [("clear",), ("code", LCS.splitlines()), ("hl", [1, 2, 4])]),
           ("Characters match? Take the diagonal answer and add one.", [("hl", [5, 6])]),
           ("No match? Take the better of skipping a letter from either string: left or up.", [("hl", [7, 8])]),
           ("We only need the previous row, so memory stays small. O of n times m. Diff tools and DNA matching use exactly this. Champion level.", [("hl", [9, 10]), ("cap", "Match: diagonal + 1. Else: max(up, left).")])]),
]

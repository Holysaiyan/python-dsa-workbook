"""Easy, Medium and Hard practice for the Accenture-priority lessons, each with a narrated solution video.

Each problem: level, title, prompt, func, starter, tests (label, args, hidden), hints, solution, explain,
and vid: a list of (narration, [items]) for the Coach Max video (items as in video/dsa_vids.py).
"""

def S(code): return code.strip("\n") + "\n"

LADDER = {}

# ---------------------------------------------------------------- Hash sets
HAS_DUP = S('''
def has_duplicate(ids):
    seen = set()
    for x in ids:
        if x in seen:
            return True
        seen.add(x)
    return False
''')
COMMON = S('''
def common_rooms(a, b):
    in_a = set(a)
    both = set()
    for room in b:
        if room in in_a:
            both.add(room)
    return sorted(both)
''')
STREAK = S('''
def longest_streak(nums):
    have = set(nums)
    best = 0
    for x in have:
        if x - 1 not in have:          # x starts a run
            length = 1
            while x + length in have:
                length += 1
            best = max(best, length)
    return best
''')
LADDER["sets"] = [
 dict(level="Easy", title="Any repeated booking?", func="has_duplicate",
      prompt="<p>Write <code>has_duplicate(ids)</code>. Return <code>True</code> if any booking ID appears more than once, otherwise <code>False</code>.</p><p>Example: <code>has_duplicate([\"B1\", \"B2\", \"B1\"])</code> returns <code>True</code>.</p>",
      starter="def has_duplicate(ids):\n    pass\n",
      tests=[("given example", [["B1", "B2", "B1"]], False), ("all different", [["B1", "B2", "B3"]], False), ("empty", [[]], True), ("one item", [["B1"]], True), ("repeat at the end", [["A", "B", "C", "D", "A"]], True), ("100,000 unique", [{"__py__": "list(range(100000))"}], True)],
      hints=["'Have I seen this before?' is a set question.", "Loop once: if <code>x in seen</code> return True, else <code>seen.add(x)</code>."],
      solution=HAS_DUP, explain="One pass with O(1) set checks: <b>O(n)</b> time, <b>O(n)</b> space for the set.",
      vid=[("Hash sets, easy. Any repeated booking? Return true if any ID shows up twice.", [("b", "has_duplicate(['B1', 'B2', 'B1']) is True")]),
           ("Two loops comparing every pair would be O of n squared. Slow. We can do better.", [("b", "Every pair: O(n²). Too slow.")]),
           ("The question is 'have I seen this before?' That's a set. Every time.", [("clear",), ("code", HAS_DUP.splitlines()), ("hl", [1])]),
           ("Walk the list once. If it's already in the set, we found a repeat. Return true straight away.", [("hl", [3, 4])]),
           ("Otherwise add it and move on. Nothing repeated? Return false after the loop.", [("hl", [5, 6])]),
           ("One pass, O of n. Checking a set is O of 1. Beautiful.", [("b", "O(n) time, O(n) space"), ("cap", "Seen it before? Use a set.")])]),
 dict(level="Medium", title="Rooms on both lists", func="common_rooms",
      prompt="<p>Write <code>common_rooms(a, b)</code>. Return the rooms that appear in <b>both</b> lists, each once, sorted.</p><p>Example: <code>common_rooms([\"C3\", \"A1\", \"B2\", \"A1\"], [\"A1\", \"D4\", \"C3\"])</code> returns <code>[\"A1\", \"C3\"]</code>.</p>",
      starter="def common_rooms(a, b):\n    pass\n",
      tests=[("given example", [["C3", "A1", "B2", "A1"], ["A1", "D4", "C3"]], False), ("nothing shared", [["A1"], ["B2"]], False), ("one list empty", [[], ["A1"]], True), ("duplicates in both", [["A1", "A1"], ["A1", "A1"]], True), ("all shared", [["B2", "A1"], ["A1", "B2"]], True), ("big lists, few shared", [{"__py__": "[f'R{i}' for i in range(50000)]"}, {"__py__": "[f'R{i}' for i in range(49990, 99990)]"}], True)],
      hints=["Turn one list into a set so 'is it in a?' is instant.", "Collect matches in a set (no repeats), then <code>return sorted(both)</code>. Or simply <code>sorted(set(a) &amp; set(b))</code>."],
      solution=COMMON, explain="Building the set is O(n), checking b is O(m), sorting the k shared rooms is O(k log k): <b>O(n + m + k log k)</b>, which is <b>O(n log n)</b> at worst. Space <b>O(n)</b>.",
      vid=[("Hash sets, medium. Rooms on both lists. Each once, sorted.", [("b", "['C3','A1','B2','A1'] and ['A1','D4','C3'] give ['A1','C3']")]),
           ("For every room in b, ask: is it in a? Searching a list is O of n each time. Make it a set and it's instant.", [("clear",), ("code", COMMON.splitlines()), ("hl", [1])]),
           ("Collect the matches in another set, so duplicates vanish automatically.", [("hl", [2, 3, 4, 5])]),
           ("Then sort, because the task said sorted. Read the output format. Always.", [("hl", [6])]),
           ("Pro move: set of a, ampersand, set of b. One line. Same answer. Tremendous.", [("b", "Shortcut: sorted(set(a) & set(b))"), ("cap", "In both lists? Set intersection.")])]),
 dict(level="Hard", title="Longest run of consecutive numbers", func="longest_streak",
      prompt="<p>Write <code>longest_streak(nums)</code>. The numbers are in any order. Return the length of the longest run of consecutive integers. Aim for O(n), without sorting.</p><p>Example: <code>longest_streak([100, 4, 200, 1, 3, 2])</code> returns <code>4</code> (1, 2, 3, 4).</p>",
      starter="def longest_streak(nums):\n    pass\n",
      tests=[("given example", [[100, 4, 200, 1, 3, 2]], False), ("with duplicates", [[1, 2, 2, 3]], False), ("empty", [[]], True), ("single", [[7]], True), ("negatives", [[-1, -3, -2, 5]], True), ("200,000 numbers", [{"__py__": "list(range(200000, 0, -1))"}], True)],
      hints=["Put everything in a set. Only start counting from a number whose left neighbour (x - 1) is missing.", "From each start, count up while <code>x + length in have</code>. Each number is counted once overall, so it stays O(n)."],
      solution=STREAK, explain="Each number is the start of at most one count, and every inner step moves through a different number: <b>O(n)</b> time, <b>O(n)</b> space.",
      vid=[("Hash sets, hard. Longest run of consecutive numbers, in any order, without sorting.", [("b", "[100, 4, 200, 1, 3, 2]: the run 1, 2, 3, 4 has length 4")]),
           ("Sorting would work, but it's O of n log n. They want O of n. So: a set.", [("clear",), ("code", STREAK.splitlines()), ("hl", [1])]),
           ("Here's the genius move. Only start counting from the beginning of a run. A number is a start if x minus one is not in the set.", [("hl", [3, 4])]),
           ("From a start, count upward while the next number is there.", [("hl", [5, 6, 7])]),
           ("Every number gets counted once, in one run. So the whole thing is O of n. Not n squared. That's the trick interviewers love.", [("hl", [8]), ("b", "Only count from run starts: O(n)"), ("cap", "Start where x - 1 is missing.")])]),
]

# ---------------------------------------------------------------- Dictionaries
VOTES = S('''
def count_votes(votes):
    counts = {}
    for name in votes:
        counts[name] = counts.get(name, 0) + 1
    return counts
''')
FIRST_UNIQUE = S('''
def first_unique(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for i, ch in enumerate(s):
        if counts[ch] == 1:
            return i
    return -1
''')
TWO_SUM = S('''
def two_sum(nums, target):
    where = {}                        # value -> index
    for i, x in enumerate(nums):
        need = target - x
        if need in where:
            return [where[need], i]
        where[x] = i
    return []
''')
LADDER["dictionaries"] = [
 dict(level="Easy", title="Count the votes", func="count_votes",
      prompt="<p>Write <code>count_votes(votes)</code>. Return a dict of each name and how many votes it got.</p><p>Example: <code>[\"Ana\", \"Ben\", \"Ana\"]</code> gives <code>{\"Ana\": 2, \"Ben\": 1}</code>.</p>",
      starter="def count_votes(votes):\n    pass\n",
      tests=[("given example", [["Ana", "Ben", "Ana"]], False), ("one voter", [["Cal"]], False), ("no votes", [[]], True), ("all the same", [["Ana", "Ana", "Ana"]], True), ("many names", [{"__py__": "[f'N{i % 50}' for i in range(10000)]"}], True)],
      hints=["The counting pattern: start at 0 the first time you see a key.", "<code>counts[name] = counts.get(name, 0) + 1</code>"],
      solution=VOTES, explain="One pass, O(1) per update: <b>O(n)</b> time, <b>O(k)</b> space for k names.",
      vid=[("Dictionaries, easy. Count the votes. Name goes in, count comes out.", [("b", "['Ana', 'Ben', 'Ana'] gives {'Ana': 2, 'Ben': 1}")]),
           ("This is the counting pattern. You'll use it a thousand times.", [("clear",), ("code", VOTES.splitlines()), ("hl", [1])]),
           ("For each name, get its count so far, zero if it's new, and add one.", [("hl", [2, 3])]),
           ("Get with a default never crashes on a new key. Square brackets would. Big difference.", [("b", "get(name, 0): safe for new keys")]),
           ("One pass. O of n. Done. Next.", [("hl", [4]), ("cap", "Counting? Dict with get(key, 0) + 1.")])]),
 dict(level="Medium", title="First character that never repeats", func="first_unique",
      prompt="<p>Write <code>first_unique(s)</code>. Return the index of the first character that appears exactly once, or <code>-1</code> if there is none.</p><p>Example: <code>first_unique(\"swiss\")</code> returns <code>1</code> (the w).</p>",
      starter="def first_unique(s):\n    pass\n",
      tests=[("given example", ["swiss"], False), ("all repeat", ["aabb"], False), ("empty", [""], True), ("first letter", ["abcab"], True), ("last letter", ["aabbc"], True), ("long string", [{"__py__": "'ab' * 50000 + 'z'"}], True)],
      hints=["Two passes: first count every character, then find the first with count 1.", "Use <code>enumerate(s)</code> in the second pass so you have the index."],
      solution=FIRST_UNIQUE, explain="Two passes over the string: <b>O(n)</b> time. The dict holds at most one entry per distinct character: <b>O(k)</b> space.",
      vid=[("Dictionaries, medium. First character that never repeats. Return its index.", [("b", "'swiss': s repeats, w is unique, so index 1")]),
           ("You can't know a letter is unique until you've seen the whole string. So: two passes.", [("clear",), ("code", FIRST_UNIQUE.splitlines()), ("hl", [1, 2, 3])]),
           ("Pass one, count every character. The counting pattern again.", [("hl", [2, 3])]),
           ("Pass two, walk in order, with enumerate for the index. First count of one wins.", [("hl", [4, 5, 6])]),
           ("Nothing found? Minus one. Two passes is still O of n. Smart.", [("hl", [7]), ("cap", "Need the whole picture first? Count, then scan.")])]),
 dict(level="Hard", title="Two numbers that add to the target", func="two_sum",
      prompt="<p>Write <code>two_sum(nums, target)</code>. Return <code>[i, j]</code>, the positions of the two numbers that add to <code>target</code>, with <code>i &lt; j</code>. There is exactly one answer, or return <code>[]</code> if there is none. The list is not sorted. Aim for O(n).</p><p>Example: <code>two_sum([2, 7, 11, 15], 9)</code> returns <code>[0, 1]</code>.</p>",
      starter="def two_sum(nums, target):\n    pass\n",
      tests=[("given example", [[2, 7, 11, 15], 9], False), ("answer at the end", [[3, 2, 4], 6], False), ("same value twice", [[3, 3], 6], True), ("no answer", [[1, 2, 3], 100], True), ("negatives", [[-4, 10, 7, 1], 3], True), ("100,000 numbers", [{"__py__": "list(range(100000))"}, 199997], True)],
      hints=["For each number, what partner does it need? <code>target - x</code>.", "Keep a dict of value to index for numbers already seen. If the partner is in it, you are done."],
      solution=TWO_SUM, explain="One pass with O(1) dict lookups: <b>O(n)</b> time, <b>O(n)</b> space.",
      vid=[("Dictionaries, hard. The famous one. Two sum. Find two positions that add to the target.", [("b", "two_sum([2, 7, 11, 15], 9) gives [0, 1]")]),
           ("Every pair is O of n squared. Too slow. Flip the question: for each number, what partner does it need?", [("b", "Partner needed = target - x")]),
           ("Keep a dictionary of numbers we've already seen, value to index.", [("clear",), ("code", TWO_SUM.splitlines()), ("hl", [1])]),
           ("For each number, work out the partner it needs. Already in the dictionary? We're done. Return both positions.", [("hl", [3, 4, 5])]),
           ("Not there? Store this number and keep going. Check first, then store. That handles the three plus three case.", [("hl", [6]), ("b", "Check before you store: [3, 3] works")]),
           ("One pass. O of n. This is the number one interview question in the world, and now you own it.", [("cap", "Need a partner? Store what you've seen in a dict.")])]),
]

# ---------------------------------------------------------------- Stacks
PARENS = S('''
def balanced_round(s):
    depth = 0
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0
''')
BRACKETS = S('''
def balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack
''')
NEXT_GREATER = S('''
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []                         # positions still waiting
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            result[stack.pop()] = x
        stack.append(i)
    return result
''')
LADDER["stacks"] = [
 dict(level="Easy", title="Round brackets balanced?", func="balanced_round",
      prompt="<p>Write <code>balanced_round(s)</code>. The string has only <code>(</code> and <code>)</code>. Return <code>True</code> if every opening bracket is closed in the right order.</p><p>Example: <code>\"(())()\"</code> is True; <code>\")(\"</code> is False.</p>",
      starter="def balanced_round(s):\n    pass\n",
      tests=[("given example", ["(())()"], False), ("closes too early", [")("], False), ("empty", [""], True), ("one open", ["("], True), ("deep", ["((((()))))"], True), ("long", [{"__py__": "'()' * 50000"}], True)],
      hints=["With one bracket type, a counter works as a stack: +1 for open, -1 for close.", "If the counter ever goes below 0, return False. At the end it must be 0."],
      solution=PARENS, explain="One pass with one counter: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Stacks, easy. Are the round brackets balanced?", [("b", "'(())()' True, ')(' False")]),
           ("With only one kind of bracket, a stack is just a counter. Open, plus one. Close, minus one.", [("clear",), ("code", PARENS.splitlines()), ("hl", [1, 3, 4, 5, 6])]),
           ("If it ever drops below zero, a bracket closed before it opened. Return false right away.", [("hl", [7, 8])]),
           ("At the end, everything opened must be closed. Depth back to zero.", [("hl", [9])]),
           ("O of n time, O of 1 space. Simple. Clean. Very effective.", [("cap", "One bracket type? A counter is enough.")])]),
 dict(level="Medium", title="All bracket types balanced?", func="balanced",
      prompt="<p>Write <code>balanced(s)</code>. The string can contain <code>()</code>, <code>[]</code>, <code>{}</code> and other characters, which you ignore. Return <code>True</code> if every bracket is closed by the right type in the right order.</p><p>Example: <code>\"{a[b]c}\"</code> is True; <code>\"(]\"</code> is False.</p>",
      starter="def balanced(s):\n    pass\n",
      tests=[("given example", ["{a[b]c}"], False), ("wrong type", ["(]"], False), ("empty", [""], True), ("unclosed", ["([]"], True), ("close with nothing open", ["]"], True), ("text only", ["hello"], True), ("crossed", ["([)]"], True)],
      hints=["Push every opening bracket. On a closing one, the top of the stack must be its partner.", "A dict maps each closer to its opener: <code>{\")\": \"(\", ...}</code>. Check the stack is not empty before popping."],
      solution=BRACKETS, explain="Each character is pushed and popped at most once: <b>O(n)</b> time, <b>O(n)</b> space for the stack.",
      vid=[("Stacks, medium. Three kinds of brackets, plus other text to ignore.", [("b", "'{a[b]c}' True, '(]' False, '([)]' False")]),
           ("Now a counter isn't enough: the type matters. Last opened must be first closed. That's a stack.", [("clear",), ("code", BRACKETS.splitlines()), ("hl", [1, 2])]),
           ("Opening bracket? Push it.", [("hl", [4, 5])]),
           ("Closing bracket? The stack must not be empty, and the top must be its partner. Otherwise, false.", [("hl", [6, 7, 8])]),
           ("Anything left open at the end? Not balanced. Return not stack.", [("hl", [9]), ("cap", "Last opened, first closed: stack.")])]),
 dict(level="Hard", title="Next warmer reading", func="next_greater",
      prompt="<p>Write <code>next_greater(nums)</code>. For each position, return the next value to its right that is <b>bigger</b>, or <code>-1</code> if there is none. Aim for O(n).</p><p>Example: <code>next_greater([2, 1, 5, 3])</code> returns <code>[5, 5, -1, -1]</code>.</p>",
      starter="def next_greater(nums):\n    pass\n",
      tests=[("given example", [[2, 1, 5, 3]], False), ("rising", [[1, 2, 3]], False), ("falling", [[3, 2, 1]], True), ("equal values", [[2, 2, 3]], True), ("empty", [[]], True), ("2,000 falling then a peak", [{"__py__": "list(range(2000, 0, -1)) + [5000]"}], True)],
      hints=["Keep a stack of positions still waiting for a bigger value.", "For each new value, pop every waiting position whose value is smaller and give it this value. Then push the new position."],
      solution=NEXT_GREATER, explain="Each position is pushed once and popped at most once: <b>O(n)</b> time overall, <b>O(n)</b> space.",
      vid=[("Stacks, hard. For each number, the next bigger number to its right.", [("b", "[2, 1, 5, 3] gives [5, 5, -1, -1]")]),
           ("Checking everything to the right is O of n squared. The pro tool here is a monotonic stack.", [("clear",), ("code", NEXT_GREATER.splitlines()), ("hl", [1, 2])]),
           ("The stack holds positions still waiting for their answer.", [("hl", [2])]),
           ("A new number arrives. Everyone waiting with a smaller value just got their answer. Pop them and fill it in.", [("hl", [4, 5])]),
           ("Then the new number joins the queue of waiters. Each position goes in once and out once. So it's O of n. Incredible.", [("hl", [6]), ("cap", "'Next bigger' or 'next warmer'? Monotonic stack.")])]),
]

# ---------------------------------------------------------------- Two pointers
PAL = S('''
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
''')
PAIR = S('''
def pair_sum_sorted(nums, target):
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
''')
AREA = S('''
def max_area(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        width = right - left
        best = max(best, width * min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best
''')
LADDER["two-pointers"] = [
 dict(level="Easy", title="Palindrome check", func="is_palindrome",
      prompt="<p>Write <code>is_palindrome(s)</code>. Return <code>True</code> if the string reads the same forwards and backwards (exact characters). Use two pointers, not <code>s[::-1]</code>.</p><p>Example: <code>\"level\"</code> is True; <code>\"levels\"</code> is False.</p>",
      starter="def is_palindrome(s):\n    pass\n",
      tests=[("given example", ["level"], False), ("not one", ["levels"], False), ("empty", [""], True), ("one letter", ["a"], True), ("even length", ["abba"], True), ("case matters", ["Aa"], True)],
      hints=["One pointer at each end. Compare, then move both inwards.", "Stop when they meet: <code>while left &lt; right</code>."],
      solution=PAL, explain="At most n/2 comparisons: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Two pointers, easy. Is it a palindrome? Same forwards and backwards.", [("b", "'level' True, 'levels' False")]),
           ("One pointer at the start, one at the end.", [("clear",), ("code", PAL.splitlines()), ("hl", [1])]),
           ("Compare them. Different? Not a palindrome. Return false.", [("hl", [3, 4])]),
           ("Same? Move both inward, until they meet in the middle.", [("hl", [2, 5, 6])]),
           ("O of n, and O of 1 space, because we never build a reversed copy. Interviewers notice that.", [("hl", [7]), ("cap", "Compare the ends, move inward.")])]),
 dict(level="Medium", title="Pair in a sorted list", func="pair_sum_sorted",
      prompt="<p>Write <code>pair_sum_sorted(nums, target)</code>. <code>nums</code> is sorted. Return <code>[i, j]</code> (i &lt; j) of two values that add to <code>target</code>, or <code>[]</code>. Use O(1) extra space.</p><p>Example: <code>pair_sum_sorted([1, 3, 5, 6, 9], 9)</code> returns <code>[1, 3]</code> (3 + 6).</p>",
      starter="def pair_sum_sorted(nums, target):\n    pass\n",
      tests=[("given example", [[1, 3, 5, 6, 9], 9], False), ("no pair", [[1, 2, 4], 10], False), ("empty", [[], 5], True), ("ends", [[2, 3, 4, 8], 10], True), ("negatives", [[-5, -1, 2, 7], 2], True), ("200,000 numbers", [{"__py__": "list(range(200000))"}, 399997], True)],
      hints=["Start at both ends. Too small? Move left up. Too big? Move right down.", "Because the list is sorted, each move safely rules out one number."],
      solution=PAIR, explain="Each step moves one pointer inward: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Two pointers, medium. A sorted list, and a pair that adds to the target.", [("b", "[1, 3, 5, 6, 9], target 9: 3 + 6, so [1, 3]")]),
           ("Sorted plus pair? Two pointers. Every time. One at each end.", [("clear",), ("code", PAIR.splitlines()), ("hl", [1])]),
           ("Add them. Spot on? Return both positions.", [("hl", [3, 4, 5])]),
           ("Too small? Move left up to get bigger. Too big? Move right down to get smaller.", [("hl", [6, 7, 8, 9])]),
           ("Each move throws away one number for good. O of n, O of 1 space. Better than the dictionary version on memory.", [("cap", "Sorted + pair: squeeze from both ends.")])]),
 dict(level="Hard", title="Biggest container", func="max_area",
      prompt="<p>Write <code>max_area(heights)</code>. Each value is a wall height; walls are 1 apart. Pick two walls: the water they hold is <code>distance between them x the shorter wall</code>. Return the most water possible. Aim for O(n).</p><p>Example: <code>max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])</code> returns <code>49</code>.</p>",
      starter="def max_area(heights):\n    pass\n",
      tests=[("given example", [[1, 8, 6, 2, 5, 4, 8, 3, 7]], False), ("two walls", [[1, 1]], False), ("one wall", [[5]], True), ("rising", [[1, 2, 3, 4, 5]], True), ("tall ends", [[9, 1, 1, 1, 9]], True), ("100,000 walls", [{"__py__": "[(i * 7919) % 10007 for i in range(100000)]"}], True)],
      hints=["Start with the widest pair: both ends.", "Always move the <b>shorter</b> wall inward. Moving the taller one can never help, because the shorter wall still limits the water."],
      solution=AREA, explain="The pointers meet after n - 1 moves: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Two pointers, hard. The container. Two walls, and the water between them.", [("b", "Water = distance × shorter wall. Best for the example: 49")]),
           ("Start with the widest container: both ends.", [("clear",), ("code", AREA.splitlines()), ("hl", [1])]),
           ("Work out the water. Width times the shorter wall. Keep the best.", [("hl", [4, 5])]),
           ("Now the key insight. Move the shorter wall inward. The shorter wall is the limit, so moving the taller one can only lose width and gain nothing.", [("hl", [6, 7, 8, 9])]),
           ("Each step drops one wall for good. O of n. Explain that reason out loud in an interview, and they will be impressed. Believe me.", [("cap", "Move the shorter side: it's the limit.")])]),
]

# ---------------------------------------------------------------- Sliding window
MAXK = S('''
def max_sum_k(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best
''')
UNIQUE = S('''
def longest_unique(s):
    last = {}                          # char -> last index
    start = 0
    best = 0
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1       # jump past the repeat
        last[ch] = i
        best = max(best, i - start + 1)
    return best
''')
MINLEN = S('''
def min_len_sum(nums, target):
    start = 0
    total = 0
    best = len(nums) + 1
    for end, x in enumerate(nums):
        total += x
        while total >= target:
            best = min(best, end - start + 1)
            total -= nums[start]
            start += 1
    return best if best <= len(nums) else 0
''')
LADDER["sliding-window"] = [
 dict(level="Easy", title="Best k days in a row", func="max_sum_k",
      prompt="<p>Write <code>max_sum_k(nums, k)</code>. Return the largest total of any <code>k</code> consecutive values. <code>1 &lt;= k &lt;= len(nums)</code>.</p><p>Example: <code>max_sum_k([2, 1, 5, 1, 3, 2], 3)</code> returns <code>9</code> (5 + 1 + 3).</p>",
      starter="def max_sum_k(nums, k):\n    pass\n",
      tests=[("given example", [[2, 1, 5, 1, 3, 2], 3], False), ("k is 1", [[4, 9, 2], 1], False), ("k is the whole list", [[1, 2, 3], 3], True), ("negatives", [[-3, -1, -2], 2], True), ("best at the end", [[1, 1, 1, 9, 9], 2], True), ("100,000 values", [{"__py__": "[(i * 31) % 97 for i in range(100000)]"}, 500], True)],
      hints=["Sum the first k once. Then slide: add the new value, subtract the one leaving.", "<code>window += nums[i] - nums[i - k]</code>"],
      solution=MAXK, explain="One pass after the first window: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Sliding window, easy. The best total of k values in a row.", [("b", "[2, 1, 5, 1, 3, 2], k = 3: 5 + 1 + 3 = 9")]),
           ("Adding up every window from scratch is O of n times k. Slow.", [("clear",), ("code", MAXK.splitlines()), ("hl", [1, 2])]),
           ("Sum the first window once.", [("hl", [1, 2])]),
           ("Then slide. Add the value coming in, subtract the one going out. One step, not k.", [("hl", [3, 4, 5])]),
           ("O of n. In a row, a stretch, consecutive? Sliding window.", [("cap", "Fixed size window: add the new, drop the old.")])]),
 dict(level="Medium", title="Longest stretch with no repeats", func="longest_unique",
      prompt="<p>Write <code>longest_unique(s)</code>. Return the length of the longest substring with no repeated characters.</p><p>Example: <code>longest_unique(\"abcabcbb\")</code> returns <code>3</code> (\"abc\").</p>",
      starter="def longest_unique(s):\n    pass\n",
      tests=[("given example", ["abcabcbb"], False), ("all the same", ["bbbb"], False), ("empty", [""], True), ("all different", ["abcdef"], True), ("repeat far back", ["abba"], True), ("long", [{"__py__": "'abcdefghij' * 10000"}], True)],
      hints=["Grow a window to the right. When a character repeats inside the window, move the start just past its last position.", "Remember each character's last index in a dict, and only jump if that index is inside the window (<code>&gt;= start</code>)."],
      solution=UNIQUE, explain="Each character is visited once, with O(1) dict work: <b>O(n)</b> time, <b>O(k)</b> space for k distinct characters.",
      vid=[("Sliding window, medium. The longest stretch with no repeated letters.", [("b", "'abcabcbb': 'abc' has length 3")]),
           ("This window changes size. Grow it to the right, one letter at a time.", [("clear",), ("code", UNIQUE.splitlines()), ("hl", [4])]),
           ("A dictionary remembers where each letter was last seen.", [("hl", [1, 7])]),
           ("If the letter repeats inside the window, jump the start just past its last spot. Inside the window only: that's the abba trap.", [("hl", [5, 6])]),
           ("Measure the window every step and keep the best. O of n. Very elegant.", [("hl", [8]), ("cap", "Variable window: grow right, jump the start.")])]),
 dict(level="Hard", title="Shortest stretch reaching a target", func="min_len_sum",
      prompt="<p>Write <code>min_len_sum(nums, target)</code>. All values are positive. Return the length of the shortest run of consecutive values whose total is at least <code>target</code>, or <code>0</code> if none.</p><p>Example: <code>min_len_sum([2, 3, 1, 2, 4, 3], 7)</code> returns <code>2</code> (4 + 3).</p>",
      starter="def min_len_sum(nums, target):\n    pass\n",
      tests=[("given example", [[2, 3, 1, 2, 4, 3], 7], False), ("impossible", [[1, 1, 1], 10], False), ("one value is enough", [[1, 9, 1], 8], True), ("needs everything", [[1, 2, 3], 6], True), ("empty", [[], 1], True), ("100,000 values", [{"__py__": "[1] * 100000"}, 50000], True)],
      hints=["Grow the window to the right. While the total is big enough, record the length and shrink from the left.", "Positive values mean shrinking always lowers the total, which is why this works."],
      solution=MINLEN, explain="Each value enters once and leaves once: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Sliding window, hard. The shortest stretch whose total reaches the target.", [("b", "[2, 3, 1, 2, 4, 3], target 7: 4 + 3, length 2")]),
           ("Grow the window to the right, adding each value.", [("clear",), ("code", MINLEN.splitlines()), ("hl", [4, 5])]),
           ("The moment the total is big enough, record the length, then shrink from the left to try for shorter.", [("hl", [6, 7, 8, 9])]),
           ("This works because every value is positive. Shrinking always lowers the total.", [("b", "Positive values only: shrinking lowers the total")]),
           ("Each value comes in once and goes out once. O of n. Nothing found? Zero. Champion stuff.", [("hl", [10]), ("cap", "Grow until it's enough, then shrink while it still is.")])]),
]

# ---------------------------------------------------------------- Binary search
SEARCH = S('''
def search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
''')
LOWER = S('''
def first_at_least(nums, x):
    lo, hi = 0, len(nums)              # answer can be len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < x:
            lo = mid + 1
        else:
            hi = mid                   # mid might be the answer
    return lo
''')
ISQRT = S('''
def int_sqrt(n):
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2       # round up so lo always moves
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo
''')
LADDER["binary-search"] = [
 dict(level="Easy", title="Find a value", func="search",
      prompt="<p>Write <code>search(nums, target)</code>. <code>nums</code> is sorted with no repeats. Return the index of <code>target</code>, or <code>-1</code>. Use binary search.</p>",
      starter="def search(nums, target):\n    pass\n",
      tests=[("in the middle", [[1, 3, 5, 7, 9], 7], False), ("missing", [[1, 3, 5], 4], False), ("empty", [[], 1], True), ("first", [[2, 4, 6], 2], True), ("last", [[2, 4, 6], 6], True), ("1,000,000 values", [{"__py__": "list(range(0, 2000000, 2))"}, 1999998], True)],
      hints=["Look at the middle; throw away the half it cannot be in.", "<code>while lo &lt;= hi</code>, then <code>lo = mid + 1</code> or <code>hi = mid - 1</code>."],
      solution=SEARCH, explain="The range halves every step: <b>O(log n)</b> time, <b>O(1)</b> space.",
      vid=[("Binary search, easy. Find a value in a sorted list.", [("b", "Sorted list: check the middle, drop half")]),
           ("Low and high mark the part we haven't ruled out.", [("clear",), ("code", SEARCH.splitlines()), ("hl", [1, 2])]),
           ("Look at the middle. Found it? Return it.", [("hl", [3, 4, 5])]),
           ("Middle too small? The answer is to the right: low becomes mid plus one. Too big? High becomes mid minus one.", [("hl", [6, 7, 8, 9])]),
           ("A million values, about twenty steps. Twenty! Watch the plus one and minus one. That's where everyone slips.", [("hl", [10]), ("cap", "lo <= hi, mid + 1, mid - 1")])]),
 dict(level="Medium", title="First value at least x", func="first_at_least",
      prompt="<p>Write <code>first_at_least(nums, x)</code>. <code>nums</code> is sorted and may have repeats. Return the first index whose value is <code>&gt;= x</code>, or <code>len(nums)</code> if every value is smaller.</p><p>Example: <code>first_at_least([1, 3, 3, 3, 8], 3)</code> returns <code>1</code>.</p>",
      starter="def first_at_least(nums, x):\n    pass\n",
      tests=[("given example", [[1, 3, 3, 3, 8], 3], False), ("bigger than all", [[1, 2, 3], 9], False), ("smaller than all", [[5, 6, 7], 1], True), ("empty", [[], 4], True), ("between values", [[10, 20, 30], 25], True), ("1,000,000 repeats", [{"__py__": "[0] * 500000 + [1] * 500000"}, 1], True)],
      hints=["Search for a boundary, not a value. Let <code>hi = len(nums)</code> so 'none' is a valid answer.", "If <code>nums[mid] &lt; x</code> go right (<code>lo = mid + 1</code>); otherwise mid might be the answer, so <code>hi = mid</code>. Loop while <code>lo &lt; hi</code>."],
      solution=LOWER, explain="Halving a range of n + 1 positions: <b>O(log n)</b> time, <b>O(1)</b> space.",
      vid=[("Binary search, medium. The first position with a value at least x. With repeats.", [("b", "[1, 3, 3, 3, 8], x = 3: first 3 is at index 1")]),
           ("Now we're hunting a boundary, not a value. High starts at the length of the list, because 'none' is a real answer.", [("clear",), ("code", LOWER.splitlines()), ("hl", [1])]),
           ("Middle too small? The boundary is to the right. Low becomes mid plus one.", [("hl", [3, 4, 5])]),
           ("Otherwise, mid might be the answer, so keep it. High becomes mid. Not minus one.", [("hl", [6, 7])]),
           ("Low and high meet at the boundary. This one pattern solves first, last, insert position, all of them. Massive.", [("hl", [8]), ("cap", "Boundary search: lo < hi, hi = mid")])]),
 dict(level="Hard", title="Whole-number square root", func="int_sqrt",
      prompt="<p>Write <code>int_sqrt(n)</code> for <code>n &gt;= 0</code>. Return the largest whole number <code>r</code> with <code>r * r &lt;= n</code>, without using <code>**</code>, <code>math</code> or floats. Aim for O(log n).</p><p>Example: <code>int_sqrt(10)</code> returns <code>3</code>.</p>",
      starter="def int_sqrt(n):\n    pass\n",
      tests=[("given example", [10], False), ("perfect square", [49], False), ("zero", [0], True), ("one", [1], True), ("just below a square", [99], True), ("huge", [10 ** 18], True)],
      hints=["Binary search on the <b>answer</b>: the answer lies between 0 and n.", "If <code>mid * mid &lt;= n</code>, mid works, so <code>lo = mid</code>; else <code>hi = mid - 1</code>. Round mid up so the loop always moves."],
      solution=ISQRT, explain="The answer range halves each step: <b>O(log n)</b> time, <b>O(1)</b> space.",
      vid=[("Binary search, hard. Square root, whole number, no maths library. The largest r with r squared at most n.", [("b", "int_sqrt(10) is 3, because 3 × 3 = 9 ≤ 10 < 16")]),
           ("Here's the leap. There's no list. We binary search the answer itself, between zero and n.", [("clear",), ("code", ISQRT.splitlines()), ("hl", [1])]),
           ("Try the middle. If mid squared fits, mid works, and maybe something bigger does. Low becomes mid.", [("hl", [3, 4, 5])]),
           ("Too big? High becomes mid minus one. And round mid up, or low equals mid can loop forever.", [("hl", [3, 6, 7])]),
           ("Ten to the eighteen, about sixty steps. Binary search on the answer: a top tier trick. You're ready.", [("hl", [8]), ("cap", "No list? Binary search the answer.")])]),
]

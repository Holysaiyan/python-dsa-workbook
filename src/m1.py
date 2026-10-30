"""Module 1: Foundations."""

MODULE = {"id": "foundations", "title": "Foundations"}

LESSONS = []

# ---------------------------------------------------------------- 1
LESSONS.append({
    "id": "how-to-solve",
    "title": "How to solve a problem",
    "minutes": 15,
    "tags": ["Accenture", "Lloyds"],
    "summary": "A data structure is a way of storing data. An algorithm is a sequence of steps that solves a problem. Assessments test whether you can pick the right one for an unfamiliar problem.",
    "blocks": [
        ("p", "A <b>data structure</b> is a way of organising data so the operations you need are fast. A Python <code>list</code>, <code>set</code> and <code>dict</code> are all data structures, and each is fast at different things."),
        ("p", "An <b>algorithm</b> is a finite sequence of steps that turns an input into the output you want. Sorting a list, finding the shortest route between two stations and checking for a duplicate booking are all algorithms."),
        ("p", "Coding assessments rarely ask you to recite an algorithm. They give you a problem you have not seen and check whether your code returns the right answer on hidden tests, quickly enough. So the most useful skill is a reliable routine for starting."),
        ("h", "The six-step routine"),
        ("steps", [
            "<b>Restate it.</b> In one sentence: what goes in, what comes out, and any rules or limits.",
            "<b>Work one example by hand.</b> Use the example given, then invent a tiny one of your own.",
            "<b>Spot the pattern.</b> Ask: is it a filter, a count, a 'seen before' check, a search? (Later lessons build this list.)",
            "<b>Write the skeleton first.</b> Function header, an empty result, the loop, the return. The hard line comes last.",
            "<b>Test the edges.</b> Empty input, one item, duplicates, negatives, all equal, very large.",
            "<b>State the complexity.</b> One line: time and space, with a reason.",
        ]),
        ("h", "The skeleton most problems share"),
        ("p", "Most 'give me the items that...' problems have the same four lines. Write them before you think about the difficult part. The problem then shrinks to one question: what goes in the condition?"),
        ("code", """def needs_attention(rooms):
    result = []                 # 1. somewhere to collect answers
    for room in rooms:          # 2. look at each item
        if room["issues"] > 0:  # 3. the only line that changes per problem
            result.append(room["name"])  # 4. keep it
    return result

rooms = [
    {"name": "Flat 1", "issues": 0},
    {"name": "Flat 2", "issues": 3},
    {"name": "Flat 3", "issues": 1},
]
print(needs_attention(rooms))"""),
        ("h", "First one, or all of them?"),
        ("p", "Ask this before you write the loop. It decides where the <code>return</code> goes."),
        ("table", ["The task asks for", "Where to return", "Example"], [
            ["The <b>first</b> match", "<code>return</code> inside the loop, as soon as you find it", "First repeated booking reference"],
            ["<b>All</b> matches", "Collect into a list, <code>return</code> after the loop", "Every room needing attention"],
            ["<b>Whether</b> any match exists", "<code>return True</code> inside, <code>return False</code> after", "Is there any pair that sums to 10?"],
        ]),
        ("code", """def first_overdue(days_open):
    for i, days in enumerate(days_open):
        if days > 30:
            return i        # first one: stop straight away
    return -1               # nothing found

def all_overdue(days_open):
    result = []
    for i, days in enumerate(days_open):
        if days > 30:
            result.append(i)
    return result           # all of them: return after the loop

cases = [12, 45, 3, 31, 30]
print(first_overdue(cases))
print(all_overdue(cases))"""),
        ("tip", "If you are stuck at a blank screen, type the skeleton anyway. Seeing <code>result = []</code>, a loop and a <code>return</code> on screen usually unlocks the next line."),
    ],
    "mistakes": [
        "Starting to code before working an example by hand.",
        "Putting <code>return</code> inside the loop when the task asks for all matches.",
        "Returning <code>None</code> when nothing matches, when the task expects an empty list or <code>-1</code>.",
        "Changing the exact output the task asked for, such as returning items when it asked for positions.",
    ],
    "practice": {
        "title": "Rooms below standard",
        "prompt": "<p>Write <code>below_standard(scores, minimum)</code>. Return the <b>positions</b> of every inspection score that is <b>strictly below</b> <code>minimum</code>, in order.</p><p>Example: <code>below_standard([82, 64, 90, 70, 59], 70)</code> returns <code>[1, 4]</code>. A score equal to the minimum passes.</p>",
        "func": "below_standard",
        "starter": "def below_standard(scores, minimum):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [[82, 64, 90, 70, 59], 70], False),
            ("all pass", [[80, 90], 70], False),
            ("empty list", [[], 50], True),
            ("equal to minimum passes", [[70, 70, 69], 70], True),
            ("every score fails", [[1, 2, 3], 10], True),
            ("single item", [[5], 6], True),
        ],
        "hints": [
            "It asks for all matches and their positions. Which skeleton, and which loop gives you positions?",
            "Use <code>for i, score in enumerate(scores):</code> and append <code>i</code>, not <code>score</code>.",
        ],
        "solution": """def below_standard(scores, minimum):
    result = []
    for i, score in enumerate(scores):
        if score < minimum:
            result.append(i)
    return result
""",
        "explain": "One pass over the list: <b>O(n)</b> time. The result can hold every position: <b>O(n)</b> extra space in the worst case.",
    },
})

# ---------------------------------------------------------------- 2
LESSONS.append({
    "id": "big-o-time",
    "title": "Big O: time complexity",
    "minutes": 25,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Big O describes how the work your code does grows as the input grows. It is how you predict whether a correct solution will pass hidden tests on large inputs.",
    "blocks": [
        ("p", "Big O does not measure seconds. It measures how the <b>number of steps grows</b> as the input size, called <code>n</code>, grows. Two solutions can both be correct while one finishes instantly on a million items and the other runs for hours."),
        ("h", "Three conventions"),
        ("steps", [
            "<b>Worst case by default.</b> A search might find its target first time, but Big O describes the slowest possible run.",
            "<b>Drop constants.</b> Three loops one after another take 3n steps, written <b>O(n)</b>. Doubling a fast thing does not change how it grows.",
            "<b>Keep the biggest term.</b> n&sup2; + n + 5 is written <b>O(n&sup2;)</b>, because for large n the n&sup2; part swamps the rest.",
        ]),
        ("h", "The complexity ladder"),
        ("widget", "bigo"),
        ("table", ["Big O", "Name", "Typical cause", "Example"], [
            ["O(1)", "Constant", "A single step, whatever the size", "<code>x in a_set</code>, <code>lst[i]</code>, <code>len(lst)</code>"],
            ["O(log n)", "Logarithmic", "Halving what is left at every step", "Binary search on a sorted list"],
            ["O(n)", "Linear", "One loop over the input", "Finding the largest value"],
            ["O(n log n)", "Linearithmic", "Efficient sorting", "<code>sorted(lst)</code>, <code>lst.sort()</code>"],
            ["O(n&sup2;)", "Quadratic", "A loop inside a loop over the same data", "Checking every pair"],
            ["O(2<sup>n</sup>)", "Exponential", "Trying every combination", "Naive recursive Fibonacci"],
        ]),
        ("p", "As a rough guide, Python manages around 10 million simple steps per second. So for an input of a million items, O(n) and O(n log n) pass comfortably, while O(n&sup2;) needs a million million steps and times out."),
        ("h", "Why O(log n) is so fast"),
        ("p", "If every step halves what is left, a million items become 500,000, then 250,000, and reach 1 after about 20 steps. Doubling the input adds just one more step."),
        ("code", """n = 1_000_000
steps = 0
while n > 1:
    n = n // 2
    steps += 1
print(steps)"""),
        ("h", "How to work it out"),
        ("p", "Count how many times the most repeated step runs, as a function of n."),
        ("code", """def total(nums):            # O(n): one loop
    s = 0
    for x in nums:
        s += x
    return s

def has_pair_slow(nums, target):   # O(n^2): loop inside a loop
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

def two_passes(nums):      # O(n) + O(n) = O(2n), written O(n)
    smallest = min(nums)
    largest = max(nums)
    return largest - smallest

print(total([4, 1, 7]), has_pair_slow([4, 1, 7], 8), two_passes([4, 1, 7]))"""),
        ("h", "Two inputs need two letters"),
        ("p", "If a function takes a list of size n and another of size m, one loop over each in turn is <b>O(n + m)</b>. A loop over one inside a loop over the other is <b>O(n &times; m)</b>. Only write O(n&sup2;) when both loops run over the same data."),
        ("h", "Hidden loops"),
        ("p", "Some single lines of Python loop internally. Count them as loops. This is the trap most candidates miss."),
        ("table", ["Operation", "Cost", "Why"], [
            ["<code>x in my_list</code>", "<b>O(n)</b>", "Checks each item in turn"],
            ["<code>x in my_set</code>, <code>key in my_dict</code>", "O(1) on average", "Jumps straight to it using a hash"],
            ["<code>lst.append(x)</code>, <code>lst.pop()</code>", "O(1)", "Works at the end of the list"],
            ["<code>lst.pop(0)</code>, <code>lst.insert(0, x)</code>", "<b>O(n)</b>", "Every other item shifts along"],
            ["<code>min</code>, <code>max</code>, <code>sum</code>, <code>lst.index(x)</code>, <code>lst.count(x)</code>", "<b>O(n)</b>", "Scans the list"],
            ["<code>lst[a:b]</code>, <code>lst.copy()</code>", "O(k), k = items copied", "Builds a new list"],
            ["<code>sorted(lst)</code>, <code>lst.sort()</code>", "O(n log n)", "Sorting"],
            ["<code>s1 + s2</code> on strings", "O(len(s1) + len(s2))", "Builds a new string"],
        ]),
        ("code", """def common_slow(a, b):
    result = []
    for x in a:          # n times
        if x in b:       # b is a list: m steps each time
            result.append(x)
    return result        # O(n * m)

def common_fast(a, b):
    b_set = set(b)       # m steps, once
    result = []
    for x in a:          # n times
        if x in b_set:   # O(1) each time
            result.append(x)
    return result        # O(n + m)

print(common_fast(["R1", "R2", "R3"], ["R3", "R1"]))"""),
        ("tip", "In an interview, give the answer and the reason in one sentence: 'O(n), because there is one loop and each set lookup inside it is O(1).'"),
    ],
    "mistakes": [
        "Missing a hidden loop, such as <code>x in some_list</code> inside a loop.",
        "Writing O(n&sup2;) for two different inputs instead of O(n &times; m).",
        "Adding loops that run one after another as if they were nested.",
        "Saying 'fast' or 'efficient' instead of naming the complexity and the reason.",
    ],
    "practice": {
        "title": "Speed up a duplicate check",
        "prompt": "<p>The function below is correct but O(n&sup2;). Rewrite <code>has_duplicate(ids)</code> so it returns <code>True</code> if any ID appears more than once, in <b>O(n)</b> time.</p><pre class='inline-code'>def has_duplicate(ids):\n    for i in range(len(ids)):\n        for j in range(i + 1, len(ids)):\n            if ids[i] == ids[j]:\n                return True\n    return False</pre><p>The last test uses 20,000 IDs. The slow version may still pass here, so state your complexity in a comment.</p>",
        "func": "has_duplicate",
        "starter": "def has_duplicate(ids):\n    # aim for O(n)\n    pass\n",
        "tests": [
            ("duplicate present", [["A1", "B2", "A1"]], False),
            ("no duplicate", [["A1", "B2", "C3"]], False),
            ("empty list", [[]], True),
            ("single item", [["A1"]], True),
            ("duplicate at the very end", [{"__py__": "['ID' + str(i) for i in range(20000)] + ['ID0']"}], True),
            ("case matters", [["a1", "A1"]], True),
        ],
        "hints": [
            "Which structure answers 'have I seen this before?' in O(1)?",
            "Keep a <code>seen = set()</code>. Check before you add.",
        ],
        "solution": """def has_duplicate(ids):
    seen = set()
    for x in ids:
        if x in seen:
            return True
        seen.add(x)
    return False
# O(n) time, O(n) space for the set
""",
        "explain": "One loop with an O(1) set check inside: <b>O(n)</b> time. The set can hold all n IDs: <b>O(n)</b> space. You traded memory for speed, which is the most common optimisation in assessments.",
    },
})

# ---------------------------------------------------------------- 3
LESSONS.append({
    "id": "big-o-space",
    "title": "Big O: space complexity",
    "minutes": 15,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Space complexity applies the same reasoning to memory: how much extra storage your code needs as the input grows.",
    "blocks": [
        ("p", "Time complexity counts steps. Space complexity counts <b>extra memory</b>: the new lists, sets, dictionaries and strings your code creates while it runs. By convention you usually do not count the input itself, only what you add."),
        ("h", "Common space costs"),
        ("table", ["Your code creates", "Space"], [
            ["A few number or text variables (a counter, a running total)", "<b>O(1)</b>"],
            ["A list, set or dict that may hold one entry per input item", "<b>O(n)</b>"],
            ["A copy of the input, such as <code>sorted(lst)</code> or <code>lst[:]</code>", "<b>O(n)</b>"],
            ["An n &times; n grid", "<b>O(n&sup2;)</b>"],
            ["Recursion that goes n calls deep", "<b>O(n)</b> for the call stack"],
        ]),
        ("code", """def largest(nums):          # O(1) space: one variable
    best = nums[0]
    for x in nums:
        if x > best:
            best = x
    return best

def doubled(nums):          # O(n) space: a new list of n items
    return [x * 2 for x in nums]

def unique_count(nums):     # O(n) space: the set can hold every item
    return len(set(nums))

print(largest([3, 9, 2]), doubled([3, 9, 2]), unique_count([3, 9, 3]))"""),
        ("h", "In place versus a copy"),
        ("p", "<code>lst.sort()</code> sorts the list where it is and returns <code>None</code>. <code>sorted(lst)</code> builds a new sorted list, which costs O(n) extra space and leaves the original unchanged."),
        ("code", """a = [3, 1, 2]
b = sorted(a)      # new list
print(a, b)
a.sort()           # changes a itself
print(a)
print(a.sort())    # sort() returns None"""),
        ("h", "The time and space trade-off"),
        ("p", "Many optimisations spend memory to save time. A set that remembers what you have seen turns an O(n&sup2;) duplicate check into O(n) time, at the cost of O(n) space. In an interview, name the trade-off: 'This uses O(n) extra space to bring time down from O(n&sup2;) to O(n).'"),
        ("table", ["Approach", "Time", "Space"], [
            ["Compare every pair", "O(n&sup2;)", "O(1)"],
            ["Sort first, then compare neighbours", "O(n log n)", "O(n) for <code>sorted</code>, O(1) extra for <code>.sort()</code>"],
            ["Remember what you have seen in a set", "O(n)", "O(n)"],
        ]),
        ("tip", "When asked for complexity, always give both: 'O(n) time and O(n) space, because the set may store every item.'"),
    ],
    "mistakes": [
        "Forgetting that the result list counts as extra space.",
        "Calling a solution O(1) space when it builds a set or a sorted copy.",
        "Writing <code>lst = lst.sort()</code>, which sets <code>lst</code> to <code>None</code>.",
        "Forgetting the call stack when the solution is recursive.",
    ],
    "practice": {
        "title": "Largest gap in constant space",
        "prompt": "<p>Write <code>largest_gap(levels)</code>. Given at least two numbers, return the largest value of <code>levels[j] - levels[i]</code> where <code>j &gt; i</code> (a later reading minus an earlier one). The answer can be negative.</p><p>Use <b>O(n) time and O(1) extra space</b>: no new lists, no sorting.</p><p>Example: <code>largest_gap([7, 1, 5, 3, 6, 4])</code> returns <code>5</code> (6 minus 1).</p>",
        "func": "largest_gap",
        "starter": "def largest_gap(levels):\n    pass\n",
        "tests": [
            ("given example", [[7, 1, 5, 3, 6, 4]], False),
            ("only falls", [[9, 7, 4]], False),
            ("two items", [[1, 10]], True),
            ("all equal", [[3, 3, 3]], True),
            ("negatives", [[-5, -9, -2, -8]], True),
            ("best pair at the very end", [[5, 4, 3, 2, 1, 10]], True),
        ],
        "hints": [
            "Walk left to right. What single number about the past do you need to remember?",
            "Track the smallest value seen so far. At each new reading, the best gap ending here is reading minus that smallest value.",
        ],
        "solution": """def largest_gap(levels):
    smallest = levels[0]
    best = levels[1] - levels[0]
    for x in levels[1:]:
        if x - smallest > best:
            best = x - smallest
        if x < smallest:
            smallest = x
    return best
""",
        "explain": "One pass with two variables: <b>O(n)</b> time, <b>O(1)</b> extra space. Strictly, <code>levels[1:]</code> copies the list; looping over <code>range(1, len(levels))</code> avoids that copy if an interviewer asks.",
    },
})

# ---------------------------------------------------------------- 4
LESSONS.append({
    "id": "python-toolkit",
    "title": "Python toolkit",
    "minutes": 25,
    "tags": ["Accenture", "Lloyds"],
    "summary": "The Python details that cause most hidden-test failures: indexing and slicing, names versus copies, conditions, and looping with positions.",
    "blocks": [
        ("h", "Indexing and slicing"),
        ("p", "Positions start at 0. Negative indices count from the end. A slice <code>s[start:stop:step]</code> includes <code>start</code> and stops <b>before</b> <code>stop</code>."),
        ("code", """s = "engineer"
#    01234567
print(s[0], s[-1], s[-2])
print(s[1:4])      # positions 1, 2, 3
print(s[:3], s[5:])
print(s[::-1])     # reversed
print(s[::-1][1:3])  # reverse first, then slice"""),
        ("tip", "Chained operations run left to right. Do one at a time on paper: reverse, then index."),
        ("h", "Names, not boxes"),
        ("p", "A Python variable is a label pointing at an object. <code>b = a</code> does not copy a list: both names point at the same list. Use <code>a[:]</code>, <code>list(a)</code> or <code>a.copy()</code> for a new list."),
        ("code", """a = [1, 2]
b = a          # same list, two names
c = a[:]       # a new list
b.append(3)
c.append(4)
print(a, b, c)"""),
        ("p", "The same rule explains a famous trap: a default list argument is created once, when the function is defined, and shared by every call."),
        ("code", """def add_bad(x, items=[]):
    items.append(x)
    return items

def add_good(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items

print(add_bad(1), add_bad(2))
print(add_good(1), add_good(2))"""),
        ("h", "Conditions and membership"),
        ("p", "<code>in</code> and <code>not in</code> ask whether a thing is inside a collection. On a string they check for a substring. Every condition needs the thing, the operator and the collection."),
        ("code", """note = "urgent: boiler leak"
print("leak" in note)
print("fire" in note or "leak" in note)
print(("urgent" in note or "fire" in note) and "resolved" not in note)

# Trap: this is always True, because "fire" on its own counts as True
print(bool("fire" or "leak" in note))"""),
        ("h", "Looping with positions"),
        ("p", "<code>enumerate</code> gives you the position and the item on each pass. Use it only when you need positions."),
        ("code", """levels = ["red", "amber", "green"]
for i, level in enumerate(levels):
    print(i, level)

# zip walks two lists side by side
names = ["Flat 1", "Flat 2"]
scores = [88, 61]
for name, score in zip(names, scores):
    print(name, score)"""),
        ("h", "List comprehensions"),
        ("p", "A comprehension is a one-line filter or transform. It is the skeleton from lesson 1 written compactly."),
        ("code", """scores = [82, 64, 90, 70, 59]
passed = [s for s in scores if s >= 70]
positions = [i for i, s in enumerate(scores) if s < 70]
squares = [s * s for s in [1, 2, 3]]
print(passed, positions, squares)"""),
        ("h", "Integer maths"),
        ("code", """print(7 // 2, 7 % 2)     # floor division and remainder
print(-7 // 2)           # floors towards minus infinity
print(divmod(17, 5))     # (quotient, remainder)
print(int("42") + 1, str(42) + "!")
print(abs(-3), 0.1 + 0.2 == 0.3)   # floats are approximate"""),
        ("h", "Reading input on HackerRank"),
        ("p", "Some assessment questions give you a function to fill in. Others give you raw text on standard input. Practise both."),
        ("code", """# Pretend input: first line is n, second line is n numbers
import io, sys
sys.stdin = io.StringIO("5\\n3 8 1 9 4\\n")

n = int(input())
nums = list(map(int, input().split()))
print(n, nums, max(nums))"""),
    ],
    "mistakes": [
        "Expecting <code>b = a</code> to copy a list.",
        "Using a mutable default argument like <code>items=[]</code>.",
        "Writing <code>if 'fire' or 'leak' in note:</code>.",
        "Off-by-one slices: <code>s[1:4]</code> stops before position 4.",
        "Forgetting to convert input text to numbers with <code>int()</code>.",
    ],
    "practice": {
        "title": "Clean reference codes",
        "prompt": "<p>Write <code>clean_refs(refs)</code>. Each reference may have spaces around it and mixed case. Return a new list where each one is stripped of outer spaces and upper-cased, <b>skipping</b> any that are empty after stripping. Do not change the input list.</p><p>Example: <code>clean_refs([' ab12', 'CD34 ', '   ', 'ef56'])</code> returns <code>['AB12', 'CD34', 'EF56']</code>.</p>",
        "func": "clean_refs",
        "starter": "def clean_refs(refs):\n    pass\n",
        "tests": [
            ("given example", [[" ab12", "CD34 ", "   ", "ef56"]], False),
            ("already clean", [["AB12"]], False),
            ("empty list", [[]], True),
            ("only blanks", [["", "  "]], True),
            ("inner spaces kept", [[" a b "]], True),
            ("duplicates kept", [["x", "X"]], True),
        ],
        "hints": [
            "String methods: <code>.strip()</code> removes outer spaces, <code>.upper()</code> upper-cases.",
            "Filter skeleton: clean each one, keep it only if the cleaned text is not empty.",
        ],
        "solution": """def clean_refs(refs):
    result = []
    for r in refs:
        cleaned = r.strip().upper()
        if cleaned:
            result.append(cleaned)
    return result
""",
        "explain": "One pass: <b>O(n &times; L)</b> time where L is the reference length, effectively O(n) for short codes. The new list is <b>O(n)</b> space.",
    },
})

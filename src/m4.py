"""Module 4: Recursion, searching and sorting."""

MODULE = {"id": "search-sort", "title": "Recursion, searching and sorting"}

LESSONS = []

# ---------------------------------------------------------------- recursion
LESSONS.append({
    "id": "recursion",
    "title": "Recursion",
    "minutes": 20,
    "tags": [],
    "summary": "A recursive function solves a problem by calling itself on a smaller version of it. Trees, graphs and many divide-and-conquer algorithms are easiest to write this way.",
    "blocks": [
        ("p", "Every recursive function needs two parts:"),
        ("steps", [
            "<b>A base case</b> that answers the smallest version directly, without recursing.",
            "<b>A recursive case</b> that shrinks the problem and calls the function on the smaller piece.",
        ]),
        ("code", """def countdown(n):
    if n == 0:                 # base case
        print("go")
        return
    print(n)
    countdown(n - 1)           # smaller problem

countdown(3)"""),
        ("code", """def total(nums):
    if not nums:               # base case: empty list sums to 0
        return 0
    return nums[0] + total(nums[1:])

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(total([4, 1, 7]), factorial(5))"""),
        ("h", "The call stack"),
        ("p", "Each call waits on the one below it. Python stores these waiting calls on the <b>call stack</b>, so recursion n levels deep uses O(n) space. Python stops at about 1,000 levels by default, so deep recursion on large inputs fails with <code>RecursionError</code>."),
        ("h", "Repeated work, and memoisation"),
        ("p", "Naive Fibonacci calls itself twice per level, recomputing the same values again and again: O(2<sup>n</sup>). Remembering answers you have already computed (<b>memoisation</b>) brings it down to O(n)."),
        ("code", """calls = 0
def fib_slow(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

memo = {}
def fib_fast(n):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_fast(n - 1) + fib_fast(n - 2)
    return memo[n]

print(fib_slow(20), calls)
print(fib_fast(80))"""),
        ("tip", "If a problem is defined in terms of smaller copies of itself (a folder containing folders, a tree of managers), think recursion first."),
    ],
    "mistakes": [
        "No base case, or a base case that is never reached: infinite recursion.",
        "Forgetting to <code>return</code> the recursive call's result.",
        "Recomputing the same sub-problems without memoisation.",
        "Using recursion 10,000 levels deep in Python. Use a loop instead.",
    ],
    "practice": {
        "title": "Count nested items",
        "prompt": "<p>Write <code>count_items(data)</code>. <code>data</code> is a list whose elements are either strings or further lists, nested to any depth. Return the total number of strings.</p><p>Example: <code>count_items(['a', ['b', 'c', ['d']], [], 'e'])</code> returns <code>5</code>.</p>",
        "func": "count_items",
        "starter": "def count_items(data):\n    pass\n",
        "tests": [
            ("given example", [["a", ["b", "c", ["d"]], [], "e"]], False),
            ("flat list", [["x", "y"]], False),
            ("empty", [[]], True),
            ("only empty lists", [[[], [[]]]], True),
            ("deep nesting", [[[[[["deep"]]]]]], True),
        ],
        "hints": [
            "Base case: a string counts as 1. Recursive case: a list's count is the sum of its elements' counts.",
            "Use <code>isinstance(x, list)</code> to tell lists from strings.",
        ],
        "solution": """def count_items(data):
    count = 0
    for x in data:
        if isinstance(x, list):
            count += count_items(x)
        else:
            count += 1
    return count
""",
        "explain": "Every element is visited once: <b>O(n)</b> time for n elements in total. The call stack grows with nesting depth d: <b>O(d)</b> space.",
    },
})

# ---------------------------------------------------------------- binary search
LESSONS.append({
    "id": "binary-search",
    "title": "Binary search",
    "minutes": 20,
    "tags": ["Accenture"],
    "summary": "On sorted data, check the middle and throw away the half that cannot contain the answer. Each step halves the search: O(log n).",
    "blocks": [
        ("p", "<b>Linear search</b> checks items one by one: O(n). If the data is <b>sorted</b>, <b>binary search</b> compares the target with the middle item and discards half the list each time: O(log n). A million items take about 20 comparisons."),
        ("code", """def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1        # answer is to the right
        else:
            hi = mid - 1        # answer is to the left
    return -1

data = [2, 5, 8, 12, 16, 23, 38]
print(binary_search(data, 23), binary_search(data, 7))"""),
        ("h", "Searching for a boundary"),
        ("p", "Often the question is not 'where is x' but 'where is the first item that meets a condition'. Python's <code>bisect</code> module does this for sorted lists."),
        ("code", """import bisect

times = [900, 930, 1000, 1000, 1100]
print(bisect.bisect_left(times, 1000))   # first position >= 1000
print(bisect.bisect_right(times, 1000))  # first position > 1000
print(bisect.bisect_left(times, 1200))   # past the end"""),
        ("h", "Binary search on the answer"),
        ("p", "If you can test 'is x big enough?' and the answer flips from no to yes exactly once as x grows, you can binary search over x itself."),
        ("code", """def smallest_capacity(loads, days):
    def fits(cap):
        used, current = 1, 0
        for w in loads:
            if current + w > cap:
                used += 1
                current = 0
            current += w
        return used <= days

    lo, hi = max(loads), sum(loads)
    while lo < hi:
        mid = (lo + hi) // 2
        if fits(mid):
            hi = mid          # mid works, try smaller
        else:
            lo = mid + 1      # mid too small
    return lo

print(smallest_capacity([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))"""),
    ],
    "mistakes": [
        "Running binary search on unsorted data.",
        "Infinite loops from <code>lo = mid</code> when the loop condition is <code>lo &lt; hi</code>.",
        "Off-by-one: decide whether <code>hi</code> is inclusive and stay consistent.",
    ],
    "practice": {
        "title": "First late arrival",
        "prompt": "<p>Write <code>first_late(arrivals, deadline)</code>. <code>arrivals</code> is sorted in increasing order. Return the position of the first arrival <b>strictly after</b> <code>deadline</code>, or <code>len(arrivals)</code> if none are late. Aim for O(log n), without using <code>bisect</code>.</p><p>Example: <code>first_late([900, 915, 930, 1000], 915)</code> returns <code>2</code>.</p>",
        "func": "first_late",
        "starter": "def first_late(arrivals, deadline):\n    pass\n",
        "tests": [
            ("given example", [[900, 915, 930, 1000], 915], False),
            ("nobody late", [[800, 850], 900], False),
            ("everyone late", [[930, 940], 900], True),
            ("empty", [[], 900], True),
            ("duplicates on the deadline", [[900, 900, 900, 901], 900], True),
            ("large list", [{"__py__": "list(range(0, 200000, 2))"}, 99999], True),
        ],
        "hints": [
            "Search for a boundary. Keep <code>lo = 0</code> and <code>hi = len(arrivals)</code> (one past the end).",
            "If <code>arrivals[mid] &gt; deadline</code>, the answer is at mid or to its left: <code>hi = mid</code>. Otherwise <code>lo = mid + 1</code>. Loop while <code>lo &lt; hi</code>.",
        ],
        "solution": """def first_late(arrivals, deadline):
    lo, hi = 0, len(arrivals)
    while lo < hi:
        mid = (lo + hi) // 2
        if arrivals[mid] > deadline:
            hi = mid
        else:
            lo = mid + 1
    return lo
""",
        "explain": "Each step halves the range: <b>O(log n)</b> time and <b>O(1)</b> space. This is exactly what <code>bisect.bisect_right</code> computes.",
    },
    "related": [("LeetCode: Binary Search", "https://leetcode.com/problems/binary-search/")],
})

# ---------------------------------------------------------------- sorting
LESSONS.append({
    "id": "sorting",
    "title": "Sorting algorithms",
    "minutes": 30,
    "tags": ["Accenture"],
    "summary": "How the classic sorts work, what they cost, and how to sort anything in Python with a key function.",
    "blocks": [
        ("p", "In assessments you will almost always call <code>sorted()</code>, which runs in O(n log n). Knowing how the classic algorithms work still matters: interviewers ask about them, and their ideas reappear in other problems."),
        ("h", "Sorting in Python"),
        ("code", """flats = [("Flat 3", 690), ("Flat 1", 650), ("Flat 2", 720), ("Flat 4", 650)]

print(sorted(flats))                                   # by name, then rent
print(sorted(flats, key=lambda f: f[1]))               # by rent
print(sorted(flats, key=lambda f: f[1], reverse=True)) # rent, high first
print(sorted(flats, key=lambda f: (-f[1], f[0])))      # rent high first, ties by name"""),
        ("p", "Python's sort is <b>stable</b>: items that compare equal keep their original order. That is why Flat 1 stays ahead of Flat 4 when sorting by rent above."),
        ("h", "Bubble sort"),
        ("p", "Repeatedly swap neighbours that are in the wrong order. After each pass the largest remaining item has 'bubbled' to the end. O(n&sup2;)."),
        ("code", """def bubble_sort(a):
    a = a[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:         # already sorted: stop early
            break
    return a

print(bubble_sort([5, 1, 4, 2, 8]))"""),
        ("h", "Insertion sort"),
        ("p", "Build a sorted section at the front. Take the next item and slide it left into place, like sorting a hand of cards. O(n&sup2;) in general, but fast on nearly sorted data."),
        ("code", """def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        item = a[i]
        j = i - 1
        while j >= 0 and a[j] > item:
            a[j + 1] = a[j]      # shift right
            j -= 1
        a[j + 1] = item
    return a

print(insertion_sort([5, 1, 4, 2, 8]))"""),
        ("h", "Merge sort"),
        ("p", "Divide and conquer: split the list in half, sort each half recursively, then merge the two sorted halves. Always O(n log n), using O(n) extra space."),
        ("code", """def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))"""),
        ("h", "Quick sort"),
        ("p", "Pick a <b>pivot</b>, split the rest into smaller and larger items, and sort each side recursively. O(n log n) on average, O(n&sup2;) in the worst case."),
        ("code", """def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    smaller = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    larger = [x for x in a if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)

print(quick_sort([3, 6, 8, 10, 1, 2, 1]))"""),
        ("h", "Comparison"),
        ("table", ["Algorithm", "Best", "Average", "Worst", "Extra space", "Stable"], [
            ["Bubble", "O(n)", "O(n&sup2;)", "O(n&sup2;)", "O(1)", "Yes"],
            ["Insertion", "O(n)", "O(n&sup2;)", "O(n&sup2;)", "O(1)", "Yes"],
            ["Merge", "O(n log n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"],
            ["Quick", "O(n log n)", "O(n log n)", "O(n&sup2;)", "O(log n) in place", "No"],
            ["Python <code>sorted</code> (Timsort)", "O(n)", "O(n log n)", "O(n log n)", "O(n)", "Yes"],
        ]),
        ("tip", "Sorting first often simplifies a problem: duplicates become neighbours, and two pointers start to work."),
    ],
    "mistakes": [
        "Writing <code>lst = lst.sort()</code>, which stores <code>None</code>.",
        "Sorting strings that hold numbers: <code>'10' &lt; '9'</code> is True. Convert with <code>key=int</code>.",
        "Forgetting that sorting costs O(n log n) when stating your complexity.",
    ],
    "practice": {
        "title": "Rank the repair jobs",
        "prompt": "<p>Write <code>rank_jobs(jobs)</code>. Each job is a list <code>[name, priority, days_waiting]</code>. Return the job <b>names</b> ordered by priority (1 is most urgent first), then by days waiting (longest first), then by name alphabetically.</p><p>Example: <code>rank_jobs([['boiler', 2, 5], ['leak', 1, 1], ['lock', 2, 9]])</code> returns <code>['leak', 'lock', 'boiler']</code>.</p>",
        "func": "rank_jobs",
        "starter": "def rank_jobs(jobs):\n    pass\n",
        "tests": [
            ("given example", [[["boiler", 2, 5], ["leak", 1, 1], ["lock", 2, 9]]], False),
            ("single job", [[["damp", 3, 0]]], False),
            ("empty", [[]], True),
            ("full tie broken by name", [[["b", 1, 1], ["a", 1, 1]]], True),
            ("waiting breaks priority ties", [[["x", 1, 2], ["y", 1, 8]]], True),
        ],
        "hints": [
            "Use <code>sorted</code> with a key that returns a tuple. Tuples compare item by item.",
            "To sort a number high-to-low inside an otherwise ascending tuple, negate it: <code>(job[1], -job[2], job[0])</code>.",
        ],
        "solution": """def rank_jobs(jobs):
    ordered = sorted(jobs, key=lambda j: (j[1], -j[2], j[0]))
    return [j[0] for j in ordered]
""",
        "explain": "Sorting dominates: <b>O(n log n)</b> time and <b>O(n)</b> space for the sorted copy and the name list.",
    },
})

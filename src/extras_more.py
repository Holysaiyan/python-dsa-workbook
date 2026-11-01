"""Mastery material for the Python basics module and the Housing Desk project."""

T_STD = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n\u00b2)"]
S_STD = ["O(1)", "O(log n)", "O(n)", "O(n\u00b2)"]
BUG = "This version passes some tests and fails others. Find the bug and fix it."

EXTRAS_MORE = {}

EXTRAS_MORE["py-values"] = {
    "limit": 4,
    "complexity": {"time": ["O(1)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD, "why": "Two arithmetic operations, however big the numbers are."},
    "quiz": [
        {"q": "What does this print?", "code": "print(7 // 2, 7 % 2, 7 / 2)", "options": ["@run", "3.5 1 3.5", "3 1 3", "4 1 3.5"], "why": "<code>//</code> rounds down to 3, <code>%</code> is the remainder 1, <code>/</code> always gives a float."},
        {"q": "What does this print?", "code": "x = 5\nx = x * 2\nx += 1\nprint(x)", "options": ["@run", "10", "6", "5"], "why": "x becomes 10, then 11. <code>=</code> means 'becomes'."},
        {"q": "Which line crashes?", "options": ["print(f\"Age: {21}\")", "print(\"Age: \" + 21)", "print(\"Age:\", 21)"], "answer": 1, "why": "You cannot add text and a number with <code>+</code>. f-strings and commas in print both work."},
        {"q": "How do you check whether n is even?", "options": ["n / 2 == 0", "n % 2 == 0", "n // 2 == 0"], "answer": 1, "why": "Even numbers leave remainder 0 when divided by 2."},
    ],
    "debug": {"intro": BUG, "starter": "def split_bill(total_pence, people):\n    return [total_pence / people, total_pence % people]\n", "hint": "The share must be a whole number. Which division gives one?"},
}

EXTRAS_MORE["py-strings"] = {
    "limit": 6,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "split walks the whole string once, and the words it returns take space proportional to the string."},
    "quiz": [
        {"q": "What does this print?", "code": "s = \"python\"\nprint(s[1:4])", "options": ["@run", "pyth", "ytho", "pyt"], "why": "Index 1 up to, but not including, 4: y, t, h."},
        {"q": "What does this print?", "code": "s = \"hi\"\ns.upper()\nprint(s)", "options": ["@run", "HI", "None", "Hi"], "why": "Strings cannot change. <code>upper()</code> returned a new string that was thrown away."},
        {"q": "What does this print?", "code": "print(\"a  b\".split(\" \"))", "options": ["@run", "['a', 'b']", "['a  b']", "['a', ' ', 'b']"], "why": "Splitting on one space leaves an empty string between the two spaces. <code>split()</code> would give ['a', 'b']."},
        {"q": "What does this print?", "code": "print(\"-\".join([\"a\", \"b\", \"c\"]))", "options": ["@run", "['a-b-c']", "-a-b-c-", "abc"], "why": "<code>join</code> puts the separator between items."},
    ],
    "debug": {"intro": BUG, "starter": "def initials(full_name):\n    result = \"\"\n    for word in full_name.split(\" \"):\n        result += word[0].upper()\n    return result\n", "hint": "Try the name with extra spaces. What does <code>split(\" \")</code> give for two spaces in a row?"},
}

EXTRAS_MORE["py-conditions"] = {
    "limit": 6,
    "complexity": {"time": ["O(1)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD, "why": "A fixed number of comparisons."},
    "quiz": [
        {"q": "What does this print?", "code": "x = 75\nif x >= 40:\n    print(\"Pass\")\nelif x >= 70:\n    print(\"First\")", "options": ["@run", "First", "Pass then First", "Nothing"], "why": "The first true branch wins. 75 is at least 40, so 'First' is never reached. Order checks strictest first."},
        {"q": "What does this print?", "code": "items = []\nif items:\n    print(\"full\")\nelse:\n    print(\"empty\")", "options": ["@run", "full", "[]", "Error"], "why": "An empty list counts as False."},
        {"q": "What does <code>if x == 1 or 2:</code> do?", "options": ["Checks whether x is 1 or 2", "Is always true, because 2 on its own counts as True", "Is a syntax error"], "answer": 1, "why": "It reads as <code>(x == 1) or 2</code>. Write <code>x in (1, 2)</code>."},
    ],
    "debug": {"intro": BUG, "starter": "def classify(mark):\n    if mark >= 40:\n        return \"Third\"\n    elif mark >= 50:\n        return \"2:2\"\n    elif mark >= 60:\n        return \"2:1\"\n    elif mark >= 70:\n        return \"First\"\n    return \"Fail\"\n", "hint": "Which branch does a mark of 72 hit first?"},
}

EXTRAS_MORE["py-loops"] = {
    "limit": 6,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "One pass, and the result holds one total per item."},
    "quiz": [
        {"q": "What does this print?", "code": "print(list(range(1, 5)))", "options": ["@run", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3, 4]", "[2, 3, 4]"], "why": "range stops before the stop value."},
        {"q": "What does this print?", "code": "total = 0\nfor n in [1, 2, 3]:\n    total = 0\n    total += n\nprint(total)", "options": ["@run", "6", "0", "1"], "why": "The total is reset every time round the loop, so only the last item survives. Set it up before the loop."},
        {"q": "What does this print?", "code": "for i, ch in enumerate(\"ab\"):\n    print(i, ch)", "options": ["@run", "a 0\nb 1", "1 a\n2 b", "0 1"], "why": "enumerate gives (position, value), starting at 0."},
        {"q": "What does this print?", "code": "n = 0\nwhile n < 10:\n    n += 4\nprint(n)", "options": ["@run", "10", "8", "4"], "why": "n goes 4, 8, 12. At 12 the condition is False and the loop stops."},
    ],
    "debug": {"intro": BUG, "starter": "def running_total(amounts):\n    result = []\n    for x in amounts:\n        total = 0\n        total += x\n        result.append(total)\n    return result\n", "hint": "Where is <code>total</code> set to 0? It should happen once."},
}

EXTRAS_MORE["py-lists"] = {
    "limit": 5,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "One pass, and the new list can hold up to n squares."},
    "quiz": [
        {"q": "What does this print?", "code": "nums = [3, 1, 2]\nnums = nums.sort()\nprint(nums)", "options": ["@run", "[1, 2, 3]", "[3, 1, 2]", "Error"], "why": "<code>sort()</code> sorts in place and returns None, which then replaced the list."},
        {"q": "What does this print?", "code": "a = [1, 2]\nb = a\nb.append(3)\nprint(a)", "options": ["@run", "[1, 2]", "[3]", "[1, 2, 3, 3]"], "why": "a and b are the same list. Copy with <code>a[:]</code>."},
        {"q": "What does this print?", "code": "print([n * 10 for n in [1, 2, 3, 4] if n > 2])", "options": ["@run", "[10, 20]", "[3, 4]", "[10, 20, 30, 40]"], "why": "Keep n above 2 (3 and 4), then multiply by 10."},
        {"q": "What does this print?", "code": "xs = [5, 6, 7]\nprint(xs[-1], xs.pop(0), xs)", "options": ["@run", "7 7 [5, 6]", "5 5 [6, 7]", "7 5 [5, 6, 7]"], "why": "-1 is the last item. <code>pop(0)</code> removes and returns the first."},
    ],
    "debug": {"intro": BUG, "starter": "def even_squares(nums):\n    return [n * n for n in nums if n % 2]\n", "hint": "<code>n % 2</code> is 1 for odd numbers, which counts as True. Which numbers does this keep?"},
}

EXTRAS_MORE["py-functions"] = {
    "limit": 6,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD, "why": "One pass with two variables."},
    "quiz": [
        {"q": "What does this print?", "code": "def f(x):\n    print(x * 2)\n\ny = f(3)\nprint(y)", "options": ["@run", "6\n6", "6", "None"], "why": "f prints 6 but returns nothing, so y is None."},
        {"q": "What does this print?", "code": "def p(n, rate=10):\n    return n * rate\n\nprint(p(2), p(2, 3))", "options": ["@run", "20 20", "6 6", "2 6"], "why": "The default rate is used when you leave it out."},
        {"q": "What does this print?", "code": "def f():\n    return 1\n    return 2\n\nprint(f())", "options": ["@run", "2", "1 2", "None"], "why": "A function stops at the first return it reaches."},
        {"q": "An assessment asks you to write <code>count_vowels(s)</code>. What should the function do with the answer?", "options": ["print it", "return it", "both print and return it"], "answer": 1, "why": "The checker calls your function and compares the returned value. Extra printing can even break some checkers."},
    ],
    "debug": {"intro": BUG, "starter": "def min_max(nums):\n    lo = nums[0]\n    hi = 0\n    for n in nums:\n        if n < lo:\n            lo = n\n        if n > hi:\n            hi = n\n    return [lo, hi]\n", "hint": "What happens when every number is negative?"},
}

EXTRAS_MORE["py-collections"] = {
    "limit": 6,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "One pass with O(1) dictionary updates; up to one key per item."},
    "quiz": [
        {"q": "What does this print?", "code": "d = {\"a\": 1}\nprint(d.get(\"b\", 0), \"a\" in d)", "options": ["@run", "None True", "0 False", "Error"], "why": "<code>get</code> returns the default for a missing key; <code>in</code> checks keys."},
        {"q": "What type is <code>x = {}</code>?", "options": ["set", "dict", "list"], "answer": 1, "why": "Empty curly braces make a dict. An empty set is <code>set()</code>."},
        {"q": "What does this print?", "code": "s = set([3, 1, 3, 2, 1])\nprint(len(s))", "options": ["@run", "5", "2", "1"], "why": "A set keeps one copy of each value: 1, 2 and 3."},
        {"q": "What does this print?", "code": "a, b = 1, 2\na, b = b, a\nprint(a, b)", "options": ["@run", "1 2", "2 2", "1 1"], "why": "Tuple unpacking swaps both at once."},
    ],
    "debug": {"intro": BUG, "starter": "def totals_by_category(spend):\n    totals = {}\n    for category, amount in spend:\n        totals[category] = amount\n    return totals\n", "hint": "The second 'food' replaces the first. You need to add to what is already there."},
}

EXTRAS_MORE["py-classes"] = {
    "limit": 6,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD, "why": "Each node is visited once, using one total and one pointer."},
    "quiz": [
        {"q": "What does this print?", "code": "class C:\n    def __init__(self, n):\n        self.n = n\n    def double(self):\n        return self.n * 2\n\nprint(C(4).double())", "options": ["@run", "4", "Error: double needs an argument", "None"], "why": "Python passes the object as <code>self</code> automatically."},
        {"q": "What does this print?", "code": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\nh = Node(1, Node(2))\nprint(h.next.val, h.next.next)", "options": ["@run", "1 2", "2 2", "Error"], "why": "The second node has no next, so it is None."},
        {"q": "Inside <code>__init__</code>, what is wrong with <code>name = name</code>?", "options": ["Nothing", "It sets a local variable and the object never stores the name; it should be self.name = name", "It is a syntax error"], "answer": 1, "why": "Attributes live on <code>self</code>."},
    ],
    "debug": {"intro": BUG, "starter": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\ndef chain_total(head):\n    total = 0\n    cur = head\n    while cur.next is not None:\n        total += cur.val\n        cur = cur.next\n    return total\n", "hint": "Does the last node get added? And what happens if the chain is empty?"},
}

EXTRAS_MORE["project-brief"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "Every line is split and checked once; the records take space proportional to the input."},
    "quiz": [
        {"q": "What does this print?", "code": "print(len(\"a,b,c,d,e\".split(\",\", 3)))", "options": ["@run", "5", "3", "2"], "why": "At most 3 splits makes at most 4 parts. The last part keeps its commas: 'd,e'."},
        {"q": "What does this print?", "code": "print(\"12\".isdigit(), \"-3\".isdigit(), \" 4\".isdigit())", "options": ["@run", "True True True", "True True False", "False False False"], "why": "isdigit is only true when every character is a digit, so a minus sign or a space fails. Strip first."},
        {"q": "Why check <code>isdigit()</code> before <code>int()</code>?", "options": ["It is faster", "int() crashes on text like 'high', so the check lets you skip the line instead", "int() cannot handle numbers above 5"], "answer": 1, "why": "Validate first, convert second."},
    ],
    "debug": {"intro": BUG, "starter": "def parse_requests(lines):\n    requests = []\n    for line in lines:\n        parts = line.split(\",\")\n        if len(parts) != 4:\n            continue\n        rid, room, pri, issue = [p.strip() for p in parts]\n        if not pri.isdigit() or not 1 <= int(pri) <= 5:\n            continue\n        requests.append([rid, room, int(pri), issue])\n    return requests\n", "hint": "Try 'broken lock, urgent'. How many parts does a plain <code>split(\",\")</code> make?"},
}

EXTRAS_MORE["project-busiest"] = {
    "limit": 10,
    "complexity": {"time": ["O(n log n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "Counting is O(n) and sorting the rooms is O(n log n) at worst."},
    "quiz": [
        {"q": "What does this print?", "code": "c = {\"B\": 2, \"A\": 2, \"C\": 5}\nprint(sorted(c, key=lambda r: (-c[r], r)))", "options": ["@run", "['A', 'B', 'C']", "['C', 'B', 'A']", "['B', 'A', 'C']"], "why": "Most first (C has 5), then the tie between A and B goes alphabetically."},
        {"q": "What does <code>key=lambda r: -counts[r]</code> do?", "options": ["Sorts rooms with the most requests first", "Removes rooms", "Sorts rooms alphabetically backwards"], "answer": 0, "why": "Sorting minus the count puts the biggest count first."},
        {"q": "What does this print?", "code": "print(sorted([\"b\", \"a\", \"c\"])[:5])", "options": ["@run", "Error: only 3 items", "['a', 'b', 'c', None, None]", "['c', 'b', 'a']"], "why": "Slicing past the end just stops at the end. No error."},
    ],
    "debug": {"intro": BUG, "starter": "def busiest_rooms(requests, k):\n    counts = {}\n    for rid, room, pri, issue in requests:\n        counts[room] = counts.get(room, 0) + 1\n    ranked = sorted(counts, key=lambda room: -counts[room])\n    return ranked[:k]\n", "hint": "Two rooms have the same count. What decides their order?"},
}

EXTRAS_MORE["project-next-jobs"] = {
    "limit": 10,
    "complexity": {"time": ["O(n log n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD, "why": "n heap pushes and up to n pops, each O(log n); the heap holds every request."},
    "quiz": [
        {"q": "What does this print?", "code": "import heapq\nh = []\nfor item in [(2, 0, \"R1\"), (1, 1, \"R2\"), (1, 2, \"R3\")]:\n    heapq.heappush(h, item)\nprint(heapq.heappop(h)[2])", "options": ["@run", "R1", "R3", "1"], "why": "Smallest tuple first: priority 1, and of those, order 1 before order 2."},
        {"q": "Why include the arrival order in the tuple?", "options": ["Heaps need three items", "So equal priorities come out oldest first, not by ID text", "To make it faster"], "answer": 1, "why": "Tuples compare item by item; the order number breaks ties the way the brief asks."},
        {"q": "Taking the next job and adding new ones, again and again: why a heap rather than sorting each time?", "options": ["A heap does each add or take in O(log n); re-sorting costs O(n log n) every time", "Sorting is not allowed", "A heap uses less memory"], "answer": 0, "why": "That is the job a heap is built for."},
    ],
    "debug": {"intro": BUG, "starter": "import heapq\n\ndef next_jobs(requests, k):\n    heap = []\n    for order, (rid, room, pri, issue) in enumerate(requests):\n        heapq.heappush(heap, (pri, rid, order))\n    return [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]\n", "hint": "For two jobs with the same priority, what is compared next in this tuple?"},
}

EXTRAS_MORE["project-find"] = {
    "limit": 8,
    "complexity": {"time": ["O(log n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD, "why": "The range halves every step, using a few variables."},
    "quiz": [
        {"q": "What does this print?", "code": "print(\"R10\" < \"R9\", \"R0010\" < \"R0009\")", "options": ["@run", "False False", "True True", "False True"], "why": "Text compares character by character, so '1' beats '9'. Padding to the same length fixes the order."},
        {"q": "About how many steps does binary search need for 4,000 IDs?", "options": ["12", "2,000", "4,000"], "answer": 0, "why": "2 to the power 12 is 4,096, so about 12 halvings."},
        {"q": "Which loop condition is correct for this binary search?", "options": ["while lo < hi:", "while lo <= hi:", "while mid != target:"], "answer": 1, "why": "With <code>&lt;</code>, a range of one item is never checked."},
    ],
    "debug": {"intro": BUG, "starter": "def find_request(ids, target):\n    lo, hi = 0, len(ids) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if ids[mid] == target:\n            return mid\n        if ids[mid] < target:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return -1\n", "hint": "Search a one-item list for its only item. Does the loop run at all?"},
}

EXTRAS_MORE["project-together"] = {
    "quiz": [
        {"q": "The desk can find a request by ID with a dict or with binary search. Which is faster for a single lookup?", "options": ["The dict: O(1) on average", "Binary search: O(log n)", "They are the same"], "answer": 0, "why": "Binary search earns its place for ranges and ordered queries, not single lookups."},
        {"q": "An interviewer asks why you used a heap for next jobs. Best answer?", "options": ["Heaps are advanced", "Jobs keep arriving and I always need the most urgent one; a heap adds and removes in O(log n) instead of re-sorting", "The tutorial used one"], "answer": 1, "why": "Tie the structure to the operation you need most, and give the Big O."},
        {"q": "What should a two-minute project explanation include?", "options": ["Every line of code", "What it does, why each data structure, the Big O, a bug you fixed, and what you would add next", "Only the features"], "answer": 1, "why": "Interviewers listen for decisions and trade-offs."},
    ],
}

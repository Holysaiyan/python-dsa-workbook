"""Mastery material keyed by lesson id: quiz questions, a bug to fix, the complexity gate, a time target.

Quiz option "@run" means: the correct answer is whatever the question's code prints (filled in and checked at build time).
"""

T_STD = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n\u00b2)"]
S_STD = ["O(1)", "O(log n)", "O(n)", "O(n\u00b2)"]

EXTRAS = {}

EXTRAS["how-to-solve"] = {
    "limit": 8,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "One loop over the scores, and the result list can hold every position."},
    "quiz": [
        {"q": "A task says: <i>return the first booking that is overdue</i>. Where does the <code>return</code> go?",
         "options": ["Inside the loop, as soon as a match is found", "After the loop, once every booking has been checked", "In both places"], "answer": 0,
         "why": "'First' means stop as soon as you find one. 'All' means collect, then return after the loop."},
        {"q": "What does this print?", "code": "def f(xs):\n    for x in xs:\n        if x > 2:\n            return x\n    return -1\n\nprint(f([1, 5, 9]))",
         "options": ["@run", "9", "[5, 9]", "-1"], "why": "The return inside the loop fires on the first value above 2, which is 5. The 9 is never reached."},
        {"q": "A function should return every position whose value is negative. When nothing is negative it returns <code>None</code>. What is wrong?",
         "options": ["Nothing: None is the natural empty result", "It should return an empty list, because the task expects a list", "It should return -1"], "answer": 1,
         "why": "Hidden tests check the type as well as the value. 'A list of positions' with no matches is <code>[]</code>."},
        {"q": "Which set of inputs should you run before submitting a function that takes a list?",
         "options": ["Only the example given in the task", "The example, an empty list, a single item, and duplicates or extremes if they are allowed", "Only a very large input"], "answer": 1,
         "why": "Hidden tests are built from exactly those edges. Running them yourself is how you find out before the marker does."},
    ],
    "debug": {
        "intro": "This version passes the first test and fails the rest. Find the one-line bug and fix it.",
        "starter": "def below_standard(scores, minimum):\n    result = []\n    for i, score in enumerate(scores):\n        if score < minimum:\n            result.append(i)\n            return result\n    return result\n",
        "hint": "The task asks for <b>all</b> positions. Where is the <code>return</code> sitting?",
    },
}

EXTRAS["big-o-time"] = {
    "limit": 8,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "One loop with an O(1) set check inside; the set may hold every ID."},
    "quiz": [
        {"q": "What is the time complexity of this function?", "code": "def pairs(xs):\n    out = 0\n    for a in xs:\n        for b in xs:\n            out += 1\n    return out",
         "options": ["O(n)", "O(n\u00b2)", "O(2n)", "O(log n)"], "answer": 1, "why": "For each of the n values of <code>a</code>, the inner loop runs n times: n &times; n."},
        {"q": "<code>for x in a: if x in b: ...</code>, where <code>b</code> is a <b>list</b> of m items and <code>a</code> has n. Time complexity?",
         "options": ["O(n + m)", "O(n \u00d7 m)", "O(n)", "O(n\u00b2)"], "answer": 1, "why": "<code>x in b</code> on a list scans up to m items, and it runs n times. That is a hidden nested loop."},
        {"q": "Same loop, but <code>b</code> was converted with <code>set(b)</code> before the loop. Time complexity?",
         "options": ["O(n + m)", "O(n \u00d7 m)", "O(1)", "O(n log m)"], "answer": 0, "why": "Building the set costs m once; each lookup is then O(1), so the loop costs n."},
        {"q": "Three separate loops over the same list, one after another:",
         "options": ["O(3n), which is written O(n)", "O(n\u00b3)", "O(n log n)"], "answer": 0, "why": "Loops in sequence add. Constants are dropped, so 3n is O(n). Only nested loops multiply."},
        {"q": "Which single line hides an O(n) loop?",
         "options": ["<code>x in my_set</code>", "<code>lst.pop(0)</code>", "<code>lst.append(x)</code>", "<code>len(lst)</code>"], "answer": 1,
         "why": "Removing the first item shifts every other item one place along. <code>pop()</code> from the end is O(1)."},
    ],
    "debug": {
        "intro": "This version says every list has a duplicate. Two lines are in the wrong order.",
        "starter": "def has_duplicate(ids):\n    seen = set()\n    for x in ids:\n        seen.add(x)\n        if x in seen:\n            return True\n    return False\n",
        "hint": "After <code>seen.add(x)</code>, is <code>x in seen</code> ever False?",
    },
}

EXTRAS["big-o-space"] = {
    "limit": 10,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "One pass; only two variables are kept whatever the input size."},
    "quiz": [
        {"q": "<code>b = sorted(a)</code> on a list of n items. Extra space?",
         "options": ["O(1)", "O(n)", "O(log n)"], "answer": 1, "why": "<code>sorted</code> builds a new list of n items. <code>a.sort()</code> would sort in place."},
        {"q": "What does this print?", "code": "a = [3, 1, 2]\nb = a.sort()\nprint(b)",
         "options": ["@run", "[1, 2, 3]", "[3, 1, 2]"], "why": "<code>sort()</code> changes <code>a</code> in place and returns <code>None</code>. Never write <code>lst = lst.sort()</code>."},
        {"q": "A recursive function calls itself n levels deep with O(1) work at each level. Space?",
         "options": ["O(1)", "O(n), for the call stack", "O(n\u00b2)"], "answer": 1, "why": "Every waiting call sits on the call stack until the deepest one returns."},
        {"q": "The set-based duplicate check from the previous lesson is:",
         "options": ["O(n) time and O(1) space", "O(n) time and O(n) space", "O(n\u00b2) time and O(1) space"], "answer": 1, "why": "It spends O(n) memory on the set to bring time down from O(n\u00b2) to O(n). That is the classic trade-off."},
    ],
    "debug": {
        "intro": "This version returns 0 for a list that only ever falls. The two <code>if</code> blocks are in the wrong order.",
        "starter": "def largest_gap(levels):\n    smallest = levels[0]\n    best = levels[1] - levels[0]\n    for x in levels[1:]:\n        if x < smallest:\n            smallest = x\n        if x - smallest > best:\n            best = x - smallest\n    return best\n",
        "hint": "When <code>x</code> is a new minimum, <code>x - smallest</code> becomes 0 before the gap is measured. Measure first, then update.",
    },
}

EXTRAS["python-toolkit"] = {
    "limit": 8,
    "complexity": {"time": ["O(n)", "O(n \u00d7 L)"], "space": ["O(n)"], "time_options": ["O(1)", "O(n)", "O(n \u00d7 L)", "O(n log n)", "O(n\u00b2)"], "space_options": S_STD,
                   "why": "One pass; each strip and upper is proportional to the reference length L. The new list is O(n)."},
    "quiz": [
        {"q": "What does this print?", "code": "s = \"compliance\"\nprint(s[2:5], s[::-1][0])",
         "options": ["mpl c", "@run", "omp e"], "why": "<code>s[2:5]</code> is positions 2, 3, 4. <code>s[::-1]</code> reverses first, so <code>[0]</code> is the original's last letter."},
        {"q": "What does this print?", "code": "a = [1, 2]\nb = a\nc = a[:]\nb.append(3)\nc.append(4)\nc.append(5)\nprint(len(a), len(b), len(c))",
         "options": ["2 3 4", "@run", "2 2 4"], "why": "<code>b</code> is another name for the same list as <code>a</code>, so both see the 3. <code>c</code> is a copy."},
        {"q": "What does this print?", "code": "def add(x, items=[]):\n    items.append(x)\n    return len(items)\n\nprint(add(1), add(2), add(3))",
         "options": ["1 1 1", "3 3 3", "@run"], "why": "The default list is created once and shared by every call, so it keeps growing."},
        {"q": "Which condition is always True, whatever <code>note</code> holds?",
         "options": ["<code>'fire' in note or 'leak' in note</code>", "<code>'fire' or 'leak' in note</code>", "<code>('fire' in note) and ('leak' in note)</code>"], "answer": 1,
         "why": "Python reads it as <code>'fire' or (...)</code>. A non-empty string counts as True, so the whole thing is True."},
        {"q": "What does this print?", "code": "for i, w in enumerate([\"red\", \"amber\", \"green\"]):\n    if w == \"green\":\n        print(i)",
         "options": ["1", "@run", "3"], "why": "<code>enumerate</code> counts from 0, so green is at position 2."},
    ],
    "debug": {
        "intro": "This version lets blank references through. One condition tests the wrong variable.",
        "starter": "def clean_refs(refs):\n    result = []\n    for r in refs:\n        cleaned = r.strip().upper()\n        if r:\n            result.append(cleaned)\n    return result\n",
        "hint": "<code>'   '</code> is a non-empty string, so <code>if r:</code> is True. Which variable holds the stripped text?",
    },
}

EXTRAS["sets"] = {
    "limit": 10,
    "complexity": {"time": ["O(n + m)"], "space": ["O(n + m)"], "time_options": ["O(1)", "O(n)", "O(n + m)", "O(n \u00d7 m)", "O(n\u00b2)"], "space_options": ["O(1)", "O(n)", "O(n + m)", "O(n \u00d7 m)"],
                   "why": "Building the set of check-outs costs m; the loop costs n with O(1) checks. Both sets together are O(n + m)."},
    "quiz": [
        {"q": "Which creates an empty set?", "options": ["<code>{}</code>", "<code>set()</code>", "<code>[]</code>"], "answer": 1, "why": "<code>{}</code> is an empty dictionary. Only <code>set()</code> makes an empty set."},
        {"q": "What does this print?", "code": "seen = set()\nfor x in [3, 1, 3, 2, 1]:\n    seen.add(x)\nprint(len(seen))",
         "options": ["5", "@run", "2"], "why": "Duplicates are ignored, leaving 3, 1 and 2."},
        {"q": "In the 'seen before' pattern, why check <i>before</i> adding?",
         "options": ["So the current item cannot match itself", "To save memory", "Because add() fails on duplicates"], "answer": 0, "why": "If you add first, every item is 'already seen' by the time you check it."},
        {"q": "<code>x in big_list</code> versus <code>x in big_set</code>, each with a million items. Roughly how do they compare?",
         "options": ["About the same", "The list check can take a million steps; the set check takes about one", "The set check is slower because of hashing"], "answer": 1,
         "why": "A list is scanned item by item. A set jumps straight to where the item would be."},
        {"q": "What does this print?", "code": "a = {\"R1\", \"R2\", \"R3\"}\nb = {\"R2\", \"R9\"}\nprint(sorted(a - b), sorted(a & b))",
         "options": ["@run", "['R1', 'R3'] ['R9']", "['R2'] ['R1', 'R3']"], "why": "<code>a - b</code> is what is only in a; <code>a &amp; b</code> is what is in both."},
    ],
    "debug": {
        "intro": "This version returns some IDs twice. Something is missing.",
        "starter": "def still_in(check_ins, check_outs):\n    left = set(check_outs)\n    result = []\n    for rid in check_ins:\n        if rid not in left:\n            result.append(rid)\n    return result\n",
        "hint": "Each ID should appear once. You need a second 'have I added this already?' check.",
    },
}

EXTRAS["dictionaries"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(k)", "O(n)"], "time_options": T_STD, "space_options": ["O(1)", "O(k) distinct issues", "O(n)", "O(n\u00b2)"],
                   "why": "Counting is one pass. The dictionary holds one entry per distinct issue, k, which is at most n."},
    "quiz": [
        {"q": "What does this print?", "code": "counts = {}\nfor w in [\"a\", \"b\", \"a\"]:\n    counts[w] = counts.get(w, 0) + 1\nprint(counts[\"a\"], len(counts))",
         "options": ["2 3", "@run", "3 2"], "why": "'a' is counted twice; there are two distinct keys."},
        {"q": "<code>counts[w] += 1</code> when <code>w</code> is not yet a key:",
         "options": ["Creates it with value 1", "Raises KeyError", "Creates it with value 0"], "answer": 1, "why": "Reading a missing key fails. Use <code>counts.get(w, 0) + 1</code> or a <code>defaultdict(int)</code>."},
        {"q": "What does this print?", "code": "counts = {\"damp\": 2, \"leak\": 3, \"lock\": 1}\nprint(max(counts, key=counts.get))",
         "options": ["3", "@run", "damp"], "why": "<code>max</code> runs over the keys and uses each key's value to compare, returning the key."},
        {"q": "Which can be a dictionary key?", "options": ["A list, e.g. <code>[1, 2]</code>", "A tuple, e.g. <code>(1, 2)</code>", "Another dictionary"], "answer": 1,
         "why": "Keys must be hashable, which means unchangeable. Tuples qualify; lists and dicts do not."},
        {"q": "What does this print?", "code": "print(isinstance(True, int), 3 == 3.0)",
         "options": ["False True", "True False", "@run"], "why": "<code>bool</code> is a subclass of <code>int</code>, and 3 equals 3.0. Both matter when validating JSON input."},
    ],
    "debug": {
        "intro": "This version breaks ties the wrong way round.",
        "starter": "def top_issue(reports):\n    counts = {}\n    for r in reports:\n        counts[r] = counts.get(r, 0) + 1\n    best = \"\"\n    for issue, n in counts.items():\n        if best == \"\" or n > counts[best] or (n == counts[best] and issue > best):\n            best = issue\n    return best\n",
        "hint": "On a tie the task wants the issue that comes first alphabetically. Which comparison picks that?",
    },
}

EXTRAS["stacks"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)", "O(n + T)"], "space": ["O(n)"], "time_options": ["O(1)", "O(n)", "O(n + T)", "O(n log n)", "O(n\u00b2)"], "space_options": S_STD,
                   "why": "Each command is O(1); the final join is proportional to the text length T. The stack holds up to n pieces."},
    "quiz": [
        {"q": "A stack returns items in which order?", "options": ["First in, first out", "Last in, first out", "Smallest first"], "answer": 1, "why": "Like a pile of plates: the last one put on is the first one taken off."},
        {"q": "What does this print?", "code": "s = []\nfor ch in \"abc\":\n    s.append(ch)\ns.pop()\ns.append(\"z\")\nprint(\"\".join(s))",
         "options": ["abcz", "@run", "zab"], "why": "<code>pop()</code> removes the most recent item, c, then z goes on top."},
        {"q": "In the bracket checker, the input <code>(((</code> finishes the loop with no mismatch. What makes it return False?",
         "options": ["The final check that the stack is empty", "An IndexError", "Nothing: it returns True"], "answer": 0, "why": "Three openers were pushed and never closed, so <code>return not stack</code> is False."},
        {"q": "<code>stack.pop()</code> on an empty list:", "options": ["Returns None", "Raises IndexError", "Returns 0"], "answer": 1, "why": "Always check <code>if stack:</code> before popping when the input might be unbalanced."},
        {"q": "Which list operation would make a stack slow?", "options": ["<code>append</code> at the end", "<code>pop()</code> from the end", "<code>pop(0)</code> from the front"], "answer": 2,
         "why": "Working at the end is O(1). The front is O(n) because everything shifts."},
    ],
    "debug": {
        "intro": "This version crashes when there is nothing to undo.",
        "starter": "def final_text(commands):\n    stack = []\n    for cmd in commands:\n        if cmd == \"undo\":\n            stack.pop()\n        elif cmd.startswith(\"add \"):\n            stack.append(cmd[4:])\n    return \"\".join(stack)\n",
        "hint": "What happens to <code>stack.pop()</code> when the stack is empty? Guard it.",
    },
}

EXTRAS["queues"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Each timestamp is appended once and removed at most once, so the total work is O(n) even though there is a while loop inside the for loop."},
    "quiz": [
        {"q": "Why is <code>list.pop(0)</code> a poor queue operation?",
         "options": ["It raises an error", "Every remaining item shifts one place: O(n)", "It removes the last item"], "answer": 1, "why": "<code>deque.popleft()</code> does the same job in O(1)."},
        {"q": "What does this print?", "code": "from collections import deque\nq = deque([1, 2, 3])\nq.append(4)\nq.popleft()\nq.appendleft(0)\nprint(list(q))",
         "options": ["[1, 2, 3, 4]", "@run", "[0, 1, 2, 3]"], "why": "4 joins the back, 1 leaves the front, 0 jumps to the front."},
        {"q": "What does this print?", "code": "from collections import deque\nd = deque(maxlen=2)\nfor x in [1, 2, 3]:\n    d.append(x)\nprint(list(d))",
         "options": ["[1, 2]", "[1, 2, 3]", "@run"], "why": "With <code>maxlen=2</code>, adding a third item drops the oldest."},
        {"q": "In the recent-calls window, each timestamp is added once and removed at most once. Total time for n calls?",
         "options": ["O(n)", "O(n\u00b2)", "O(n log n)"], "answer": 0, "why": "The inner while loop looks nested, but across the whole run it can only remove n items in total."},
    ],
    "debug": {
        "intro": "This version drops calls that are exactly 3000 seconds old, which the task says should count.",
        "starter": "from collections import deque\n\ndef recent_counts(times):\n    q = deque()\n    result = []\n    for t in times:\n        q.append(t)\n        while q[0] <= t - 3000:\n            q.popleft()\n        result.append(len(q))\n    return result\n",
        "hint": "The window is inclusive: a call at exactly <code>t - 3000</code> stays. Check the comparison operator.",
    },
}

EXTRAS["linked-lists"] = {
    "limit": 15,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "One walk along the chain, re-pointing links in place."},
    "quiz": [
        {"q": "Reading the item at position i in a linked list of n nodes costs:", "options": ["O(1)", "O(n)", "O(log n)"], "answer": 1, "why": "There is no index. You walk from the head, one node at a time."},
        {"q": "In <code>reverse()</code>, what goes wrong if you set <code>cur.next = prev</code> before saving the old <code>cur.next</code>?",
         "options": ["Nothing: the order does not matter", "You lose the rest of the list", "The list gets an extra node"], "answer": 1, "why": "The only reference to the remaining nodes was <code>cur.next</code>. Overwrite it and they are gone."},
        {"q": "Why use a dummy node in <code>remove_all</code>?", "options": ["To make the list longer", "So removing the head needs no special case", "To store the count"], "answer": 1,
         "why": "With a dummy in front, the head is just another <code>cur.next</code>."},
        {"q": "What does this print?", "code": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\nhead = Node(1, Node(2, Node(3, Node(4))))\nslow = fast = head\nwhile fast and fast.next:\n    slow = slow.next\n    fast = fast.next.next\nprint(slow.val)",
         "options": ["2", "@run", "4"], "why": "Fast moves two steps per turn, slow one. When fast runs out, slow is at the second of the two middle nodes."},
    ],
    "debug": {
        "intro": "This version misses consecutive targets and can crash. It steps forward even after removing a node.",
        "starter": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\ndef remove_all(head, target):\n    dummy = Node(0, head)\n    cur = dummy\n    while cur.next:\n        if cur.next.val == target:\n            cur.next = cur.next.next\n        cur = cur.next\n    return dummy.next\n",
        "hint": "After skipping a node, <code>cur.next</code> is already the next candidate. Only step forward when you did <b>not</b> remove.",
    },
}

EXTRAS["two-pointers"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Each pointer only moves inward, so every character is visited at most once, with no extra storage."},
    "quiz": [
        {"q": "Opposite-end pointers find a pair sum in O(n) only when:", "options": ["The list is sorted", "The list has no duplicates", "The target is positive"], "answer": 0,
         "why": "The rule 'too small, move left up; too big, move right down' only works on sorted data."},
        {"q": "What does this print?", "code": "s = \"abca\"\nleft, right = 0, len(s) - 1\nwhile left < right:\n    if s[left] != s[right]:\n        print(left, right)\n        break\n    left += 1\n    right -= 1",
         "options": ["0 3", "@run", "1 1"], "why": "a matches a, then b and c differ at positions 1 and 2."},
        {"q": "In <code>move_zeroes</code>, what does the <code>write</code> pointer mark?", "options": ["The last zero seen", "Where the next non-zero item goes", "The length of the list"], "answer": 1,
         "why": "The reader scans everything; the writer only advances when something is kept."},
        {"q": "What does this print?", "code": "a, b = 1, 2\na, b = b, a\nprint(a, b)", "options": ["1 2", "@run", "2 2"], "why": "Python evaluates the right side first, then assigns, so this swaps."},
    ],
    "debug": {
        "intro": "This version says a mixed-case palindrome is not one.",
        "starter": "def is_clean_palindrome(s):\n    left, right = 0, len(s) - 1\n    while left < right:\n        if not s[left].isalnum():\n            left += 1\n        elif not s[right].isalnum():\n            right -= 1\n        elif s[left] != s[right]:\n            return False\n        else:\n            left += 1\n            right -= 1\n    return True\n",
        "hint": "'A' and 'a' are different characters. The task says to ignore case.",
    },
}

EXTRAS["sliding-window"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "The first window costs k, then each slide is one add and one subtract."},
    "quiz": [
        {"q": "The window from index <code>left</code> to <code>right</code> inclusive has length:", "options": ["right - left", "right - left + 1", "right + left"], "answer": 1,
         "why": "Positions 2 to 4 inclusive are three items: 4 - 2 + 1."},
        {"q": "Recomputing <code>sum(nums[i:i+k])</code> for each of the n windows costs:", "options": ["O(n)", "O(n \u00d7 k)", "O(k)"], "answer": 1,
         "why": "Each sum is k steps and there are about n windows. Sliding makes each step O(1)."},
        {"q": "What does this print?", "code": "nums = [4, 2, 7, 1]\nk = 2\nwindow = sum(nums[:k])\nbest = window\nfor i in range(k, len(nums)):\n    window += nums[i] - nums[i - k]\n    best = max(best, window)\nprint(best)",
         "options": ["6", "@run", "8"], "why": "Windows are 6, 9, 8. The best is 9."},
        {"q": "<code>busiest_stretch([5, 6], 3)</code> should return:", "options": ["11", "0", "6"], "answer": 1, "why": "k is larger than the list, which the task defines as 0."},
        {"q": "In <code>longest_unique</code>, when does the left pointer move?", "options": ["On every step", "Only when the new character is already in the window", "Never"], "answer": 1,
         "why": "The window grows on the right and shrinks on the left only when the no-duplicates rule breaks."},
    ],
    "debug": {
        "intro": "This version subtracts the wrong item when it slides. Classic off-by-one.",
        "starter": "def busiest_stretch(occupancy, k):\n    if k <= 0 or k > len(occupancy):\n        return 0\n    window = sum(occupancy[:k])\n    best = window\n    for i in range(k, len(occupancy)):\n        window += occupancy[i] - occupancy[i - k + 1]\n        if window > best:\n            best = window\n    return best\n",
        "hint": "When item <code>i</code> enters a window of size k, which index leaves? Write out k = 2, i = 2 by hand.",
    },
}

EXTRAS["prefix-sums"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "One pass for the total, one pass to check each position, two variables."},
    "quiz": [
        {"q": "What does this print?", "code": "nums = [3, 1, 4, 1, 5]\nprefix = [0]\nfor x in nums:\n    prefix.append(prefix[-1] + x)\nprint(prefix[4] - prefix[1])",
         "options": ["@run", "9", "8"], "why": "<code>prefix[4] - prefix[1]</code> is the sum of positions 1 to 3: 1 + 4 + 1."},
        {"q": "Why does the prefix list start with a 0?", "options": ["To make it one longer", "So a range starting at position 0 works with the same formula", "It does not matter"], "answer": 1,
         "why": "<code>prefix[j + 1] - prefix[0]</code> then gives the sum from the very start without a special case."},
        {"q": "With n items and q range queries, prefix sums cost:", "options": ["O(n \u00d7 q)", "O(n + q)", "O(q)"], "answer": 1, "why": "Build once in O(n), then answer each query in O(1)."},
        {"q": "Sliding window fails but prefix sums with a dictionary still work when:", "options": ["Numbers can be negative", "The list is sorted", "k is 1"], "answer": 0,
         "why": "With negatives, growing a window can make its sum smaller, so the window rule breaks. Prefix differences do not care."},
    ],
    "debug": {
        "intro": "This version never finds the balance point. The running total is updated at the wrong moment.",
        "starter": "def balance_day(spend):\n    total = sum(spend)\n    left = 0\n    for i, x in enumerate(spend):\n        left += x\n        if left == total - left - x:\n            return i\n    return -1\n",
        "hint": "'Before that day' means the current day's spend must not be in <code>left</code> yet when you compare.",
    },
}

EXTRAS["recursion"] = {
    "limit": 12,
    "complexity": {"time": ["O(n)"], "space": ["O(d)", "O(n)"], "time_options": T_STD, "space_options": ["O(1)", "O(d) nesting depth", "O(n)", "O(n\u00b2)"],
                   "why": "Every element is visited once. The call stack grows with the nesting depth d, which is at most n."},
    "quiz": [
        {"q": "Every recursive function needs:", "options": ["A base case, and a recursive case that shrinks the problem", "A loop", "A global variable"], "answer": 0,
         "why": "Without a base case it never stops. Without shrinking, it never reaches the base case."},
        {"q": "What does this print?", "code": "def f(n):\n    if n == 0:\n        return 0\n    return n + f(n - 1)\n\nprint(f(4))", "options": ["4", "@run", "24"],
         "why": "4 + 3 + 2 + 1 + 0."},
        {"q": "Naive recursive Fibonacci is O(2\u207f) because:", "options": ["Each call makes two more calls, recomputing the same values", "Python is slow", "It uses a list"], "answer": 0,
         "why": "The call tree doubles at every level. Memoisation computes each value once instead."},
        {"q": "Memoisation means:", "options": ["Remembering results already computed so each sub-problem is solved once", "Removing the base case", "Using a loop instead"], "answer": 0,
         "why": "A dictionary (or <code>lru_cache</code>) stores answers by argument."},
        {"q": "Recursion 50,000 levels deep in Python will:", "options": ["Work fine", "Raise RecursionError", "Return None"], "answer": 1, "why": "The default limit is about 1,000. Deep problems need a loop or an explicit stack."},
    ],
    "debug": {
        "intro": "This version recurses into nested lists but throws the answer away.",
        "starter": "def count_items(data):\n    count = 0\n    for x in data:\n        if isinstance(x, list):\n            count_items(x)\n        else:\n            count += 1\n    return count\n",
        "hint": "The recursive call returns a number. Nothing is done with it.",
    },
}

EXTRAS["binary-search"] = {
    "limit": 15,
    "complexity": {"time": ["O(log n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Each step halves the remaining range; only two indices are stored."},
    "quiz": [
        {"q": "Binary search on 1,000,000 sorted items needs about how many comparisons?", "options": ["1,000,000", "1,000", "20"], "answer": 2, "why": "2\u00b2\u2070 is just over a million, so about 20 halvings."},
        {"q": "Binary search requires the data to be:", "options": ["Sorted", "Unique", "Numeric"], "answer": 0, "why": "Throwing away half only works if you know which half cannot contain the answer."},
        {"q": "What does this print?", "code": "import bisect\nxs = [1, 3, 3, 3, 8]\nprint(bisect.bisect_left(xs, 3), bisect.bisect_right(xs, 3))",
         "options": ["1 3", "@run", "2 4"], "why": "<code>bisect_left</code> gives the first position of 3; <code>bisect_right</code> gives the position just after the last 3."},
        {"q": "With <code>while lo &lt; hi</code>, which update can loop forever?", "options": ["<code>lo = mid + 1</code>", "<code>hi = mid</code>", "<code>lo = mid</code>"], "answer": 2,
         "why": "When <code>hi = lo + 1</code>, <code>mid</code> equals <code>lo</code>, so <code>lo = mid</code> changes nothing."},
    ],
    "debug": {
        "intro": "This version can never return <code>len(arrivals)</code>, so 'nobody late' comes out wrong.",
        "starter": "def first_late(arrivals, deadline):\n    lo, hi = 0, len(arrivals) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if arrivals[mid] > deadline:\n            hi = mid\n        else:\n            lo = mid + 1\n    return lo\n",
        "hint": "The answer can be one past the last index. What should <code>hi</code> start as?",
    },
}

EXTRAS["sorting"] = {
    "limit": 10,
    "complexity": {"time": ["O(n log n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Sorting dominates. <code>sorted</code> builds a new list and so does the list of names."},
    "quiz": [
        {"q": "What does this print?", "code": "pairs = [(\"b\", 2), (\"a\", 2), (\"c\", 1)]\nprint(sorted(pairs, key=lambda p: p[1]))",
         "options": ["@run", "[('c', 1), ('a', 2), ('b', 2)]", "[('a', 2), ('b', 2), ('c', 1)]"], "why": "Python's sort is stable: the two items with value 2 keep their original order, b before a."},
        {"q": "What does this print?", "code": "print(sorted([\"10\", \"9\", \"2\"]))", "options": ["['2', '9', '10']", "@run", "['9', '10', '2']"],
         "why": "Strings compare character by character, and '1' comes before '2'. Use <code>key=int</code> for numeric order."},
        {"q": "Worst case: merge sort versus quick sort", "options": ["Both O(n log n)", "Merge O(n log n), quick O(n\u00b2)", "Merge O(n\u00b2), quick O(n log n)"], "answer": 1,
         "why": "Quick sort degrades with bad pivots. Merge sort always splits evenly."},
        {"q": "To sort high-to-low on a number but A-to-Z on a name in one key:",
         "options": ["<code>key=lambda j: (-j[1], j[0])</code>", "<code>key=lambda j: (j[1], j[0]), reverse=True</code>", "<code>key=lambda j: j[0] - j[1]</code>"], "answer": 0,
         "why": "Negating the number flips just that part of the tuple. <code>reverse=True</code> would flip the names too."},
        {"q": "Python's built-in sort costs:", "options": ["O(n)", "O(n log n)", "O(n\u00b2)"], "answer": 1, "why": "Timsort. Remember to include it when stating the complexity of a solution that sorts."},
    ],
    "debug": {
        "intro": "This version orders waiting time the wrong way.",
        "starter": "def rank_jobs(jobs):\n    ordered = sorted(jobs, key=lambda j: (j[1], j[2], j[0]))\n    return [j[0] for j in ordered]\n",
        "hint": "Longest wait first means that part of the key must sort descending while the others ascend.",
    },
}

EXTRAS["trees"] = {
    "limit": 15,
    "complexity": {"time": ["O(n)"], "space": ["O(h)", "O(n)"], "time_options": T_STD, "space_options": ["O(1)", "O(h) tree height", "O(n)", "O(n\u00b2)"],
                   "why": "Each node is visited once. The recursion goes as deep as the tree's height h."},
    "quiz": [
        {"q": "In-order traversal of a binary search tree visits values:", "options": ["In sorted order", "Root first", "Level by level"], "answer": 0,
         "why": "Left subtree (smaller), node, right subtree (larger)."},
        {"q": "Height of the tree with root 8, children 3 and 10, and leaves 1, 6 and 14, counting levels:", "options": ["2", "3", "6"], "answer": 1, "why": "Three levels: 8; 3 and 10; 1, 6 and 14."},
        {"q": "Searching a BST that has degenerated into a chain costs:", "options": ["O(log n)", "O(n)", "O(1)"], "answer": 1, "why": "A chain is a linked list in disguise."},
        {"q": "What does this print?", "code": "class T:\n    def __init__(self, v, l=None, r=None):\n        self.v, self.l, self.r = v, l, r\n\ndef count(n):\n    if n is None:\n        return 0\n    return 1 + count(n.l) + count(n.r)\n\nprint(count(T(1, T(2), T(3, T(4)))))",
         "options": ["3", "@run", "5"], "why": "Four nodes: 1, 2, 3 and 4."},
        {"q": "Level-order traversal uses:", "options": ["A stack", "A queue", "Sorting"], "answer": 1, "why": "Take from the front, add children to the back."},
    ],
    "debug": {
        "intro": "This version treats a node with one child as a leaf.",
        "starter": "class TreeNode:\n    def __init__(self, val, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right\n\ndef leaf_sum(root):\n    if root is None:\n        return 0\n    if root.left is None or root.right is None:\n        return root.val\n    return leaf_sum(root.left) + leaf_sum(root.right)\n",
        "hint": "A leaf has <b>no</b> children. Which logical operator says 'both are missing'?",
    },
}

EXTRAS["heaps"] = {
    "limit": 12,
    "complexity": {"time": ["O(n log k)"], "space": ["O(k)"], "time_options": ["O(n)", "O(k)", "O(n log k)", "O(n log n)", "O(n\u00b2)"], "space_options": ["O(1)", "O(k)", "O(n)", "O(n log n)"],
                   "why": "n pushes and pops on a heap that never exceeds k items."},
    "quiz": [
        {"q": "After <code>heapq.heapify(lst)</code>, which is guaranteed?", "options": ["The whole list is sorted", "<code>lst[0]</code> is the smallest item", "<code>lst[-1]</code> is the largest"], "answer": 1,
         "why": "A heap only promises the minimum at the front."},
        {"q": "What does this print?", "code": "import heapq\nh = [5, 1, 8, 3]\nheapq.heapify(h)\nprint(heapq.heappop(h), heapq.heappop(h))", "options": ["5 1", "@run", "8 5"],
         "why": "Pops come out smallest first."},
        {"q": "To get a max-heap with <code>heapq</code>:", "options": ["Push negated values", "Use <code>heapq.maxheap</code>", "Reverse the list first"], "answer": 0, "why": "The smallest negated value is the largest original."},
        {"q": "Keeping a heap of size k while scanning n items costs:", "options": ["O(n log k)", "O(n log n)", "O(k)"], "answer": 0, "why": "Each of the n pushes or pops costs log k on a heap of size k."},
    ],
    "debug": {
        "intro": "This version keeps one item too few in the heap.",
        "starter": "import heapq\n\ndef kth_largest(costs, k):\n    h = []\n    for c in costs:\n        heapq.heappush(h, c)\n        if len(h) >= k:\n            heapq.heappop(h)\n    return h[0]\n",
        "hint": "The heap should hold exactly k items at the end. When should you pop: at k, or past k?",
    },
}

EXTRAS["graphs"] = {
    "limit": 20,
    "complexity": {"time": ["O(V + E)"], "space": ["O(V + E)"], "time_options": ["O(V)", "O(E)", "O(V + E)", "O(V \u00d7 E)", "O(V\u00b2)"], "space_options": ["O(1)", "O(V)", "O(V + E)", "O(V\u00b2)"],
                   "why": "BFS visits each vertex once and looks at each edge once; the adjacency list stores every edge."},
    "quiz": [
        {"q": "BFS gives the shortest path in hops when the graph is:", "options": ["Unweighted", "Weighted", "Sorted"], "answer": 0, "why": "With weights, a path with more hops can be shorter. That needs Dijkstra."},
        {"q": "Forgetting the visited set on a graph with a cycle causes:", "options": ["A wrong but finite answer", "An infinite loop", "A KeyError"], "answer": 1, "why": "The search keeps going round the cycle for ever."},
        {"q": "For an undirected edge (u, v) in an adjacency list you add:", "options": ["v to graph[u] only", "u to graph[v] only", "Both v to graph[u] and u to graph[v]"], "answer": 2,
         "why": "One direction only turns a road into a one-way street."},
        {"q": "What does this print?", "code": "from collections import deque\ngraph = {\"A\": [\"B\", \"C\"], \"B\": [\"D\"], \"C\": [\"D\"], \"D\": []}\ndist = {\"A\": 0}\nq = deque([\"A\"])\nwhile q:\n    node = q.popleft()\n    for nxt in graph[node]:\n        if nxt not in dist:\n            dist[nxt] = dist[node] + 1\n            q.append(nxt)\nprint(dist[\"D\"])",
         "options": ["1", "@run", "3"], "why": "A to B or C is 1 hop, then on to D is 2."},
        {"q": "Weighted shortest paths with no negative weights:", "options": ["BFS", "DFS", "Dijkstra with a heap"], "answer": 2, "why": "Dijkstra always expands the closest unfinished vertex next."},
    ],
    "debug": {
        "intro": "This version only records each connection in one direction, so some journeys look impossible.",
        "starter": "from collections import deque, defaultdict\n\ndef fewest_hops(edges, start, goal):\n    graph = defaultdict(list)\n    for a, b in edges:\n        graph[a].append(b)\n    dist = {start: 0}\n    q = deque([start])\n    while q:\n        node = q.popleft()\n        if node == goal:\n            return dist[node]\n        for nxt in graph[node]:\n            if nxt not in dist:\n                dist[nxt] = dist[node] + 1\n                q.append(nxt)\n    return -1\n",
        "hint": "Connections are two-way. Each edge needs adding to both stations' lists.",
        "extra_tests": [("edge written the other way round", [[["B", "A"]], "A", "B"], False)],
    },
}

EXTRAS["greedy"] = {
    "limit": 20,
    "complexity": {"time": ["O(n log n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Sorting is O(n log n) and the heap operations add O(n log n); the heap can hold every booking."},
    "quiz": [
        {"q": "To fit the most meetings into one room, sort by:", "options": ["Start time", "End time", "Duration"], "answer": 1, "why": "Finishing earliest leaves the most room for what follows."},
        {"q": "Greedy coin change with coins 1, 3 and 4 for amount 6 gives 4 + 1 + 1. The best is:", "options": ["3 + 3", "4 + 1 + 1 is already best", "1 \u00d7 6"], "answer": 0,
         "why": "Two coins beat three. Greedy fails here because the biggest coin is not always part of the best answer."},
        {"q": "A greedy solution that sorts first costs at least:", "options": ["O(n)", "O(n log n)", "O(n\u00b2)"], "answer": 1, "why": "The sort dominates everything after it."},
        {"q": "Before trusting a greedy idea you should:", "options": ["Try to break it with a small counter-example", "Assume it works", "Convert it to recursion"], "answer": 0,
         "why": "Greedy is right only when the locally best choice never needs undoing. A tiny counter-example exposes it quickly."},
    ],
    "debug": {
        "intro": "This version refuses to reuse a room that frees up at exactly the moment the next booking starts.",
        "starter": "import heapq\n\ndef rooms_needed(bookings):\n    ends = []\n    best = 0\n    for start, end in sorted(bookings):\n        if ends and ends[0] < start:\n            heapq.heappop(ends)\n        heapq.heappush(ends, end)\n        best = max(best, len(ends))\n    return best\n",
        "hint": "A booking occupies its room up to but not including <code>end</code>. Is a room ending at 11 free for a booking starting at 11?",
    },
}

EXTRAS["dynamic-programming"] = {
    "limit": 20,
    "complexity": {"time": ["O(n)"], "space": ["O(1)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "One pass, keeping only the two previous answers instead of a whole table."},
    "quiz": [
        {"q": "The first thing to write for a DP problem is:", "options": ["The loop", "A one-sentence definition of the state dp[i]", "The imports"], "answer": 1,
         "why": "Base cases and transitions follow from the state. Without it, you are guessing."},
        {"q": "What does this print?", "code": "ways = [1, 1]\nfor i in range(2, 6):\n    ways.append(ways[i - 1] + ways[i - 2])\nprint(ways[5])", "options": ["5", "@run", "13"],
         "why": "1, 1, 2, 3, 5, 8: the number of ways to climb 5 stairs."},
        {"q": "Top-down DP means:", "options": ["Recursion with a cache", "Filling a table from the base cases up", "A greedy choice"], "answer": 0, "why": "Bottom-up is the table. Both compute each sub-problem once."},
        {"q": "In <code>best_shifts</code>, taking shift i means adding <code>pay[i]</code> to:", "options": ["best[i - 1]", "best[i - 2]", "pay[i - 1]"], "answer": 1,
         "why": "You cannot also take shift i - 1, so you build on the best answer up to i - 2."},
        {"q": "Which phrase most suggests DP?", "options": ["'seen before'", "'number of ways to reach'", "'shortest path in an unweighted graph'"], "answer": 1,
         "why": "Counting ways over choices that build on each other is the DP signature. The others are a set and BFS."},
    ],
    "debug": {
        "intro": "This version happily works two shifts in a row.",
        "starter": "def best_shifts(pay):\n    take_prev2, best_prev = 0, 0\n    for p in pay:\n        take_prev2, best_prev = best_prev, max(best_prev, best_prev + p)\n    return best_prev\n",
        "hint": "Taking shift i must build on the answer from two shifts back, not one.",
    },
}

EXTRAS["pattern-guide"] = {
    "quiz": [
        {"q": "'Return the first ID that appears twice.'", "options": ["Set", "Stack", "Binary search"], "answer": 0, "why": "'Appears twice' is a 'seen before' question."},
        {"q": "'Largest total over any 7 consecutive days.'", "options": ["Sliding window", "Heap", "Recursion"], "answer": 0, "why": "'Consecutive' plus a fixed size is a fixed window."},
        {"q": "'Fewest connections between two stations.'", "options": ["DFS", "BFS", "Sorting"], "answer": 1, "why": "Fewest hops in an unweighted graph is BFS."},
        {"q": "'Are these brackets balanced?'", "options": ["Queue", "Stack", "Set"], "answer": 1, "why": "Each closer must match the most recent opener."},
        {"q": "'The smallest capacity that still works', over a sorted range of possible answers.", "options": ["Binary search", "Prefix sums", "Greedy"], "answer": 0,
         "why": "'Is x enough?' flips from no to yes once, so binary search over x."},
        {"q": "'The 3 most expensive repairs out of a million.'", "options": ["Heap of size 3", "Linked list", "Two pointers"], "answer": 0, "why": "A min-heap of size k in O(n log k) beats a full sort."},
        {"q": "Input size up to 100,000 and your solution is O(n\u00b2). You should:", "options": ["Submit it", "Look for O(n log n) or O(n)", "Add more tests"], "answer": 1,
         "why": "10 billion steps will time out. The limits tell you the complexity the setter expects."},
    ],
}

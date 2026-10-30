"""Module 2: Core data structures."""

MODULE = {"id": "structures", "title": "Core data structures"}

LESSONS = []

# ---------------------------------------------------------------- sets
LESSONS.append({
    "id": "sets",
    "title": "Hash sets",
    "minutes": 15,
    "tags": ["Accenture"],
    "summary": "A set stores unique items and answers 'is this in here?' in O(1). Reach for one whenever a problem says seen, already, duplicate, unique or contains.",
    "blocks": [
        ("p", "A <b>set</b> is an unordered collection with no duplicates. Python stores each item by its <b>hash</b>, a number computed from the item, so it can jump straight to where an item would be instead of checking every item."),
        ("code", """seen = set()          # empty set. Note: {} is an empty dict
seen.add("R1")
seen.add("R7")
seen.add("R1")        # ignored, already present
print(sorted(seen), len(seen))   # sorted: sets have no order
print("R7" in seen, "R9" in seen)
seen.discard("R7")    # remove if present, no error if missing
print(sorted(seen))
print(sorted(set([3, 5, 3, 8])))   # from a list: duplicates vanish"""),
        ("h", "Set versus list"),
        ("table", ["", "List", "Set"], [
            ["Keeps order", "Yes", "No"],
            ["Allows duplicates", "Yes", "No"],
            ["<code>x in ...</code>", "<b>O(n)</b>", "<b>O(1)</b> average"],
            ["Add an item", "<code>append</code>, O(1)", "<code>add</code>, O(1) average"],
            ["Can hold lists", "Yes", "No, items must be hashable (strings, numbers, tuples)"],
        ]),
        ("h", "Set operations"),
        ("code", """morning = {"Ali", "Bea", "Cal"}
evening = {"Bea", "Dev"}
print(sorted(morning & evening))   # in both
print(sorted(morning | evening))   # in either
print(sorted(morning - evening))   # in morning only
print(sorted(morning ^ evening))  # in exactly one"""),
        ("h", "Pattern: seen before"),
        ("p", "Walk the list once. Before adding an item to the set, check whether it is already there."),
        ("code", """def first_repeat(refs):
    seen = set()
    for ref in refs:
        if ref in seen:
            return ref
        seen.add(ref)
    return "NONE"

print(first_repeat(["R1", "R7", "R3", "R7", "R1"]))"""),
        ("h", "Pattern: complement lookup"),
        ("p", "To find two numbers that sum to a target, ask at each number: have I already seen the partner I need, <code>target - num</code>? Checking before adding stops a number pairing with itself."),
        ("code", """def has_pair(nums, target):
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        seen.add(num)
    return False

print(has_pair([3, 9, 7], 10), has_pair([5], 10), has_pair([5, 5], 10))"""),
    ],
    "mistakes": [
        "Writing <code>{}</code> for an empty set. It creates an empty dict.",
        "Expecting a set to keep insertion order. Use a list alongside it if order matters.",
        "Adding before checking in the 'seen before' pattern.",
        "Trying to put a list in a set. Convert it to a tuple first.",
    ],
    "practice": {
        "title": "Residents still checked in",
        "prompt": "<p>Write <code>still_in(check_ins, check_outs)</code>. Return the IDs that appear in <code>check_ins</code> but never in <code>check_outs</code>, in the order they first appear in <code>check_ins</code>, each only once.</p><p>Example: <code>still_in(['A3', 'B1', 'A3', 'C7', 'D2'], ['B1', 'D2', 'Z9'])</code> returns <code>['A3', 'C7']</code>.</p>",
        "func": "still_in",
        "starter": "def still_in(check_ins, check_outs):\n    pass\n",
        "tests": [
            ("given example", [["A3", "B1", "A3", "C7", "D2"], ["B1", "D2", "Z9"]], False),
            ("nobody left", [["A1"], ["A1"]], False),
            ("no check-outs", [["A1", "B2"], []], True),
            ("empty check-ins", [[], ["A1"]], True),
            ("repeated check-ins", [["X", "X", "X"], []], True),
            ("order kept", [["C", "A", "B"], ["Z"]], True),
        ],
        "hints": [
            "Two 'have I met this?' questions: has it been checked out, and have I already added it?",
            "Turn <code>check_outs</code> into a set once, before the loop. Keep a second set of IDs already added.",
        ],
        "solution": """def still_in(check_ins, check_outs):
    left = set(check_outs)
    added = set()
    result = []
    for rid in check_ins:
        if rid not in left and rid not in added:
            result.append(rid)
            added.add(rid)
    return result
""",
        "explain": "Building the set is O(m), the loop is O(n) with O(1) checks: <b>O(n + m)</b> time and <b>O(n + m)</b> space.",
    },
})

# ---------------------------------------------------------------- dicts
LESSONS.append({
    "id": "dictionaries",
    "title": "Hash maps and counting",
    "minutes": 25,
    "tags": ["Accenture", "Lloyds"],
    "summary": "A dictionary maps keys to values with O(1) lookups. It powers counting, grouping, and remembering where you saw something.",
    "blocks": [
        ("p", "A <b>dictionary</b> (hash map) stores <b>key: value</b> pairs. Like a set, it finds a key in O(1) on average. Unlike a set, each key carries a value. Since Python 3.7, dictionaries keep the order keys were added."),
        ("code", """rent = {"Flat 1": 650, "Flat 2": 720}
rent["Flat 3"] = 690        # add or overwrite
print(rent["Flat 2"])
print("Flat 4" in rent)     # checks keys
print(rent.get("Flat 4"))   # None instead of an error
print(rent.get("Flat 4", 0))
for flat, amount in rent.items():
    print(flat, amount)"""),
        ("h", "Pattern: counting"),
        ("p", "<code>counts.get(x, 0) + 1</code> reads the current count, defaulting to 0, and adds one. This line solves a surprising number of easy assessment problems."),
        ("code", """words = ["log", "risk", "log", "audit", "log"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)
print(max(counts, key=counts.get))   # key with the largest value

from collections import Counter
c = Counter(words)                    # the same in one line
print(c.most_common(2))"""),
        ("h", "Pattern: grouping"),
        ("p", "Map each key to a list of items that share it. <code>defaultdict(list)</code> creates the empty list for you the first time a key appears."),
        ("code", """from collections import defaultdict

incidents = [("Flat 1", "leak"), ("Flat 2", "lock"), ("Flat 1", "damp")]
by_flat = defaultdict(list)
for flat, issue in incidents:
    by_flat[flat].append(issue)
print(dict(by_flat))

# Group anagrams: words with the same sorted letters share a key
groups = defaultdict(list)
for w in ["eat", "tea", "tan", "ate", "nat"]:
    groups["".join(sorted(w))].append(w)
print(list(groups.values()))"""),
        ("h", "Pattern: remember the position"),
        ("p", "Store where you saw each value. The classic example is Two Sum, which returns positions instead of True or False."),
        ("code", """def two_sum(nums, target):
    where = {}                  # value -> position
    for i, num in enumerate(nums):
        need = target - num
        if need in where:
            return [where[need], i]
        where[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 3], 6))"""),
        ("h", "Dictionaries and JSON"),
        ("p", "JSON objects arrive in Python as dictionaries. Validating them safely is a typical practical task (Lloyds lists one)."),
        ("code", """import json

raw = '{"id": "B12", "nights": 3, "guest": {"name": "Sam"}}'
data = json.loads(raw)
print(data["guest"]["name"], data.get("email", "no email"))

try:
    json.loads("{not valid json}")
except json.JSONDecodeError:  # a kind of ValueError
    print("invalid JSON rejected")

print(isinstance(True, int))   # True! bool is a kind of int"""),
    ],
    "mistakes": [
        "Using <code>counts[x] += 1</code> before the key exists (KeyError). Use <code>.get(x, 0)</code> or <code>defaultdict(int)</code>.",
        "Using a list as a key. Keys must be hashable; use a tuple.",
        "Changing a dictionary's size while looping over it.",
        "Forgetting that <code>True</code> passes an <code>isinstance(x, int)</code> check.",
    ],
    "practice": {
        "title": "Most reported issue",
        "prompt": "<p>Write <code>top_issue(reports)</code>. Each report is a string naming an issue. Return the issue reported most often. If several tie, return the one that comes <b>first alphabetically</b>. If there are no reports, return <code>''</code>.</p><p>Example: <code>top_issue(['damp', 'leak', 'damp', 'lock', 'leak'])</code> returns <code>'damp'</code> (damp and leak tie on 2; damp is first alphabetically).</p>",
        "func": "top_issue",
        "starter": "def top_issue(reports):\n    pass\n",
        "tests": [
            ("given example", [["damp", "leak", "damp", "lock", "leak"]], False),
            ("clear winner", [["lock", "leak", "lock"]], False),
            ("empty", [[]], True),
            ("single report", [["mould"]], True),
            ("three-way tie", [["c", "b", "a"]], True),
            ("tie decided alphabetically, not by order", [["zeta", "alpha", "zeta", "alpha"]], True),
        ],
        "hints": [
            "Count first with a dictionary. Then pick the winner as a separate step.",
            "Loop over the counts: keep a key if its count is higher, or equal with a smaller name.",
        ],
        "solution": """def top_issue(reports):
    counts = {}
    for r in reports:
        counts[r] = counts.get(r, 0) + 1
    best = ""
    for issue, n in counts.items():
        if best == "" or n > counts[best] or (n == counts[best] and issue < best):
            best = issue
    return best
""",
        "explain": "Counting is O(n), choosing the winner is O(k) for k distinct issues: <b>O(n)</b> time, <b>O(k)</b> space. A one-liner also works: <code>min(counts, key=lambda k: (-counts[k], k))</code>.",
    },
})

# ---------------------------------------------------------------- stacks
LESSONS.append({
    "id": "stacks",
    "title": "Stacks",
    "minutes": 20,
    "tags": ["Accenture", "Lloyds"],
    "summary": "A stack is last in, first out. Use one for matching pairs, undo, nested structure, and anything where the most recent item matters most.",
    "blocks": [
        ("p", "A <b>stack</b> works like a pile of plates: you add to the top (<b>push</b>) and take from the top (<b>pop</b>). The last item in is the first out, called <b>LIFO</b>. A Python list is a perfect stack, because <code>append</code> and <code>pop</code> at the end are both O(1)."),
        ("code", """stack = []
stack.append("open file")     # push
stack.append("edit line 3")
stack.append("edit line 9")
print(stack[-1])              # peek at the top
print(stack.pop())            # undo the most recent
print(stack)
print(len(stack) == 0)        # is it empty?"""),
        ("table", ["Operation", "Code", "Cost"], [
            ["Push", "<code>stack.append(x)</code>", "O(1)"],
            ["Pop", "<code>stack.pop()</code>", "O(1)"],
            ["Peek", "<code>stack[-1]</code>", "O(1)"],
            ["Is empty", "<code>not stack</code>", "O(1)"],
        ]),
        ("h", "Pattern: matching pairs"),
        ("p", "When you meet an opener, push it. When you meet a closer, the top of the stack must be its partner. At the end, the stack must be empty."),
        ("code", """def balanced(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

for test in ["([]{})", "([)]", "((", ""]:
    print(repr(test), balanced(test))"""),
        ("h", "Pattern: nested state"),
        ("p", "A stack of dictionaries can model nested transactions: each <code>begin</code> pushes a new layer of changes, <code>rollback</code> pops it, and <code>commit</code> merges it into the layer below. This is the idea behind the Lloyds transactional task."),
        ("code", """layers = [{}]                 # bottom layer = committed data
layers.append({})             # begin
layers[-1]["balance"] = 100
layers.append({})             # nested begin
layers[-1]["balance"] = 50
layers.pop()                  # rollback the inner change
top = layers.pop()            # commit the outer one
layers[-1].update(top)
print(layers)"""),
    ],
    "mistakes": [
        "Popping from an empty stack (IndexError). Check <code>if stack</code> first.",
        "Forgetting the final 'is the stack empty?' check.",
        "Using <code>pop(0)</code>, which makes it a slow queue rather than a stack.",
    ],
    "practice": {
        "title": "Edit history with undo",
        "prompt": "<p>Write <code>final_text(commands)</code>. Start with an empty string. Each command is either <code>'add X'</code>, which appends the text X, or <code>'undo'</code>, which reverses the most recent <b>add</b> that has not already been undone. An <code>undo</code> with nothing to undo does nothing. Return the final text.</p><p>Example: <code>final_text(['add Hi', 'add  there', 'undo', 'add !'])</code> returns <code>'Hi!'</code>.</p>",
        "func": "final_text",
        "starter": "def final_text(commands):\n    pass\n",
        "tests": [
            ("given example", [["add Hi", "add  there", "undo", "add !"]], False),
            ("no undo", [["add a", "add b"]], False),
            ("undo on empty", [["undo", "add x"]], True),
            ("undo everything", [["add a", "add b", "undo", "undo", "undo"]], True),
            ("empty", [[]], True),
            ("text with spaces", [["add one two", "add  three"]], True),
        ],
        "hints": [
            "Push each added piece of text onto a stack. Undo pops the most recent piece.",
            "<code>cmd[4:]</code> is everything after <code>'add '</code>. Join the stack at the end with <code>''.join(stack)</code>.",
        ],
        "solution": """def final_text(commands):
    stack = []
    for cmd in commands:
        if cmd == "undo":
            if stack:
                stack.pop()
        elif cmd.startswith("add "):
            stack.append(cmd[4:])
    return "".join(stack)
""",
        "explain": "Each command is O(1) apart from the final join: <b>O(n + T)</b> time where T is the total text length, and <b>O(n)</b> space for the stack.",
    },
})

# ---------------------------------------------------------------- queues
LESSONS.append({
    "id": "queues",
    "title": "Queues and deques",
    "minutes": 15,
    "tags": ["Lloyds"],
    "summary": "A queue is first in, first out. Use collections.deque so both ends are O(1). Queues drive breadth-first search and anything processed in arrival order.",
    "blocks": [
        ("p", "A <b>queue</b> works like a line at a counter: join at the back (<b>enqueue</b>) and leave from the front (<b>dequeue</b>). The first in is the first out, called <b>FIFO</b>."),
        ("p", "A list makes a poor queue: <code>pop(0)</code> shifts every remaining item, which is O(n). <code>collections.deque</code> (double-ended queue) adds and removes at either end in O(1)."),
        ("code", """from collections import deque

q = deque()
q.append("Ali")        # join the back
q.append("Bea")
q.append("Cal")
print(q.popleft())     # serve the front: Ali
print(q[0])            # peek at the next: Bea
q.appendleft("VIP")    # jump the queue
print(list(q), len(q))"""),
        ("table", ["Operation", "list", "deque"], [
            ["Add at back", "<code>append</code>, O(1)", "<code>append</code>, O(1)"],
            ["Remove from front", "<code>pop(0)</code>, <b>O(n)</b>", "<code>popleft()</code>, O(1)"],
            ["Add at front", "<code>insert(0, x)</code>, <b>O(n)</b>", "<code>appendleft</code>, O(1)"],
            ["Index the middle", "O(1)", "O(n)"],
        ]),
        ("h", "Pattern: process in arrival order"),
        ("code", """from collections import deque

def process(jobs, capacity_per_tick):
    q = deque(jobs)
    tick = 0
    while q:
        tick += 1
        for _ in range(min(capacity_per_tick, len(q))):
            job = q.popleft()
            print(f"tick {tick}: {job}")
    return tick

print(process(["inspect", "repair", "audit", "report", "file"], 2))"""),
        ("h", "Pattern: a rolling window of recent events"),
        ("p", "<code>deque(maxlen=k)</code> keeps only the last k items, dropping the oldest automatically."),
        ("code", """from collections import deque
recent = deque(maxlen=3)
for reading in [21, 22, 25, 19, 18]:
    recent.append(reading)
    print(list(recent))"""),
    ],
    "mistakes": [
        "Using <code>list.pop(0)</code> in a loop, which turns O(n) into O(n&sup2;).",
        "Forgetting <code>from collections import deque</code>.",
        "Calling <code>pop()</code> when you meant <code>popleft()</code>: that makes it a stack.",
    ],
    "practice": {
        "title": "Recent call counter",
        "prompt": "<p>Write <code>recent_counts(times)</code>. <code>times</code> is a list of call timestamps in seconds, in increasing order. For each call, count how many calls happened in the <b>last 3000 seconds inclusive</b>, that is, with a timestamp in <code>[t - 3000, t]</code>. Return the list of counts.</p><p>Example: <code>recent_counts([1, 100, 3001, 3002])</code> returns <code>[1, 2, 3, 3]</code>.</p>",
        "func": "recent_counts",
        "starter": "from collections import deque\n\ndef recent_counts(times):\n    pass\n",
        "tests": [
            ("given example", [[1, 100, 3001, 3002]], False),
            ("far apart", [[1, 5000, 10000]], False),
            ("empty", [[]], True),
            ("same second", [[10, 10, 10]], True),
            ("exactly 3000 apart counts", [[0, 3000]], True),
            ("3001 apart drops", [[0, 3001]], True),
        ],
        "hints": [
            "Keep a deque of recent timestamps. Add the new one, then drop old ones from the front.",
            "While <code>q[0] &lt; t - 3000</code>, call <code>q.popleft()</code>. The count is <code>len(q)</code>.",
        ],
        "solution": """from collections import deque

def recent_counts(times):
    q = deque()
    result = []
    for t in times:
        q.append(t)
        while q[0] < t - 3000:
            q.popleft()
        result.append(len(q))
    return result
""",
        "explain": "Each timestamp is added once and removed at most once: <b>O(n)</b> total time (amortised), and <b>O(n)</b> space.",
    },
    "related": [("LeetCode: Number of Recent Calls", "https://leetcode.com/problems/number-of-recent-calls/")],
})

# ---------------------------------------------------------------- linked lists
LESSONS.append({
    "id": "linked-lists",
    "title": "Linked lists",
    "minutes": 20,
    "tags": [],
    "summary": "A linked list is a chain of nodes, each pointing to the next. It is common in interviews because it tests careful pointer handling.",
    "blocks": [
        ("p", "Each <b>node</b> holds a value and a reference to the next node. The list is reached through its first node, the <b>head</b>. The last node points to <code>None</code>."),
        ("code", """class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Build 3 -> 7 -> 1
head = Node(3, Node(7, Node(1)))

node = head
while node:              # walk until we fall off the end
    print(node.val)
    node = node.next"""),
        ("table", ["Operation", "Python list", "Linked list"], [
            ["Read item i", "O(1)", "O(n), walk from the head"],
            ["Insert at the front", "O(n)", "O(1)"],
            ["Insert after a known node", "O(n)", "O(1)"],
            ["Find a value", "O(n)", "O(n)"],
        ]),
        ("h", "Reversing a list"),
        ("p", "The classic linked list question. Walk forwards and flip each arrow, keeping three references: the previous node, the current node and the next node."),
        ("code", """class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next     # remember the rest
        cur.next = prev    # flip the arrow
        prev = cur         # step forward
        cur = nxt
    return prev            # new head

head = Node(1, Node(2, Node(3)))
print(to_list(reverse(head)))"""),
        ("h", "Pattern: fast and slow pointers"),
        ("p", "Move one pointer one step and another two steps. When the fast one reaches the end, the slow one is in the middle. If there is a loop, they eventually meet."),
        ("code", """class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

print(middle(Node(1, Node(2, Node(3, Node(4, Node(5)))))))"""),
    ],
    "mistakes": [
        "Losing the rest of the list by overwriting <code>cur.next</code> before saving it.",
        "Forgetting the empty list (<code>head is None</code>).",
        "Checking <code>fast.next.next</code> without first checking <code>fast.next</code>.",
    ],
    "practice": {
        "title": "Remove a value from a chain",
        "prompt": "<p>A <code>Node</code> class is provided. Write <code>remove_all(head, target)</code>, which removes every node whose <code>val</code> equals <code>target</code> and returns the new head. The checker turns your result back into a Python list.</p><p>Example: the chain <code>1 -> 2 -> 6 -> 3 -> 6</code> with target 6 becomes <code>1 -> 2 -> 3</code>.</p>",
        "func": "remove_all",
        "starter": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\ndef remove_all(head, target):\n    pass\n",
        "wrapper": """def __call(values, target):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    res = remove_all(head, target)
    out = []
    steps = 0
    while res is not None and steps < 10000:
        out.append(res.val)
        res = res.next
        steps += 1
    return out
""",
        "tests": [
            ("given example", [[1, 2, 6, 3, 6], 6], False),
            ("nothing removed", [[1, 2, 3], 9], False),
            ("empty chain", [[], 1], True),
            ("remove the head", [[7, 7, 1], 7], True),
            ("remove everything", [[4, 4, 4], 4], True),
            ("single node kept", [[5], 4], True),
        ],
        "hints": [
            "Removing the head is awkward. Put a dummy node in front: <code>dummy = Node(0, head)</code>.",
            "Walk with <code>cur = dummy</code>. If <code>cur.next.val == target</code>, skip it with <code>cur.next = cur.next.next</code>; otherwise step forward. Return <code>dummy.next</code>.",
        ],
        "solution": """class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_all(head, target):
    dummy = Node(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == target:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next
""",
        "explain": "One walk along the chain: <b>O(n)</b> time, <b>O(1)</b> extra space. The dummy node removes the special case for the head.",
    },
})

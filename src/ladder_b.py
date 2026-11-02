"""Easy, Medium and Hard ladder for queues, linked lists, prefix sums, recursion and sorting.

Same format as ladder.py. Linked-list problems carry a wrapper that builds the chain from a list.
"""

def S(code): return code.strip("\n") + "\n"

NODE = S('''
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
''')

LADDER_B = {}

# ---------------------------------------------------------------- Queues
SERVE = S('''
from collections import deque

def process_queue(events):
    q = deque()
    served = []
    for e in events:
        if e[0] == "join":
            q.append(e[1])
        elif q:                         # "serve", if anyone waits
            served.append(q.popleft())
    return served
''')
MOVAVG = S('''
from collections import deque

def moving_average(values, k):
    window = deque()
    total = 0
    result = []
    for v in values:
        window.append(v)
        total += v
        if len(window) > k:
            total -= window.popleft()
        result.append(round(total / len(window), 2))
    return result
''')
CIRCLE = S('''
from collections import deque

def last_in_circle(n, k):
    q = deque(range(1, n + 1))
    while len(q) > 1:
        q.rotate(-(k - 1))              # skip k - 1 people
        q.popleft()                     # the k-th leaves
    return q[0]
''')
LADDER_B["queues"] = [
 dict(level="Easy", title="Who gets served?", func="process_queue",
      prompt="<p>Write <code>process_queue(events)</code>. Each event is <code>[\"join\", name]</code> or <code>[\"serve\"]</code>. Serving takes the person at the front. Serving an empty queue does nothing. Return the names in the order they were served.</p><p>Example: <code>[[\"join\", \"Ana\"], [\"join\", \"Ben\"], [\"serve\"], [\"join\", \"Cal\"], [\"serve\"]]</code> gives <code>[\"Ana\", \"Ben\"]</code>.</p>",
      starter="from collections import deque\n\ndef process_queue(events):\n    pass\n",
      tests=[("given example", [[["join", "Ana"], ["join", "Ben"], ["serve"], ["join", "Cal"], ["serve"]]], False),
             ("serve an empty queue", [[["serve"], ["join", "Ana"], ["serve"], ["serve"]]], False),
             ("nobody served", [[["join", "Ana"]]], True), ("no events", [[]], True),
             ("first in, first out", [[["join", "A"], ["join", "B"], ["join", "C"], ["serve"], ["serve"], ["serve"]]], True),
             ("alternating join and serve", [{"__py__": "[['join', i] if i % 2 == 0 else ['serve'] for i in range(20)]"}], True)],
      hints=["First in, first out: a deque. <code>append</code> to join the back, <code>popleft</code> to serve the front.", "Check the queue is not empty before <code>popleft</code>."],
      solution=SERVE, explain="Each join and serve is O(1) on a deque: <b>O(n)</b> time for n events, <b>O(n)</b> space.",
      vid=[("Queues, easy. Who gets served? Join the back, serve the front.", [("b", "join Ana, join Ben, serve, join Cal, serve: Ana, Ben")]),
           ("First in, first out. That's a queue. In Python, a deque.", [("clear",), ("code", SERVE.splitlines()), ("hl", [3])]),
           ("Join? Append to the back.", [("hl", [6, 7])]),
           ("Serve? Pop left, from the front. But only if someone's waiting. Empty queue, do nothing. No crash.", [("hl", [8, 9])]),
           ("Every step O of 1. Never use a list's pop zero for this: it shuffles everyone along. Deque. Always.", [("cap", "First in, first out: deque, append, popleft.")])]),
 dict(level="Medium", title="Moving average of the last k readings", func="moving_average",
      prompt="<p>Write <code>moving_average(values, k)</code>. After each value, record the average of the last <code>k</code> values (or of all values so far, if fewer than k), rounded to 2 decimal places. Return the list of averages. Aim for O(n).</p><p>Example: <code>moving_average([1, 10, 3, 5], 3)</code> returns <code>[1.0, 5.5, 4.67, 6.0]</code>.</p>",
      starter="from collections import deque\n\ndef moving_average(values, k):\n    pass\n",
      tests=[("given example", [[1, 10, 3, 5], 3], False), ("k is 1", [[4, 8, 2], 1], False),
             ("fewer values than k", [[2, 4], 5], True), ("no values", [[], 3], True),
             ("negatives", [[-3, 3, -3, 3], 2], True), ("long run, short output", [{"__py__": "[7] * 30"}, 4], True)],
      hints=["Keep the last k values in a deque and a running total.", "Add the new value to the total; if the window is bigger than k, subtract the value you <code>popleft</code>."],
      solution=MOVAVG, explain="Each value enters and leaves the window once: <b>O(n)</b> time, <b>O(k)</b> space.",
      vid=[("Queues, medium. A moving average of the last k readings.", [("b", "[1, 10, 3, 5], k = 3 gives [1.0, 5.5, 4.67, 6.0]")]),
           ("Re-adding the last k values every time is O of n times k. We can do better.", [("clear",), ("code", MOVAVG.splitlines()), ("hl", [3, 4])]),
           ("Keep a deque of the window, and a running total.", [("hl", [3, 4, 7, 8])]),
           ("Window too big? Pop the oldest off the front and subtract it. That's the queue doing its job.", [("hl", [9, 10])]),
           ("Average, round to two places, record. O of n. Smooth. Very smooth.", [("hl", [11]), ("cap", "Last k of a stream: deque plus running total.")])]),
 dict(level="Hard", title="Last one left in the circle", func="last_in_circle",
      prompt="<p>Write <code>last_in_circle(n, k)</code>. People numbered 1 to n stand in a circle. Counting starts at person 1; every k-th person leaves, and counting carries on from the next person. Return the number of the last person left.</p><p>Example: <code>last_in_circle(5, 2)</code> returns <code>3</code> (2, 4, 1 and 5 leave in that order).</p>",
      starter="from collections import deque\n\ndef last_in_circle(n, k):\n    pass\n",
      tests=[("given example", [5, 2], False), ("everyone in turn", [4, 1], False), ("one person", [1, 3], True),
             ("k bigger than n", [3, 5], True), ("seven people, every third", [7, 3], True), ("2,000 people", [2000, 3], True)],
      hints=["Put 1 to n in a deque. Skipping someone means moving them from the front to the back.", "<code>q.rotate(-(k - 1))</code> skips k - 1 people, then <code>popleft()</code> removes the k-th. Repeat until one is left."],
      solution=CIRCLE, explain="n - 1 removals, each rotating up to k - 1 places: <b>O(n x k)</b> time, <b>O(n)</b> space.",
      vid=[("Queues, hard. The circle. Every k-th person leaves. Who's last?", [("b", "n = 5, k = 2: 2, 4, 1, 5 leave. 3 is last.")]),
           ("A circle is just a queue where skipped people go to the back.", [("clear",), ("code", CIRCLE.splitlines()), ("hl", [3])]),
           ("Rotate moves k minus one people from the front to the back. They're safe this round.", [("hl", [5])]),
           ("Then the person at the front is number k. Pop them. Out.", [("hl", [6])]),
           ("Repeat until one's left. Simulation with a deque. Clear, correct, and you can explain every line. That wins interviews.", [("hl", [4, 7]), ("cap", "Circle? Deque and rotate.")])]),
]

# ---------------------------------------------------------------- Linked lists
LENGTH = NODE + "\n" + S('''
def chain_length(head):
    count = 0
    cur = head
    while cur is not None:
        count += 1
        cur = cur.next
    return count
''')
REVERSE = NODE + "\n" + S('''
def reverse_chain(head):
    prev = None
    cur = head
    while cur is not None:
        nxt = cur.next                  # remember the rest
        cur.next = prev                 # turn the arrow round
        prev = cur
        cur = nxt
    return prev
''')
MERGE = NODE + "\n" + S('''
def merge_chains(a, b):
    dummy = Node(0)
    tail = dummy
    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a if a is not None else b
    return dummy.next
''')
BUILD = '''    def build(values):
        head = None
        for v in reversed(values):
            head = Node(v, head)
        return head
'''
TOLIST = '''    out, steps = [], 0
    while res is not None and steps < 100000:
        out.append(res.val)
        res = res.next
        steps += 1
    return out
'''
def code_lines(src):
    return [l for l in src.splitlines() if l.strip()][4:]   # drop the Node class lines in videos

LADDER_B["linked-lists"] = [
 dict(level="Easy", title="How long is the chain?", func="chain_length",
      prompt="<p>A <code>Node</code> class is provided. Write <code>chain_length(head)</code>, which returns the number of nodes. An empty chain (<code>head</code> is <code>None</code>) has length 0. The checker builds the chain from a list for you.</p>",
      starter=NODE + "\ndef chain_length(head):\n    pass\n",
      wrapper="def __call(values):\n" + BUILD + "    return chain_length(build(values))\n",
      tests=[("three nodes", [[4, 8, 15]], False), ("one node", [[1]], False), ("empty chain", [[]], True),
             ("repeats count", [[2, 2, 2, 2]], True), ("10,000 nodes", [{"__py__": "list(range(10000))"}], True)],
      hints=["Walk with <code>cur = head</code> until <code>cur is None</code>.", "Add 1 for each node, then move with <code>cur = cur.next</code>."],
      solution=LENGTH, explain="Each node is visited once: <b>O(n)</b> time, <b>O(1)</b> space.",
      vid=[("Linked lists, easy. How long is the chain? No len function here. You walk it.", [("b", "4 -> 8 -> 15 has length 3")]),
           ("Start at the head with a pointer called cur.", [("clear",), ("code", code_lines(LENGTH)), ("hl", [1, 2])]),
           ("While cur isn't None, count one and step to the next node.", [("hl", [3, 4, 5])]),
           ("Empty chain? The loop never runs. Zero. Correct, no crash.", [("hl", [6])]),
           ("This walk is the skeleton of every linked list problem. Learn it cold.", [("cap", "Walk: while cur is not None, cur = cur.next")])]),
 dict(level="Medium", title="Reverse the chain", func="reverse_chain",
      prompt="<p>A <code>Node</code> class is provided. Write <code>reverse_chain(head)</code>, which reverses the chain in place and returns the new head. The checker turns your result back into a Python list.</p><p>Example: <code>1 -> 2 -> 3</code> becomes <code>3 -> 2 -> 1</code>.</p>",
      starter=NODE + "\ndef reverse_chain(head):\n    pass\n",
      wrapper="def __call(values):\n" + BUILD + "    res = reverse_chain(build(values))\n" + TOLIST,
      tests=[("three nodes", [[1, 2, 3]], False), ("two nodes", [[5, 9]], False), ("empty chain", [[]], True),
             ("one node", [[7]], True), ("repeats", [[1, 1, 2]], True), ("all the same value", [[0, 0, 0]], True)],
      hints=["Keep three pointers: <code>prev</code>, <code>cur</code> and the next node.", "Save <code>nxt = cur.next</code> before you point <code>cur.next</code> back at <code>prev</code>; then move both forward. Return <code>prev</code>."],
      solution=REVERSE, explain="Each node is visited once: <b>O(n)</b> time, <b>O(1)</b> extra space.",
      vid=[("Linked lists, medium. Reverse the chain. A classic. Everybody asks it.", [("b", "1 -> 2 -> 3 becomes 3 -> 2 -> 1")]),
           ("Three pointers. Previous starts as None. Current starts at the head.", [("clear",), ("code", code_lines(REVERSE)), ("hl", [1, 2])]),
           ("Step one: remember the rest of the chain. Lose that, and it's gone forever.", [("hl", [4])]),
           ("Step two: turn the arrow round, current points back to previous. Then move both forward.", [("hl", [5, 6, 7])]),
           ("When current runs out, previous is the new head. O of n time, O of 1 space. Draw it on paper first. Always.", [("hl", [8]), ("cap", "Save next, flip the arrow, step forward.")])]),
 dict(level="Hard", title="Merge two sorted chains", func="merge_chains",
      prompt="<p>A <code>Node</code> class is provided. Write <code>merge_chains(a, b)</code>. Both chains are sorted. Return the head of one sorted chain containing every node, reusing the nodes. The checker builds both chains and turns your result into a list.</p><p>Example: <code>1 -> 4 -> 6</code> and <code>2 -> 3</code> give <code>1 -> 2 -> 3 -> 4 -> 6</code>.</p>",
      starter=NODE + "\ndef merge_chains(a, b):\n    pass\n",
      wrapper="def __call(xs, ys):\n" + BUILD + "    res = merge_chains(build(xs), build(ys))\n" + TOLIST,
      tests=[("given example", [[1, 4, 6], [2, 3]], False), ("one empty", [[], [5, 7]], False), ("both empty", [[], []], True),
             ("equal values", [[1, 2], [1, 2]], True), ("all of a first", [[1, 2], [8, 9]], True), ("different lengths", [[5], [1, 2, 3, 9]], True)],
      hints=["Use a dummy node and a <code>tail</code> pointer. Attach whichever front node is smaller and move that chain on.", "When one chain runs out, attach the rest of the other in one step."],
      solution=MERGE, explain="Each node is attached once: <b>O(n + m)</b> time, <b>O(1)</b> extra space.",
      vid=[("Linked lists, hard. Merge two sorted chains into one sorted chain.", [("b", "1 -> 4 -> 6 and 2 -> 3 give 1 -> 2 -> 3 -> 4 -> 6")]),
           ("Pro move: a dummy node. It gives us somewhere to attach the first node, no special cases.", [("clear",), ("code", code_lines(MERGE)), ("hl", [1, 2])]),
           ("While both chains have nodes, take the smaller front node, attach it, move that chain on.", [("hl", [3, 4, 5, 6, 7, 8, 9])]),
           ("One chain runs out? Attach the whole rest of the other. It's already sorted. One step.", [("hl", [11])]),
           ("Return dummy dot next. O of n plus m, no extra space. This is the merge step of merge sort. Huge.", [("hl", [12]), ("cap", "Dummy node + tail: attach the smaller, move on.")])]),
]

# ---------------------------------------------------------------- Prefix sums
RANGES = S('''
def range_totals(nums, queries):
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    return [prefix[j + 1] - prefix[i] for i, j in queries]
''')
BOOKINGS = S('''
def room_load(n, bookings):
    diff = [0] * (n + 1)
    for start, end, people in bookings:
        diff[start] += people           # starts here
        diff[end + 1] -= people         # stops after end
    load, running = [], 0
    for i in range(n):
        running += diff[i]
        load.append(running)
    return load
''')
COUNTK = S('''
def count_sum_k(nums, k):
    seen = {0: 1}                       # prefix total -> times seen
    total = 0
    count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)
        seen[total] = seen.get(total, 0) + 1
    return count
''')
LADDER_B["prefix-sums"] = [
 dict(level="Easy", title="Answer many range totals", func="range_totals",
      prompt="<p>Write <code>range_totals(nums, queries)</code>. Each query is <code>[i, j]</code>; answer with the total of <code>nums[i]</code> to <code>nums[j]</code> <b>inclusive</b>. Return the answers in order. Aim for O(1) per query after an O(n) setup.</p><p>Example: <code>range_totals([3, 1, 4, 1, 5], [[0, 2], [1, 3], [4, 4]])</code> returns <code>[8, 6, 5]</code>.</p>",
      starter="def range_totals(nums, queries):\n    pass\n",
      tests=[("given example", [[3, 1, 4, 1, 5], [[0, 2], [1, 3], [4, 4]]], False), ("whole list", [[2, 2, 2], [[0, 2]]], False),
             ("no queries", [[1, 2], []], True), ("negatives", [[-1, 5, -2], [[0, 1], [1, 2]]], True),
             ("100,000 values, few queries", [{"__py__": "list(range(100000))"}, [[0, 99999], [500, 500], [10, 20]]], True)],
      hints=["Build <code>prefix</code> where <code>prefix[i]</code> is the total of the first i values. Start it with 0.", "The total from i to j inclusive is <code>prefix[j + 1] - prefix[i]</code>."],
      solution=RANGES, explain="O(n) to build the prefix list, then O(1) per query: <b>O(n + q)</b> time, <b>O(n)</b> space.",
      vid=[("Prefix sums, easy. Lots of questions about range totals.", [("b", "[3, 1, 4, 1, 5]: 0 to 2 is 8, 1 to 3 is 6")]),
           ("Adding up each range from scratch is slow when there are thousands of questions. So build a running total once.", [("clear",), ("code", RANGES.splitlines()), ("hl", [1, 2, 3])]),
           ("Prefix starts with zero. Each entry is the total of everything before it.", [("b", "[3, 1, 4, 1, 5] -> prefix [0, 3, 4, 8, 9, 14]")]),
           ("Range i to j inclusive? Prefix of j plus one, minus prefix of i. One subtraction. Instant.", [("hl", [4])]),
           ("The plus one is the bit people get wrong. Inclusive end means j plus one. Remember that and you win.", [("cap", "Total i..j = prefix[j + 1] - prefix[i]")])]),
 dict(level="Medium", title="People per room after bookings", func="room_load",
      prompt="<p>Write <code>room_load(n, bookings)</code>. There are rooms 0 to n - 1. Each booking <code>[start, end, people]</code> adds <code>people</code> to every room from start to end inclusive. Return the final number of people in each room. Aim for O(n + b), not O(n x b).</p><p>Example: <code>room_load(5, [[0, 2, 3], [1, 4, 2]])</code> returns <code>[3, 5, 5, 2, 2]</code>.</p>",
      starter="def room_load(n, bookings):\n    pass\n",
      tests=[("given example", [5, [[0, 2, 3], [1, 4, 2]]], False), ("no bookings", [3, []], False),
             ("single room", [4, [[2, 2, 7]]], True), ("whole range", [3, [[0, 2, 1], [0, 2, 1]]], True),
             ("overlapping ends", [4, [[0, 1, 5], [1, 3, 1], [3, 3, 2]]], True),
             ("100,000 bookings", [10, {"__py__": "[[i % 10, 9, 1] for i in range(100000)]"}], True)],
      hints=["Mark only the edges: add at <code>start</code>, subtract just after <code>end</code>. That is a difference list.", "A running total over the difference list gives each room's load."],
      solution=BOOKINGS, explain="O(1) per booking plus one O(n) pass: <b>O(n + b)</b> time, <b>O(n)</b> space.",
      vid=[("Prefix sums, medium. Bookings add people to a range of rooms. What's the final load?", [("b", "5 rooms, [0..2] +3, [1..4] +2 -> [3, 5, 5, 2, 2]")]),
           ("Updating every room for every booking is O of n times b. Too slow with big numbers.", [("clear",), ("code", BOOKINGS.splitlines()), ("hl", [1])]),
           ("The trick: a difference list. Mark only where a booking starts, and where it stops.", [("hl", [3, 4])]),
           ("Then one running total over the marks rebuilds every room's load.", [("hl", [5, 6, 7, 8])]),
           ("Two edges per booking, one pass at the end. O of n plus b. A pro technique. Most candidates have never seen it.", [("cap", "Range updates: mark the edges, then prefix-sum.")])]),
 dict(level="Hard", title="How many stretches add to k?", func="count_sum_k",
      prompt="<p>Write <code>count_sum_k(nums, k)</code>. Return how many contiguous stretches of <code>nums</code> add up to exactly <code>k</code>. Values can be negative. Aim for O(n).</p><p>Example: <code>count_sum_k([1, 2, 3, -3, 3], 3)</code> returns <code>5</code>.</p>",
      starter="def count_sum_k(nums, k):\n    pass\n",
      tests=[("given example", [[1, 2, 3, -3, 3], 3], False), ("simple", [[1, 1, 1], 2], False), ("none", [[1, 2, 3], 7], True),
             ("zeros", [[0, 0, 0], 0], True), ("empty", [[], 0], True), ("50,000 values", [{"__py__": "[1, -1] * 25000"}, 0], True)],
      hints=["A stretch from i to j adds to k when <code>prefix[j] - prefix[i] == k</code>, so you need earlier prefix totals equal to <code>total - k</code>.", "Count how often each prefix total has appeared in a dict, starting with <code>{0: 1}</code>."],
      solution=COUNTK, explain="One pass with O(1) dict work: <b>O(n)</b> time, <b>O(n)</b> space.",
      vid=[("Prefix sums, hard. How many stretches add to exactly k? And there are negatives, so no sliding window.", [("b", "[1, 2, 3, -3, 3], k = 3: five stretches")]),
           ("Keep a running total. A stretch ending here adds to k if some earlier running total was total minus k.", [("clear",), ("code", COUNTK.splitlines()), ("b", "Earlier total = total - k")]),
           ("So count how many times each running total has appeared, in a dictionary. Start with zero seen once: the empty start.", [("hl", [1])]),
           ("Each step: add how many earlier totals equal total minus k, then record this total.", [("hl", [5, 6, 7])]),
           ("Prefix sums plus a dictionary. O of n. This is a genuine top-tier pattern. You've got it.", [("hl", [8]), ("cap", "Negatives? Prefix totals + a dict of counts.")])]),
]

# ---------------------------------------------------------------- Recursion
DIGITS = S('''
def sum_digits(n):
    if n < 10:                          # base case: one digit
        return n
    return n % 10 + sum_digits(n // 10)
''')
POWER = S('''
def fast_power(base, exp):
    if exp == 0:
        return 1
    half = fast_power(base, exp // 2)   # solve half once
    if exp % 2 == 0:
        return half * half
    return half * half * base
''')
BRACKETS = S('''
def all_brackets(n):
    out = []
    def build(s, opened, closed):
        if len(s) == 2 * n:
            out.append(s)
            return
        if opened < n:
            build(s + "(", opened + 1, closed)
        if closed < opened:
            build(s + ")", opened, closed + 1)
    build("", 0, 0)
    return out
''')
LADDER_B["recursion"] = [
 dict(level="Easy", title="Add up the digits", func="sum_digits",
      prompt="<p>Write <code>sum_digits(n)</code> recursively, for <code>n &gt;= 0</code>. Return the sum of its digits. Do not convert to a string.</p><p>Example: <code>sum_digits(4096)</code> returns <code>19</code>.</p>",
      starter="def sum_digits(n):\n    pass\n",
      tests=[("given example", [4096], False), ("one digit", [7], False), ("zero", [0], True), ("all nines", [999], True), ("big number", [10 ** 15 + 5], True)],
      hints=["Base case: a single digit (<code>n &lt; 10</code>) is its own sum.", "Otherwise: last digit <code>n % 10</code> plus the sum of the rest, <code>n // 10</code>."],
      solution=DIGITS, explain="One call per digit: <b>O(d)</b> time and <b>O(d)</b> call-stack space for d digits.",
      vid=[("Recursion, easy. Add up the digits of a number, no strings.", [("b", "sum_digits(4096) = 4 + 0 + 9 + 6 = 19")]),
           ("Base case first. Always. A single digit is its own answer.", [("clear",), ("code", DIGITS.splitlines()), ("hl", [1, 2])]),
           ("Otherwise, peel off the last digit with percent ten, and trust recursion for the rest, with floor divide ten.", [("hl", [3])]),
           ("4096 becomes 6 plus the digits of 409. Smaller every time, so it must stop.", [("b", "4096 -> 6 + sum_digits(409) -> ...")]),
           ("Base case, smaller problem, trust it. That's recursion. Every single time.", [("cap", "Base case first, then shrink the problem.")])]),
 dict(level="Medium", title="Power, the fast way", func="fast_power",
      prompt="<p>Write <code>fast_power(base, exp)</code> recursively for whole numbers, <code>exp &gt;= 0</code>, without <code>**</code> or <code>pow</code>. Aim for O(log exp) multiplications by halving the exponent.</p><p>Example: <code>fast_power(3, 5)</code> returns <code>243</code>.</p>",
      starter="def fast_power(base, exp):\n    pass\n",
      tests=[("given example", [3, 5], False), ("exponent zero", [9, 0], False), ("power of two", [2, 10], True),
             ("negative base", [-2, 3], True), ("base one", [1, 1000], True), ("huge exponent", [1, 10 ** 6], True)],
      hints=["base^exp = (base^(exp // 2))² when exp is even, and that times base when it is odd.", "Call yourself once for the half and store it in a variable; calling it twice loses the speed-up."],
      solution=POWER, explain="The exponent halves each call: <b>O(log exp)</b> calls and multiplications, <b>O(log exp)</b> stack space.",
      vid=[("Recursion, medium. Power, the fast way. Three to the five, without the star star.", [("b", "fast_power(3, 5) = 243")]),
           ("Multiplying five times is O of n. With a million, that's a million steps. We halve instead.", [("clear",), ("code", POWER.splitlines()), ("hl", [1, 2])]),
           ("Work out the power for half the exponent, once, and store it.", [("hl", [3])]),
           ("Even exponent? Half times half. Odd? Half times half times base.", [("hl", [4, 5, 6])]),
           ("A million becomes about twenty calls. Divide and conquer. Massive speed-up, tiny code.", [("cap", "Halve the problem, solve it once, reuse it.")])]),
 dict(level="Hard", title="Every balanced bracket string", func="all_brackets",
      prompt="<p>Write <code>all_brackets(n)</code>. Return every string of n pairs of round brackets that is balanced, in alphabetical order (\"(\" comes before \")\").</p><p>Example: <code>all_brackets(2)</code> returns <code>[\"(())\", \"()()\"]</code>.</p>",
      starter="def all_brackets(n):\n    pass\n",
      tests=[("given example", [2], False), ("one pair", [1], False), ("three pairs", [3], True), ("zero pairs", [0], True), ("four pairs", [4], True)],
      hints=["Build the string one character at a time. You may add \"(\" while fewer than n are open, and \")\" while fewer are closed than opened.", "When the string reaches length 2n, record it. Trying \"(\" before \")\" gives alphabetical order for free."],
      solution=BRACKETS, explain="One call per valid prefix; the number of answers grows quickly (the Catalan numbers), so time is proportional to the output. Stack depth is <b>O(n)</b>.",
      vid=[("Recursion, hard. Every balanced string of n bracket pairs. This is backtracking.", [("b", "n = 2: (()) and ()()")]),
           ("Build the string one character at a time, with a helper that remembers how many we've opened and closed.", [("clear",), ("code", BRACKETS.splitlines()), ("hl", [2])]),
           ("Base case: the string is full length. Record it, go back.", [("hl", [3, 4, 5])]),
           ("Two choices. Open a bracket if we haven't used all n. Close one only if something is open. Those rules mean we never build a bad string.", [("hl", [6, 7, 8, 9])]),
           ("Try open first, and the answers come out in alphabetical order for free. Choose, recurse, undo: backtracking. Championship level.", [("cap", "Backtracking: only make choices that can still work.")])]),
]

# ---------------------------------------------------------------- Sorting
TOP3 = S('''
def top_three(scores):
    return sorted(scores, reverse=True)[:3]
''')
MERGE_LISTS = S('''
def merge_lists(a, b):
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    return out + a[i:] + b[j:]
''')
INTERVALS = S('''
def merge_slots(slots):
    slots = sorted(slots)               # by start time
    merged = []
    for start, end in slots:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
''')
LADDER_B["sorting"] = [
 dict(level="Easy", title="Top three scores", func="top_three",
      prompt="<p>Write <code>top_three(scores)</code>. Return the three highest scores, highest first. If there are fewer than three, return them all, highest first. Repeated scores count separately.</p><p>Example: <code>top_three([40, 90, 75, 90, 10])</code> returns <code>[90, 90, 75]</code>.</p>",
      starter="def top_three(scores):\n    pass\n",
      tests=[("given example", [[40, 90, 75, 90, 10]], False), ("two scores", [[5, 9]], False), ("empty", [[]], True),
             ("negatives", [[-5, -1, -3, -2]], True), ("already sorted", [[1, 2, 3, 4]], True), ("100,000 scores", [{"__py__": "[(i * 37) % 1000 for i in range(100000)]"}], True)],
      hints=["Sort highest first with <code>reverse=True</code>.", "Slice the first three: <code>[:3]</code> never fails on a short list."],
      solution=TOP3, explain="Sorting dominates: <b>O(n log n)</b> time, <b>O(n)</b> space for the sorted copy. (heapq.nlargest(3, ...) would be O(n).)",
      vid=[("Sorting, easy. The top three scores, highest first.", [("b", "[40, 90, 75, 90, 10] gives [90, 90, 75]")]),
           ("Python's sorted, with reverse equals true, gives highest first.", [("clear",), ("code", TOP3.splitlines()), ("hl", [1])]),
           ("Then slice the first three. If there are only two, the slice just gives two. No crash.", [("b", "[:3] is safe on short lists")]),
           ("O of n log n. Want to show off? heapq dot nlargest does it in O of n. Mention it. Interviewers love that.", [("cap", "Top k: sort and slice, or heapq.nlargest.")])]),
 dict(level="Medium", title="Merge two sorted lists", func="merge_lists",
      prompt="<p>Write <code>merge_lists(a, b)</code>. Both lists are sorted. Return one sorted list with every value, in O(n + m), without calling <code>sorted</code>.</p><p>Example: <code>merge_lists([1, 4, 9], [2, 3, 10])</code> returns <code>[1, 2, 3, 4, 9, 10]</code>.</p>",
      starter="def merge_lists(a, b):\n    pass\n",
      tests=[("given example", [[1, 4, 9], [2, 3, 10]], False), ("one empty", [[], [1, 2]], False), ("both empty", [[], []], True),
             ("repeats", [[1, 1, 3], [1, 2]], True), ("all of b first", [[7, 8], [1, 2]], True),
             ("long lists, short check", [{"__py__": "list(range(0, 10, 2))"}, {"__py__": "list(range(1, 10, 2))"}], True)],
      hints=["One index into each list. Take the smaller front value and move that index on.", "When one list runs out, add the rest of the other: <code>out + a[i:] + b[j:]</code>."],
      solution=MERGE_LISTS, explain="Each value is copied once: <b>O(n + m)</b> time and space.",
      vid=[("Sorting, medium. Merge two sorted lists, without calling sorted.", [("b", "[1, 4, 9] and [2, 3, 10] give [1, 2, 3, 4, 9, 10]")]),
           ("One finger on each list.", [("clear",), ("code", MERGE_LISTS.splitlines()), ("hl", [1])]),
           ("Compare the two front values. Take the smaller. Move that finger on.", [("hl", [3, 4, 5, 6, 7, 8, 9])]),
           ("One list runs out? The rest of the other is already sorted. Tack it on.", [("hl", [10])]),
           ("O of n plus m. This is the heart of merge sort. Split, sort halves, merge. You just wrote the merge.", [("cap", "Two sorted lists: two pointers, take the smaller.")])]),
 dict(level="Hard", title="Merge overlapping time slots", func="merge_slots",
      prompt="<p>Write <code>merge_slots(slots)</code>. Each slot is <code>[start, end]</code>, in any order. Merge any slots that overlap or touch (one ends exactly when the next starts) and return the merged slots sorted by start.</p><p>Example: <code>merge_slots([[8, 10], [1, 3], [2, 6], [15, 18]])</code> returns <code>[[1, 6], [8, 10], [15, 18]]</code>.</p>",
      starter="def merge_slots(slots):\n    pass\n",
      tests=[("given example", [[[8, 10], [1, 3], [2, 6], [15, 18]]], False), ("touching", [[[1, 4], [4, 5]]], False), ("empty", [[]], True),
             ("one inside another", [[[1, 10], [2, 3], [4, 5]]], True), ("no overlaps", [[[5, 6], [1, 2]]], True),
             ("many into one", [{"__py__": "[[i, i + 2] for i in range(0, 1000, 2)]"}], True)],
      hints=["Sort by start first. Then overlapping slots sit next to each other.", "Walk through: if a slot starts before the last merged one ends, stretch that end with <code>max</code>; otherwise start a new merged slot."],
      solution=INTERVALS, explain="Sorting is O(n log n) and the merge pass is O(n): <b>O(n log n)</b> time, <b>O(n)</b> space.",
      vid=[("Sorting, hard. Merge overlapping time slots. A favourite in interviews.", [("b", "[8,10] [1,3] [2,6] [15,18] -> [1,6] [8,10] [15,18]")]),
           ("Step one: sort by start time. Then anything that overlaps sits right next to each other.", [("clear",), ("code", INTERVALS.splitlines()), ("hl", [1])]),
           ("Walk through. Does this slot start before the last merged one ends? Overlap. Stretch the end, using max.", [("hl", [4, 5])]),
           ("Max matters: a slot completely inside another must not shrink it.", [("b", "[1, 10] then [2, 3]: keep 10, not 3")]),
           ("No overlap? Start a new slot. Sort, then one pass. O of n log n. Sorting first unlocks the whole problem.", [("hl", [6, 7]), ("cap", "Intervals: sort by start, then merge in one pass.")])]),
]

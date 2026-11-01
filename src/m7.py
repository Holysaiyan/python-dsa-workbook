"""Module 7: Project. Build a student housing maintenance desk, one tested milestone at a time."""

MODULE = {"id": "project", "title": "Project: Housing Desk"}

LESSONS = []

SAMPLE = '''LINES = [
    "R1,B12,2,leaking tap",
    "R2,A03,1,no heating",
    "R3,B12,3,squeaky door",
    "bad line with no commas",
    "R4,C07,1,broken lock, urgent",
    "R5,A03,9,priority out of range",
    "R6,B12,2,mould in shower",
]'''

PARSE = '''def parse_requests(lines):
    requests = []
    for line in lines:
        parts = line.split(",", 3)          # the issue may contain commas
        if len(parts) != 4:
            continue
        rid, room, pri, issue = [p.strip() for p in parts]
        if not pri.isdigit() or not 1 <= int(pri) <= 5:
            continue
        requests.append([rid, room, int(pri), issue])
    return requests'''

BUSIEST = '''def busiest_rooms(requests, k):
    counts = {}
    for rid, room, pri, issue in requests:
        counts[room] = counts.get(room, 0) + 1
    ranked = sorted(counts, key=lambda room: (-counts[room], room))
    return ranked[:k]'''

NEXT = '''import heapq

def next_jobs(requests, k):
    heap = []
    for order, (rid, room, pri, issue) in enumerate(requests):
        heapq.heappush(heap, (pri, order, rid))   # lowest priority number first, then oldest
    return [heapq.heappop(heap)[2] for _ in range(min(k, len(heap)))]'''

FIND = '''def find_request(ids, target):
    lo, hi = 0, len(ids) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if ids[mid] == target:
            return mid
        if ids[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1'''

# ---------------------------------------------------------------- brief + milestone 1
LESSONS.append({
    "id": "project-brief",
    "title": "The brief, and milestone 1: read the requests",
    "minutes": 25,
    "tags": ["Accenture", "Lloyds"],
    "summary": "You are building the maintenance desk for a block of student halls: read messy request lines, find the busiest rooms, choose the next urgent jobs and look any request up instantly. Each milestone is auto-tested, and the last lesson joins them into one program.",
    "blocks": [
        ("h", "The brief"),
        ("p", "Students report problems as text lines: <code>id,room,priority,issue</code>. Priority runs from <b>1</b> (most urgent) to <b>5</b>. Some lines are broken. The desk manager wants four things:"),
        ("steps", [
            "<b>Milestone 1: read the requests.</b> Turn the lines into clean records and skip the broken ones. Uses strings, conditions and lists.",
            "<b>Milestone 2: busiest rooms.</b> Which rooms report the most problems? Uses a dictionary and sorting with a key.",
            "<b>Milestone 3: next jobs.</b> Which jobs should the caretaker do next? Uses a heap.",
            "<b>Milestone 4: find a request.</b> Look a request up by its ID among thousands. Uses binary search.",
            "<b>Put it together.</b> One program, run on sample data, plus stretch goals.",
        ]),
        ("p", "This is also a portfolio piece. When an interviewer asks 'tell me about something you built', you can explain each data structure choice and its Big O."),
        ("h", "Milestone 1: read the requests"),
        ("p", "A good line splits into exactly four parts. The issue text itself can contain commas, so split at most 3 times: <code>line.split(\",\", 3)</code>. Then check the priority is a whole number from 1 to 5."),
        ("code", """line = "R4,C07,1,broken lock, urgent"
print(line.split(","))        # too many parts
print(line.split(",", 3))     # at most 3 splits: 4 parts
print("7".isdigit(), "x".isdigit(), "-1".isdigit())"""),
        ("p", "Here is the sample data the whole project uses. Lines 4 and 6 are broken: one has no commas, one has priority 9."),
        ("code", SAMPLE + "\nprint(len(LINES), \"lines\")"),
        ("tip", "Write the skeleton from lesson 1 first: an empty result, a loop, a <code>continue</code> for each way a line can be bad, then the append."),
    ],
    "mistakes": [
        "Splitting on every comma, which breaks issues like 'broken lock, urgent'.",
        "Forgetting to strip spaces, so ' B12' and 'B12' count as different rooms.",
        "Calling <code>int()</code> before checking <code>isdigit()</code>, which crashes on text.",
    ],
    "practice": {
        "title": "Milestone 1: parse the requests",
        "prompt": "<p>Write <code>parse_requests(lines)</code>. Return a list of <code>[id, room, priority, issue]</code> records, with priority as an <code>int</code> and spaces stripped from every field. Skip a line if it does not split into 4 parts with <code>split(\",\", 3)</code>, or if its priority is not a whole number from 1 to 5.</p><p>Example: <code>[\"R1,B12,2,leaking tap\", \"oops\"]</code> gives <code>[[\"R1\", \"B12\", 2, \"leaking tap\"]]</code>.</p>",
        "func": "parse_requests",
        "starter": "def parse_requests(lines):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [["R1,B12,2,leaking tap", "oops"]], False),
            ("comma inside the issue", [["R4,C07,1,broken lock, urgent"]], False),
            ("priority out of range", [["R5,A03,9,too high", "R6,A03,0,too low"]], True),
            ("priority not a number", [["R7,A03,high,bad"]], True),
            ("spaces around fields", [[" R8 , D01 , 3 , flickering light "]], True),
            ("empty input", [[]], True),
            ("full sample", [["R1,B12,2,leaking tap", "R2,A03,1,no heating", "R3,B12,3,squeaky door", "bad line with no commas", "R4,C07,1,broken lock, urgent", "R5,A03,9,priority out of range", "R6,B12,2,mould in shower"]], True),
        ],
        "hints": ["<code>parts = line.split(\",\", 3)</code>, then <code>continue</code> if <code>len(parts) != 4</code>.", "Strip every part, check <code>pri.isdigit()</code> and <code>1 &lt;= int(pri) &lt;= 5</code>, then append with <code>int(pri)</code>."],
        "solution": PARSE + "\n",
        "explain": "Each character of input is handled a constant number of times: <b>O(n)</b> time in the size of the input. The records take <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- milestone 2
LESSONS.append({
    "id": "project-busiest",
    "title": "Milestone 2: the busiest rooms",
    "minutes": 20,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Count requests per room with a dictionary, then sort the rooms by count. A sort key with a minus sign gives 'biggest first', and a second key breaks ties.",
    "blocks": [
        ("p", "Two steps. First count, using the dictionary counting pattern from Module 2. Then rank the rooms."),
        ("h", "Sorting by two things at once"),
        ("p", "A sort key can return a tuple. Python compares the first item, and only looks at the second when the first is a tie. Putting a minus sign on a number sorts it biggest first."),
        ("code", """counts = {"B12": 3, "A03": 2, "C07": 1, "A01": 2}
print(sorted(counts))                                   # alphabetical keys
print(sorted(counts, key=lambda r: -counts[r]))         # most first
print(sorted(counts, key=lambda r: (-counts[r], r)))    # most first, ties A to Z"""),
        ("p", "<code>lambda r: ...</code> is a tiny one-line function. <code>key=lambda r: (-counts[r], r)</code> means 'sort each room by minus its count, then by its name'."),
        ("tip", "Ties are where hidden tests catch people. When a task says 'break ties alphabetically', it always has a test for it."),
    ],
    "mistakes": [
        "Sorting the counts instead of the rooms, and losing which room had which count.",
        "Forgetting the tie-break, so equal rooms come out in a random-looking order.",
        "Slicing <code>[:k]</code> before sorting.",
    ],
    "practice": {
        "title": "Milestone 2: busiest rooms",
        "prompt": "<p>Write <code>busiest_rooms(requests, k)</code>. <code>requests</code> is a list of <code>[id, room, priority, issue]</code> records. Return the <code>k</code> rooms with the most requests, most first. Break ties alphabetically by room. If there are fewer than k rooms, return them all.</p>",
        "func": "busiest_rooms",
        "starter": "def busiest_rooms(requests, k):\n    # your code here\n    pass\n",
        "tests": [
            ("sample, top 2", [[["R1", "B12", 2, "tap"], ["R2", "A03", 1, "heat"], ["R3", "B12", 3, "door"], ["R4", "C07", 1, "lock"], ["R6", "B12", 2, "mould"]], 2], False),
            ("tie broken A to Z", [[["R1", "C1", 1, "x"], ["R2", "A1", 1, "x"], ["R3", "B1", 1, "x"]], 2], False),
            ("k bigger than rooms", [[["R1", "A1", 1, "x"]], 5], True),
            ("no requests", [[], 3], True),
            ("k is zero", [[["R1", "A1", 1, "x"]], 0], True),
            ("count beats alphabet", [[["R1", "Z9", 1, "x"], ["R2", "Z9", 2, "y"], ["R3", "A1", 1, "z"]], 1], True),
        ],
        "hints": ["Count first: <code>counts[room] = counts.get(room, 0) + 1</code>.", "<code>sorted(counts, key=lambda room: (-counts[room], room))[:k]</code>"],
        "solution": BUSIEST + "\n",
        "explain": "Counting is O(n). Sorting r rooms is O(r log r), and r is at most n, so <b>O(n log n)</b> time. The dictionary holds up to n rooms: <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- milestone 3
LESSONS.append({
    "id": "project-next-jobs",
    "title": "Milestone 3: the next jobs",
    "minutes": 20,
    "tags": ["Accenture", "Lloyds"],
    "summary": "The caretaker wants the most urgent jobs first, and the oldest first among equals. A heap of tuples does both: the tuple order is the priority rule.",
    "blocks": [
        ("p", "A heap always gives back its smallest item. If each item is a tuple <code>(priority, order, id)</code>, 'smallest' means lowest priority number first, then the one that arrived first. That is exactly the rule."),
        ("code", """import heapq
heap = []
heapq.heappush(heap, (2, 0, "R1"))
heapq.heappush(heap, (1, 1, "R2"))
heapq.heappush(heap, (1, 2, "R4"))
print(heapq.heappop(heap))   # priority 1, arrived first
print(heapq.heappop(heap))
print(heapq.heappop(heap))"""),
        ("p", "The <code>order</code> number matters: without it, two jobs with the same priority would be compared by ID text, which is not the order they arrived in."),
        ("tip", "Could you just use <code>sorted</code>? Yes, and it is fine here. A heap shines when new jobs keep arriving while you take the next one out, which is how a real desk works."),
    ],
    "mistakes": [
        "Popping from an empty heap when k is bigger than the number of jobs. Use <code>min(k, len(heap))</code>.",
        "Treating 5 as most urgent. Here, 1 is most urgent.",
        "Leaving out the arrival order, so ties come out by ID instead of by age.",
    ],
    "practice": {
        "title": "Milestone 3: next jobs",
        "prompt": "<p>Write <code>next_jobs(requests, k)</code>. Return the IDs of the <code>k</code> most urgent requests: lowest priority number first, and for equal priority, the one that appears earlier in the list first. If there are fewer than k requests, return them all.</p>",
        "func": "next_jobs",
        "starter": "import heapq\n\ndef next_jobs(requests, k):\n    # your code here\n    pass\n",
        "tests": [
            ("sample, top 3", [[["R1", "B12", 2, "tap"], ["R2", "A03", 1, "heat"], ["R3", "B12", 3, "door"], ["R4", "C07", 1, "lock"], ["R6", "B12", 2, "mould"]], 3], False),
            ("ties keep arrival order", [[["R9", "A1", 3, "x"], ["R1", "A2", 3, "y"]], 2], False),
            ("k bigger than jobs", [[["R1", "A1", 4, "x"]], 3], True),
            ("no jobs", [[], 2], True),
            ("ties not by ID", [[["R5", "A1", 1, "x"], ["R2", "A1", 1, "y"], ["R3", "A1", 2, "z"]], 2], True),
        ],
        "hints": ["Push <code>(pri, order, rid)</code> for each request, using <code>enumerate</code> for <code>order</code>.", "Pop <code>min(k, len(heap))</code> times and keep the ID, which is item <code>[2]</code>."],
        "solution": NEXT + "\n",
        "explain": "n pushes and up to k pops, each O(log n): <b>O(n log n)</b> time in the worst case. The heap holds n items: <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- milestone 4
LESSONS.append({
    "id": "project-find",
    "title": "Milestone 4: find a request fast",
    "minutes": 15,
    "tags": ["Accenture", "Lloyds"],
    "summary": "With thousands of requests kept in ID order, binary search finds any one in about 12 steps instead of checking each in turn.",
    "blocks": [
        ("p", "The desk keeps request IDs sorted, padded to the same length so text order matches number order: <code>\"R0001\"</code>, <code>\"R0002\"</code> and so on. Because the list is sorted, you can use binary search from Module 4."),
        ("code", """ids = [f"R{n:04d}" for n in range(1, 4001)]   # R0001 to R4000
print(ids[:3], ids[-1])
print("R0010" < "R0100", "R10" < "R9")         # why padding matters"""),
        ("p", "Without padding, <code>\"R10\" &lt; \"R9\"</code> is True, because text compares character by character. Sorted text would then be in the wrong number order and binary search would fail."),
        ("tip", "Binary search bugs are nearly always in three places: <code>lo &lt;= hi</code>, <code>mid + 1</code> and <code>mid - 1</code>. Check those three before anything else."),
    ],
    "mistakes": [
        "Using <code>lo &lt; hi</code>, which misses a one-item range.",
        "Setting <code>lo = mid</code> instead of <code>mid + 1</code>, which can loop forever.",
        "Searching unsorted data.",
    ],
    "practice": {
        "title": "Milestone 4: find a request",
        "prompt": "<p>Write <code>find_request(ids, target)</code>. <code>ids</code> is a sorted list of ID strings. Return the index of <code>target</code>, or <code>-1</code> if it is not there. Use binary search: the hidden test has 200,000 IDs.</p>",
        "func": "find_request",
        "starter": "def find_request(ids, target):\n    # your code here\n    pass\n",
        "tests": [
            ("in the middle", [["R0001", "R0002", "R0003", "R0004", "R0005"], "R0003"], False),
            ("not there", [["R0001", "R0003"], "R0002"], False),
            ("first item", [["R0001", "R0002"], "R0001"], True),
            ("last item", [["R0001", "R0002", "R0009"], "R0009"], True),
            ("empty list", [[], "R0001"], True),
            ("200,000 ids", [{"__py__": "[f'R{n:06d}' for n in range(200000)]"}, "R123456"], True),
        ],
        "hints": ["Keep <code>lo</code> and <code>hi</code>, look at <code>mid = (lo + hi) // 2</code>.", "Too small: <code>lo = mid + 1</code>. Too big: <code>hi = mid - 1</code>. Loop while <code>lo &lt;= hi</code>."],
        "solution": FIND + "\n",
        "explain": "Each step halves the range: <b>O(log n)</b> time, and only a few variables: <b>O(1)</b> space.",
    },
})

# ---------------------------------------------------------------- put it together
LESSONS.append({
    "id": "project-together",
    "title": "Put it together, and stretch goals",
    "minutes": 25,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Join the four milestones into one HousingDesk class and run it on the sample data. Then extend it, and practise explaining every choice as you would in an interview.",
    "blocks": [
        ("p", "Here is the whole desk. Read it top to bottom: every function is one you have already written and tested. Run it, then change the sample lines and run it again."),
        ("code", SAMPLE + "\n\n" + PARSE + "\n\n" + BUSIEST + "\n\n" + NEXT + "\n\n" + FIND + '''


class HousingDesk:
    def __init__(self, lines):
        self.requests = parse_requests(lines)
        self.by_id = {r[0]: r for r in self.requests}    # O(1) lookup by ID
        self.ids = sorted(self.by_id)

    def report(self):
        print(len(self.requests), "valid requests")
        print("Busiest rooms:", busiest_rooms(self.requests, 2))
        print("Do next:", next_jobs(self.requests, 3))

    def lookup(self, rid):
        i = find_request(self.ids, rid)
        return self.by_id[self.ids[i]] if i != -1 else None


desk = HousingDesk(LINES)
desk.report()
print(desk.lookup("R4"))
print(desk.lookup("R99"))'''),
        ("p", "Notice <code>self.by_id</code>: a dictionary already gives O(1) lookup by ID, which is even faster than binary search. Binary search earns its place when you need ranges, such as 'every request between R2000 and R2100'. Saying that in an interview shows real judgement."),
        ("h", "Stretch goals"),
        ("steps", [
            "<b>Close a job.</b> Add <code>close(rid)</code> that removes a request. Which structures need updating?",
            "<b>Live queue.</b> Keep the heap inside the class so new requests can be added while jobs are taken off.",
            "<b>Repeat problems.</b> Flag any room with 3 or more requests in a row of 10 using a sliding window.",
            "<b>Routes.</b> Store which rooms connect by corridors as a graph and use BFS to plan the caretaker's shortest walk.",
            "<b>Save to a file.</b> Read the lines from <code>requests.txt</code> with <code>open()</code> and run it on your own computer.",
        ]),
        ("h", "Your interview story"),
        ("p", "Practise saying this in under two minutes: what it does, the data structure for each feature and why, the Big O of each, one bug you hit and how you found it, and what you would add next. Your STAR stories can use it too."),
    ],
    "mistakes": [
        "Copying the code without running it. Change the data and predict the output first.",
        "Describing the project by listing features, instead of explaining choices and trade-offs.",
    ],
    "practice": None,
})

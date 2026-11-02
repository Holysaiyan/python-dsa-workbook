"""Module: Lloyds-style tasks. Input validation, a transactional key-value store, and weighted graphs."""

MODULE = {"id": "lloyds", "title": "Lloyds-style tasks"}

LESSONS = []

PAY = '''import json

def handle_payment(body):
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return {"status": 400, "error": "invalid JSON"}
    if not isinstance(data, dict):
        return {"status": 400, "error": "body must be an object"}
    for field in ("account", "amount", "currency"):
        if field not in data:
            return {"status": 400, "error": "missing field: " + field}
    amount = data["amount"]
    if isinstance(amount, bool) or not isinstance(amount, (int, float)) or amount <= 0:
        return {"status": 422, "error": "amount must be a positive number"}
    if data["currency"] != "GBP":
        return {"status": 422, "error": "unsupported currency"}
    return {"status": 201, "account": data["account"], "amount": amount}'''

# ---------------------------------------------------------------- JSON validation
LESSONS.append({
    "id": "json-validation",
    "title": "Validating JSON input",
    "minutes": 25,
    "tags": ["Lloyds"],
    "summary": "An API endpoint receives text it cannot trust. Parse it safely, check its shape, check each field, and answer with a clear status code instead of crashing. This is the first Lloyds task.",
    "blocks": [
        ("p", "An endpoint gets a request <b>body</b>: a string of JSON. Anything can arrive: broken JSON, a list instead of an object, missing fields, a number written as text. Your handler must never crash. It returns a status code and a message instead."),
        ("table", ["Status", "Meaning", "Use it when"], [
            ["<code>200</code> / <code>201</code>", "OK / created", "Everything was valid"],
            ["<code>400</code>", "Bad request", "The body cannot be read: invalid JSON, wrong shape, missing field"],
            ["<code>422</code>", "Unprocessable", "The body is readable but a value breaks a rule: negative amount, unknown currency"],
            ["<code>404</code>", "Not found", "The thing asked for does not exist"],
        ]),
        ("h", "Step 1: parse safely"),
        ("code", """import json

for body in ['{"amount": 10}', '{amount: 10}', '']:
    try:
        data = json.loads(body)
        print("parsed:", data)
    except json.JSONDecodeError:
        print("invalid JSON:", repr(body))"""),
        ("p", "<code>json.loads</code> turns JSON text into Python: objects become dicts, arrays become lists, <code>true</code> becomes <code>True</code>, <code>null</code> becomes <code>None</code>. Bad text raises <code>json.JSONDecodeError</code>. Catch that exact error, not every error, so real bugs still show up."),
        ("h", "Step 2: check the shape, then each field"),
        ("code", """import json

def check(body):
    data = json.loads(body)
    if not isinstance(data, dict):
        return "body must be an object"
    if "amount" not in data:
        return "missing field: amount"
    a = data["amount"]
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        return "amount must be a number"
    return "ok"

print(check('[1, 2]'))
print(check('{"name": "Ana"}'))
print(check('{"amount": "10"}'))
print(check('{"amount": true}'))
print(check('{"amount": 10.5}'))"""),
        ("tip", "In Python, <code>True</code> counts as an <code>int</code>: <code>isinstance(True, int)</code> is True. Hidden tests love sending <code>true</code> as an amount. Rule booleans out first."),
        ("h", "A full handler"),
        ("p", "Check in a fixed order and return at the first problem. The order is part of the specification, so follow the task exactly: parse, shape, required fields, then the rules for each value."),
        ("code", PAY + """

print(handle_payment('{"account": "A1", "amount": 25, "currency": "GBP"}'))
print(handle_payment('{"account": "A1", "amount": -5, "currency": "GBP"}'))
print(handle_payment('{"account": "A1"}'))
print(handle_payment('not json'))"""),
    ],
    "mistakes": [
        "Catching every exception with a bare <code>except:</code>, which hides your own bugs.",
        "Forgetting that <code>True</code> passes an <code>isinstance(x, int)</code> check.",
        "Checking rules in a different order from the task, so the error message does not match the test.",
        "Accepting a number sent as text, like <code>\"10\"</code>, when the task says number.",
    ],
    "practice": {
        "title": "Payment endpoint",
        "prompt": "<p>Write <code>handle_payment(body)</code>. <code>body</code> is a string. Check in this order and return a dict:</p><ol><li>Not valid JSON: <code>{\"status\": 400, \"error\": \"invalid JSON\"}</code></li><li>Not a JSON object: <code>{\"status\": 400, \"error\": \"body must be an object\"}</code></li><li>Missing any of <code>account</code>, <code>amount</code>, <code>currency</code> (check in that order): <code>{\"status\": 400, \"error\": \"missing field: NAME\"}</code></li><li><code>amount</code> not a number above 0 (booleans are not numbers): <code>{\"status\": 422, \"error\": \"amount must be a positive number\"}</code></li><li><code>currency</code> not <code>\"GBP\"</code>: <code>{\"status\": 422, \"error\": \"unsupported currency\"}</code></li><li>Otherwise: <code>{\"status\": 201, \"account\": ..., \"amount\": ...}</code></li></ol>",
        "func": "handle_payment",
        "starter": "import json\n\ndef handle_payment(body):\n    # your code here\n    pass\n",
        "tests": [
            ("valid payment", ['{"account": "A1", "amount": 25, "currency": "GBP"}'], False),
            ("broken JSON", ['{"account": "A1",'], False),
            ("a list, not an object", ['[1, 2, 3]'], True),
            ("missing amount", ['{"account": "A1", "currency": "GBP"}'], True),
            ("missing two fields: first one named", ['{"currency": "GBP"}'], True),
            ("amount as text", ['{"account": "A1", "amount": "25", "currency": "GBP"}'], True),
            ("amount is true", ['{"account": "A1", "amount": true, "currency": "GBP"}'], True),
            ("zero amount", ['{"account": "A1", "amount": 0, "currency": "GBP"}'], True),
            ("wrong currency", ['{"account": "A1", "amount": 5, "currency": "EUR"}'], True),
            ("decimal amount", ['{"account": "B7", "amount": 12.5, "currency": "GBP"}'], True),
            ("empty body", [''], True),
        ],
        "hints": ["Wrap only <code>json.loads</code> in <code>try</code> / <code>except json.JSONDecodeError</code>, then check <code>isinstance(data, dict)</code>.", "Loop over the three field names in order for the missing check. For the amount, reject <code>bool</code> first, then require <code>int</code> or <code>float</code> and <code>&gt; 0</code>."],
        "solution": PAY + "\n",
        "explain": "Parsing reads the body once: <b>O(n)</b> time in its length, and the parsed data takes <b>O(n)</b> space. The checks themselves are a fixed number of steps.",
    },
})

KV = '''class KVStore:
    def __init__(self):
        self.data = {}
        self.layers = []            # one dict of changes per open transaction

    def get(self, key):
        for layer in reversed(self.layers):     # newest change wins
            if key in layer:
                return layer[key]               # None means deleted
        return self.data.get(key)

    def set(self, key, value):
        if self.layers:
            self.layers[-1][key] = value
        else:
            self.data[key] = value

    def delete(self, key):
        if self.layers:
            self.layers[-1][key] = None
        else:
            self.data.pop(key, None)

    def begin(self):
        self.layers.append({})

    def rollback(self):
        if not self.layers:
            return False
        self.layers.pop()
        return True

    def commit(self):
        if not self.layers:
            return False
        top = self.layers.pop()
        if self.layers:
            self.layers[-1].update(top)         # merge into the outer transaction
        else:
            for k, v in top.items():
                if v is None:
                    self.data.pop(k, None)
                else:
                    self.data[k] = v
        return True'''

KV_WRAP = '''def __call(commands):
    s = KVStore()
    out = []
    for c in commands:
        op = c[0]
        if op == "SET":
            s.set(c[1], c[2])
        elif op == "GET":
            v = s.get(c[1])
            out.append("NULL" if v is None else v)
        elif op == "DELETE":
            s.delete(c[1])
        elif op == "BEGIN":
            s.begin()
        elif op in ("COMMIT", "ROLLBACK"):
            ok = s.commit() if op == "COMMIT" else s.rollback()
            if ok is False:
                out.append("NO TRANSACTION")
    return out
'''

# ---------------------------------------------------------------- transactional store
LESSONS.append({
    "id": "kv-transactions",
    "title": "Transactional key-value store",
    "minutes": 30,
    "tags": ["Lloyds"],
    "summary": "A store that can undo: changes made inside a transaction are kept separate until commit, thrown away on rollback, and transactions can nest. A stack of dictionaries does all of it. This is the second Lloyds task.",
    "blocks": [
        ("p", "A key-value store is a dictionary with rules. The interesting part is <b>transactions</b>: <code>begin</code> starts a group of changes, <code>rollback</code> throws that group away, <code>commit</code> keeps it. Banks use exactly this idea so a half-finished transfer never shows up."),
        ("h", "The idea: a stack of change layers"),
        ("p", "Keep the committed data in one dict. Each <code>begin</code> pushes an empty dict of changes onto a stack. Writes go into the top layer. Reads look from the top layer down to the committed data. Rollback pops the top layer. Commit pops it and merges it one level down."),
        ("code", """data = {"a": 1}
layers = []

layers.append({})          # BEGIN
layers[-1]["a"] = 2        # SET a 2, inside the transaction

def get(key):
    for layer in reversed(layers):
        if key in layer:
            return layer[key]
    return data.get(key)

print(get("a"))            # 2: the transaction sees its own change
layers.pop()               # ROLLBACK
print(get("a"))            # 1: as if it never happened"""),
        ("h", "Deletes inside a transaction"),
        ("p", "You cannot just remove the key from the top layer: the old value underneath would show through again. Store a marker that means 'deleted', such as <code>None</code>, and treat it as missing when you read."),
        ("tip", "Draw the stack on paper for nested cases: <code>BEGIN, SET, BEGIN, SET, ROLLBACK, GET</code>. The inner rollback only removes the inner layer. Tests are built from exactly these sequences."),
        ("h", "The full store"),
        ("code", KV + """


s = KVStore()
s.set("a", "10")
s.begin(); s.set("a", "20")
s.begin(); s.delete("a")
print(s.get("a"))      # None: deleted in the inner transaction
s.rollback()
print(s.get("a"))      # 20: inner change undone
s.commit()
print(s.get("a"), s.commit())   # 20 False: nothing left to commit"""),
    ],
    "mistakes": [
        "Writing straight into the committed data during a transaction, so rollback cannot undo it.",
        "Deleting a key from the top layer instead of marking it deleted, so an old value reappears.",
        "Committing the inner transaction straight to the committed data instead of into the outer transaction.",
        "Crashing on <code>commit</code> or <code>rollback</code> when no transaction is open.",
    ],
    "practice": {
        "title": "Store with nested transactions",
        "prompt": "<p>Write the class <code>KVStore</code> with <code>set(key, value)</code>, <code>get(key)</code> (the value, or <code>None</code> if missing or deleted), <code>delete(key)</code>, <code>begin()</code>, <code>commit()</code> and <code>rollback()</code>. Transactions can nest. <code>commit</code> merges the newest transaction into the one below it (or into the saved data if it was the only one). <code>commit</code> and <code>rollback</code> return <code>False</code> if no transaction is open, otherwise <code>True</code>.</p><p>The checker runs a list of commands and collects outputs: each <code>GET</code> gives the value or <code>\"NULL\"</code>, and a <code>COMMIT</code> or <code>ROLLBACK</code> with nothing open gives <code>\"NO TRANSACTION\"</code>.</p>",
        "func": "KVStore",
        "starter": "class KVStore:\n    def __init__(self):\n        pass\n\n    def get(self, key):\n        pass\n\n    def set(self, key, value):\n        pass\n\n    def delete(self, key):\n        pass\n\n    def begin(self):\n        pass\n\n    def commit(self):\n        pass\n\n    def rollback(self):\n        pass\n",
        "wrapper": KV_WRAP,
        "tests": [
            ("set and get", [[["SET", "a", "1"], ["GET", "a"], ["GET", "b"]]], False),
            ("rollback undoes", [[["SET", "a", "1"], ["BEGIN"], ["SET", "a", "2"], ["GET", "a"], ["ROLLBACK"], ["GET", "a"]]], False),
            ("commit keeps", [[["BEGIN"], ["SET", "x", "5"], ["COMMIT"], ["GET", "x"], ["ROLLBACK"]]], True),
            ("nested rollback is inner only", [[["BEGIN"], ["SET", "a", "1"], ["BEGIN"], ["SET", "a", "2"], ["ROLLBACK"], ["GET", "a"], ["ROLLBACK"], ["GET", "a"]]], True),
            ("delete inside a transaction", [[["SET", "k", "v"], ["BEGIN"], ["DELETE", "k"], ["GET", "k"], ["ROLLBACK"], ["GET", "k"]]], True),
            ("inner commit then outer rollback", [[["BEGIN"], ["BEGIN"], ["SET", "a", "9"], ["COMMIT"], ["GET", "a"], ["ROLLBACK"], ["GET", "a"]]], True),
            ("nothing open", [[["COMMIT"], ["ROLLBACK"]]], True),
            ("committed delete", [[["SET", "a", "1"], ["BEGIN"], ["DELETE", "a"], ["COMMIT"], ["GET", "a"]]], True),
        ],
        "hints": ["Keep <code>self.data</code> for committed values and <code>self.layers</code>, a list of dicts, for open transactions. <code>set</code> and <code>delete</code> write to <code>self.layers[-1]</code> when it exists.", "<code>get</code> searches <code>reversed(self.layers)</code> first. <code>commit</code> pops the top layer and either <code>update</code>s the next layer or applies it to <code>self.data</code>, removing keys marked <code>None</code>."],
        "solution": KV + "\n",
        "explain": "<code>set</code>, <code>delete</code>, <code>begin</code> and <code>rollback</code> are O(1). <code>get</code> is <b>O(d)</b> for d open transactions, and <code>commit</code> is <b>O(c)</b> for the c changes it merges. Space is <b>O(n)</b> for all stored keys and changes.",
    },
})

DIJ = '''import heapq

def quickest_time(edges, start, end):
    graph = {}
    for a, b, mins in edges:
        graph.setdefault(a, []).append((b, mins))
        graph.setdefault(b, []).append((a, mins))
    best = {start: 0}
    heap = [(0, start)]
    while heap:
        t, node = heapq.heappop(heap)
        if node == end:
            return t
        if t > best.get(node, float("inf")):
            continue                     # an old, slower entry
        for nxt, mins in graph.get(node, []):
            nt = t + mins
            if nt < best.get(nxt, float("inf")):
                best[nxt] = nt
                heapq.heappush(heap, (nt, nxt))
    return -1'''

# ---------------------------------------------------------------- weighted graphs
LESSONS.append({
    "id": "graph-distances",
    "title": "Graphs: distances and reachability",
    "minutes": 30,
    "tags": ["Lloyds"],
    "summary": "Lesson 18 found the fewest steps with BFS. Real networks have costs on each link: minutes, pounds, distance. Dijkstra's algorithm finds the cheapest route, and BFS still answers 'can I get there at all?'. This is the third Lloyds task.",
    "blocks": [
        ("p", "Graph tasks come with a list of connections. Turn it into an <b>adjacency dict</b> first: each node maps to its neighbours. For links with a cost, store pairs of <code>(neighbour, cost)</code>."),
        ("code", """edges = [["A", "B", 4], ["A", "C", 1], ["C", "B", 2], ["B", "D", 5]]
graph = {}
for a, b, cost in edges:
    graph.setdefault(a, []).append((b, cost))
    graph.setdefault(b, []).append((a, cost))   # two-way links
for node in sorted(graph):
    print(node, graph[node])"""),
        ("h", "Which tool?"),
        ("table", ["Question", "Tool", "Time"], [
            ["Can I reach it? Which nodes are connected?", "BFS or DFS with a <code>seen</code> set", "O(V + E)"],
            ["Fewest steps, every link equal", "BFS", "O(V + E)"],
            ["Cheapest or quickest, links have costs", "Dijkstra with a heap", "O(E log V)"],
            ["How many separate networks?", "Run BFS from each unseen node and count", "O(V + E)"],
        ]),
        ("h", "Dijkstra in one sentence"),
        ("p", "Always expand the node you can reach most cheaply so far, using a heap ordered by total cost. The first time you pop the destination, that cost is the cheapest possible, because every other route still waiting already costs more. It needs costs that are never negative."),
        ("code", DIJ + """

edges = [["A", "B", 4], ["A", "C", 1], ["C", "B", 2], ["B", "D", 5]]
print(quickest_time(edges, "A", "D"))   # A-C-B-D = 1 + 2 + 5
print(quickest_time(edges, "A", "Z"))"""),
        ("tip", "Fewer stops is not always quicker. A to B direct takes 4, but A to C to B takes 3. That is the difference between BFS and Dijkstra, and tests are built around it."),
    ],
    "mistakes": [
        "Using BFS when the links have different costs: it finds the fewest links, not the cheapest route.",
        "Forgetting links go both ways when the task says connections are two-way.",
        "Not skipping stale heap entries, which is slower and can give wrong totals if you also update on them.",
        "Crashing when the start or end node has no links at all. Use <code>graph.get(node, [])</code>.",
    ],
    "practice": {
        "title": "Quickest journey",
        "prompt": "<p>Write <code>quickest_time(edges, start, end)</code>. Each edge is <code>[a, b, minutes]</code>, a two-way link. Return the smallest total minutes from <code>start</code> to <code>end</code>, or <code>-1</code> if you cannot get there. From a node to itself is 0.</p><p>Example: with <code>[[\"A\",\"B\",4],[\"A\",\"C\",1],[\"C\",\"B\",2],[\"B\",\"D\",5]]</code>, A to D is <code>8</code>.</p>",
        "func": "quickest_time",
        "starter": "import heapq\n\ndef quickest_time(edges, start, end):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [[["A", "B", 4], ["A", "C", 1], ["C", "B", 2], ["B", "D", 5]], "A", "D"], False),
            ("more stops is quicker", [[["A", "B", 10], ["A", "C", 2], ["C", "D", 2], ["D", "B", 2]], "A", "B"], False),
            ("unreachable", [[["A", "B", 1], ["C", "D", 1]], "A", "D"], True),
            ("start is end", [[["A", "B", 3]], "A", "A"], True),
            ("two-way links", [[["B", "A", 7]], "A", "B"], True),
            ("unknown node", [[["A", "B", 1]], "A", "Q"], True),
            ("long chain", [{"__py__": "[[i, i + 1, 1] for i in range(300)]"}, 0, 300], True),
        ],
        "hints": ["Build an adjacency dict of <code>(neighbour, minutes)</code> pairs, both directions.", "Heap of <code>(time so far, node)</code>. Pop the smallest; if it is the end, return its time. Push a neighbour only when you have found a quicker time to it than before."],
        "solution": DIJ + "\n",
        "explain": "Each edge can push one heap entry and each push or pop is O(log E): <b>O(E log E)</b>, usually written <b>O(E log V)</b>. Space is <b>O(V + E)</b> for the graph, the heap and the best times.",
    },
})

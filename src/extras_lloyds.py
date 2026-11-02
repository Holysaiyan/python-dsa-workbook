"""Mastery material for the Lloyds-style tasks module."""

T_STD = ["O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n\u00b2)"]
S_STD = ["O(1)", "O(log n)", "O(n)", "O(n\u00b2)"]
BUG = "This version passes some tests and fails others. Find the bug and fix it."

EXTRAS_LLOYDS = {}

EXTRAS_LLOYDS["json-validation"] = {
    "limit": 20,
    "complexity": {"time": ["O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Parsing reads the whole body once and builds a structure of the same size; the checks are a fixed number of steps."},
    "quiz": [
        {"q": "What does this print?", "code": "import json\nprint(type(json.loads('[1, 2]')).__name__, json.loads('null'), json.loads('true'))",
         "options": ["@run", "list None true", "dict None True", "list null True"], "why": "Arrays become lists, null becomes None, true becomes True."},
        {"q": "What does this print?", "code": "print(isinstance(True, int), isinstance(1.5, int))",
         "options": ["@run", "False False", "True True", "False True"], "why": "bool is a kind of int in Python, so True passes an int check. Rule booleans out first."},
        {"q": "The body is readable JSON but the amount is negative. Which status fits best?",
         "options": ["400: bad request", "422: unprocessable", "500: server error", "201: created"], "answer": 1,
         "why": "400 is for a body you cannot read or that has the wrong shape; 422 is for readable data that breaks a rule. 500 means your code failed, which should never happen on bad input."},
        {"q": "Why catch <code>json.JSONDecodeError</code> rather than using a bare <code>except:</code>?",
         "options": ["It is faster", "A bare except also hides your own bugs, like a typo, and turns them into a fake 'invalid JSON' answer", "A bare except is a syntax error"], "answer": 1,
         "why": "Catch the narrowest error you expect. Anything else should show up while you test."},
    ],
    "debug": {"intro": BUG,
              "starter": "import json\n\ndef handle_payment(body):\n    try:\n        data = json.loads(body)\n    except json.JSONDecodeError:\n        return {\"status\": 400, \"error\": \"invalid JSON\"}\n    if not isinstance(data, dict):\n        return {\"status\": 400, \"error\": \"body must be an object\"}\n    for field in (\"account\", \"amount\", \"currency\"):\n        if field not in data:\n            return {\"status\": 400, \"error\": \"missing field: \" + field}\n    amount = data[\"amount\"]\n    if not isinstance(amount, (int, float)) or amount < 0:\n        return {\"status\": 422, \"error\": \"amount must be a positive number\"}\n    if data[\"currency\"] != \"GBP\":\n        return {\"status\": 422, \"error\": \"unsupported currency\"}\n    return {\"status\": 201, \"account\": data[\"account\"], \"amount\": amount}\n",
              "hint": "Two values slip through the amount check: one that is not really a number, and one that is not above zero.",
              "extra_tests": [("amount is true (visible)", ['{"account": "A1", "amount": true, "currency": "GBP"}'], False)]},
}

EXTRAS_LLOYDS["kv-transactions"] = {
    "limit": 30,
    "complexity": {"time": ["O(1)", "O(n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "Writes and rollback are O(1). A get may look through every open layer, and a commit copies the changes it merges, so the worst case per command grows with the data: O(n). Space holds every key and change."},
    "quiz": [
        {"q": "What does this print?", "code": "data = {\"a\": 1}\nlayers = [{}]\nlayers[-1][\"a\"] = 2\nlayers.pop()\nprint(data[\"a\"])",
         "options": ["@run", "2", "None", "Error"], "why": "The change lived only in the popped layer, so the committed value is untouched. That is a rollback."},
        {"q": "Why mark a deleted key as <code>None</code> in the top layer instead of removing it?",
         "options": ["It uses less memory", "Removing it would let the older value underneath show through again", "None is required by Python"], "answer": 1,
         "why": "Reads search the layers top-down; a marker stops the search at the delete."},
        {"q": "Inside two open transactions, the inner one commits. Where do its changes go?",
         "options": ["Straight into the saved data", "Into the outer transaction's layer", "Nowhere until both commit"], "answer": 1,
         "why": "If the outer transaction later rolls back, the inner changes must disappear with it."},
    ],
    "debug": {"intro": BUG,
              "starter": "class KVStore:\n    def __init__(self):\n        self.data = {}\n        self.layers = []\n\n    def get(self, key):\n        for layer in reversed(self.layers):\n            if key in layer:\n                return layer[key]\n        return self.data.get(key)\n\n    def set(self, key, value):\n        if self.layers:\n            self.layers[-1][key] = value\n        else:\n            self.data[key] = value\n\n    def delete(self, key):\n        if self.layers:\n            self.layers[-1][key] = None\n        else:\n            self.data.pop(key, None)\n\n    def begin(self):\n        self.layers.append({})\n\n    def rollback(self):\n        if not self.layers:\n            return False\n        self.layers.pop()\n        return True\n\n    def commit(self):\n        if not self.layers:\n            return False\n        top = self.layers.pop()\n        for k, v in top.items():\n            if v is None:\n                self.data.pop(k, None)\n            else:\n                self.data[k] = v\n        return True\n",
              "hint": "Commit an inner transaction, then roll back the outer one. Where did the inner changes go?",
              "extra_tests": [("inner commit, outer rollback (visible)", [[["BEGIN"], ["BEGIN"], ["SET", "z", "1"], ["COMMIT"], ["ROLLBACK"], ["GET", "z"]]], False)]},
}

EXTRAS_LLOYDS["graph-distances"] = {
    "limit": 25,
    "complexity": {"time": ["O(n log n)"], "space": ["O(n)"], "time_options": T_STD, "space_options": S_STD,
                   "why": "With n edges, every heap push and pop is O(log n): O(n log n) overall. The graph, heap and best times are O(n) space."},
    "quiz": [
        {"q": "Links A-B cost 10, A-C 2, C-B 2. Which finds the quickest A to B?",
         "options": ["BFS: it finds A-B in one step", "Dijkstra: it finds A-C-B, total 4", "Either; they always agree"], "answer": 1,
         "why": "BFS counts links, not costs. With costs, use Dijkstra."},
        {"q": "What does this print?", "code": "graph = {}\nfor a, b in [[\"A\", \"B\"], [\"B\", \"C\"]]:\n    graph.setdefault(a, []).append(b)\n    graph.setdefault(b, []).append(a)\nprint(graph[\"B\"], graph.get(\"Z\", []))",
         "options": ["@run", "['C'] []", "['A'] None", "Error"], "why": "Two-way links add both directions; <code>get</code> with a default avoids a KeyError for unknown nodes."},
        {"q": "Dijkstra pops (7, 'X') but best['X'] is already 5. What should it do?",
         "options": ["Expand X again with time 7", "Skip it: it is an old, slower entry", "Stop the search"], "answer": 1,
         "why": "Lazy deletion: the heap can hold stale entries, so ignore any that are worse than the best known time."},
    ],
    "debug": {"intro": BUG,
              "starter": "from collections import deque\n\ndef quickest_time(edges, start, end):\n    graph = {}\n    for a, b, mins in edges:\n        graph.setdefault(a, []).append((b, mins))\n        graph.setdefault(b, []).append((a, mins))\n    best = {start: 0}\n    q = deque([start])\n    while q:\n        node = q.popleft()\n        for nxt, mins in graph.get(node, []):\n            if nxt not in best:\n                best[nxt] = best[node] + mins\n                q.append(nxt)\n    return best.get(end, -1)\n",
              "hint": "This is BFS with costs added on. It fixes each node the first time it is reached. Is the first route always the quickest?"},
}

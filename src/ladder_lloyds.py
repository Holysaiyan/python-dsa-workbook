"""Easy, Medium and Hard practice for the Lloyds-style lessons, with Coach Max video segments (same format as ladder.py)."""

def S(code): return code.strip("\n") + "\n"

LADDER_L = {}

# ---------------------------------------------------------------- JSON validation
IS_VALID = S('''
import json

def is_valid_json(text):
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False
''')
MISSING = S('''
import json

def missing_fields(text, required):
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, dict):
        return None
    return [f for f in required if f not in data]
''')
ORDER = S('''
import json

def validate_order(text):
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {"status": 400, "error": "invalid JSON"}
    if not isinstance(data, dict) or not isinstance(data.get("items"), list):
        return {"status": 400, "error": "items must be a list"}
    if not data["items"]:
        return {"status": 422, "error": "no items"}
    total = 0
    for i, item in enumerate(data["items"]):
        if not isinstance(item, dict):
            return {"status": 422, "error": f"items[{i}]: must be an object"}
        if not isinstance(item.get("sku"), str) or not item["sku"]:
            return {"status": 422, "error": f"items[{i}]: bad sku"}
        q = item.get("qty")
        if isinstance(q, bool) or not isinstance(q, int) or q < 1:
            return {"status": 422, "error": f"items[{i}]: bad qty"}
        total += q
    return {"status": 200, "total_qty": total}
''')
LADDER_L["json-validation"] = [
 dict(level="Easy", title="Is it valid JSON?", func="is_valid_json",
      prompt="<p>Write <code>is_valid_json(text)</code>. Return <code>True</code> if the string is valid JSON, otherwise <code>False</code>. Never crash.</p>",
      starter="import json\n\ndef is_valid_json(text):\n    pass\n",
      tests=[("an object", ['{"a": 1}'], False), ("missing quotes", ['{a: 1}'], False), ("empty string", [''], True), ("a plain number", ['42'], True), ("trailing comma", ['[1, 2,]'], True), ("single quotes", ["{'a': 1}"], True)],
      hints=["Try to parse it and catch the error.", "<code>try: json.loads(text); return True</code> / <code>except json.JSONDecodeError: return False</code>."],
      solution=IS_VALID, explain="Parsing reads the string once: <b>O(n)</b> time and <b>O(n)</b> space for the parsed result.",
      vid=[("Lloyds tasks, easy. Is this string valid JSON? True or false, and never crash.", [("b", "'{\"a\": 1}' True, '{a: 1}' False, '' False")]),
           ("Don't try to check the text by hand. Let json loads do it, and catch the error.", [("clear",), ("code", IS_VALID.splitlines()), ("hl", [4])]),
           ("If it parses, return true. If it raises a decode error, return false.", [("hl", [3, 4, 5, 6, 7])]),
           ("Catch that exact error, not everything. A bare except hides your own bugs. Professional habit. Very important.", [("b", "except json.JSONDecodeError, not except:"), ("cap", "Parse it, catch the exact error.")])]),
 dict(level="Medium", title="Which fields are missing?", func="missing_fields",
      prompt="<p>Write <code>missing_fields(text, required)</code>. If <code>text</code> is not a JSON object, return <code>None</code>. Otherwise return the names in <code>required</code> that are not keys of the object, in the order given.</p><p>Example: <code>missing_fields('{\"name\": \"Ana\"}', [\"name\", \"email\", \"age\"])</code> returns <code>[\"email\", \"age\"]</code>.</p>",
      starter="import json\n\ndef missing_fields(text, required):\n    pass\n",
      tests=[("given example", ['{"name": "Ana"}', ["name", "email", "age"]], False), ("nothing missing", ['{"a": 1, "b": 2}', ["a", "b"]], False), ("not JSON", ['{name', ["name"]], True), ("a list, not an object", ['["name"]', ["name"]], True), ("null value still counts as present", ['{"email": null}', ["email"]], True), ("no requirements", ['{}', []], True)],
      hints=["Parse with a try/except, then check <code>isinstance(data, dict)</code>.", "<code>[f for f in required if f not in data]</code> keeps the given order."],
      solution=MISSING, explain="Parsing is O(n) in the text; each membership check is O(1) on a dict: <b>O(n + r)</b> for r required fields, which is <b>O(n)</b>.",
      vid=[("Lloyds tasks, medium. Which required fields are missing from a JSON body?", [("b", "{'name': 'Ana'} needs name, email, age: missing email, age")]),
           ("Step one, parse safely. Broken text? Return none.", [("clear",), ("code", MISSING.splitlines()), ("hl", [3, 4, 5, 6])]),
           ("Step two, check the shape. A list isn't an object. Return none.", [("hl", [7, 8])]),
           ("Step three, one line. Every required name that isn't a key, in the order given.", [("hl", [9])]),
           ("Careful: a field set to null is still present. It's there, it's just empty. Tests check that. Every time.", [("b", "\"email\": null counts as present"), ("cap", "Parse, check the shape, then the fields.")])]),
 dict(level="Hard", title="Validate an order", func="validate_order",
      prompt="<p>Write <code>validate_order(text)</code>. Check in this order and return a dict:</p><ol><li>Invalid JSON: <code>{\"status\": 400, \"error\": \"invalid JSON\"}</code></li><li>Not an object, or <code>items</code> is missing or not a list: <code>{\"status\": 400, \"error\": \"items must be a list\"}</code></li><li>Empty list: <code>{\"status\": 422, \"error\": \"no items\"}</code></li><li>For each item i in order: not an object gives <code>\"items[i]: must be an object\"</code>; <code>sku</code> not a non-empty string gives <code>\"items[i]: bad sku\"</code>; <code>qty</code> not a whole number of at least 1 (booleans do not count) gives <code>\"items[i]: bad qty\"</code>. All with status 422. Stop at the first error.</li><li>Otherwise <code>{\"status\": 200, \"total_qty\": total}</code>.</li></ol>",
      starter="import json\n\ndef validate_order(text):\n    pass\n",
      tests=[("valid order", ['{"items": [{"sku": "A1", "qty": 2}, {"sku": "B2", "qty": 3}]}'], False), ("second item bad qty", ['{"items": [{"sku": "A1", "qty": 1}, {"sku": "B2", "qty": 0}]}'], False),
             ("broken JSON", ['{"items": ['], True), ("items not a list", ['{"items": "A1"}'], True), ("no items", ['{"items": []}'], True),
             ("item not an object", ['{"items": [5]}'], True), ("empty sku", ['{"items": [{"sku": "", "qty": 1}]}'], True),
             ("qty is true", ['{"items": [{"sku": "A1", "qty": true}]}'], True), ("qty is 1.5", ['{"items": [{"sku": "A1", "qty": 1.5}]}'], True)],
      hints=["Same order as the payment endpoint: parse, shape, then each item. Use <code>enumerate</code> so the error can name <code>items[i]</code>.", "<code>data.get(\"items\")</code> avoids a KeyError. For qty, reject <code>bool</code> first, then require <code>int</code> and <code>&gt;= 1</code>."],
      solution=ORDER, explain="Parsing is O(n) and each item is checked once: <b>O(n)</b> time, <b>O(n)</b> space for the parsed body.",
      vid=[("Lloyds tasks, hard. Validate a whole order: a list of items, each with a code and a quantity.", [("b", "Stop at the first error, and name the item: items[1]: bad qty")]),
           ("Same backbone as every endpoint. Parse safely, then check the shape.", [("clear",), ("code", ORDER.splitlines()), ("hl", [3, 4, 5, 6, 7, 8])]),
           ("An empty list is readable but useless: four two two, no items.", [("hl", [9, 10])]),
           ("Now each item, with enumerate, so the error message can say which one.", [("hl", [12, 13, 14])]),
           ("Code must be a non-empty string. Quantity a real whole number, at least one. Not true, not one point five.", [("hl", [15, 16, 17, 18, 19])]),
           ("Everything passes? Two hundred, with the total. Methodical, step by step. That's how you win this task.", [("hl", [21]), ("cap", "Parse, shape, then each item in order.")])]),
]

# ---------------------------------------------------------------- key-value store
SIMPLE = S('''
def simple_store(commands):
    data = {}
    out = []
    for c in commands:
        if c[0] == "SET":
            data[c[1]] = c[2]
        elif c[0] == "GET":
            out.append(data.get(c[1], "NULL"))
        elif c[0] == "DELETE":
            data.pop(c[1], None)
    return out
''')
ONE_TX = S('''
def one_level_store(commands):
    data = {}
    tx = None                         # changes in the open transaction
    out = []
    for c in commands:
        op = c[0]
        if op == "SET":
            (tx if tx is not None else data)[c[1]] = c[2]
        elif op == "GET":
            if tx is not None and c[1] in tx:
                out.append(tx[c[1]])
            else:
                out.append(data.get(c[1], "NULL"))
        elif op == "BEGIN":
            tx = {}
        elif op == "COMMIT":
            if tx is None:
                out.append("NO TRANSACTION")
            else:
                data.update(tx)
                tx = None
        elif op == "ROLLBACK":
            if tx is None:
                out.append("NO TRANSACTION")
            else:
                tx = None
    return out
''')
COUNT_TX = S('''
def counting_store(commands):
    layers = [{}]                     # layers[0] is committed data
    out = []
    def get(key):
        for layer in reversed(layers):
            if key in layer:
                return layer[key]
        return None
    for c in commands:
        op = c[0]
        if op == "SET":
            layers[-1][c[1]] = c[2]
        elif op == "DELETE":
            layers[-1][c[1]] = None
        elif op == "GET":
            v = get(c[1])
            out.append("NULL" if v is None else v)
        elif op == "COUNT":
            keys = set().union(*layers)
            out.append(sum(1 for k in keys if get(k) == c[1]))
        elif op == "BEGIN":
            layers.append({})
        elif op in ("COMMIT", "ROLLBACK"):
            if len(layers) == 1:
                out.append("NO TRANSACTION")
            elif op == "ROLLBACK":
                layers.pop()
            else:
                top = layers.pop()
                layers[-1].update(top)
    return out
''')
LADDER_L["kv-transactions"] = [
 dict(level="Easy", title="Plain key-value store", func="simple_store",
      prompt="<p>Write <code>simple_store(commands)</code>. Each command is a list: <code>[\"SET\", key, value]</code>, <code>[\"GET\", key]</code> or <code>[\"DELETE\", key]</code>. Return the list of GET results, using <code>\"NULL\"</code> for a missing key.</p>",
      starter="def simple_store(commands):\n    pass\n",
      tests=[("set then get", [[["SET", "a", "1"], ["GET", "a"]]], False), ("missing key", [[["GET", "z"]]], False), ("overwrite", [[["SET", "a", "1"], ["SET", "a", "2"], ["GET", "a"]]], True), ("delete", [[["SET", "a", "1"], ["DELETE", "a"], ["GET", "a"]]], True), ("delete a missing key", [[["DELETE", "q"], ["GET", "q"]]], True), ("no commands", [[]], True)],
      hints=["A dict holds the data. Loop over the commands and branch on <code>c[0]</code>.", "<code>data.get(key, \"NULL\")</code> for GET; <code>data.pop(key, None)</code> deletes without crashing."],
      solution=SIMPLE, explain="Each command is O(1): <b>O(n)</b> for n commands, <b>O(n)</b> space.",
      vid=[("Lloyds tasks, easy. A plain key-value store, driven by a list of commands.", [("b", "SET a 1, GET a gives ['1']")]),
           ("A dictionary is the store. Loop over the commands and look at the first word.", [("clear",), ("code", SIMPLE.splitlines()), ("hl", [4, 5])]),
           ("Set: store it. Get: get with a default of null, so a missing key never crashes.", [("hl", [5, 6, 7, 8])]),
           ("Delete: pop with a default, so deleting something that isn't there is fine too.", [("hl", [9, 10])]),
           ("Every command O of one. This is the foundation. Next, we add transactions.", [("cap", "Command loop: branch on the first word.")])]),
 dict(level="Medium", title="One level of transaction", func="one_level_store",
      prompt="<p>Write <code>one_level_store(commands)</code>. Commands are <code>SET</code>, <code>GET</code>, <code>BEGIN</code>, <code>COMMIT</code> and <code>ROLLBACK</code>. Only one transaction is open at a time (a new <code>BEGIN</code> while one is open just starts fresh, throwing away the old changes). Return GET results (<code>\"NULL\"</code> if missing), and <code>\"NO TRANSACTION\"</code> for a COMMIT or ROLLBACK with nothing open.</p>",
      starter="def one_level_store(commands):\n    pass\n",
      tests=[("rollback undoes", [[["SET", "a", "1"], ["BEGIN"], ["SET", "a", "2"], ["GET", "a"], ["ROLLBACK"], ["GET", "a"]]], False), ("commit keeps", [[["BEGIN"], ["SET", "b", "5"], ["COMMIT"], ["GET", "b"]]], False),
             ("nothing open", [[["COMMIT"], ["ROLLBACK"]]], True), ("reads fall through", [[["SET", "x", "9"], ["BEGIN"], ["GET", "x"]]], True), ("rollback twice", [[["BEGIN"], ["ROLLBACK"], ["ROLLBACK"]]], True), ("new key rolled back", [[["BEGIN"], ["SET", "n", "1"], ["ROLLBACK"], ["GET", "n"]]], True)],
      hints=["Keep the open transaction's changes in a separate dict, or <code>None</code> when nothing is open.", "GET checks the transaction dict first, then the saved data. COMMIT copies the changes across with <code>data.update(tx)</code>."],
      solution=ONE_TX, explain="SET, GET, BEGIN and ROLLBACK are O(1); COMMIT copies c changes: <b>O(n)</b> overall for n commands, <b>O(n)</b> space.",
      vid=[("Lloyds tasks, medium. One level of transaction. Begin, then commit or roll back.", [("b", "SET a 1, BEGIN, SET a 2, ROLLBACK, GET a gives 1")]),
           ("Keep the transaction's changes in their own dictionary. None means nothing is open.", [("clear",), ("code", ONE_TX.splitlines()), ("hl", [2, 3])]),
           ("Writes go to the transaction if one is open. Reads check the transaction first, then the saved data.", [("hl", [7, 8, 9, 10, 11, 12, 13])]),
           ("Commit copies the changes across. Rollback just throws them away. Nothing open? Say so.", [("hl", [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])]),
           ("Separate the changes, and undo becomes trivial. Smart design. Very smart.", [("cap", "Keep uncommitted changes separate.")])]),
 dict(level="Hard", title="Nested transactions with COUNT", func="counting_store",
      prompt="<p>Write <code>counting_store(commands)</code>. Commands: <code>SET</code>, <code>GET</code>, <code>DELETE</code>, <code>BEGIN</code>, <code>COMMIT</code>, <code>ROLLBACK</code> and <code>[\"COUNT\", value]</code>, which outputs how many keys currently have that value. Transactions nest; COMMIT merges the newest into the one below. Outputs: GET gives the value or <code>\"NULL\"</code>, COUNT gives a number, and COMMIT or ROLLBACK with nothing open gives <code>\"NO TRANSACTION\"</code>.</p>",
      starter="def counting_store(commands):\n    pass\n",
      tests=[("count after sets", [[["SET", "a", "x"], ["SET", "b", "x"], ["SET", "c", "y"], ["COUNT", "x"]]], False), ("nested rollback", [[["BEGIN"], ["SET", "a", "1"], ["BEGIN"], ["SET", "a", "2"], ["ROLLBACK"], ["GET", "a"], ["COUNT", "2"]]], False),
             ("delete changes the count", [[["SET", "a", "x"], ["BEGIN"], ["DELETE", "a"], ["COUNT", "x"], ["ROLLBACK"], ["COUNT", "x"]]], True), ("overwrite inside a transaction", [[["SET", "a", "x"], ["BEGIN"], ["SET", "a", "y"], ["COUNT", "x"], ["COUNT", "y"]]], True),
             ("inner commit, outer rollback", [[["BEGIN"], ["BEGIN"], ["SET", "k", "v"], ["COMMIT"], ["ROLLBACK"], ["GET", "k"]]], True), ("nothing open", [[["ROLLBACK"]]], True)],
      hints=["Use a list of layers where <code>layers[0]</code> is the committed data. Write to <code>layers[-1]</code>; mark deletes with <code>None</code>.", "COUNT: take every key in any layer, look up its current value through the layers, and count the matches."],
      solution=COUNT_TX, explain="Most commands are O(d) for d open layers. COUNT looks at every key: <b>O(k x d)</b> per COUNT. A faster version keeps a running count per value, updated on every SET and DELETE and undone on rollback.",
      vid=[("Lloyds tasks, hard. Nested transactions, plus count: how many keys hold this value right now?", [("b", "BEGIN, SET a 1, BEGIN, SET a 2, ROLLBACK, GET a gives 1")]),
           ("A list of layers. Layer zero is the saved data. Each begin pushes a new layer.", [("clear",), ("code", COUNT_TX.splitlines()), ("hl", [1, 2])]),
           ("Reads look from the newest layer down. A delete is a none marker, so old values can't leak through.", [("hl", [3, 4, 5, 6, 7, 8, 13, 14])]),
           ("Count: gather every key from every layer, look up its current value, and count the matches.", [("hl", [18, 19, 20])]),
           ("Commit merges the top layer into the one below, so an outer rollback still undoes it. Draw the stack on paper. That's how champions debug this.", [("hl", [27, 28, 29]), ("cap", "Layers: newest wins; commit merges down.")])]),
]

# ---------------------------------------------------------------- graphs
REACH = S('''
def reachable(edges, start):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)
    seen = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in graph.get(node, []):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return sorted(seen)
''')
NETWORKS = S('''
def count_networks(nodes, edges):
    graph = {n: [] for n in nodes}
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen = set()
    count = 0
    for n in nodes:
        if n in seen:
            continue
        count += 1                    # a new, separate network
        seen.add(n)
        stack = [n]
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
    return count
''')
BUDGET = S('''
import heapq

def within_budget(edges, start, budget):
    graph = {}
    for a, b, cost in edges:
        graph.setdefault(a, []).append((b, cost))
        graph.setdefault(b, []).append((a, cost))
    best = {start: 0}
    heap = [(0, start)]
    while heap:
        c, node = heapq.heappop(heap)
        if c > best[node]:
            continue
        for nxt, cost in graph.get(node, []):
            nc = c + cost
            if nc <= budget and nc < best.get(nxt, float("inf")):
                best[nxt] = nc
                heapq.heappush(heap, (nc, nxt))
    return sorted(best)
''')
LADDER_L["graph-distances"] = [
 dict(level="Easy", title="Who can I reach?", func="reachable",
      prompt="<p>Write <code>reachable(edges, start)</code>. Each edge <code>[a, b]</code> is a two-way connection. Return every node you can reach from <code>start</code>, including <code>start</code>, sorted.</p>",
      starter="def reachable(edges, start):\n    pass\n",
      tests=[("small network", [[["A", "B"], ["B", "C"], ["D", "E"]], "A"], False), ("start has no links", [[["A", "B"]], "Z"], False), ("cycle", [[["A", "B"], ["B", "C"], ["C", "A"]], "B"], True), ("two-way", [[["B", "A"]], "A"], True), ("long chain", [{"__py__": "[[i, i + 1] for i in range(40)]"}, 38], True)],
      hints=["Build an adjacency dict both ways, then walk from the start with a stack or queue.", "A <code>seen</code> set stops you going round cycles. Return <code>sorted(seen)</code>."],
      solution=REACH, explain="Every node and edge is handled once: <b>O(V + E)</b> time, then O(V log V) to sort. Space <b>O(V + E)</b>.",
      vid=[("Lloyds graphs, easy. Who can I reach from here?", [("b", "A-B, B-C, D-E: from A you reach A, B, C")]),
           ("Build the adjacency dictionary. Two-way links, so add both directions.", [("clear",), ("code", REACH.splitlines()), ("hl", [1, 2, 3, 4])]),
           ("Walk from the start. A stack works, a queue works. Reachability doesn't care about order.", [("hl", [5, 6, 7, 8])]),
           ("The seen set is the hero. Without it, a cycle loops forever. Disaster.", [("hl", [9, 10, 11, 12])]),
           ("Every node once, every edge once. O of V plus E. Then sort, because the task said sorted.", [("hl", [13]), ("cap", "Reachable? Walk with a seen set.")])]),
 dict(level="Medium", title="How many separate networks?", func="count_networks",
      prompt="<p>Write <code>count_networks(nodes, edges)</code>. <code>nodes</code> lists every node; each edge is a two-way connection. Return how many separate networks there are (groups that cannot reach each other). A node with no links is a network on its own.</p>",
      starter="def count_networks(nodes, edges):\n    pass\n",
      tests=[("two networks", [["A", "B", "C", "D"], [["A", "B"], ["C", "D"]]], False), ("all joined", [["A", "B", "C"], [["A", "B"], ["B", "C"]]], False), ("no links", [["A", "B", "C"], []], True), ("no nodes", [[], []], True), ("cycle and a loner", [["A", "B", "C", "D"], [["A", "B"], ["B", "C"], ["C", "A"]]], True), ("1,000 pairs", [{"__py__": "list(range(2000))"}, {"__py__": "[[i, i + 1] for i in range(0, 2000, 2)]"}], True)],
      hints=["Go through every node. If it is not seen yet, it starts a new network: count it and mark everything it reaches.", "Reuse the reachability walk from the easy problem inside the loop."],
      solution=NETWORKS, explain="Each node and edge is visited once across all the walks: <b>O(V + E)</b> time, <b>O(V + E)</b> space.",
      vid=[("Lloyds graphs, medium. How many separate networks are there?", [("b", "A-B and C-D: two networks. A loner counts as one too.")]),
           ("Start the graph with every node, so nodes with no links still exist.", [("clear",), ("code", NETWORKS.splitlines()), ("hl", [1, 2, 3, 4])]),
           ("Go through the nodes. Already seen? Skip it. Not seen? It starts a brand new network. Count it.", [("hl", [7, 8, 9, 10])]),
           ("Then flood out from it and mark everything it reaches, so none of them get counted again.", [("hl", [11, 12, 13, 14, 15, 16, 17, 18])]),
           ("All the walks together touch each node once. O of V plus E. Classic. Beautiful.", [("hl", [19]), ("cap", "Unseen node = new network; flood it.")])]),
 dict(level="Hard", title="Everywhere within budget", func="within_budget",
      prompt="<p>Write <code>within_budget(edges, start, budget)</code>. Each edge <code>[a, b, cost]</code> is two-way with a cost of at least 0. Return every node whose cheapest route from <code>start</code> costs at most <code>budget</code>, including <code>start</code>, sorted.</p>",
      starter="import heapq\n\ndef within_budget(edges, start, budget):\n    pass\n",
      tests=[("given example", [[["A", "B", 4], ["A", "C", 1], ["C", "B", 2], ["B", "D", 5]], "A", 3], False), ("cheaper the long way", [[["A", "B", 10], ["A", "C", 2], ["C", "B", 2]], "A", 5], False),
             ("budget zero", [[["A", "B", 1]], "A", 0], True), ("free links", [[["A", "B", 0], ["B", "C", 0]], "A", 0], True), ("exactly on budget", [[["A", "B", 3], ["B", "C", 3]], "A", 6], True), ("unknown start", [[["A", "B", 1]], "Q", 10], True)],
      hints=["This is Dijkstra from the start node. Only push a neighbour if its new cost is within budget and cheaper than any found so far.", "At the end, the keys of the best-cost dict are exactly the nodes within budget."],
      solution=BUDGET, explain="Dijkstra with a heap: <b>O(E log E)</b> time, <b>O(V + E)</b> space.",
      vid=[("Lloyds graphs, hard. Every place I can reach within a budget, by the cheapest route.", [("b", "A-C costs 1, C-B 2: B is within 3 even though A-B direct costs 4")]),
           ("Costs on the links means Dijkstra. Heap of cost so far, and node.", [("clear",), ("code", BUDGET.splitlines()), ("hl", [8, 9])]),
           ("Pop the cheapest. If it's an old, worse entry, skip it.", [("hl", [10, 11, 12, 13])]),
           ("For each neighbour, only keep a route that's within budget and cheaper than before.", [("hl", [14, 15, 16, 17, 18])]),
           ("Every node that got a best cost is reachable within budget. Return them sorted. Dijkstra with a twist. You've got this.", [("hl", [19]), ("cap", "Dijkstra, and prune anything over budget.")])]),
]

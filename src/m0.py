"""Module P: Python basics, from the very start to everything the DSA modules use."""

MODULE = {"id": "python", "title": "Python basics", "n": "P"}

LESSONS = []

# ---------------------------------------------------------------- P1
LESSONS.append({
    "id": "py-values",
    "title": "Values, variables and maths",
    "minutes": 15,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Every program is values stored in variables and combined with operators. Get the four basic types and the three kinds of division right, and most beginner bugs disappear.",
    "blocks": [
        ("p", "A <b>value</b> is a piece of data. Python has four basic types you will use constantly: whole numbers (<code>int</code>), decimals (<code>float</code>), text (<code>str</code>) and true or false (<code>bool</code>). There is also <code>None</code>, which means 'no value'."),
        ("p", "A <b>variable</b> is a name that points at a value. You create one with <code>=</code>. Read <code>=</code> as 'becomes', not 'equals'."),
        ("code", """rent = 450          # int
rate = 0.2          # float
name = "Edikan"     # str
paid = False        # bool
print(name, rent, rate, paid)
print(type(rent), type(name))
rent = rent + 50    # rent becomes 500
print(rent)"""),
        ("h", "Maths, and the three kinds of division"),
        ("table", ["Operator", "Meaning", "Example", "Result"], [
            ["<code>+ - *</code>", "add, subtract, multiply", "<code>7 * 3</code>", "21"],
            ["<code>/</code>", "true division, always a float", "<code>7 / 2</code>", "3.5"],
            ["<code>//</code>", "floor division, rounds down", "<code>7 // 2</code>", "3"],
            ["<code>%</code>", "remainder (modulo)", "<code>7 % 2</code>", "1"],
            ["<code>**</code>", "power", "<code>2 ** 10</code>", "1024"],
        ]),
        ("code", """pence = 1037
people = 4
print(pence / people)    # 259.25
print(pence // people)   # 259 each
print(pence % people)    # 1 penny left over
print(10 % 2 == 0)       # even check: True"""),
        ("tip", "<code>n % 2 == 0</code> means 'n is even'. <code>n % 10</code> gives the last digit. <code>//</code> and <code>%</code> appear in assessments all the time."),
        ("h", "f-strings: putting values into text"),
        ("code", """name = "Ana"
nights = 3
price = 41.5
print(f"{name} owes {nights * price} for {nights} nights")
print(f"Rounded: {nights * price:.2f}")"""),
        ("p", "Put an <code>f</code> before the quotes and any expression inside <code>{ }</code> (curly braces) is worked out and inserted. <code>:.2f</code> shows two decimal places."),
    ],
    "mistakes": [
        "Using <code>/</code> when you need a whole number. <code>/</code> always gives a float, so use <code>//</code>.",
        "Mixing text and numbers with <code>+</code>: <code>\"Age: \" + 21</code> crashes. Use an f-string.",
        "Reading <code>=</code> as 'is equal to'. Comparison is <code>==</code>.",
    ],
    "practice": {
        "title": "Split the bill",
        "prompt": "<p>Write <code>split_bill(total_pence, people)</code>. Return a list <code>[share, left_over]</code>: how many whole pence each person pays, and how many pence are left over.</p><p>Example: <code>split_bill(1037, 4)</code> returns <code>[259, 1]</code>.</p>",
        "func": "split_bill",
        "starter": "def split_bill(total_pence, people):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [1037, 4], False),
            ("splits exactly", [900, 3], False),
            ("one person", [555, 1], True),
            ("more people than pence", [3, 5], True),
            ("nothing to pay", [0, 2], True),
        ],
        "hints": ["Which operator gives the whole-number share, and which gives the remainder?", "<code>return [total_pence // people, total_pence % people]</code>"],
        "solution": "def split_bill(total_pence, people):\n    return [total_pence // people, total_pence % people]\n",
        "explain": "Two arithmetic operations, whatever the numbers: <b>O(1)</b> time and <b>O(1)</b> space.",
    },
})

# ---------------------------------------------------------------- P2
LESSONS.append({
    "id": "py-strings",
    "title": "Strings",
    "minutes": 18,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Text is a sequence of characters. Indexing, slicing and a handful of methods (split, join, strip, lower) solve most text tasks you will meet.",
    "blocks": [
        ("p", "A string is a sequence of characters in quotes. Each character has a position, called an <b>index</b>, starting at <b>0</b>. Negative indexes count from the end."),
        ("code", """word = "python"
print(word[0])      # first character
print(word[-1])     # last character
print(len(word))    # how many characters
print(word[1:4])    # slice: index 1 up to, not including, 4
print(word[:2], word[2:])
print(word[::-1])   # reversed"""),
        ("tip", "A slice <code>s[a:b]</code> includes <code>a</code> and stops <b>before</b> <code>b</code>. So <code>s[0:3]</code> is the first three characters."),
        ("h", "The methods you need"),
        ("code", """s = "  Ada Lovelace  "
print(s.strip())               # remove spaces at both ends
print(s.lower(), s.upper())
print(s.split())               # split on any whitespace
print("a,b,c".split(","))      # split on commas
print("-".join(["2026", "11", "01"]))
print("love" in s.lower())     # substring check
print("banana".count("a"), "banana".replace("a", "o"))"""),
        ("p", "<code>split()</code> with nothing in the parentheses ( ) splits on any run of spaces and ignores extra ones. <code>split(\" \")</code> with a single space does not, and leaves empty strings behind. That difference causes real bugs."),
        ("h", "Strings cannot be changed"),
        ("p", "Strings are <b>immutable</b>: <code>s[0] = \"X\"</code> is an error. Methods like <code>upper()</code> return a <b>new</b> string, so you must store the result: <code>s = s.upper()</code>."),
        ("code", """name = "sam"
name.upper()          # result thrown away
print(name)
name = name.upper()   # stored
print(name)
for ch in "abc":      # loop over characters
    print(ch)"""),
    ],
    "mistakes": [
        "Calling <code>s.upper()</code> and expecting <code>s</code> to change. Store the result.",
        "Using <code>split(\" \")</code> on text with double spaces. Use <code>split()</code>.",
        "Off by one in slices: the end index is not included.",
    ],
    "practice": {
        "title": "Initials",
        "prompt": "<p>Write <code>initials(full_name)</code>. Return the capital first letter of each word, joined together. Names may have extra spaces anywhere.</p><p>Example: <code>initials(\"  ada   lovelace \")</code> returns <code>\"AL\"</code>.</p>",
        "func": "initials",
        "starter": "def initials(full_name):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", ["  ada   lovelace "], False),
            ("three names", ["Edikan Grace Eshett"], False),
            ("one name", ["prince"], True),
            ("already capitals", ["ALAN TURING"], True),
            ("empty string", [""], True),
            ("double spaces", ["grace  hopper"], True),
        ],
        "hints": ["Which split ignores extra spaces?", "<code>\"\".join(w[0].upper() for w in full_name.split())</code>, or build a result string in a loop."],
        "solution": "def initials(full_name):\n    result = \"\"\n    for word in full_name.split():\n        result += word[0].upper()\n    return result\n",
        "explain": "One pass over the characters: <b>O(n)</b> time. The split words take <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- P3
LESSONS.append({
    "id": "py-conditions",
    "title": "Conditions: if, elif, else",
    "minutes": 15,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Programs make decisions with comparisons and if statements. The order of your elif checks matters, and Python treats empty things as False.",
    "blocks": [
        ("p", "A comparison gives <code>True</code> or <code>False</code>: <code>==</code> equal, <code>!=</code> not equal, <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;</code>, <code>&gt;=</code>. Combine them with <code>and</code>, <code>or</code> and <code>not</code>."),
        ("code", """age = 21
student = True
print(age >= 18 and student)
print(age < 18 or student)
print(not student)
print(18 <= age <= 25)   # chained comparison"""),
        ("h", "if, elif, else"),
        ("p", "Python checks each condition from the top and runs the <b>first</b> one that is true, then skips the rest. The indented block (4 spaces) belongs to the line with the colon."),
        ("code", """def band(score):
    if score >= 70:
        return "First"
    elif score >= 60:
        return "2:1"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

for s in [85, 64, 40, 12]:
    print(s, band(s))"""),
        ("tip", "Check the <b>strictest</b> condition first. If <code>score &gt;= 40</code> came first, an 85 would be called a Pass and never reach First."),
        ("h", "Truthiness"),
        ("p", "In an <code>if</code>, empty things count as False: <code>0</code>, <code>\"\"</code>, <code>[]</code>, <code>{}</code>, <code>None</code>. Everything else counts as True. So <code>if items:</code> means 'if the list is not empty'."),
        ("code", """items = []
if not items:
    print("nothing to do")
name = "Ana"
if name:
    print("hello", name)"""),
    ],
    "mistakes": [
        "Putting a looser check above a stricter one, so the strict branch is never reached.",
        "Writing <code>if x = 5:</code>. Comparison needs <code>==</code>.",
        "Writing <code>if x == 1 or 2:</code>. That is always true. Write <code>if x == 1 or x == 2:</code> or <code>if x in (1, 2):</code>.",
    ],
    "practice": {
        "title": "Degree classification",
        "prompt": "<p>Write <code>classify(mark)</code> for a UK degree: 70 and above is <code>\"First\"</code>, 60 to 69 is <code>\"2:1\"</code>, 50 to 59 is <code>\"2:2\"</code>, 40 to 49 is <code>\"Third\"</code>, below 40 is <code>\"Fail\"</code>.</p>",
        "func": "classify",
        "starter": "def classify(mark):\n    # your code here\n    pass\n",
        "tests": [
            ("a First", [72], False),
            ("a 2:2", [55], False),
            ("boundary 70", [70], True),
            ("boundary 60", [60], True),
            ("boundary 40", [40], True),
            ("just below 40", [39], True),
            ("full marks", [100], True),
        ],
        "hints": ["Start with the highest band and work down with <code>elif</code>.", "Use <code>&gt;=</code> so that 70 itself is a First."],
        "solution": "def classify(mark):\n    if mark >= 70:\n        return \"First\"\n    elif mark >= 60:\n        return \"2:1\"\n    elif mark >= 50:\n        return \"2:2\"\n    elif mark >= 40:\n        return \"Third\"\n    return \"Fail\"\n",
        "explain": "At most four comparisons, whatever the mark: <b>O(1)</b> time and space.",
    },
})

# ---------------------------------------------------------------- P4
LESSONS.append({
    "id": "py-loops",
    "title": "Loops: for, range and while",
    "minutes": 20,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Loops repeat work. A for loop walks through items or a range of numbers; a while loop repeats until a condition fails. The accumulator pattern builds an answer as you go.",
    "blocks": [
        ("h", "for loops"),
        ("code", """for room in ["A1", "A2", "B1"]:
    print("checking", room)

for i in range(3):          # 0, 1, 2
    print(i)

print(list(range(2, 10, 3)))   # start, stop (not included), step
print(list(range(5, 0, -1)))   # counting down"""),
        ("p", "<code>range(n)</code> gives 0 up to <code>n - 1</code>: exactly <code>n</code> numbers. It never includes the stop value."),
        ("h", "The accumulator pattern"),
        ("p", "Make a variable <b>before</b> the loop, update it <b>inside</b>, use it <b>after</b>. Totals, counts and best-so-far values all work this way."),
        ("code", """scores = [12, 7, 30, 4]
total = 0                 # before the loop
best = scores[0]
for s in scores:
    total += s            # same as total = total + s
    if s > best:
        best = s
print(total, best)"""),
        ("h", "enumerate: position and value together"),
        ("code", """names = ["Ana", "Ben", "Cal"]
for i, name in enumerate(names):
    print(i, name)"""),
        ("p", "<code>enumerate</code> hands you pairs: (0, \"Ana\"), (1, \"Ben\"), (2, \"Cal\"). <code>for i, name in ...</code> unpacks each pair into two variables. Use it whenever you need the position."),
        ("h", "while, break and continue"),
        ("code", """balance = 100
weeks = 0
while balance > 0:        # repeat until the condition is False
    balance -= 30
    weeks += 1
print(weeks, balance)

for n in [3, 8, -1, 5]:
    if n < 0:
        break             # leave the loop completely
    if n % 2 == 0:
        continue          # skip to the next item
    print("odd:", n)"""),
        ("tip", "An <b>IndexError</b> usually means an off-by-one: the last valid index is <code>len(xs) - 1</code>. Read the error's last line first; it names the problem and the line number."),
    ],
    "mistakes": [
        "Resetting the accumulator inside the loop, so it only remembers the last item.",
        "Expecting <code>range(1, 5)</code> to include 5.",
        "A while loop whose condition never becomes False: an infinite loop.",
    ],
    "practice": {
        "title": "Running total",
        "prompt": "<p>Write <code>running_total(amounts)</code>. Return a new list where each item is the total of everything up to and including that position.</p><p>Example: <code>running_total([5, 2, 10])</code> returns <code>[5, 7, 17]</code>.</p>",
        "func": "running_total",
        "starter": "def running_total(amounts):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [[5, 2, 10]], False),
            ("with negatives", [[3, -1, 4]], False),
            ("empty list", [[]], True),
            ("one item", [[9]], True),
            ("zeros", [[0, 0, 0]], True),
        ],
        "hints": ["You need two accumulators: the total so far, and the result list.", "Inside the loop: <code>total += x</code>, then <code>result.append(total)</code>."],
        "solution": "def running_total(amounts):\n    total = 0\n    result = []\n    for x in amounts:\n        total += x\n        result.append(total)\n    return result\n",
        "explain": "One pass: <b>O(n)</b> time. The result list holds n totals: <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- P5
LESSONS.append({
    "id": "py-lists",
    "title": "Lists",
    "minutes": 20,
    "tags": ["Accenture", "Lloyds"],
    "summary": "A list is an ordered, changeable collection, written with square brackets [ ]. Know how to index, slice, add, remove, sort and build lists with a comprehension.",
    "blocks": [
        ("code", """rooms = ["A1", "B2", "C3"]
print(rooms[0], rooms[-1], len(rooms))
rooms.append("D4")        # add to the end
rooms.insert(0, "Z0")     # add at a position
print(rooms)
last = rooms.pop()        # remove and return the last item
rooms.remove("B2")        # remove by value
print(last, rooms)
print("C3" in rooms)"""),
        ("h", "sort versus sorted"),
        ("code", """nums = [4, 1, 3]
print(sorted(nums))          # new sorted list, nums unchanged
print(nums)
nums.sort()                  # sorts in place, returns None
print(nums)
print(sorted(["pear", "fig", "apple"], key=len))
print(sorted(nums, reverse=True))"""),
        ("h", "List comprehensions"),
        ("p", "A comprehension builds a list in one line: <code>[expression for item in list if condition]</code>. Read it as 'give me this, for each item, if that'."),
        ("code", """nums = [1, 2, 3, 4, 5, 6]
squares = [n * n for n in nums]
evens = [n for n in nums if n % 2 == 0]
print(squares)
print(evens)

# the same as:
evens2 = []
for n in nums:
    if n % 2 == 0:
        evens2.append(n)
print(evens2)"""),
        ("h", "Two names, one list"),
        ("p", "<code>b = a</code> does not copy a list. Both names point at the <b>same</b> list, so changing one changes 'both'. Copy with <code>a[:]</code> or <code>list(a)</code>."),
        ("code", """a = [1, 2]
b = a
b.append(3)
print(a)          # a changed too
c = a[:]          # a real copy
c.append(4)
print(a, c)
grid = [[0] * 3 for _ in range(2)]   # a 2 by 3 grid
grid[0][1] = 9
print(grid)"""),
    ],
    "mistakes": [
        "Writing <code>nums = nums.sort()</code>. <code>sort()</code> returns <code>None</code>; use <code>sorted(nums)</code> if you need the result.",
        "Thinking <code>b = a</code> copies a list.",
        "Removing items from a list while looping over it. Build a new list instead.",
    ],
    "practice": {
        "title": "Even squares",
        "prompt": "<p>Write <code>even_squares(nums)</code>. Return the squares of the <b>even</b> numbers only, in their original order.</p><p>Example: <code>even_squares([1, 2, 3, 4])</code> returns <code>[4, 16]</code>.</p>",
        "func": "even_squares",
        "starter": "def even_squares(nums):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [[1, 2, 3, 4]], False),
            ("no evens", [[1, 3, 5]], False),
            ("empty list", [[]], True),
            ("negatives and zero", [[-2, 0, 7]], True),
            ("all even", [[2, 4, 6]], True),
        ],
        "hints": ["A comprehension with an if at the end does this in one line.", "<code>return [n * n for n in nums if n % 2 == 0]</code>"],
        "solution": "def even_squares(nums):\n    return [n * n for n in nums if n % 2 == 0]\n",
        "explain": "One pass: <b>O(n)</b> time. The new list can hold up to n items: <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- P6
LESSONS.append({
    "id": "py-functions",
    "title": "Functions",
    "minutes": 18,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Every assessment answer is a function. Know the difference between return and print, how parameters and defaults work, and how to hand back more than one value.",
    "blocks": [
        ("code", """def area(width, height):      # parameters
    return width * height      # hand the answer back

a = area(3, 4)                 # arguments
print(a)
print(area(2, 5) + 1)"""),
        ("h", "return is not print"),
        ("p", "<code>print</code> shows something on the screen. <code>return</code> hands a value back to whoever called the function. Test checkers read what you <b>return</b>. A function with no <code>return</code> gives back <code>None</code>."),
        ("code", """def shout(word):
    print(word.upper())        # shows it, returns None

result = shout("hi")
print(result)

def shout2(word):
    return word.upper()

print(shout2("hi"))"""),
        ("h", "Defaults, several return values, and scope"),
        ("code", """def price(nights, rate=40):    # rate has a default
    return nights * rate

print(price(3), price(3, 55))

def low_high(nums):
    return min(nums), max(nums)   # returns a tuple

lo, hi = low_high([4, 9, 1])      # unpack it
print(lo, hi)

total = 10
def add_one(x):
    total = x + 1      # a new local variable, not the outer one
    return total
print(add_one(5), total)"""),
        ("tip", "In assessments, never use <code>input()</code> or <code>print</code> inside the function you are asked to write unless the task says so. Take parameters, return the answer."),
        ("h", "Functions can call themselves"),
        ("p", "A function can call other functions, including itself. That is recursion, covered in Module 4. For now: a function stops the moment it hits <code>return</code>."),
    ],
    "mistakes": [
        "Printing the answer instead of returning it.",
        "Forgetting <code>return</code>, so the function gives back <code>None</code>.",
        "Starting a 'largest so far' at 0, which fails when every number is negative.",
    ],
    "practice": {
        "title": "Smallest and largest",
        "prompt": "<p>Write <code>min_max(nums)</code> <b>without</b> using <code>min()</code> or <code>max()</code>. Return <code>[smallest, largest]</code>. The list always has at least one number.</p><p>Example: <code>min_max([4, 9, 1])</code> returns <code>[1, 9]</code>.</p>",
        "func": "min_max",
        "starter": "def min_max(nums):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [[4, 9, 1]], False),
            ("one number", [[7]], False),
            ("all negative", [[-5, -2, -9]], True),
            ("duplicates", [[3, 3, 3]], True),
            ("sorted already", [[1, 2, 3, 4]], True),
        ],
        "hints": ["Start both trackers at the first number, not at 0.", "Loop through and update <code>lo</code> and <code>hi</code> when you see something smaller or bigger."],
        "solution": "def min_max(nums):\n    lo = hi = nums[0]\n    for n in nums:\n        if n < lo:\n            lo = n\n        if n > hi:\n            hi = n\n    return [lo, hi]\n",
        "explain": "One pass: <b>O(n)</b> time. Two variables: <b>O(1)</b> space.",
    },
})

# ---------------------------------------------------------------- P7
LESSONS.append({
    "id": "py-collections",
    "title": "Dictionaries, tuples and sets",
    "minutes": 20,
    "tags": ["Accenture", "Lloyds"],
    "summary": "Dictionaries map keys to values, tuples are fixed groups, and sets hold unique items. These three, plus lists, are the raw material of every data structure in this course.",
    "blocks": [
        ("h", "Dictionaries: look things up by key"),
        ("code", """rent = {"Ana": 450, "Ben": 520}     # key: value
print(rent["Ana"])
rent["Cal"] = 480                     # add or update
print("Ben" in rent)                  # checks keys
print(rent.get("Dan", 0))             # default if missing
for name, amount in rent.items():
    print(name, amount)
print(list(rent.keys()), list(rent.values()))"""),
        ("tip", "<code>d[key]</code> crashes with a <b>KeyError</b> if the key is missing. <code>d.get(key, default)</code> never crashes."),
        ("h", "Adding up by key"),
        ("p", "A very common pattern: start each key at 0 the first time you see it, then add."),
        ("code", """spend = [["food", 12], ["travel", 5], ["food", 8]]
totals = {}
for category, amount in spend:
    totals[category] = totals.get(category, 0) + amount
print(totals)"""),
        ("h", "Tuples: fixed groups"),
        ("code", """point = (3, 4)            # parentheses ( )
x, y = point              # unpacking
print(x + y)
a, b = 1, 2
a, b = b, a               # swap in one line
print(a, b)"""),
        ("p", "Tuples cannot be changed after creation. That makes them usable as dictionary keys and set items, which lists are not."),
        ("h", "Sets: unique items, fast 'is it in?'"),
        ("code", """seen = set()
for room in ["A1", "B2", "A1"]:
    seen.add(room)
print(sorted(seen), len(seen))
print("B2" in seen)
print(sorted({1, 2, 3} & {2, 3, 4}))   # in both"""),
        ("table", ["Use a", "When you need", "Written"], [
            ["list", "order, duplicates allowed, by position", "<code>[1, 2]</code>"],
            ["dict", "look up a value by a key", "<code>{\"a\": 1}</code>"],
            ["set", "unique items, fast membership", "<code>{1, 2}</code> or <code>set()</code>"],
            ["tuple", "a fixed group, or a key", "<code>(1, 2)</code>"],
        ]),
    ],
    "mistakes": [
        "Writing <code>{}</code> for an empty set. That is an empty dict; use <code>set()</code>.",
        "Using <code>d[key]</code> for a key that might not exist.",
        "Overwriting a total with <code>totals[k] = amount</code> instead of adding to it.",
    ],
    "practice": {
        "title": "Spending by category",
        "prompt": "<p>Write <code>totals_by_category(spend)</code>. <code>spend</code> is a list of <code>[category, amount]</code> pairs. Return a dict of each category's total.</p><p>Example: <code>[[\"food\", 12], [\"travel\", 5], [\"food\", 8]]</code> gives <code>{\"food\": 20, \"travel\": 5}</code>.</p>",
        "func": "totals_by_category",
        "starter": "def totals_by_category(spend):\n    # your code here\n    pass\n",
        "tests": [
            ("given example", [[["food", 12], ["travel", 5], ["food", 8]]], False),
            ("one category", [[["rent", 450]]], False),
            ("empty", [[]], True),
            ("same category three times", [[["food", 1], ["food", 2], ["food", 3]]], True),
            ("a zero amount", [[["gym", 0], ["gym", 20]]], True),
        ],
        "hints": ["Start with an empty dict and loop through the pairs.", "<code>totals[c] = totals.get(c, 0) + amount</code>"],
        "solution": "def totals_by_category(spend):\n    totals = {}\n    for category, amount in spend:\n        totals[category] = totals.get(category, 0) + amount\n    return totals\n",
        "explain": "One pass with O(1) dict updates: <b>O(n)</b> time. Up to one key per item: <b>O(n)</b> space.",
    },
})

# ---------------------------------------------------------------- P8
LESSONS.append({
    "id": "py-classes",
    "title": "Classes and objects",
    "minutes": 18,
    "tags": ["Accenture", "Lloyds"],
    "summary": "A class is a blueprint for objects that bundle data and behaviour. Linked lists, trees and graphs in later modules are built from tiny classes like these.",
    "blocks": [
        ("code", """class Room:
    def __init__(self, name, capacity):   # runs when you create one
        self.name = name                  # attributes
        self.capacity = capacity
        self.guests = []

    def add(self, guest):                 # a method
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            return True
        return False

r = Room("A1", 2)            # create an object
print(r.add("Ana"), r.add("Ben"), r.add("Cal"))
print(r.name, r.guests)"""),
        ("p", "<code>__init__</code> sets up a new object. <code>self</code> means 'this particular object': <code>self.name</code> is this room's name. Every method takes <code>self</code> first, but you do not pass it yourself."),
        ("h", "Objects that point at other objects"),
        ("p", "An attribute can hold another object. A chain of objects, each pointing at the next, is a <b>linked list</b>. This is exactly the <code>Node</code> class in Module 2."),
        ("code", """class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = Node(1, Node(2, Node(3)))   # 1 -> 2 -> 3
cur = head
while cur is not None:
    print(cur.val)
    cur = cur.next"""),
        ("h", "A readable print"),
        ("code", """class Booking:
    def __init__(self, ref, nights):
        self.ref = ref
        self.nights = nights

    def __repr__(self):
        return f"Booking({self.ref}, {self.nights})"

print(Booking("B12", 3))"""),
        ("tip", "Use <code>is None</code> to check for 'no object'. It is the standard way and reads clearly."),
    ],
    "mistakes": [
        "Forgetting <code>self</code> as the first parameter of a method.",
        "Writing <code>name = name</code> in <code>__init__</code> instead of <code>self.name = name</code>.",
        "Following <code>.next</code> without checking for <code>None</code>, which crashes at the end of the chain.",
    ],
    "practice": {
        "title": "Total along a chain",
        "prompt": "<p>A <code>Node</code> class is provided. Write <code>chain_total(head)</code>, which returns the sum of every <code>val</code> in the chain. An empty chain (<code>head</code> is <code>None</code>) totals 0. The checker builds the chain from a list for you.</p>",
        "func": "chain_total",
        "starter": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\ndef chain_total(head):\n    # your code here\n    pass\n",
        "wrapper": """def __call(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return chain_total(head)
""",
        "tests": [
            ("three nodes", [[1, 2, 3]], False),
            ("one node", [[10]], False),
            ("empty chain", [[]], True),
            ("negatives", [[-4, 6, -1]], True),
            ("long chain", [{"__py__": "list(range(1000))"}], True),
        ],
        "hints": ["Walk with <code>cur = head</code> and a <code>while cur is not None</code> loop.", "Add <code>cur.val</code> to a total, then move with <code>cur = cur.next</code>."],
        "solution": "class Node:\n    def __init__(self, val, next=None):\n        self.val = val\n        self.next = next\n\ndef chain_total(head):\n    total = 0\n    cur = head\n    while cur is not None:\n        total += cur.val\n        cur = cur.next\n    return total\n",
        "explain": "Each node is visited once: <b>O(n)</b> time. One total and one pointer: <b>O(1)</b> space.",
    },
})

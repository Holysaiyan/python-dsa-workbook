"""Section introductions, shown at the top of each module's first lesson."""

INTROS = {
 "python": dict(
    why="Every coding test is written in a language, and here it is Python. This section takes you from your first variable to classes, which is everything the DSA sections use.",
    learn=["Values, maths and the three kinds of division", "Strings, conditions and loops", "Lists, functions, dictionaries and sets", "Classes and objects, the building block of linked lists and trees"],
    forwho="Everyone who is new to Python or rusty. If you are comfortable, skim the mistakes boxes and do each practice problem as a check.",
    how="Read each lesson, run every example, then do the practice before looking at the hints."),
 "foundations": dict(
    why="Before any data structure, you need a way to attack a problem and a way to say how fast your answer is. That is what interviewers listen for.",
    learn=["A six-step routine for any problem", "Big O for time: how work grows as the input grows", "Big O for space: how much extra memory you use", "The Python tools the pros use: enumerate, sorted with a key, Counter, deque"],
    forwho="All three assessments. Big O comes up in every technical interview.",
    how="Watch Coach Max's video, then take each lesson in order. Lesson 2 is the most important: do not skip it."),
 "structures": dict(
    why="Picking the right structure turns a hard problem into an easy one. Most graduate coding questions are a set, a dictionary or a stack in disguise.",
    learn=["Hash sets: 'have I seen this before?' in O(1)", "Dictionaries and the counting pattern", "Stacks: brackets, undo, and nested transactions", "Queues and deques, and linked lists"],
    forwho="Accenture and Lloyds coding tests. Lessons 5 to 7 are the highest priority.",
    how="Do the practice, then the Easy, Medium and Hard ladder. Watch each solution video only after a genuine try."),
 "techniques": dict(
    why="Three tricks that turn slow nested loops into a single fast pass. They show up constantly in timed tests.",
    learn=["Two pointers: pairs in sorted lists, palindromes", "Sliding window: the best run of k in a row", "Prefix sums: many range totals, fast"],
    forwho="Accenture's coding test especially.",
    how="Each lesson's ladder goes from a direct use of the trick to a twist on it. Aim to finish the Medium."),
 "search-sort": dict(
    why="The classic algorithms. Interviewers use them to check you can reason step by step and spot off-by-one errors.",
    learn=["Recursion: base case and a smaller step", "Binary search, and binary search on the answer", "Sorting: what O(n log n) means, and when to just use sorted()"],
    forwho="Technical interviews at all three employers.",
    how="Trace each example on paper before running it. Recursion clicks when you draw the calls."),
 "trees-graphs": dict(
    why="The big leagues: structures where items connect to other items. Lloyds' third task is a graph problem.",
    learn=["Trees and traversals", "Heaps: the smallest item, fast", "Graphs: building one from edges, BFS and DFS"],
    forwho="Lloyds especially (lesson 18), and technical interviews.",
    how="For graphs, always start by building the adjacency dictionary, then choose BFS or DFS."),
 "strategies": dict(
    why="How to think when you do not recognise a problem straight away: when greedy works, when you need dynamic programming, and which pattern fits.",
    learn=["Greedy, and how to test whether it fails", "Dynamic programming: never solve the same small problem twice", "A pattern table: which tool for which kind of question"],
    forwho="Everyone, once the earlier sections feel comfortable.",
    how="Lesson 21's pattern table is your revision sheet the night before any test."),
 "lloyds": dict(
    why="Lloyds' online assessment is three practical tasks in 130 minutes. This section practises exactly those three task types, one lesson each.",
    learn=["Task 1: validating JSON input like an API endpoint, and returning clear errors", "Task 2: a key-value store with set, get, delete, and nested transactions with commit and rollback", "Task 3: graphs: who is connected, how far apart, and the quickest route"],
    forwho="The Lloyds Banking Group online assessment.",
    how="Start with lesson 23 (the key-value store): it is the least familiar and carries a whole task. Do each practice and the Easy and Medium problems. Before the test, read the 'mistakes' box in each lesson again."),
 "project": dict(
    why="A project you can explain is worth more in an interview than any number of solved puzzles. This one uses the data structures from the course in a realistic setting.",
    learn=["Parse messy real-world input safely", "Count and rank with a dictionary", "Pick urgent jobs with a heap", "Look things up fast with binary search, then join it all into one program"],
    forwho="Your portfolio and your 'tell me about something you built' answer.",
    how="Each milestone is auto-tested. The last lesson shows how to explain the project in two minutes."),
}

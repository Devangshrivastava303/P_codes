# PYTHON FUNDAMENTALS DRILL
# ========================
# RULES:
# 1. Type every line yourself. Do NOT copy-paste.
# 2. Run this file after completing each section. Fix ALL errors before moving on.
# 3. If you get an error, READ the error message. It tells you exactly what's wrong.
# 4. No functions yet. Pure statements. Write them in order.

# =============================================
# SECTION 1: THE COLON PROBLEM
# =============================================
# You keep forgetting colons. Write these correctly:

# 1a. Write an if statement that checks if 10 > 5, and prints "yes"


# 1b. Write an else clause for 1a that prints "no"


# 1c. Write a for loop that iterates over [1, 2, 3, 4, 5] and prints each number


# 1d. Write a for loop that iterates over range(10) and prints the number if it's even


# 1e. Write a while loop that prints numbers 0 through 4


# 1f. Write a for loop with an if-elif-else inside it:
#     For numbers 0 through 5: if number is 0, print "zero"
#     elif number is even, print "even"
#     else print "odd"


# =============================================
# SECTION 2: THE RETURN PROBLEM
# =============================================
# You keep forgetting return statements. These are NOT functions yet,
# but practice the logic:

# 2a. Write a for loop that finds the maximum in [3, 7, 2, 9, 4]
#     Use a variable called "max_val" starting at the first element.
#     Print max_val after the loop.

# 2b. Write a for loop that counts how many times "a" appears in "banana"
#     Use a variable called "count" starting at 0.
#     Print count after the loop.


# =============================================
# SECTION 3: THE .APPEND() ON STRINGS PROBLEM
# =============================================
# Strings are IMMUTABLE. You CANNOT append to them.
# Lists are MUTABLE. You CAN append to them.

# 3a. This is WRONG. Fix it:
# my_str = ""
# for ch in "hello":
#     my_str.append(ch)  # ERROR! strings don't have .append()

# Write the correct version below:


# 3b. This is WRONG. Fix it:
# my_str = "hello"
# my_str.append(" world")  # ERROR!

# Write the correct version below (hint: use +):


# 3c. Write a loop that builds a string "12345" by iterating over range(1, 6)


# =============================================
# SECTION 4: THE .COUNT() ARGUMENT ORDER PROBLEM
# =============================================
# .count() takes the VALUE first, then start index, then end index.
# It does NOT take the container first.

# 4a. Write correct .count() to find how many times 3 appears in [1, 3, 3, 5]


# 4b. Write correct .count() to find how many times "l" appears in "hello"


# 4c. Write correct .count() to find how many times 2 appears in [1,2,3,2,4,2]
#     but ONLY in the first 4 elements (start=0, end=4)


# =============================================
# SECTION 5: THE COMPARISON OPERATOR PROBLEM
# =============================================
# You keep guessing >= instead of >, < instead of <=, etc.
# The RULE: Think about the EXACT boundary. What value should be INCLUDED?

# 5a. Write a loop that prints numbers 0, 1, 2, 3, 4 (NOT 5)
#     What comparison do you need? Write it. Run it. Did it stop at 4?


# 5b. Write a loop that prints numbers 1, 2, 3, 4, 5 (including 5)
#     What comparison do you need?


# 5c. Write a loop that prints numbers from 9 down to 0 (including 0)


# 5d. Write a loop that checks every element in [10, 20, 30, 40, 50]
#     and prints it if it's strictly less than 40


# =============================================
# SECTION 6: THE LOOP BOUNDARY PROBLEM
# =============================================
# You keep getting i < n vs i > n wrong.
# RULE: If counting UP, use < or <=. If counting DOWN, use > or >=.

# 6a. Given n = 5, write a for loop using range() that goes 0, 1, 2, 3, 4


# 6b. Given n = 5, write a for loop that goes 1, 2, 3, 4, 5


# 6c. Given n = 5, write a for loop that goes 4, 3, 2, 1, 0


# 6d. Given arr = [10, 20, 30, 40, 50], write a loop that prints
#     each element with its index using enumerate()


# =============================================
# SECTION 7: THE "WHAT SHOULD THIS VARIABLE START AS" PROBLEM
# =============================================
# RULE: Think about what the variable ACCUMULATES or TRACKS.
# Then ask: "What is the empty/initial state of that accumulation?"

# 7a. You're finding the SUM of a list.
#     What should sum_val start as? (0 or something else?)


# 7b. You're finding the MAXIMUM of a list [3, 7, 2, 9, 4].
#     What should max_val start as?
#     Option A: 0
#     Option B: -1
#     Option C: The first element of the list (3)
#     Option D: float('inf')
#     Which is correct and WHY? Write the answer and the loop.


# 7c. You're checking if ALL elements in a list are positive.
#     What should a boolean variable start as? True or False? Why?


# 7d. You're building a list of even numbers from range(10).
#     What should the list start as? [] or something else?


# =============================================
# SECTION 8: THE DIRECTION PROBLEM
# =============================================
# When you're guessing at comparisons, STOP and draw it out.

# 8a. You have arr = [1, 2, 3, 4, 5] and two pointers: left = 0, right = 4
#     You want to move them TOWARD each other.
#     left should INCREASE. right should DECREASE.
#     Write the while loop condition that keeps going while they haven't met.


# 8b. You have arr = [1, 2, 3, 4, 5] and you're checking if it's sorted.
#     You compare arr[i] and arr[i+1].
#     For sorted: arr[i] should be <= arr[i+1] for ALL i.
#     Write a loop that checks this. If any pair fails, print "not sorted".
#     If the loop finishes without finding a problem, print "sorted".


# =============================================
# SECTION 9: COMBINING EVERYTHING
# =============================================
# Write a single block of code (no functions) that:
# 1. Has a list: arr = [4, 2, 7, 1, 9, 3]
# 2. Creates an empty list called "evens"
# 3. Loops through arr
# 4. For each element, if it's even, append it to evens
# 5. Prints evens

# Write it below. Then run it. Then check: is the output [4, 2] or [4, 2, 1, 9, 3] or something else?



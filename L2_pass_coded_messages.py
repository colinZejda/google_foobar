"""
Please Pass the Coded Messages==============================

You need to pass a message to the bunny workers, but to avoid detection, the code you agreed to use is... obscure, to say the least. 
The bunnies are given food on standard-issue plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. 
The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. 
Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.You have L, a list containing some digits (0 to 9). 
Write a function solution(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the solution. 
L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

Languages=========
To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases==========
Your code should pass the following test cases.Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:Solution.solution({3, 1, 4, 1})
Output:    4311
Input:Solution.solution({3, 1, 4, 1, 5, 9})
Output:    94311

-- Python cases --
Input:solution.solution([3, 1, 4, 1])
Output:    4311
Input:solution.solution([3, 1, 4, 1, 5, 9])
Output:    94311

Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit your answer.
If your solution passes the test cases, it will be removed from your home folder.
"""

"""
MAIN IDEAS (old soln)
-- trick to check divisibility by 3: if all the digits add to a multiple of 3, it's divisible by 3
-- use backtracking (not all digits must be used, so 2**n possibilities)

def is_div_by_3(lst):
    return sum(lst) % 3 == 0

def backtrack_helper(s, max_found):
    if s and is_div_by_3(s):
        max_found[0] = max(max_found[0], int("".join(map(str, sorted(s, reverse=True)))))
    for i in range(len(s)):
        val = s.pop(i)
        backtrack_helper(s, max_found)
        s.insert(i, val)

def solution(l):
    max_found = [-1]
    backtrack_helper(l, max_found)
    return max_found[0]

if __name__ == "__main__":
    print(solution([3, 1, 4, 1]))        # Out: 4311
    print(solution([3, 1, 4, 1, 5, 9]))  # Out: 94311
"""


"""
MAIN IDEAS (new soln)
    -- digits sum to multiple of 3
    -- sum(l) % 3 == how much we're off by (1 or 2)
    -- find 1 or 2 numbers that, when modded by 3, sum to the amount we're off by
    -- we can remove at most 2 elements, linear time (one scan)
"""

def solution(l):
    l.sort(reverse=True)
    off_by = sum(l) % 3
    if off_by == 0:                           # soln found immediately
        return int(''.join(map(str, l)))
    
    def bye_digit(offby):                     # helper
        for i, digit in enumerate(l[::-1]):
            if digit % 3 == offby:
                del l[len(l) - i - 1]
                return True 
        return False

    if off_by == 1:                          # off by 1 (1 or 2+2)
        if not bye_digit(1):
            if not (bye_digit(2) and bye_digit(2)):
                return 0
    else:                                    # off by 2 (2 or 1+1)
        if not bye_digit(2):
            if not (bye_digit(1) and bye_digit(1)):
                return 0
    return int(''.join(map(str, l))) if l else 0

if __name__ == "__main__":
    print(solution([3, 1, 4, 1]))        # Out: 4311
    print(solution([3, 1, 4, 1, 5, 9]))  # Out: 94311

    print(solution([3, 1, 5, 9]))        # Out: 9531 (or any permutation of these digits)
    print(solution([1, 2, 4]))           # Out: 42
    print(solution([2, 2, 1, 1]))        # Out: 2211
    print(solution([0, 0, 0]))           # Out: 0
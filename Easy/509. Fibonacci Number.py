#https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return n
        if n == 0:
            return n
        return self.fib(n-2) + self.fib(n-1)

"""
Notes/Realizations
 - In all languages except JavaScript and the idea of hoisting (declarations of variables and functions are moved to the top of the defined scope), function declarations must come BEFORE function call.
 - Fibonacci Sequence only applies to the TWO preceding numbers, not a sum of ALL numbers. Can't believe I didn't notice this...
 - When two or more recursive calls are made in the return statemnt, the calls must be terminated fully from left to right before moving onto the next one.
    :Stack frames are made for each recursive call of fib(n-2) until we get to fib(1) + fib(0), then all stack frames are popped and the resulting value is finalized in fib(n-2)
 
 FYI
 Objects are instances of classes, so in order to use the defined Solution, create an object of "Solution" then call it's internal function
"""
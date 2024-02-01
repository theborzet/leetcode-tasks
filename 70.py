# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
class Solution:
    def climbStairs(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        step1 = 1
        step2 = 2
        all = 0
#первый и второй шаг уже учтены
        for _ in range(2, n):
            all = step1 + step2
            step1 = step2
            step2 = all
        
        return all
    

#числа фибоначчи так не считаются, это модификация для этой задачи, если бы нужно было число, то нужно было бы написать условие:
#        if n == 1 or n == 2:
#             return 1 
# И ЕЩЁ, ОН ДОЛГИЙ!
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
    
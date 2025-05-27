# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 

# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # Brute Force
        # if len(s)!=len(goal):
        #     return False
        # curr_s=s
        # n=len(curr_s)
        # for i in range(0,n):
        #     if curr_s==goal:
        #         return True
        #     curr_s=curr_s[-1]+curr_s[:-1]
        # return False

        # Optimal
        if len(s)!=len(goal):
            return False
        double_s=s+s
        if goal in double_s:
            return True
        return False
# https://docs.google.com/document/d/1iHnjJK4cjCK3TYxdDutV__1PqhDVc-dR5bvDvRvuyro/edit?tab=t.0
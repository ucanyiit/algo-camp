# https://leetcode.com/problems/valid-palindrome/

'''
The Python isalpha() method returns true if a string only contains letters. Python isnumeric() returns true if all characters in a string are numbers. Python isalnum() only returns true if a string contains alphanumeric characters, without symbols.
'''

def isPalindromeHelper(s: str, i:int, j: int) -> bool:
    if(i >= j):
        return True
    if (s[i] == s[j]):
        return isPalindromeHelper(s, i+1, j-1)
    return False
    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str = ""
        
        for x in s:
            if(x.isalnum()):
                str += x.lower()
                
        print(str)
        
        return isPalindromeHelper(str, 0, len(str)-1)
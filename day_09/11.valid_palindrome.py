"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

s = input("Enter string: ")

alphabet_str = ""

for ch in s.lower():

    if ch.isalnum():

        alphabet_str += ch

left = 0
right = len(alphabet_str)-1

while(left<right):

    if alphabet_str[left] != alphabet_str[right]:

        print(False)
        break

    else:
        left +=1
        right-=1

else: print(True) 

# Problem Set 1 question 3: alphabetical substrings
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc

# test
s = 'azcbobobegghakl'

# 'a' < 'b' = True

s = list(s)

for i in range(0,len(s)-1):
    alpha_check = s[i] <= s[i+1]
    print(alpha_check)
    print(s[i]+s[i+1])
        





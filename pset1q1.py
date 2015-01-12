# Problem Set 1 question 1: counting vowels

# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5

# for testing
s = 'thequickbrownfoxjumpedoverthelazydog'

vowels = 0

# test individual vowels
vowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

print 'Number of vowels: %d' % vowels
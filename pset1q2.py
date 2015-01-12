# Problem Set 1 question 2: counting bobs
#Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

# should be 8 bobs
s = 'lobobbobbobborboobobobbobobyoboobobb'

bobs = []
# count number of bobs for string s
for i in range(0,len(s)-1):
    # create length 3 tuples from s (in order)
    stuple = s[i:i+3]
    bobs.append(stuple.count('bob')) # append the count (either 1 or 0) to bobs list

count_bobs = sum(bobs)

print 'Number of time bob occurs is: %d' % count_bobs
    
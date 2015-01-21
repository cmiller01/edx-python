print "Please think of a number between 0 and 100!"
print "Is your secret number 50?"

feedback = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
min_point = 0
max_point = 100

if feedback not in ['h','l','c']:
    print 'Sorry, I did not understand your input.'
    feedback = 

if feedback == 'h':
    print 'h'
    
if feedback == 'l':
    print 'l'

if feedback == 'c':
    print 'Game over. Your secret number was: blah'
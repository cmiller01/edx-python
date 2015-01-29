# use vars: balance, annualInterestRate, monthlyPaymentRate
# write out amount paid each month, plus at end amount still due

# Month: 1
# Minimum monthly payment: 96.0
# Remaining balance: 4784.0

# at end
# Total paid: 96.0
# Remaining balance: 4784.0
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


balance = float(balance)
monthlyInterestRate = float(annualInterestRate)/12.0
totalPaid = 0
minimumMonthlyPayment = monthlyPaymentRate*balance
interestDue = monthlyInterestRate*balance
i = 0
while i < 12:
    minimumMonthlyPayment = balance * monthlyPaymentRate
    balance -= minimumMonthlyPayment
    interestDue = balance*monthlyInterestRate
    balance += interestDue
    totalPaid += minimumMonthlyPayment
    i += 1
    print "Month: %d" % (i)
    print "Minimum monthly payment: %s" % (round(minimumMonthlyPayment,2))
    print "Remaining balance: %s" % (round(balance,2))
print "Total paid: %s" % (round(totalPaid,2))
print "Remaining balance: %s" % (round(balance,2))
        
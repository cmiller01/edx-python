# use vars: balance, annualInterestRate
# write out min amount necessary to pay off balance in 12 months
annualInterestRate = 0.2
balance = 3329

def annualAmount(monthlyPayment,annualInterestRate,balance):
    i = 0
    monthlyInterestRate = annualInterestRate/12
    totalPaid = 0
    while i < 12:
        balance -= monthlyPayment
        interestDue = balance*monthlyInterestRate
        balance += interestDue
        totalPaid += monthlyPayment
        i += 1
    return balance

monthlyPayment = 10
while annualAmount(monthlyPayment,annualInterestRate,balance) > 0:
    monthlyPayment +=10
print "Lowest payment: %s" % (monthlyPayment)

    
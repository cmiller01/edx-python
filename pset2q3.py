# use bisection search to the nearest cent
annualInterestRate = 0.2
balance = 320000


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

epsilon = 0.01
low = balance/12.0
high = (balance*(1+annualInterestRate/12.0)**12)/12.0
ans = (low + high)/2.0
while abs(annualAmount(ans,annualInterestRate,balance)) >= epsilon:
    if annualAmount(ans,annualInterestRate,balance) < epsilon:
        high = ans
    else:
        low = ans
    ans = (low + high)/2.0 
print "Lowest payment: %s" % (round(ans,2))
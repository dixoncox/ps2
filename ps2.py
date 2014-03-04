balance = float(raw_input('Enter starting balance:'))
annualInterestRate = float(raw_input('Enter annual interest rate:'))
monthlyPaymentRate = float(raw_input('Enter monthly payment rate:'))
for i in range (1,13):
    minPayment = balance*(1+(annualInterestRate/12.0))*monthlyPaymentRate
    balance = balance - minPayment
    print 'Month:',i
    print 'Minimum monthly payment:', minPayment
    print 'Remaining balance:', balance
    
    
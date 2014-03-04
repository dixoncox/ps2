balance = float(raw_input('Enter starting balance:'))
annualInterestRate = float(raw_input('Enter annual interest rate:'))
monthlyPaymentRate = float(raw_input('Enter monthly payment rate:'))
monthlyInterestRate = annualInterestRate/12.0
updatedMonthlyBalance = balance
for i in range (1,13):
    #balance = balance + balance*annualInterestRate/12.0
    #minPayment = (balance + balance*annualInterestRate/12.0)*monthlyPaymentRate
    #balance = balance - minPayment
    minPayment = updatedMonthlyBalance * monthlyInterestRate
    monthlyUnpaidBalance = updatedMonthlyBalance - minPayment
    updatedMonthlyBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance
    print 'Month:',i
    print 'Minimum monthly payment:', minPayment
    print 'Remaining balance:', updatedMonthlyBalance
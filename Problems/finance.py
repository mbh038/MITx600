def annualStatement(balance,annualInterestRate,monthlyPaymentRate):
    totalPaid=0
    for month in range (1,13):
        minPayment=monthlyPaymentRate*balance
        unpaidbalance=balance-minPayment
        balance=unpaidbalance*(1+annualInterestRate/12)
        totalPaid=totalPaid+minPayment
        print("Month: "+str(month))
        print("Minimum monthly payment: "+str(round(minPayment,2)))
        print("Remaining balance: "+str(round(balance,2)))

    print("Total paid: "+str(round(totalPaid,2)))
    print("Remaining balance: "+str(round(balance,2)))
	
def FinalBalance(balance,annualInterestRate,monthlyPayment):
    """
    Calculates balance owed after one year
    """
    totalPaid=0
    for month in range (1,13):
        unpaidbalance=balance-monthlyPayment
        balance=unpaidbalance*(1+annualInterestRate/12) #print str(balance) 	
    return balance
    
    
def minpayment1(balance,annualInterestRate):
    """
    minimum payment required to pay off balance in one year
    Does not use bisection
    payment must be multiple of $10
    slow with large balances
    """
    
    epsilon=1
    monthlyPayment= -10
       
    endBalance=1
    ncount=0
    while endBalance>0:
        monthlyPayment += 10     
        endBalance=FinalBalance(balance,annualInterestRate,monthlyPayment) 
        print("Monthly payment is: "+str(monthlyPayment))
        print("End balance is: "+str(endBalance))
        
        ncount +=1
        if ncount >100:
            break 
    
    return monthlyPayment
    
	
def minpayment2(balance,annualInterestRate):	
    """
    Calculates minimum payment required to pay off balance in one year
    to within $0.01, using bisection.
    """
    monthlyInterestRate = (annualInterestRate) / 12.0
    monthlyPaymentlb = float(balance / 12)
    monthlyPaymentub = float((balance * (1 + monthlyInterestRate)**12) / 12.0)

    ncount=0
    epsilon=0.01
    monthlyPayment=monthlyPaymentub
    while  True:    
        endBalance=FinalBalance(balance,annualInterestRate,monthlyPayment) 
        #print("Monthly payment is: "+str(monthlyPayment))
        #print("End balance is: "+str(endBalance))
        #print("balance is: "+str(balance))

        if endBalance < -epsilon:
            monthlyPaymentub=monthlyPayment
            monthlyPayment=(monthlyPayment+monthlyPaymentlb)/2
        elif endBalance > epsilon:
            monthlyPaymentlb=monthlyPayment
            monthlyPayment=(monthlyPayment+monthlyPaymentub)/2
        else:
            break
            
        ncount +=1
        if ncount >100:
            break 
    endBalance=FinalBalance(balance,annualInterestRate,monthlyPayment)   
    #print("ncount: "+str(ncount))
    #print("lb is: "+str(monthlyPaymentlb))
    #print("ub is: "+str(monthlyPaymentub))
    print("Lowest Payment: "+str(round(monthlyPayment,2)))
    #print("End balance is: "+str(endBalance))

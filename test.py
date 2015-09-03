balance=float(320000)
annualInterestRate=0.2

monthlyInterestRate = (annualInterestRate) / 12.0
monthlyPaymentlb = float(balance / 12)
monthlyPaymentub = float((balance * (1 + monthlyInterestRate)**12) / 12.0)


def FinalBalance(balance,annualInterestRate,monthlyPayment):
    """
    Calculates balance owed after one year
    """
    totalPaid=0
    for month in range (1,13):
        unpaidbalance=balance-monthlyPayment
        balance=unpaidbalance*(1+annualInterestRate/12) #print str(balance) 	
    return balance
    
endBalance=1
ncount=0
epsilon=0.01
monthlyPayment=monthlyPaymentub
while  True: #abs(endBalance)>epsilon:    
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

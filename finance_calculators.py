#importing math library to use maths functions
import math

#printing the menu for the user to select 
print("investment - To calculate the amoun of interest you'll earn on your investment.")
print("bond - To calculate the amount you'll have to pay on a home loan.\n\n")


#using if else statements enabling the user to select b/w  'investment' or 'bond' irrespective of case-sensitive
select=input("please enter either 'investment' or 'bond' from the menu above to proceed: ")
select=select.lower()

#using if-else statenment to find the total amount user gets based on his interest_type as 'simple interest' or 'comound interst' 
if select=='investment':
    Principal_amount=float(input("please enter the amount you want to deposit: "))
    interest_rate=float(input("enter the interest rate: "))
    r=interest_rate/100
    years=float(input("please enter the no.of years you are planning to invest: "))
    interest_type=input("please enter your interest type as 'simple' or 'compound': ")
    if interest_type=='simple':
        amount=Principal_amount*(1+(r*years))
    else:
        amount=Principal_amount*math.pow((1+r),years)
        amount=round(amount,3)
    print(f"The total amount you get after {years} years with interest rate {interest_rate}% is {amount}")

#calculating the total amount the user will have to repay each month if he enters 'bond'
 
elif select=='bond':
    house_value=float(input("please enter your present value of the house: "))
    interest_rate=float(input("please enter interest rate: "))
    r=interest_rate/100
    monthly_interest=r/12
    months=int(input("please enter the no. of months you take to repay the bond: "))
    repayment=(monthly_interest*house_value)/(1-((1+monthly_interest)**(-months)))
    repayment=round(repayment,3)
    print(f"The amount you have to repay each month is  {repayment}")
else:
    print("Invalid selection. please select either of the above menu.")    


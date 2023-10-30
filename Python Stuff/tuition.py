#Name: Loren Lemarr
#Name: Christina Creegan
#Prog Purpose: This program computes PVCC college tuition & fees based on the number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees
#   Price for adults: $156.61
#   price for children: $336.21
#   Service fee rate: $23.50
#   Sales tax rate: $1.75
#                   $2.90

import datetime

######################     define global variables      ######################
# define tax rate and prices
RATE_TUITION_IN = 156.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1 #1 = instate,  2 = out of state
numcredits = 0
scholarshipamt = 0
capital_amt = 0

######################     define program functions     ######################
def main():
    
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nWould you like to calculate tuition and fees for another student (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain == "n":
            more = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition_amount, capital_amt,  institution_fee, student_fee, total, balance
    if inout == 1:
        tuition_amount = RATE_TUITION_IN * numcredits
    else:
        tuition_amount = RATE_TUITION_OUT * numcredits
        capital_amt = RATE_CAPITAL_FEE * numcredits

    institution_fee = RATE_INSTITUTION_FEE * numcredits
    student_fee = RATE_ACTIVITY_FEE * numcredits
    total = tuition_amount + capital_amt + institution_fee + student_fee
    balance = total - scholarshipamt
def display_results():
    moneyf = '8,.2f'
    print('------------------------------')
    print('**** PVCC*****')
    print('Costs for enrollment')
    print('------------------------------')
    print('Tuition amount\t\t$'+format(tuition_amount, moneyf))
    print('Capital fee\t\t$'+format(capital_amt, moneyf))
    print('Institution fee\t\t$'+format(institution_fee, moneyf))
    print('Activity fee\t\t$'+format(student_fee, moneyf))
    print('Total\t\t\t$'+format(total, moneyf))
    print('Scholarship amount\t$'+format(scholarshipamt, moneyf))
    print('Balance\t\t\t$'+format(balance, moneyf))
    print('------------------------------')
    print(str(datetime.datetime.now()))
    
######################      call on main program to execute ######################

main()




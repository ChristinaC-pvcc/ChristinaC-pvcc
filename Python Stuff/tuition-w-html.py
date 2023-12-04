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

import os

import webbrowser

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

# create output file
outfile = 'tuition-webpage.html'

# html stuff
tr = '<tr><td>'
endtd = '</td><td>'
endtr = '</td></tr>\n'
colsp = '<tr><td colspan= "3">'
sp = " "

######################     define program functions     ######################
def main():
    open_outfile()
    
    more = True

    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        askAgain = input("\nWould you like to calculate tuition and fees for another student (Y or N)?: ")
        if askAgain.upper() == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()
            webbrowser.open_new_tab(outfile)

def get_user_data():
    global inout, numcredits, scholarshipamt
    
    inout = check_inout()
    numcredits = check_numcredits()
    scholarshipamt = check_scholarshipamt()

def check_inout():
    again = True
    while again:
        var = input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: ")
        if var.isnumeric():
            if int(var) > 2 or int(var) == 0:
                again = True
                print("ERROR")
            else:
                again = False
        else:
            again = True
            print("ERROR")
    return int(var)

def check_numcredits():
    again = True
    while again:
        var = input("Number of credits registered for: ")
        if var.isnumeric():
            again = False
        else:
            again = True
            print("ERROR")
    return int(var)

def check_scholarshipamt():
    again = True
    while again:
        var = input("Scholarship amount received: ")
        if var.replace(".", "").isnumeric():
            again = False
        else:
            again = True
            print("ERROR")
    return float(var)

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

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Cinema House Movies </title>\n')
    f.write('<style> td{text-align: left} h2{text-align: center} </style> </head>\n')
    f.write('<body style ="background-color: #985b45; background-image: url(wp-tuition.png); color: #A20045;">\n')

def create_output_file():
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    f.write('\n<table border="3"   style ="background-color: #FFFFFF;  font-family: arial; margin: auto;">\n')
    f.write(colsp + '\n')
    f.write('<h2>PVCC</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('*** Costs for enrollment ***\n')

    create_row('Tuition amount', tuition_amount)
    create_row('Capital fee', capital_amt)
    create_row('Institution fee', institution_fee)
    create_row('Activity fee', student_fee)
    create_row('Total', total)
    create_row('Scholarship amount', scholarshipamt)
    create_row('Balance', balance)

    f.write(colsp + 'Date/Time: '+ day_time + endtr)

    f.write('</table><br/>')

def create_row(text, money):
    fmoney = '$' + format(money, '8,.2f')
    
    f.write(tr + text + endtd + sp + endtd + fmoney + endtr)
    
######################      call on main program to execute ######################

main()




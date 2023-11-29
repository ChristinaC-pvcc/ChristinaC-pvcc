# Name: Christina Creegan
# Prog Purpose: This program creates a payroll report

import datetime

    ### LISTS of data (freshfoods_skeleton.py) ####

emp = [
"Smith, James ", "Johnson, Patricia", "Williams, John ",
"Brown, Michael ", "Jones, Elizabeth ", "Garcia, Brian ",
"Miller, Deborah ", "Davis, Timothy ", "Rodriguez, Ronald",
"Martinez, Karen ", "Hernandez, Lisa ", "Lopez, Nancy ",
"Gonzales, Betty ", "Wilson, Sandra ", "Anderson, Margie ",
"Thomas, Daniel ", "Taylor, Steven ", "Moore, Andrew ",
"Jackson, Donna ", "Martin, Yolanda ", "Lee, Carolina ",
"Perez, Kevin ", "Thompson, Brian ", "White, Deborah ",]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M",]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

    ### TUPLES of constants ###

# Cashier, Stocker, Janitorial, Maintenance
# vvv       C     S      J      M
# vv INDEX: 0     1      2      3
PAY_RATE = (16.5, 15.75, 15.75, 19.5)

# vvv       fed, state, social, medi, retire
# vv INDEX:    0   1    2      3    4
DED_RATE = (.12, .03, .062, .0145, .04)

    ### NEW LISTS for calculated amounts ###
gross_pay = []

fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []

net_pay = []

total_gross = 0
total_net = 0

    ### program functions ###
def main():
    perform_calculations()
    display_results()
    pass

def calc_pay(i, num):
    return hours[i]* PAY_RATE[num]

def perform_calculations():
    global total_gross, total_net

    #calculate gross pay
    for i in range(num_emps):
        if job[i] == "C":
            pay = calc_pay(i, 0)
            pass
        
        elif job[i] == "S":
            pay = calc_pay(i, 1)
            pass
        
        elif job[i] == "J":
            pay = calc_pay(i, 2)
            pass
        
        else:
            pay = calc_pay(i, 3)
            pass
        
        gross_pay.append(pay)
        
        #calculate deductions
        #+ append amount to lists
        fed = pay * DED_RATE[0]
        fed_tax.append(fed)
        
        state = pay * DED_RATE[1]
        state_tax.append(state)
        
        soc = pay * DED_RATE[2]
        soc_sec.append(soc)
        
        med = pay * DED_RATE[3]
        medicare.append(med)

        retire = pay * DED_RATE[4]
        ret401k.append(retire)

        net = pay - fed - state - soc - med - retire
        net_pay.append(net)

        #add to totals
        total_gross += pay
        total_net += net

        pass
    pass

def display_results():
    moneyF = '8,.2f'
    
    line = '-----------------------------------------------------------------------------------------------------------------------------'
    stars = '****************************************************'
    sm_line = '---------------------------------------------------'
    tab = "\t"

    print(line)
    print(stars + " FRESH FOODS MARKET " + stars)
    print(sm_line + " WEEKLY PAYROLL REPORT " + sm_line)
    print(tab + str(datetime.datetime.now()))
    print(line)

    titles1 = "| Employe Name       |_| Code |_| Gross   |_| Fed Inc Tax |_"
    titles2 = "| State Inc Tax |_| Soc Sec |_| Medicare |_| 401k   |_| Net     |"
    print( titles1 + titles2)
    print(line)

    for i in range(num_emps):
        emp_name = "   "+format(emp[i], '<23')
        code = format(job[i], '<7')
        gross = format(format(gross_pay[i], moneyF), '<11')
        fed = format(format(fed_tax[i], moneyF), '<16')
        state = format(format(state_tax[i], moneyF), '<18')
        soc = format(format(soc_sec[i], moneyF), '<11')
        med = format(format(medicare[i], moneyF), '<14')
        retire = format(format(ret401k[i], moneyF), '12')
        net = format(net_pay[i], moneyF)
        print(emp_name + code + gross + fed + state + soc + med + retire + net)
    
    print(line)
    print(stars + " TOTAL GROSS: $" + format(total_gross, moneyF))
    print(stars + " TOTAL NET  : $" + format(total_net, moneyF))
    print(line)
    pass

    ### run finctions ###
main()

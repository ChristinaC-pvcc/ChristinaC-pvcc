# Name: Christina Creegan
# Prog Purpose: This program creates a payroll report

import datetime

import subprocess

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
    create_output_file()
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

def create_output_file():
    moneyF = '8,.2f'
    
    line = '-----------------------------------------------------------------------------------------------------------------------------------------'
    stars = '**************************************'
    sm_line = '----------------------------------------------------'
    tab = "\t"
    new = "\n"

    ### output file ###
    out_file = "payroll.txt"
    f = open(out_file, "w")
    
    f.write(line)
    f.write(new + stars + " FRESH FOODS MARKET " + stars)
    f.write(new + sm_line + " WEEKLY PAYROLL REPORT " + sm_line)
    f.write(new + tab + tab + tab + tab + str(datetime.datetime.now()))
    f.write(new + line)

    titles1 = "| Employe Name | Code \t| Gross | Fed Inc Tax "
    titles2 = "| State Inc Tax \t| Soc Sec | Medicare | 401k \t| Net |"
    f.write(new + titles1 + titles2)
    f.write( new + line)

    for i in range(num_emps):
        emp_name = emp[i] + tab
        code = job[i] + tab
        gross = add_tab(gross_pay[i])
        fed = add_tab(fed_tax[i])
        state = add_tab(state_tax[i]) + tab
        soc = add_tab(soc_sec[i])
        med = add_tab(medicare[i])
        retire = add_tab(ret401k[i])
        net = format(net_pay[i], moneyF)
        f.write(new + emp_name + code + gross + fed + state + soc + med + retire + net)
    
    f.write(new + line)
    f.write(new + stars + " TOTAL GROSS: $" + format(total_gross, moneyF))
    f.write(new + stars + " TOTAL NET  : $" + format(total_net, moneyF))
    f.write(new + line)
    f.close()
    
    print("Open " + out_file + " to view your report")
    #subprocess.Popen(['\\Windows\\notepad.exe', 'payroll.txt'])
    pass

def add_tab(var): 
    finished = format(var, '8,.2f') + "\t"
    return finished
    pass

    ### run finctions ###
main()

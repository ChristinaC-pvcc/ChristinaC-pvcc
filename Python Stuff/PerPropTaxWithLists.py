# Name: Christina
# Program Purpose:
'''
This program uses lists to find the personal property tax for
vehicals in Charlottesville and produces a report which displays all
data and the total tax due.
'''
# Personal property tax in Charlottesville:
#   -- $4.20 per $100 of vehicle value (4.20% per year)
#   -- Paid every six months (6/12 months of a year)
# Personal Property Tax Relief (PPTR):
#   -- Eligibility:
'''
        Owned or leased vehicles are predominately used for non-buisness
        purposes & have passenger license plates
'''
#   -- Tax relief for qualified vehicles is 33%

import datetime

    ### define tax rates ###
PPT_RATE = 0.042
RELIEF_RATE = 0.33

    ### create list data ###
vehicle = ["2019 Volvo", "2018 Toyota", "2022 Kia", "2020 Ford", "2023 Honda", "2019 Lexus"]

vehicle_value = [13000, 10200, 17000, 21000, 28000, 16700]

pptr_eligible = ["y", "y", "n", "Y", "N", "y"]

owner_name = ["Brand, Debra", "Smith, Carter", "Johnson, Bradley", "Garcia, Jennifer", "Wenderson, Leticia",
              "white, Danielle"]
ppt_owed = []

    ### other varibles ###
num_vehicles = len(vehicle)
tax_due = 0
total = 0

    ### define functions ###
def main():
    again = True
    while again:
        perform_calculations()
        display_results()
        input("print again?\nEnter Y or N: ")
    pass

def perform_calculations():
    global total#, ppt_owed

    for i in range(num_vehicles):
        tax_due = (vehicle_value[i] * PPT_RATE) / 2

        if pptr_eligible[i].upper() == "Y":
            tax_due = tax_due * 0.67

        ppt_owed.append(tax_due)

        total += tax_due
    pass

def display_results():
    moneyf = '8,.2f'
    line = "------------------------------------------------------------------------"
    sm_line = "*********************"
    tab = "\t"
    tabx2 = "\t\t"
    tabx3 = "\t\t\t"

    print(line)
    print(sm_line + " PERSONAL PROPERTY TAX REPORT " + sm_line)
    print("\n\t\t\tCharlottesville, Virginia")

    print("\n\t\tRUN DATE/TIME: " + str(datetime.datetime.now()))
    print(format("\nNAME", '25') + format("VEHICLE", '16') + format("VALUE", '16') +
          format("RELIEF", '9') + "TAX DUE")
    print(line)

    for i in range(num_vehicles):
        dataline1 = a_format( owner_name[i] ) + a_format( vehicle[i] ) + a_format( format(vehicle_value[i],moneyf) )
        dataline2 = a_format( pptr_eligible[i].upper() ) + a_format( format(ppt_owed[i],moneyf) )
        print(dataline1 + dataline2)
        pass
    
    print(line)
    print(sm_line + sm_line + "****** TOTAL TAX DUE: " + format(total,moneyf))
    pass

def a_format(text):
    if len(text) > 11:
        return(format(text, '24'))
    elif len(text) > 1:
        return(format(text, '16'))
    else:
        return(format(text, '7'))
    pass

### active functions ###

main()

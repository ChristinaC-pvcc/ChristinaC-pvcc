# Name: Christina C
# Prog Purpose: Dispay a tax bill for the
#               amount owed for the property tax for vehicles in CHarlottesvile

import datetime

    ### define global varibles ###
# fixed varibles

PP_TAX_RATE = 0.042 # 4.20% Anual Personal Property Tax Rate
VEHICAL_VAL_RATE = 100 # $100 Amount that the PP Tax Rate is apllied
PAID_TIME = 0.5 # Time in a year or less when pay occours
TAX_RELIEF = 0.33 #Tax relief

# other varibles

assesed_value = "null"
is_eligible = "null"
line = "---- ---- ---- ---- ----"

anual_tax_amnt = 0

sub_total = 0
relief_amnt = 0
total = 0

    ### Functions/Methods ###

def main():
    is_entering = "Y"
    
    while is_entering.upper() != "N":
        is_entering = input("\nEnter a vehicle for tax?\nType Yes(Y) or No(N): ")
        if is_entering.upper() != "Y" and is_entering.upper() != "N":
            error("lower or upper case 'y' or 'n'.")

        if is_entering.upper() == "Y":
            reset()
            get_userinput()
            perform_calculations()
            print_bill()

def format_it(number):
    moneyfrmt = '10,.2f'
    number = float(number)
    number = round(number, 2)
    return format(number, moneyfrmt)

def error(error_type):
    global line
    
    print("\n"+line)
    print("ERROR: This input has to be a " + str(error_type))
    print(line+"\n")

def reset():
    global assesed_value, is_eligible, anual_tax_amnt, sub_total, relief_amnt, total
    assesed_value = "null"
    is_eligible = "null"

    anual_tax_amnt = 0

    sub_total = 0
    relief_amnt = 0
    total = 0

def get_userinput():
    global line, assesed_value, is_eligible

    is_float = False
    
    while is_float == False:
        assesed_value = input("\nInput the assessed value of the vehicle.\nEnter Amount: ")

        # vvv check if assesed_value is a float
        if assesed_value.replace(".", "").isnumeric():
            is_float = True
        else:
            is_float = False
            error("number greater or equal to zero.")
    print()
            
    while is_eligible.upper() != "Y" and is_eligible.upper() != "N":
        print("To be eligible the vehical has to be owned or leased- which are predominately\n"+
              "used for non-buisness purposes and have passenger license plates.")
        print(line)
        is_eligible = input("Is the vehical eligible?\nEnter Yes(Y) or No(N): ")
        if is_eligible.upper() != "Y" and is_eligible.upper() != "N":
            error("lower or upper case 'y' or 'n'.")

def perform_calculations():
    global line, assesed_value, sub_total, relief_amnt, total
    anual_tax_amnt = float(assesed_value) * PP_TAX_RATE
    sub_total = anual_tax_amnt * PAID_TIME
    
    if is_eligible.upper() == "Y":
        relief_amnt = sub_total * TAX_RELIEF
        
    total = sub_total - relief_amnt

def print_bill():
    print("\n"+line+"\n\tTAX BILL\n"+line)
    print("Assesed Value:\t $" + format_it(assesed_value))
    print("Full Tax Amount: $" + format_it(sub_total))
    print("Relief:\t\t $" + format_it(relief_amnt))
    print("Total Due:\t $" + format_it(total))
    print(line)
    print(str(datetime.datetime.now()))
    print(line+"\n"+line)

    ### Run Main ###

main()

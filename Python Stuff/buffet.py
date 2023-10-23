# Name: Christina Creegan, Edward Watson
# Prog Purpose: This program finds the cost of movie tickets

#   Price for one ticket: $19.95
#   Price for one bucket of popcorn $11.95
#   Service fee rate: 10%
#   Sales tax rate: 6.2%

import datetime

    ### define global varibles ###
# define tax rate and prices
SALES_TAX_RATE = 0.062
SERVICE_FEE_RATE = 0.1
PR_ADULT = 19.95
PR_CHILD = 11.95


#define global variables
num_adults = 0
num_children = 0

subtotal = 0
sales_tax = 0
total = 0

    ### define program functions ###
def main():
    more_orders = True

    while more_orders:
        y_or_n_ans = False
        
        get_user_data() # get user input -> set/change num_adults
        perform_calculations()
        display_results()
        
        while y_or_n_ans == False:
            askAgain = input('\nWould you like to order again (Y or N)?: ')
            
            if askAgain.upper() == "Y":
                y_or_n_ans = True
                
            if askAgain.upper() == "N": #.upper() uppercases a string
                more_orders = False
                y_or_n_ans = True
                print('Thank you for ordering. Enjoy your meal!')

def get_user_data(): # get user input -> set/change num_adults
    global num_adults, num_children # get global varible
    
    num_adults = int(get_amount("How many adults?: \n"))   
    num_children = int(get_amount("How many children?: \n"))
            
def get_amount(text):
    is_int_input = False
    var = 0
    
    while is_int_input == False:
        var = input(text) # starts a prompt and sets varible to the input given
        if var.isnumeric() == True:
            var = int(var)
            is_int_input = True
            return var

# money stuff
def perform_calculations():  
    global adult_cost, child_cost, drink_cost, sales_tax, total, base_cost, service_fee # get multiple global varible

    adult_cost = num_adults * PR_ADULT # set base price -> cost
    child_cost = num_children * PR_CHILD
    
    base_cost = adult_cost + child_cost # add all costs | subtotal = int(input()) * 10.99
    service_fee = base_cost * SERVICE_FEE_RATE
    sales_tax = base_cost * SALES_TAX_RATE # sales_tax = subtotal * 0.055 
    total = base_cost + sales_tax
    

def display_results():
    moneyfrmt = '10,.2f'
    line = '._.>^);:\',L;: >^);:\',L;:._.\n'
    
    print(line)
    print('| BRANCH BARBECUE BUFFET |')
    print(line)
    # '8,.2f' output should be: (use format(#, #) not str(#)
    #   in a width of 8/ 8 integers(int)
    #   floating point of 2 decimals/floats
    print('Adults\t\t$ ' + format(adult_cost, moneyfrmt))
    print('Children\t$ ' + format(child_cost, moneyfrmt) + '\n')
    print(line)
    print('Subtotal\t$ ' + format(base_cost, moneyfrmt))
    print('Service Fee\t$ ' + format(service_fee, moneyfrmt))
    print('Sales Tax\t$ ' + format(sales_tax, moneyfrmt))
    print('Total\t\t$ ' + format(total, moneyfrmt) + '\n')
    print(line)
    print(str(datetime.datetime.now()))
    
    ### call on main program to execute ###
main()

    ### PYTHONIC/PYTHON NOTES ###
# uppercase = will not change
# functions, subroutine, procedure
# inorder to change a global var within a func you have to get it
#   ex. global num_adults
# double bubble rule:
#   %

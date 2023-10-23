# Name: Christina
# Prog Purpose: This program finds the cost of movie tickets

#   Price for one ticket: $10.99
#   Price for one bucket of popcorn $12.99
#   Price for one drink is $4.99
#   Sales tax rate: 5.5%

import datetime

    ### define global varibles ###
# define tax rate and prices
SALES_TAX_RATE = 0.055
PR_TICKET = 10.99
PR_POPCORN = 12.99
PR_DRINK = 4.99

#define global variables
num_tickets = 0
num_popcorn = 0
num_drinks = 0

extra_costs = 0

subtotal = 0
sales_tax = 0
total = 0

    ### define program functions ###
def main():
    more_tickets = True

    while more_tickets:
        y_or_n_ans = False
        
        get_user_data() # get user input -> set/change num_tickets
        perform_calculations()
        display_results()
        
        while y_or_n_ans == False:
            askAgain = input('\nWould you like to order again (Y or N)?: ')
            
            if askAgain.upper() == "Y":
                y_or_n_ans = True
                
            if askAgain.upper() == "N": #.upper() uppercases a string
                more_tickets = False
                y_or_n_ans = True
                print('Thank you for ordering. Enjoy your movie!')

def get_user_data(): # get user input -> set/change num_tickets
    global num_tickets, num_popcorn, num_drinks # get global varible
    
    num_tickets = int(get_amount("Insert number of moive tickets: \n"))   
    num_popcorn = int(get_amount("Insert popcorn amount: \n"))
    num_drinks = int(get_amount("Insert drink amount: \n"))

#def number_of(var):
    #

#figure out how to choose a size and have it add an extra cost if bigger then a small
def get_size(var, text):
    global extra_costs
    
    is_str_input = False
    amount = 0

    while is_str_input == False:
        var = input(text) # starts a prompt and sets varible to the input given
        if var.is_string() == True:
            var = str(var)
            match var.upper():
                case 'S':
                    amount = 1.99
                case 'M':
                    amount = 2.99
                case 'L':
                    amount = 3.99
                    
            extra_costs = extra_costs + amount
            is_str_input = True
            
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
    global ticket_cost, popcorn_cost, drink_cost, sales_tax, total # get multiple global varible

    ticket_cost = num_tickets * PR_TICKET # set base price -> cost
    popcorn_cost = num_popcorn * PR_POPCORN
    drink_cost = num_drinks * PR_DRINK
    
    base_cost = ticket_cost + popcorn_cost + drink_cost # add all costs
    # subtotal = int(input()) * 10.99
    sales_tax = base_cost * SALES_TAX_RATE
    # sales_tax = subtotal * 0.055 
    total = base_cost + sales_tax
    

def display_results():
    moneyfrmt = '10,.2f'
    line = '\t._.>^);:\',L;: >^);:\',L;:._.\n'
    
    print(line)
    print('\t   | CINEMA HOUSE MOVIES |')
    print('\tYour neighborhood movie house\n')
    print(line)
    # '8,.2f' output should be: (use format(#, #) not str(#)
    #   in a width of 8/ 8 integers(int)
    #   floating point of 2 decimals/floats
    print('\tTickets\t  $ ' + format(ticket_cost, moneyfrmt))
    print('\tPopcorn\t  $ ' + format(popcorn_cost, moneyfrmt))
    print('\tDrinks\t  $ ' + format(drink_cost, moneyfrmt) + '\n')
    print(line)
    print('\tSales Tax $ ' + format(sales_tax, moneyfrmt))
    print('\tTotal\t  $ ' + format(total, moneyfrmt) + '\n')
    print(line)
    print('\t' + str(datetime.datetime.now()))
    
    ### call on main program to execute ###
main()

    ### PYTHONIC/PYTHON NOTES ###
# uppercase = will not change
# functions, subroutine, procedure
# inorder to change a global var within a func you have to get it
#   ex. global num_tickets
# double bubble rule:
#   %

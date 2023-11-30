# Name: Christina Creegan
# Prog Purpose: This program computes and displays a receipt for items purchased

#   PIZZAS
#   Price for Small: $9.99
#   Price for Medium: $12.99
#   Price for Large: $17.99
#   Price for Extra Large: 21.99
#   Price for Drink: $3.99
#   Price for Breadsticks: $6.99
#   Sales tax rate: 5.5%

import datetime

    ### define global varibles ###
# fixed varibles
#   define tax rate and prices
SALES_TAX_RT = 0.055
PR_PSMLL = 9.99 # pizza small
PR_PMED = 12.99 # pizza medium
PR_PLRG = 17.99 # pizza large
PR_PXLRG = 21.99 # pizza extra large
PR_DRNK = 3.99 # drink
PR_BRDSTCK = 6.99 # breadstick

# other varibles
num_pizzas = 0
num_drinks = 0
num_breadsticks = 0

num_psmll = 0
num_pmed = 0
num_plrg = 0
num_pxlrg = 0

pizza_sizes = []

pizza_cost = 0
drink_cost = 0
bread_cost = 0
subtotal = 0
sales_tax = 0
total = 0

line = '-------------------------------'

### functions ###
def main():
    order_again = True
    ask = ''
    
    while order_again == True:
        get_userinput()
        perform_calculations()
        print_recipt()

        retry = True

        while retry == True:
            print(line)
            
            ask = input("\nOrder again?\nEnter Yes(Y) or No(N): ")
            
            if ask.upper() != "Y" and ask.upper() != "N":
                print(line)
                print("ERROR: '" + ask + "'" + " is not a vaild input")
                print(line)
                retry = True
                
                
            else:
                retry = False
                if ask.upper() == "N":
                    order_again = False
                else:
                    order_again = True
            print(line)
                    
    pass

def get_userinput(): # set input to global varibles
    global num_pizzas, num_drinks, num_breadsticks

    text = "Enter Amount (0, 1, 2...etc): "

    print(line)
    num_pizzas = retry_input("pizza", text)
    print(line)
    order_pizza(num_pizzas)
    num_drinks = retry_input("drinks", text)
    print(line)
    num_breadsticks = retry_input("breadsticks", text)
    print(line)
    pass

def retry_input(item, enter): # obtains and checks input to see if numeric (an integer above 0)
    retry = True
    
    while retry == True:
        num = input("\nOrder " + item + "?\n" + enter)
        if num.isnumeric(): # 'num' IS numeric
            retry = False
        else: # 'num' is NOT numeric
            retry = True
            print(line)
            print("ERROR: '" + num + "'" + " is not a vaild input")
            print(line)
    return(num)

def order_pizza(num):
    global pizza_sizes

    textp = "Enter size (0, 1, 2, 3): "
    
    print("(there are " + num + " pizzas total)")
    
    num = int(num)
    
    if num > 0:
        for i in range(num):
            retry = True
            
            while retry == True:
                print(line)
                data1 = "[Sizes: 0 for Small, 1 for Medium, 2 for Large, and 3 for Extra Large]"
                print("\nWhat size is pizza #" + str(i+1) + "?\n" + data1)
                pizza_sizes.append(retry_input("size", textp))
                
                if int(pizza_sizes[i]) > 3:
                    print(line)
                    print("\nERROR: '" + str(pizza_sizes[i]) + "'" + " is not a vaild input")
                    pizza_sizes.pop(i)
                    retry = True
                else:
                    retry = False
                    print(line)
    pass
    

def perform_calculations():
    global num_pizzas, pizza_cost, drink_cost, bread_cost, subtotal, sales_tax, total
    
    if int(num_pizzas) > 0:
        for i in pizza_sizes:
            if int(i) == 0:
                pizza_cost += PR_PSMLL
                
            elif int(i) == 1:
                pizza_cost += PR_PMED
                
            elif int(i) == 2:
                pizza_cost += PR_PLRG
                
            else:
                pizza_cost += PR_PMED
    else:
        pizza_sizes.clear()
        pizza_cost = 0
                
    drink_cost = float(num_drinks) * PR_DRNK
    bread_cost = float(num_breadsticks) * PR_BRDSTCK
    subtotal = pizza_cost + drink_cost + bread_cost
    sales_tax = subtotal * SALES_TAX_RT
    total = subtotal + sales_tax
    pass

def print_recipt():
    print("\n Receipt:" + line)
    print("******** PALERMO PIZZA ********")
    print(line)
    string("Pizza", num_pizzas, pizza_cost)
    string("Drinks", num_drinks, drink_cost)
    string("Breadsticks", num_breadsticks, bread_cost)
    print(line)
    string("Subtotal:", '', subtotal)
    string("Tax:", '', sales_tax)
    print(line)
    string("Total:", '',total)
    print(line)
    print(str(datetime.datetime.now()))
    pass

def string(text, num, var):
    money = '8,.2f'
    tab = "\t"
    
    if num != '':
        print(str(format((text + "[" + num + "]:"), '10')) + tab + "$" +str(format(var, money)))
    else:
        print(str(format(text, '10')) + tab + "$" +str(format(var, money)))
    pass
    

### run functions ###
main()

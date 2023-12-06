# Name: Christina Creegan
# Prog Purp: Create a web page sales report for
#            Emerald Beach Hotel & Resort

import datetime
import webbrowser

    ### define global varibles ###

#Room codes and room rates
SR = 195 # Single Room per Night
DR = 250 # Double Room per Night
SU = 350 # Suite per Night

#Tax rates
SALES_TX_RT = .065 # Sales tax rate
OCCUPANCY_TX_RT = .1125 # Occupancy tax rate

#Calculations
subtotal = []
sales_tax = []
occupancy_tax = []
total = []
grand_total = 0

#
cust = []
outfile = "emerald.csv"
html_file = "hotelsalesrep.html"


    ### create functions ###
def main():
    read_in_cust_files()
    perform_calculations()
    create_html_file()
    #webbrowser.open_new_tab(html_file)

def perform_calculations():
    global subtotal, sales_tax, occupancy_tax, total, grand_total, num_cust
    
    num_cust = len(cust_in)
    
    #calculate room price
    for i in range(num_cust):
        
        room = cust[i][2]

        #calculate room price
        if room == "SR":
            room_pr = SR
            
        if room == "DR":
            room_pr = DR
            
        if room == "SU":
            room_pr = SU

        #calculate subtotal
        nights = cust[i][3]
        subtotal.append(int(nights) * room_pr)

        #calculate sales tax
        sales_tax.append(subtotal[i] * SALES_TX_RT)

        #calculate occupancy tax
        occupancy_tax.append(subtotal[i] * OCCUPANCY_TX_RT)

        #calculate total (add subtotal, sales tax, and occupancy tax)
        total.append(subtotal[i] + sales_tax[i] + occupancy_tax[i])

        #calculate grand total (add all totals)
        grand_total += total[i]
        
def read_in_cust_files():
    global cust_in
    
    cust_data = open(outfile, "r")
    cust_in = cust_data.readlines()
    cust_data.close()

    #split the data into fields
    for i in cust_in:
        cust.append(i.split(","))

def open_html_file():
    global f
    f = open(html_file, 'w')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: left; padding: 5px; padding-right: 7px; background-color: #EFF5EB;} h2{text-align: center} </style> </head>\n')
    f.write('<body style ="background-color: #D0DCC6; background-image: url(emerald-wp.png); color: #36A455;">\n')
    pass

# html stuff
TR = '<tr><td>'
ENDTD = '</td><td>'
ENDTR = '</td></tr>\n'
COLSP = '<tr><td colspan = "7">'
SP = " "

def create_html_file():
    open_html_file()

    today = str(datetime.datetime.now())
    day_time = today[0:16]
    
    f.write('\n<table border="3" style = "border: 3px solid#1F853C; background-color: #D0DCC6;;  font-family: Trebuchet MS; margin: auto;">\n')
    f.write(COLSP+ '\n')
    f.write('<h2>Emerald Beach Hotel & Resort</h2></td></tr>')
    f.write('<tr><td colspan = "7" style="text-align: center">' + '\n')
    f.write('Sales Report Date/Time: '+ day_time +'\n')

    f.write(TR + "Last Name" + ENDTD + "First Name" + ENDTD + "Number of Nights" + ENDTD + "Subtotal" + ENDTD + "Sales Tax" + ENDTD + "Occupancy Tax" + ENDTD + "Total" + ENDTR)
    for i in range(num_cust):
        create_row(i)
        
    f.write(COLSP + TR + "Grand Total" + '</td><td COLSPan= "6">' + format_money(grand_total) + ENDTR + ENDTR)

    #close html file    
    f.write('</body></html>')
    f.close()
    pass

def create_row(num):

    last_name = cust[num][0]
    first_name = cust[num][1]
    night = cust[num][3]

    sub = format_money(subtotal[num])
    sales = format_money(sales_tax[num])
    occupancy = format_money(occupancy_tax[num])
    tot = format_money(total[num])
    
    f.write(TR + last_name + ENDTD + first_name + '</td><td style="text-align: center">' + night + ENDTD + sub + ENDTD + sales + ENDTD + occupancy + ENDTD + tot + ENDTR)

def format_money(var):
    return '$' + format(var, '10,.2f')

    ### run functions ###
main()

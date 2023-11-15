import datetime

# Define constants
PR_TICKET = 10.99
SALES_TAX_RATE = 0.055

# Initialize global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

def main():
    more_tickets = True
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()
        ask_again = input("Would you like to order more tickets? (Y/N): ")
        more_tickets = ask_again.upper() == 'Y'

    print("Thank you for your order. Enjoy your movie!")

def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print("***CIRENA HOUSE MOVIES ***")
    print("Your neighborhood movie house")
    print('Tickets   $'+format(subtotal,'8,.2f'))
    print('Sale Tax  $'+format(sales_tax,'8,.2f'))
    print('Total     $'+format(total,'8,.2f'))
    print('-----------------------')
    print(str(datetime.datetime.now()))
    

# Run the program
if __name__ == "__main__":
    main()

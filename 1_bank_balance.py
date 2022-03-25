customer_name = input("Welcome, what is your name? ")
starting_balance = 5000.25
pay_check = float(input("How much of your paycheck would you like to deposit? $"))



def welcome_message(customer_name):
    global starting_balance
    starting_balance = starting_balance + pay_check
    print(f"Hello {customer_name}, your starting balance is at ${starting_balance}")
welcome_message(customer_name) 
#! You need ^^^ this to actually make the text pop up

expenditure_items = input("You went shopping earlier today. What did you buy? ")
expenditure = float(input("How much did it cost? $"))

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    global pay_check, starting_balance, customer_name, expenditure_items, expenditure
    customer_name = user_name
    starting_balance = balance
    pay_check = deposits
    expenditure_items = expense_item
    expenditure = expense_amount
    ending_balance = balance + deposits - expense_amount
    print(f"{user_name}, after spending money on the {expense_item} in the amount of {expense_amount}, your checking balance now stands at {ending_balance}.")
checking_balance(customer_name, starting_balance, pay_check, expenditure_items, expenditure)
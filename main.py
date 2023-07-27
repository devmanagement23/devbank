import pyfiglet
from termcolor import colored
def main():
    print(pyfiglet.figlet_format("DEV BANK",font="starwars"))
    print(colored("__________________________DevBank Always At Your Service_________________________", 'green', 'on_yellow'))
    print('''
    1.OPEN NEW ACCOUNT
    2.DEPOSITE AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSE AN ACCOUNT
    ''')

    choice = input("Enter The Task You Want To Perform  ")
    
    if(choice=='1'):
        OpenAccount()
    elif(choice=='2'):
        DepositeAmount()
    elif(choice=='3'):
        WithdrawAmount()
    elif(choice=='4'):
        BalanceEnquiry()
    elif(choice=='5'):
        DisplayDetails()
    elif(choice=='6'):
        CloseAccount()
    else:
        print("Invalid Choice")
        main()

main()
print()
print("---------------------------------ATM started------------------------------------")
print()
print("                       Plese swipe your card")
print()
trans = ["balance enquiry","withdraw money","change your pin","transfer money","deposit","quit app"]
pin = input("Enter your pin number:-  ")
ob = pin.strip()
print()
if ob == "15122000" or ob == "one five one two two zero zero zero" or ob == "ONE FIVE ONE TWO TWO ZERO ZERO ZERO" or ob == "One Five One Two Two Zero Zero Zero":
    print("    select your transcation")
    print("    1.Balance enquiry")
    print("    2.Withdraw money")
    print("    3.Change Your Pin ")
    print("    4.Transfer Money")
    print("    5.Deposit")
    print("    6.Quit App")
    print()
    choice = input("Enter your transcation:-  ")
    bo = choice.strip()
    print()
    if bo == "balance enquiry" or bo == "1" or bo == "BALANCE ENQUIRY" or bo == "Balance Enquiry" :
        print("Do you want to sleep...?")
        print()
        action = input("Yes or No:-  ")
        no = action.strip()
        print()
        if no == "yes" or no == "YES" or no == "Yes":
            print("your sleep is here and thanks for useing bankword")
        else:
            print("Thanks for useing bankword")
        print()
    elif bo == "withdraw money" or bo == "2" or bo == "Withdraw Money" or bo == "WITHDRAW MONEY":
        amount = input("Enter you withdraw amount:-  ")
        on = amount.strip()
        if (on > "10000"):
            print("plese fill the pan number for sequrity reason")
        else:    
            if on > "0":
                print()
                print("collect your withdraw amount and thanks to useing bankword")
            else:
                print()
                print("Plese enter the valid amount")
    elif bo == "change your pin" or bo == "3" or bo == "CHANGE YOUR PIN" or bo == "Change Your Pin":
        current_pin = input("Enter your current pin:-  ")
        ao = current_pin.strip()
        print()
        if ao == "15122000" or ob == "one five one two two zero zero zero" or ob == "ONE FIVE ONE TWO TWO ZERO ZERO ZERO" or ob == "One Five One Two Two Zero Zero Zero":
            new_pin = input("Now enter your New pin:-  ")
            co = new_pin.strip()
            if new_pin == "15122000" or new_pin == "one five one two two zero zero zero" or new_pin == "One Five One Two Two Zero Zero Zero"   or new_pin == "ONE FIVE ONE TWO TWO ZERO ZERO ZERO":
                print("OOPS ! you can't take this pin so try again later")
                print()
            else:
                print("your pin change Scussesfully and thank to using bank word")
        else:
        
            print("Plese enter your valid current pin")
    elif bo == "transfer money" or bo == "4" or bo == "Transfer Money" or bo == "TRANSFER MONEY":
        trans_amount = input("Enter your transfer amount:-  ")
        do = trans_amount.strip()
        print()
        if do > "0":
            print("congratulations ! your transcation is scussesfully")
        else:
            print("Plese enter your valid amount")
    elif bo == "deposit" or bo == "5" or bo == "Deposit" or bo == "DEPOSIT":
        deposit = input("Enter you deposit amount:-  ")
        b = deposit.strip()
        if b > "50000":
            print("plese fill the pan number for sequrity reason")
        else:    
            if b>"0":
                print("your deposit is scussesfull and thank for useing bankword")
            else:
                print("plese enter the valid deposit amount")
    elif bo == "quit app" or bo == "6" or bo == "QUIT APP" or bo == "Quit App":
        print("Are you shure you want to exit:-  ")
        print()
        read = input("enter your choice:-  ")
        a = read.strip()
        print()
        if a == "yes" or a == "YES" or a == "Yes":
            print("quit app")
        else:
            print("select any transcation") 
else:
    print("   OOPS ! your pin is invalid so try again later")
    





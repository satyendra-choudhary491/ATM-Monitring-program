print("welcome to sbi")
print('''\n       Select the option
                  1.check balance
                  2.pin change
                  3.mini statement
                  4.fund transfer
                  5.cash widthwral
                  ''')
opt = input("\nSelect the option : ")
if opt == "check balance":
    pin=int(input("\nenter your 4 digit pin : "))
    if pin==7742:
        print("\nyour balance is 4005")
    else:
        print("\nyou have enter wrong pin")
elif opt=="pin change":
    pin = int(input("\nEnter your 4 digit pin : "))
    if pin ==5566:
        new_pin=int(input("\nEnter your new pin : "))
        if new_pin==0000:
            print("\nyour new_pin is being procced")
            print("\nyour new_pin is successfully change")
        else:
            print("\ninvalid user input")
    else:
        print("\nyou have entered wrong pin")
elif opt=="mini statement":
    pin = int(input("\n enter you 4 digit pin : "))
    if pin==9828:
        print('''\n your mini statement of account 79**********78 is 
                sr.no        amount        credit/debit          date 
                1             40000           credit             23/07/2022
                2             50000           debit              23/07/2022
                3             70000           credit             23/07/2022
                4             89998           debit              23/07/2022
                ''')
    else:
        print("\n you have entered the wrong pin")
elif opt=="fund transfer":
    pin=int(input("\n enter your 4 digit pin : "))
    if pin==7878:
        print("\n your transtion is being procced")
        print("\n your amount is successfully transfered")
    else:
        print("\n you have entered wrong pin")
elif opt =="cash withdrawal":
    Amount=int(input("\n Enter amount to withdrawal"))
    if Amount>0<4000:
        pin=int(input("\n Enter your four digit pin : "))
        if pin==5555:
            print("\n your transction is being procced please wait")
            print("\n Please collect your cash")
            print("\n your transction is successfully completed")
        else:
            print("\n you have entered wrong pin")
    else:
        print("\n insufficent balance")
else:
    print("\n Please choice correct option")

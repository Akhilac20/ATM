print("INSERT YOUR CARD")
pin="akhila123"
amount=1000
username="akhila"
transaction_history = []
x=str(input("enter username:"))
y=input("enter password:")
if x==username and y==pin:
    while True:
        print("\n***WELCOME TO ATM SERVICES***")
        print("\n1.CHECK BALANCE\n2.CASH WITHDRAWAL\n3.CASH DEPOSIT\n4.CHANGE PIN\n5.TRANSACTION HISTORY\n6.QUIT")
        option=int(input("enter your option:"))
        if option==1:
            print("balance amount is",amount,"rs only")
        elif option==2:
            w_amount=int(input("enter withdrawal amount:"))
            if w_amount<=amount:
                amount=amount-w_amount
                transaction_history.append(f"Withdrawal Rs:{w_amount}")
                print("avaliable balance:",amount)
            else:
                print("enter sufficient amount")
        elif option==3:
            d_amount=int(input("enter deposit amount:"))
            amount=amount+d_amount
            transaction_history.append(f"Deposit Rs:{d_amount}")
            print("avaliable balance:",amount)
        elif option==4:
            n_pin=input("enter new pin:")
            m_pin=input("confrim new pin:")
            if n_pin==m_pin:
                print("***NEW PIN GENERATION IS SUCCESSFULLY COMPLETED***")
            else:
                print("once again check your pin")
        elif option==5:
            if not transaction_history:
                print("no transaction historys")
            else:
                for transaction in transaction_history:
                    print(transaction)
        elif option==6:
            exit()
        else:
            print("enter valid option")
else:
    print("***INCORRECT USER NAME OR PASSWORD***")
    print("-----TRY AGAIN-----")
      
        
    
    




balance=1000
def deposit (amount):
    global balance 
    balance = balance + amount
    return balance 
def withdraw(amount):
    global balance 
    
    if amount<= balance :
        balance = balance - amount 
        return balance 
    else:
        return "❌Insufficient balance"
def check_balance ():
    return balance  
while True:
    print("\n" + "=" * 35)
    print("    🏦  MY   BANKING   SYSTEM ")
    print("="*35)
    print("1. 💰 Deposit")
    print("2. 💸 withdraw")
    print("3. 💳 Check_balance")
    print("4. 🚪  Exit ")
    
    choice = input("Chose an option:")
    if choice == "1" :
        amount  = float(input("Enter deposit amount:"))
        result = deposit(amount)
        print(f"✅New balance: Rs. {result}")
    elif choice == "2":
        amount=float(input("Enter withdraw amount:"))
        result = withdraw (amount)
        print(f"Result:{result}")
    elif choice == "3":
        result = check_balance()    
        print(f"💳 Your balance is: Rs. {result}")
    elif choice == "4":
        print("👋 Thanks for using our bank! ")
        break 
    else:
        print("❌Invalid option! ")
        

    
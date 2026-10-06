

# 🏦 Banking System

A simple **Python beginner project** that simulates a basic banking system using concepts such as **functions, variables, global variables, conditions, loops, user input, type casting, and formatted output**.

## 📌 Project Overview

The **Banking System** allows a user to perform basic banking operations through a simple menu.

The user can:

* 💰 Deposit money
* 💸 Withdraw money
* 💳 Check their balance
* 🚪 Exit the banking system

The program starts with an initial balance of **Rs. 1000**.

The system continues running until the user chooses the **Exit** option.

## 🚀 Features

* 💰 Deposit money

* 💸 Withdraw money

* 💳 Check current balance

* ⚠️ Prevent withdrawal when there is insufficient balance

* 🔄 Menu runs continuously

* 🚪 Exit the banking system

* 🖥️ Simple and clean banking interface

## 🛠️ Python Concepts Used

This project demonstrates:

* Variables — to store the bank balance

* Functions — to organize banking operations

* `global` — to modify the global balance inside functions

* `input()` — to get information from the user

* `float()` — to convert input into decimal numbers

* `if`, `elif`, and `else` — to make decisions

* `while` loop — to keep the banking system running

* `return` — to send results back from functions

* `break` — to exit the program

* f-strings — to display formatted results

## 💻 Code

```python
balance = 1000

def deposit(amount):
    global balance
    balance = balance + amount
    return balance


def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        return balance
    else:
        return "❌ Insufficient balance"


def check_balance():
    return balance


while True:
    print("\n" + "=" * 35)
    print("    🏦  MY BANKING SYSTEM")
    print("=" * 35)

    print("1. 💰 Deposit")
    print("2. 💸 Withdraw")
    print("3. 💳 Check Balance")
    print("4. 🚪 Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        result = deposit(amount)
        print(f"✅ New balance: Rs. {result}")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        result = withdraw(amount)
        print(f"Result: {result}")

    elif choice == "3":
        result = check_balance()
        print(f"💳 Your balance is: Rs. {result}")

    elif choice == "4":
        print("👋 Thanks for using our bank!")
        break

    else:
        print("❌ Invalid option!")
```

## 🔍 How It Works

### 1. Starting Balance

```python
balance = 1000
```

The program starts with:

```text
Rs. 1000
```

The `balance` variable stores the current amount of money.

---

### 2. Deposit Function

```python
def deposit(amount):
    global balance
    balance = balance + amount
    return balance
```

The `deposit()` function adds money to the current balance.

For example:

```text
Current balance: Rs. 1000
Deposit: Rs. 500

New balance: Rs. 1500
```

---

### 3. Withdraw Function

```python
def withdraw(amount):
    global balance

    if amount <= balance:
        balance = balance - amount
        return balance
    else:
        return "❌ Insufficient balance"
```

The `withdraw()` function checks whether the user has enough money.

If the balance is:

```text
Rs. 1000
```

and the user withdraws:

```text
Rs. 300
```

the new balance becomes:

```text
Rs. 700
```

But if the user tries to withdraw:

```text
Rs. 1500
```

the program displays:

```text
❌ Insufficient balance
```

---

### 4. Check Balance Function

```python
def check_balance():
    return balance
```

This function simply returns the current balance.

For example:

```text
💳 Your balance is: Rs. 700
```

---

### 5. Main Menu

The program uses:

```python
while True:
```

to keep showing the banking menu.

The user can select:

```text
1. Deposit
2. Withdraw
3. Check Balance
4. Exit
```

The `if`, `elif`, and `else` statements determine which operation should be performed.

---

### 6. Exit

```python
elif choice == "4":
    print("👋 Thanks for using our bank!")
    break
```

When the user chooses `4`, the `break` statement stops the `while` loop and ends the program.

## 🖥️ Example

```text
===================================
    🏦  MY BANKING SYSTEM
===================================
1. 💰 Deposit
2. 💸 Withdraw
3. 💳 Check Balance
4. 🚪 Exit

Choose an option: 3

💳 Your balance is: Rs. 1000
```

### Deposit Example

```text
Choose an option: 1
Enter deposit amount: 500

✅ New balance: Rs. 1500
```

### Withdraw Example

```text
Choose an option: 2
Enter withdrawal amount: 300

Result: 1200
```

### Insufficient Balance Example

```text
Choose an option: 2
Enter withdrawal amount: 5000

Result: ❌ Insufficient balance
```

### Exit Example

```text
Choose an option: 4

👋 Thanks for using our bank!
```

## 📂 Project Structure

```text
Banking-System/

│
├── banking_system.py
│
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 3. Open the Project Folder

```bash
cd Banking-System
```

### 4. Run the Program

```bash
python banking_system.py
```

## 🎯 Purpose

This project was created as a **Python practice project** to understand how functions, variables, conditions, loops, and user input can be combined to create a simple real-world application.

It provides practice with the basic logic used in banking systems.

## 🚀 Future Improvements

This project can be improved by adding:

* 🔐 PIN/password authentication

* 👤 Multiple user accounts

* 📜 Transaction history

* 💰 Transfer money between accounts

* ⚠️ Input validation

* 💾 Save account data to a file

* 📅 Transaction dates

* 🏦 Account creation system

## 👨‍💻 Author

**Muhammad Rehan**

> Beginner Python Developer | Learning Programming Step by Step

---

⭐ If you find this project useful, feel free to give it a star!

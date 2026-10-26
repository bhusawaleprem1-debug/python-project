# python-project

#Project 1

Python ATM Simulation CLI

A lightweight, console-based Automated Teller Machine (ATM) simulation built with Python. This application mimics real-world ATM functionalities, including secure PIN verification, balance inquiries, deposits, withdrawals, and an end-of-session mini-statement generation.

Features
• Secure Card Authentication:
	• Simulates card verification with a preset 4-digit PIN.
	• Limits login access to a maximum of 3 attempts before temporarily blocking the card.
• Core Banking Services:
	• Check Balance: Instantly view current account funds.
	• Deposit Cash: Add funds to the account with real-time balance updates.
	• Withdraw Cash: Deduct funds securely with built-in overdraft/insufficient funds checks.
• Session Mini-Statement: Tracks all deposits and withdrawals during the active session and prints a clean summary upon card removal.


How It Works 

1. Default Configurations:
	• Default PIN: 1234
	• Starting Balance: $10,000
2. Authentication: The user is prompted to enter their PIN. They have 3 attempts to enter the correct code.
3. Main Menu: Once authenticated, an interactive console menu displays four options (Check Balance, Deposit, Withdraw, Exit).
4. Card Removal: Selecting option 4 breaks the operational loop, prints a chronological list of all transaction histories processed during the session, and safely ends the program.


#Project 2

Student Management System

A simple, interactive command-line Python application to manage student records, calculate grade averages, assign letter grades, and track the top-performing student.

Features

• Initial Report Generation: Automatically processes existing student data on startup to display names, averages, letter grades, and the current topper.
• Dynamic Data Entry: Add new students with a custom 3-subject score list.
• Input Validation: Protects against invalid entries (e.g., handles non-numeric inputs gracefully and restricts marks between 0 and 100).
• Live Leaderboard: Real-time checking to see which student holds the highest total score.
• Grading Scale: Automatically maps calculated averages to classic school grades:
	• A (Average ≥ 85)
	• B (Average ≥ 70)
	• C (Average ≥ 50)
	• F (Average < 50)

How To Use

When you launch the script, it will print an initial report of the pre-loaded students and present an interactive menu:
text
--- Student Management System ---
1. Add Student
2. View all
3. Show topper
4. Exit
Enter Your Query: 
Use code with caution.

Menu Options

• Option 1 (Add Student): Prompts for a new name. If the name is unique, it asks for 3 subject scores sequentially.
• Option 2 (View all): Prints a raw dictionary-style list of all stored student records and their marks.
• Option 3 (Show topper): Scans the database and prints the name and total cumulative score of the highest-achieving student.
• Option 4 (Exit): Safely terminates the script with a goodbye message.



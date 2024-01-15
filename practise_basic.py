# Welcome to Capitec Bank Customer Service System!

# Question 1: Create a variable 'customer_name' and assign your own name to it.

customer_name = input("Hello, who's transacting today? \nEnter your name: ")

# Question 2: Print a welcome message using the 'customer_name' variable.

print("Hello, " + customer_name.capitalize() + "!")

# Question 3: Define a variable 'account_balance' and assign a random float value to it (representing your bank account balance).

account_balance = 2207.89

# Question 4: Print the account balance in a formatted message.

print("Your account balance is: R" + str(account_balance) + ".")

# Question 5: Ask the user to input a withdrawal amount and store it in a variable 'withdrawal_amount'.

withdrawal_amount = 0
withdrawal_amount = float(input("How much are you withdrawing today? \nR"))

while withdrawal_amount > account_balance:
    print(
        customer_name.capitalize() +
        ", you don't have enough in your account. Please choose a lower amount."
    )
    withdrawal_amount = float(input("How much are you withdrawing today? \nR"))

# Question 6: Calculate the remaining balance after the withdrawal and print it.

account_balance = account_balance - withdrawal_amount
print("R" + str(withdrawal_amount) +
      " successfully withdrawn.\nYour account balance is now R" +
      str(account_balance))

# Question 7: Implement a condition to check if the remaining balance is below a certain threshold (you can define the threshold).

if account_balance < 100.00:

    # Question 8: If the balance is below the threshold, print a message warning the user about low balance.

    print("Your balance is less than R100. Please fund your account soon!")

# Question 9: Ask the user to input a deposit amount and store it in a variable 'deposit_amount'.

deposit_amount = float(input("How much are you depositing today?\nR"))

# Question 10: Calculate the new balance after the deposit and print it.

account_balance = account_balance + deposit_amount
print("Your deposit of R" + str(deposit_amount) +
      " was successful.\nYour account balance is now R" +
      str(account_balance) + ".")

# Question 11: Thank the user for using Capitec Bank's services.

# End of Exercise

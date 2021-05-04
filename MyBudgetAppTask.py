#Importing TIME module for delay
import random
import time
from datetime import datetime

now = datetime.now()
dtString = now.strftime ("%d/%m/%y \nTIME: %H:%M:%S %p")
print ("DATE:", dtString)

database = {}

# CREATING A BUDGET CLASS
class Budget:
    def __init__(self, category):
        self.name = category
        self.food_balance = 10000
        self.cloth_balance = 15000
        self.entertainment_balance = 20000


# CREATING METHODS FOR THE BUDGET CLASS

    def budgetOperations(self):
        isValidOptionSelected = False
        print ("**** Welcome to MYFIRST BUDGET APP ****")
        time.sleep(1.2)
        print ("One Account for Managing Your Budgets")
        time.sleep(1.2)
        print ("Reach your goals with personalized insights, custom budgets and spend tracking - All for Free")
        while isValidOptionSelected == False:
            userOnboarding = int (input ("Do you have an account with us? \n 1. YES \n 2. NO \n"))

            if (userOnboarding == 1):
                isValidOptionSelected = True
                self.login()

            elif (userOnboarding == 2):
                isValidOptionSelected = 2
                self.register()

            else:
                print ("Invalid Option Selected")


# USER LOGIN SECTION
    def login(self):
        print ("**** SIGN IN ****")

        login_OTP = input ("Enter Your OTP \n")
        userPassword = input ("Enter Your Password \n")

        for user_OTP, userDetails in database.items():
            if (login_OTP == user_OTP):
                if (userDetails[3] == userPassword):
                    self.budgetCategories()
                    
                else:
                    print ("Incorrect Username or password")
                    self.login()
            else:
                print ("Incorrect Username or password11")
                self.login()


# USER REGISTRATION SECTION
    def register(self):
        print ("**** SIGN UP ****")
        first_name = (input ("What is your First Name \n"))
        last_name = (input ("What is your Last Name \n"))
        email_address = (input("What is your Email Address? \n"))
        userPassword = (input ("Create a Password \n"))
        time.sleep(1.2)
        print ("Please wait, system is processing your details....")
        time.sleep(2.5)
        print ("Welcome %s, You have successfully created your Budget Account!!" % first_name)
        print ("====== ====== ====== ====== ====== ====== ====== \n")
        time.sleep(1.2)
        
        user_OTP = self.generate_user_OTP()
        print ("====== ====== ====== ====== ====== ====== ======")
        print ("Here is your MYFIRST BUDGET APP OTP Number %d" % user_OTP)
        print ("====== ====== ====== ====== ====== ====== ======")
        print ("Make sure you keep it safe as it would be required to Login to your Account \n")

        database[user_OTP] = [first_name, last_name, email_address, userPassword]
        
        time.sleep(1.2)
        self.login()


# USER BUDGET CATEGORY SECTION
    def budgetCategories():
        print ("What would you like to do? \n")
        print ("1. Withdraw")
        print ("2. Deposit")
        print ("3. Transfer")
        print ("4. Check Balance")
        print ("5. Exit")
        
        budget_category_option = int (input ("Please Select an option \n"))
        if (budget_category_option == 1):
            self.withdraw()

        elif (budget_category_option == 2):
            self.deposit()

        elif (budget_category_option == 3):
            self.transfer()

        elif (budget_category_option == 4):
            self.check_balance()

        elif (budget_category_option == 5):
            self.exit()

        else:
            print ("Invalid Option Selected, Please try again")
            self.budgetCategories()


# USER WITHDRAWAL SECTION
    def withdraw(self):
        print ("**** Withdrawal Budget Category ****")
        print ("1. FOOD")
        print ("2. CLOTH")
        print ("3. ENTERTAINMENT")
        print ("4. EXIT")

        selectedWithdrawalOption = int (input ("Please Select a Budget Category \n"))
        if (selectedWithdrawalOption == 1):
            print ("Your FOOD Balance is:", self.food_balance)
            print ("How much would you like to withdraw \n")
            amount = int (input("Enter Amount \n"))
            self.food_balance
            if amount <= self.food_balance:
                print ("Please Wait Your Transaction is Processing......")
                time.sleep(3.5)
                print ("Withdrawal Successful!!") 
                print ("Your New FOOD Balance is:", self.food_balance - amount)

            elif amount > self.food_balance:
                print ("Insufficient Balance, Please Try Again")
                print ("Would you like to deposit? If \n 1. YES \n 2. NO")

                optionSelected = int (input ("Please Select an Option \n"))
                if (optionSelected == 1):
                    self.deposit()
                elif (optionSelected == 2):
                    self.exit()

        elif (selectedWithdrawalOption == 2):
            print ("Your CLOTH Balance is:", self.cloth_balance)
            print ("How much would you like to withdraw \n")
            amount = int (input("Enter Amount \n"))
            self.cloth_balance
            if amount <= self.cloth_balance:
                print ("Please Wait Your Transaction is Processing......")
                time.sleep(3.5)
                print ("Withdrawal Successful!!") 
                print ("Your New CLOTH Balance is:", self.cloth_balance - amount)

            elif amount > self.cloth_balance:
                print ("Insufficient Balance, Please Try Again")
                print ("Would you like to deposit? If \n 1. YES \n 2. NO")
                optionSelected = int (input ("Please Select an Option \n"))
                if (optionSelected == 1):
                    self.deposit()
                elif (optionSelected == 2):
                    self.exit()

        elif (selectedWithdrawalOption == 3):
            print ("Your ENTERTAINMENT Balance is:", self.entertainment_balance)
            print ("How much would you like to withdraw \n")
            amount = int (input("Enter Amount \n"))
            self.entertainment_balance
            if amount <= self.entertainment_balance:
                print ("Please Wait Your Transaction is Processing......")
                time.sleep(3.5)
                print ("Withdrawal Successful!!") 
                print ("Your New CLOTH Balance is:", self.entertainment_balance - amount)

            elif amount > self.entertainment_balance:
                print ("Insufficient Balance, Please Try Again")
                print ("Would you like to deposit? If \n 1. YES \n 2. NO")
                optionSelected = int (input ("Please Select an Option \n"))
                if (optionSelected == 1):
                    self.deposit()
                elif (optionSelected == 2):
                    self.exit()

        elif (selectedWithdrawalOption == 4):
            self.exit()


# USER DEPOSIT SECTION
    def deposit(self):
        print ("**** Deposit Budget Option ****")
        print ("1. FOOD")
        print ("2. CLOTH")
        print ("3. ENTERTAINMENT")
        
        selectedDepositCategory = int (input ("Please Select a Budget Category \n"))
        if (selectedDepositCategory == 1):
            print ("Your FOOD Balance is :", self.food_balance)
            print ("How much would you like to deposit? \n")
            depositAmount = int (input ("Enter Amount \n"))
            self.food_balance
            print ("Please Wait Your Transaction is Processing......")
            time.sleep(3.5)
            print ("Deposit Successful!!") 
            print ("Your New FOOD Balance is: \n", self.food_balance + depositAmount)

            print ("Would You like do something else? If: \n 1. YES \n 2. NO \n")

            alternateOption = int (input ("Select an Option \n"))
            if (alternateOption == 1):
                print ("1. Transfer Funds")
                print ("2. Withdraw")

                optionSelected = int (input ("Please Select an Option \n"))
                if (optionSelected == 1):
                    self.transfer()

                elif (optionSelected == 2):
                    self.withdraw()

                else:
                    print ("Invalid Option Selected")


            elif (alternateOption == 2):
                print ("Please Have a Nice Day!!")
                time.sleep(2.5)
                exit ()

            else:
                print ("Invalid Option Selected12")





    def check_balance(self):
        print ("**** Check Balance Budget Option ****")
        print ("1. FOOD")
        print ("2. CLOTH")
        print ("3. ENTERTAINMENT")
        
        selectedBalanceCategory = int (input ("Please Select a Budget Category \n"))
        if (selectedBalanceCategory == 1):
            print ("Please Wait Your Transaction is Processing......")
            self.food_balance
            time.sleep(3.5)
            print ("Your FOOD Balance is: \n", self.food_balance)

        elif (selectedBalanceCategory == 2):
            print ("Please Wait Your Transaction is Processing......")
            self.food_balance
            time.sleep(3.5)
            print ("Your CLOTH Balance is: \n", self.cloth_balance)

        elif (selectedBalanceCategory == 3):
            print ("Please Wait Your Transaction is Processing......")
            self.entertainment_balance
            time.sleep(3.5)
            print ("Your ENTERTAINMENT Balance is: \n", self.entertainment_balance)

        else:
            print ("Invalid Option Selected")




    def transfer(self):
        
        print ("**** Transfer Budget Option ****")
        print ("1. FOOD")
        print ("2. CLOTH")
        print ("3. ENTERTAINMENT")
        
        selectedTransferCategory = int (input ("Please Select a Budget Category to transfer From: \n"))
        if (selectedTransferCategory == 1):
            self.food_balance
            print ("Your FOOD Balance is:", self.food_balance)
            time.sleep(1.5)
            print ("Which Category would you like to make a transfer to?") 
            print ("1. CLOTH") 
            print ("2. ENTERTAINMENT")
            transferCategoryOption = int (input ("Please Select an Option \n"))
            if (transferCategoryOption == 1):
                print ("How much would you like to transfer?")
                transferAmount = int (input ("Enter Amount \n"))
                if transferAmount <= self.food_balance:
                    self.food_balance -= transferAmount
                    time.sleep(1.5)
                    print ("Please Wait Your Transaction is Processing......\n")
                    time.sleep(1.5)
                    print ("Your Transfer to your CLOTH Budget Category was successful!!")
                    print ("You transferred:", transferAmount)
                    time.sleep(1.5)
                    print ("\n **** DEBIT ALERT NOTIFICATION !!! ****")
                    print ("Your FOOD Balance has just been debited:", transferAmount)
                    print ("Your New FOOD Balance is:", self.food_balance)
                    time.sleep(1.5)
                    print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
                    print ("Your CLOTH Balance has Just been credited with", transferAmount)
                    self.cloth_balance += transferAmount
                    print ("Your New CLOTH Balance is:", self.cloth_balance)

                elif transferAmount > self.food_balance:
                    print ("Insufficient Funds, Please Try Again..")
                    print ("Would you like To Do Something Else? \n")
                    print ("1. YES")
                    print ("2. NO")

                    alternateOption = int (input ("Please Select an  \n"))
                    if (alternateOption == 1):
                        print ("1. Withdraw")
                        print ("2. Deposit")

                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            self.withdraw()

                        elif (altOptionSelect == 2):
                            self.deposit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption  == 2):
                        self.exit()

                    else:
                        print ("Invalid Option Selected")

            elif (transferCategoryOption == 2):
                print ("How much would you like to transfer?")
                transferAmount = int (input ("Enter Amount \n"))
                if transferAmount <= self.food_balance:
                    self.food_balance -= transferAmount
                    time.sleep(1.5)
                    print ("Please Wait Your Transaction is Processing......\n")
                    time.sleep(1.5)
                    print ("Your Transfer to your ENTERTAINMENT Budget Category was successful!!")
                    print ("You transferred:", transferAmount)
                    time.sleep(1.5)
                    print ("\n **** DEBIT ALERT NOTIFICATION !!! ****")
                    print ("Your FOOD Balance has just been debited:", transferAmount)
                    print ("Your New FOOD Balance is:", self.food_balance)
                    time.sleep(1.5)
                    print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
                    print ("Your ENTERTAINMENT Balance has Just been credited with", transferAmount)
                    self.entertainment_balance += transferAmount
                    print ("Your New ENTERTAINMENT Balance is:", self.entertainment_balance)
                
                elif transferAmount > self.food_balance:
                    print ("Insufficient Funds, Please Try Again..")
                    print ("Would you like To Do Something Else? \n")
                    print ("1. YES")
                    print ("2. NO")

                    alternateOption = int (input ("Please Select an  \n"))
                    if (alternateOption == 1):
                        print ("1. Withdraw")
                        print ("2. Deposit")

                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            self.withdraw() 
                        elif (altOptionSelect == 2):
                            self.deposit()

                        elif (altOptionSelect == 2):
                            self.exit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption == 2):
                        self.exit()
                    
                    else:
                            print ("Invalid Option Selected")
            else:
                print ("Invalid option Selected")
        
        elif (selectedTransferCategory == 2):
            self.cloth_balance
            print ("Your CLOTH Balance is:", self.cloth_balance)
            time.sleep(1.5)
            print ("Which Category would you like to make a transfer to?") 
            print ("1. FOOD") 
            print ("2. ENTERTAINMENT")
            transferCategoryOption = int (input ("Please Select an Option \n"))
            if (transferCategoryOption == 1):
                print ("How much would you like to transfer?")
                transferAmount = int (input ("Enter Amount \n"))
                if transferAmount <= self.cloth_balance:
                    self.cloth_balance -= transferAmount
                    time.sleep(1.5)
                    print ("Please Wait Your Transaction is Processing......\n")
                    time.sleep(1.5)
                    print ("Your Transfer to your FOOD Budget Category was successful!!")
                    print ("You transferred:", transferAmount)
                    time.sleep(1.5)
                    print ("\n **** DEBIT ALERT NOTIFICATION !!! ****")
                    print ("Your CLOTH Balance has just been debited:", transferAmount)
                    print ("Your New CLOTH Balance is:", self.cloth_balance)
                    time.sleep(1.5)
                    print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
                    print ("Your FOOD Balance has Just been credited with", transferAmount)
                    self.food_balance += transferAmount
                    print ("Your New FOOD Balance is:", self.food_balance)

                elif transferAmount > self.food_balance:
                    print ("Insufficient Funds, Please Try Again..")
                    print ("Would you like To Do Something Else? \n")
                    print ("1. YES")
                    print ("2. NO")

                    alternateOption = int (input ("Please Select an  \n"))
                    if (alternateOption == 1):
                        print ("1. Withdraw")
                        print ("2. Deposit")

                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            self.withdraw()

                        elif (altOptionSelect == 2):
                            self.deposit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption  == 2):
                        self.exit()

                    else:
                        print ("Invalid Option Selected")

            elif (transferCategoryOption == 2):
                print ("How much would you like to transfer?")
                transferAmount = int (input ("Enter Amount \n"))
                if transferAmount <= self.cloth_balance:
                    self.cloth_balance -= transferAmount
                    time.sleep(1.5)
                    print ("Please Wait Your Transaction is Processing......\n")
                    time.sleep(1.5)
                    print ("Your Transfer to your ENTERTAINMENT Budget Category was successful!!")
                    print ("You transferred:", transferAmount)
                    time.sleep(1.5)
                    print ("\n **** DEBIT ALERT NOTIFICATION !!! ****")
                    print ("Your CLOTH Balance has just been debited:", transferAmount)
                    print ("Your New CLOTH Balance is:", self.cloth_balance)
                    time.sleep(1.5)
                    print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
                    print ("Your ENTERTAINMENT Balance has Just been credited with", transferAmount)
                    self.entertainment_balance += transferAmount
                    print ("Your New ENTERTAINMENT Balance is:", self.entertainment_balance)
                
                elif transferAmount > self.food_balance:
                    print ("Insufficient Funds, Please Try Again..")
                    print ("Would you like To Do Something Else? \n")
                    print ("1. YES")
                    print ("2. NO")

                    alternateOption = int (input ("Please Select an  \n"))
                    if (alternateOption == 1):
                        print ("1. Withdraw")
                        print ("2. Deposit")

                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            self.withdraw() 
                        elif (altOptionSelect == 2):
                            self.deposit()

                        elif (altOptionSelect == 2):
                            self.exit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption == 2):
                        self.exit()
                    
                    else:
                            print ("Invalid Option Selected")


            else:
                print ("Invalid option Selected")


#####################################################################################
        elif (selectedTransferCategory == 3):
            self.entertainment_balance
            print ("Your ENTERTAINMENT Balance is:", self.entertainment_balance)
            time.sleep(1.5)
            print ("Which Category would you like to make a transfer to?") 
            print ("1. FOOD") 
            print ("2. CLOTH")
            transferCategoryOption = int (input ("Please Select an Option \n"))
            if (transferCategoryOption == 1):
                print ("How much would you like to transfer?")
                transferAmount = int (input ("Enter Amount \n"))
                if transferAmount <= self.entertainment_balance:
                    self.entertainment_balance -= transferAmount
                    time.sleep(1.5)
                    print ("Please Wait Your Transaction is Processing......\n")
                    time.sleep(1.5)
                    print ("Your Transfer to your FOOD Budget Category was successful!!")
                    print ("You transferred:", transferAmount)
                    time.sleep(1.5)
                    print ("\n **** DEBIT ALERT NOTIFICATION !!! ****")
                    print ("Your ENTERTAINMENT Balance has just been debited:", transferAmount)
                    print ("Your New ENTERTAINMENT Balance is:", self.entertainment_balance)
                    time.sleep(1.5)
                    print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
                    print ("Your FOOD Balance has Just been credited with", transferAmount)
                    self.food_balance += transferAmount
                    print ("Your New FOOD Balance is:", self.food_balance)

                elif transferAmount > self.entertainment_balance:
                    print ("Insufficient Funds, Please Try Again..")
                    print ("Would you like To Do Something Else? \n")
                    print ("1. YES")
                    print ("2. NO")

                    alternateOption = int (input ("Please Select an  \n"))
                    if (alternateOption == 1):
                        print ("1. Withdraw")
                        print ("2. Deposit")

                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            self.withdraw()

                        elif (altOptionSelect == 2):
                            self.deposit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption  == 2):
                        self.exit()

                    else:
                        print ("Invalid Option Selected")

            elif (transferCategoryOption == 2):
                print ("How much would you like to transfer?")
                transferAmount = int (input ("Enter Amount \n"))
                if transferAmount <= self.entertainment_balance:
                    self.entertainment_balance -= transferAmount
                    time.sleep(1.5)
                    print ("Please Wait Your Transaction is Processing......\n")
                    time.sleep(1.5)
                    print ("Your Transfer to your CLOTH Budget Category was successful!!")
                    print ("You transferred:", transferAmount)
                    time.sleep(1.5)
                    print ("\n **** DEBIT ALERT NOTIFICATION !!! ****")
                    print ("Your ENTERTAINMENT Balance has just been debited:", transferAmount)
                    print ("Your New ENTERTAINMENT Balance is:", self.entertainment_balance)
                    time.sleep(1.5)
                    print ("\n **** CREDIT ALERT NOTIFICATION !!! ****")
                    print ("Your CLOTH Balance has Just been credited with", transferAmount)
                    self.cloth_balance += transferAmount
                    print ("Your New CLOTH Balance is:", self.cloth_balance)
                
                elif transferAmount > self.food_balance:
                    print ("Insufficient Funds, Please Try Again..")
                    print ("Would you like To Do Something Else? \n")
                    print ("1. YES")
                    print ("2. NO")

                    alternateOption = int (input ("Please Select an  \n"))
                    if (alternateOption == 1):
                        print ("1. Withdraw")
                        print ("2. Deposit")

                        altOptionSelect = int (input("Please Select an Option \n"))
                        if (altOptionSelect == 1):
                            self.withdraw() 
                        elif (altOptionSelect == 2):
                            self.deposit()

                        elif (altOptionSelect == 2):
                            self.exit()

                        else:
                            print ("Invalid Option Selected")

                    elif (alternateOption == 2):
                        self.exit()
                    
                    else:
                            print ("Invalid Option Selected")


            else:
                print ("Invalid option Selected")

        


        else:
            print ("Invalid Option Selected")



                

    def exit(self):
        print ("Please Have a Nice Day!!")
        time.sleep(2.5)
        exit

    def generate_user_OTP(self):
        return random.randrange(11111,99999)
        self.user_OTP()
    

category = Budget("Food")
category_1 = Budget("Cloth")
category_2 = Budget("Entertainment")

print (category.budgetOperations())

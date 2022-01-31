#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos
import random

class Account:
    def __init__(self):
        self.account_balance=0
        print(f"Your account balance is {self.account_balance}.")
    """
    This is free rolling section.Role any number between 0 and 9885,you win 40.Role any number between 9886 and 9993,you can win 400.
    Role any number between 9994 and 9997,you can win 4000.Role any number between 9998 and 9999,you can win 40000.Role the number 10000,you
    you can wind up to 80000.
    """
    def free_rolling(self):
        smallest_number=0
        largest_number=10000
        roll_number=random.randint(smallest_number,largest_number)
        if roll_number <= 9885:
            self.account_balance+=40
        elif roll_number <= 9993:
            self.account_balance +=400
        elif roll_number <= 9997:
            self.account_balance +=4000
        elif roll_number <= 9999:
            self.account_balance +=40000
        else:
            self.account_balance +=80000
        print(f"your roll number is {roll_number}.")
        print(f"your updated account balance is {self.account_balance}.")
    """ 
    All you have to decide is to bet high(hi) or low.If you bet on High with your desire amount and roll any number higher than 5000,
    you win as your desire amount.If you belt low with your desire amount and roll any number lower than 5000,you win as your desire
    amount.Otherwise,you lost as your desire amount.
    """
    def multi_rolling(self):
        desire_amount=float(input("Enter desire amount: "))
        desire_belt=input("Enter desire belt(hi or low): ")
        def multi():
            smallest_number=0
            largest_number=10000
            roll_number=random.randint(smallest_number,largest_number)
            return roll_number        
        multi_result=multi()
        desire_belt=desire_belt.title()
        if desire_belt == "Hi":
            print("Roll number is: ",multi_result)
            if multi_result <= 5000:
                print(f"You lost {desire_amount}.")
                self.account_balance-=desire_amount
                print(f"Your account balance is {self.account_balance}.")
            else:
                print(f"You win {desire_amount}.")
                self.account_balance+=desire_amount
                print(f"Your account balance is {self.account_balance}.")
        elif desire_belt == "Low":
            print("Roll number is: ",multi_result)
            if multi_result >= 5001:
                print(f"You lost {desire_amount}.")
                self.account_balance-=desire_amount
                print(f"Your account balance is {self.account_balance}.")
            else:
                print(f"You win {desire_amount}.")
                self.account_balance+=desire_amount
                print(f"Your account balance is {self.account_balance}.")

wintunhlaing=Account()
wintunhlaing.multi_rolling()
kyawkyaw=Account()
kyawkyaw.free_rolling()     




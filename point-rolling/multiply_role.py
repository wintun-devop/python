#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos
import random
accont_balance=8500.88777378
""" 
    All you have to decide is to bet high(hi) or low.If you bet on High with your desire amount and roll any number higher than 5000,
    you win as your desire amount.If you belt low with your desire amount and roll any number lower than 5000,you win as your desire
    amount.Otherwise,you lost as your desire amount.
"""
def multi_rolling(desire_amount,desire_belt):
    def multi():
        smallest_number=0
        largest_number=10000
        roll_number=random.randint(smallest_number,largest_number)
        return roll_number
    global accont_balance
    multi_result=multi()
    desire_belt=desire_belt.title()
    print("crrent balance :",accont_balance)
    if desire_belt == "Hi":
        print("Roll number is: ",multi_result)
        if multi_result <= 5000:
            print(f"You lost {desire_amount}.")
            accont_balance-=desire_amount
            print(f"Your account balance is {accont_balance}.")
        else:
            print(f"You win {desire_amount}.")
            accont_balance+=desire_amount
            print(f"Your account balance is {accont_balance}.")
    elif desire_belt == "Low":
        print("Roll number is: ",multi_result)
        if multi_result >= 5001:
            print(f"You lost {desire_amount}.")
            accont_balance-=desire_amount
            print(f"Your account balance is {accont_balance}.")
        else:
            print(f"You win {desire_amount}.")
            accont_balance+=desire_amount
            print(f"Your account balance is {accont_balance}.")
        
            
def main():
     multi_rolling(float(input("Enter desire amount: ")),(input("Enter desire belt(hi or low) ")))
     
if __name__ == "__main__":
    main()
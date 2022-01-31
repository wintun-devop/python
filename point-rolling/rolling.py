#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA/videos
import random
roll_number = 0
accont_balance=800.00000000
"""
    This is free rolling section.Role any number between 0 and 9885,you win 40.Role any number between 9886 and 9993,you can win 400.
    Role any number between 9994 and 9997,you can win 4000.Role any number between 9998 and 9999,you can win 40000.Role the number 10000,you
    you can wind up to 80000.
"""
def free_rolling():
    smallest_number=0
    largest_number=10000
    roll_number=random.randint(smallest_number,largest_number)
    global accont_balance
    if roll_number <=9885:
        accont_balance +=40
    elif roll_number <= 9993:
        accont_balance +=400
    elif roll_number <= 9997:
        accont_balance +=4000
    elif roll_number <= 9999:
        accont_balance +=40000
    else:
        accont_balance +=80000
    print(f"your roll number is {roll_number}.")
    print(f"your account balance is {accont_balance}.")
    
def main():
    free_rolling()
    
if __name__ == "__main__":
    main()
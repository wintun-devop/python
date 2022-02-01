#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
import time

#define count down function with desire countdown in second
def count_down(count_time):
    while count_time:
        mins,secs=divmod(count_time,60)
        timer="{:02d}:{:02d}".format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        count_time -= 1
    print("Timer completed!")

def main():
    count_down(int(input("Enter the time in seconds: ")))

if __name__ == '__main__':
    main()
         
    
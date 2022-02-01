#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
#we need to install random module and captcha module
import random
from captcha.image import ImageCaptcha

def CaptchaInputCheck():
    #Declare randon character for capture system.
    randon_characters = "abcdefghijkmlnopqrstuvwxyzABCDEFGHIJKMLNOPQRSTUVWHYZ1234567890"
    capture_image=ImageCaptcha()
    capture_char=""
    #Collect randon caracture to use as a capture in lenght of six.
    for char_lenght in range(6):
        capture_char += random.choice(randon_characters)

    print("Your capture data is:",capture_char)
    capture_input=input("Vertify the capture:")
    if (capture_input == capture_char):
        print("Capture is corretc!")
        #define captuer data to and out put as a file  
        capture_data=capture_image.generate(capture_char)
        capture_image.write(capture_char,'capture.png')
    else:
        print("Capture is wrong!")    
            
def main():
    CaptchaInputCheck()
            
if __name__ == '__main__':
    main()
    

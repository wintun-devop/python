#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():
    return 'Hello to the World of Flask!'
    
if __name__ == '__main__':
    app.run()
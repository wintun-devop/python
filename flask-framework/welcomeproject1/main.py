#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
from flask import *
from config import DevConfig

app=Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask Project.</h1>"


if __name__ == '__main__':
    app.run()
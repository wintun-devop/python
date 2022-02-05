#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
from flask import *
app = Flask(__name__)

#routing for index page
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

#routing for css file link
@app.route("/css/main.css")
def styles():
    return send_from_directory("templates", "css/main.css")                        

if __name__ == '__main__':
    app.run()
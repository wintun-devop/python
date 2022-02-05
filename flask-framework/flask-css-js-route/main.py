from flask import *
app = Flask(__name__)

#routing for index page
@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")

#routing for css file link
@app.route("/css/main.css")
def styles():
    return send_from_directory("templates", "css/main.css")  

#routing for javascript file link
@app.route("/js/main.js")
def action():
    return send_from_directory("templates", "js/main.js")

if __name__ == '__main__':
    app.run(debug=True)
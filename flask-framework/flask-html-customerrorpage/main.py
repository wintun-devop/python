from flask import *

#initiate application instance
app = Flask(__name__)

#route decoration
@app.route('/',methods=['GET'])

#route the index page
def index():
    first_name="Win Tun Hlaing"
    #useage of safe on jinja
    fevourate_fruits=['Orange','Banana','Kiwi','Strawberry','Mango','Pear']
    staff="This <strong>bold</strong> text."
    return render_template("index.html",f_name=first_name,
                           f_staff=staff,f_fruits=fevourate_fruits)

#127.0.0.1:5000/user/yourinput
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)


#custom error page(invalid url)
@app.errorhandler(404)
def no_page_found(e):
    return render_template("404.html"),404 
        
#custom error page(Internal Server Error url)
@app.errorhandler(500)
def no_page_found(e):
    return render_template("500.html"),500
    
if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template,flash
from userform import UserForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#initiate application instance(00000001)
app = Flask(__name__)

#Assign secret key(00000006)
app.config['SECRET_KEY']="asd123!@#"

#sqlalchemy mysql connection(00000007)
#app.config['SQLALCHEMY_DATABASE_URI']='mysql+driver://username:password@dbhost/yourdatabasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:efsafaf567@127.0.0.1/flaskapp9'

#initiate database instance (00000008)
db=SQLAlchemy(app)

#crate db mode(00000009)
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(120),nullable=False)
    lastname=db.Column(db.String(120),nullable=False)
    email=db.Column(db.String(200),nullable=False,unique=True)
    #additional migrate to existing database-favorite_color=db.column(db.String(150))
    gender=db.Column(db.String(150),nullable=False)
    date_added=db.Column(db.DateTime,default=datetime.utcnow())
    #create string 
    def __repr__(self):
        return '<Name %r>' % self.name



#index routing page for user input form(00000005)
@app.route('/input',methods=['GET', 'POST'])
def userinput():
    first_name=None
    last_name=None
    user_form=UserForm()
    #validation process here(00000010)
    if user_form.validate_on_submit():
        user=Users.query.filter_by(email=user_form.email.data).first()
        if user is None:
            user=Users(firstname=user_form.firstname.data,lastname=user_form.lastname.data,email=user_form.email.data,
                       gender=user_form.gender.data)
            db.session.add(user)
            db.session.commit()
        first_name=user_form.firstname.data
        last_name=user_form.lastname.data
        user_form.firstname.data=''
        user_form.lastname.data=''
        user_form.email.data=''
        user_form.gender.data=''
        flash("User Added Successfully!")
    our_users=Users.query.order_by(Users.date_added) 
    return render_template("userinput.html",input_firstname=first_name,input_lastname=last_name,
                           disply_users=our_users,input_form=user_form)

#Index page routing(00000003)
@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

#custom error page(00000004)
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404

#(00000002)
if __name__ == '__main__':
    app.run(debug=True)
#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired


#create class for user form
#render_kw={"placeholder": "Enter First Name"} is for place holder
class UserForm(FlaskForm):
    firstname=StringField("First Name:",validators=[DataRequired()],render_kw={"placeholder": "Enter First Name.."})
    lastname=StringField("Last Name:",validators=[DataRequired()],render_kw={"placeholder": "Enter Last Name.."})
    email=StringField("E-mail:",validators=[DataRequired()],render_kw={"placeholder": "Enter E-mail Address.."})
    #Select form SelectField("Field Name",choices=[("Actual Value", "Display Value"), ('female', "Female")])
    gender=SelectField("Gender:",choices=[("male", "Male"), ('female', "Female")])
    submit=SubmitField("Submit")
    
#creat a main function for class
def main():
    a=UserForm()

if __name__ == '__main__':
    main()
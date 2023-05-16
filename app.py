from flask import Flask,render_template, request,flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from weather import main as get_weather

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

class Nameform(FlaskForm):
    cityName = StringField(validators=[DataRequired()])
    stateName = StringField()
    countryName = StringField()
    stateName = StringField()
    countryName = StringField()
    submit = SubmitField("Submit")


@app.route('/', methods=['GET','POST'])
def index():
    cityName = None
    stateName = None
    countryName = None
    submit_data =  None
    form = Nameform()
    #validate
    if form.validate_on_submit():
        cityName = form.cityName.data
        stateName = form.stateName.data
        countryName = form.countryName.data
        submit_data = get_weather(cityName,stateName,countryName)
        if submit_data == "Error":
            flash("invalid Inputs, Please verify and correct the values and try again")  
    return render_template('index.html', 
                           cityName=cityName, 
                           stateName=stateName,
                           countryName=countryName,
                           form = form,
                           submit_data=submit_data)

if __name__ == '__main__':
    app.run(debug=True)
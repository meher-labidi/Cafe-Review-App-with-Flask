from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from cafe_data import CafeManager



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    name = StringField("Cafe Name", validators=[DataRequired()])
    # make sure this is a proper URL
    location = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    time_open = StringField("Opening Time e.g. 8:00 AM", validators=[DataRequired()])
    time_close = StringField("Closing Time e.g. 5:30 PM", validators=[DataRequired()])
    coffee = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                         validators=[DataRequired()])
    wifi = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                       validators=[DataRequired()])
    power = SelectField("Power Socket Availability", choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                        validators=[DataRequired()])
    submit = SubmitField('Submit')


cafe_list = CafeManager()



@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():

    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [form.data[item] for item in form.data][:7]
        cafe_list.add_cafe(new_cafe)
        return redirect("/cafes")

    return render_template('add.html', add_cafe_form=form)


@app.route('/cafes')
def cafes():
    header, entries = cafe_list.get_cafes()
    return render_template('cafes.html',header=header,  cafes=entries)


if __name__ == '__main__':
    app.run(debug=True)

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


class AddSnackForm(FlaskForm):

    name = StringField("Snack Name")
    price = FloatField("Price in USD")


class NewEmployeeForm(FlaskForm):

    name = StringField("Employee Name")
    state = StringField("State")
    dept_code = StringField("Department Code")

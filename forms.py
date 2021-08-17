from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired


class AddSnackForm(FlaskForm):

    name = StringField("Snack Name", validators=InputRequired())
    price = FloatField("Price in USD")
    quantity = IntegerField("How Many?")
    is_healthy = BooleanField("Healthy Snack")

    category = RadioField("Category", choices=[
                          ('ic', 'Ice Cream'), ('chips', 'Potato Chips'), ('candy', 'Candy')])


class NewEmployeeForm(FlaskForm):

    name = StringField("Employee Name")
    state = StringField("State")
    dept_code = SelectField("Department Code")

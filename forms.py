from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import DataRequired, Length


class ConvertForm(FlaskForm):
    """Form for editing users."""

    converting_from = StringField('Converting From', validators=[Length(min=3, max=3)])
    converting_to = StringField('Converting To', validators=[Length(min=3, max=3)])
    amount = DecimalField('Amount', places=2)
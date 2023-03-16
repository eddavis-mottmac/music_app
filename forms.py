from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired, URL, ValidationError, Length
from enums import *
from functools import partial

class ComponentForm(Form):
    name = StringField(
        'name', validators=[Length(min=2, message="Venue name must be at least two characters")]
    )
    datasheet_link = StringField(
        'datasheet_link', validators=[URL()]
    )
    component_type = SelectField(
        # Done implement enum restriction
        'types', validators=[DataRequired(message="You must select one type")],
        choices=[(type.value, type.value) for type in ComponentTypes]
    )







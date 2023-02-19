from datetime import datetime
from flask_wtf import Form, FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired, AnyOf, URL, ValidationError, InputRequired, Length, Regexp
from enums import *
from functools import partial

class ShowForm(Form):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[Length(min=2, message="Venue name must be at least two characters")]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[(state.name, state.name) for state in States]
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # Done implement enum restriction
        'genres', validators=[DataRequired(message="You must select at least one genre")],
        choices=[(genre.value, genre.value) for genre in Genres]
    )

    facebook_link = StringField(
        'facebook_link'
    )
    website_link = StringField(
        'website_link', validators=[DataRequired()]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )
    def validate_phone(form, field):
        state = form.state.data
        phone_number=field.data

        area_codes = getattr(StatesPhoneCodes, state).codes
        if not any(phone_number.startswith(code) for code in area_codes):
            raise ValidationError("Invalid phone number for selected state")







class ArtistForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=[(state.value, state.value) for state in States]
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=[(genre.value, genre.value) for genre in Genres]
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

from .const import SHORT_ID_MAX_LENGTH, SHORT_ID_MIN_LENGTH


class URLForm(FlaskForm):
    original_link = StringField(
        'Paste your original long URL here',
        validators=[DataRequired(message='This field is mandatory!')]
    )
    custom_id = StringField(
        'Propose a short name (if you like)',
        validators=[
            Length(SHORT_ID_MIN_LENGTH, SHORT_ID_MAX_LENGTH),
            Optional()
        ]
    )
    submit = SubmitField('Create')

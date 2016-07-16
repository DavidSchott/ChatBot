from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, RadioField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    room = StringField('Room', validators=[Required()])
    botroom = RadioField(u'Select a ChatBot', choices=[
        ('10', 'Therapist'), ('20', 'Sun Tsu'),
        ('30', 'Crazy Teen'), ('40', "Chad")
    ])
    submit = SubmitField('Enter Chatroom')
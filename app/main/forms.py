from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, RadioField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    room = RadioField(u'Select a ChatBot', choices=[
        ('10', 'Therapist'), ('20', 'Sun Tsu'),
        ('50', 'Ass'), ('30', 'Teen'),
        ('40', "Zen Master"), ('1', 'Bot free :( [Public]')
    ])
    submit = SubmitField('Enter Chatroom')
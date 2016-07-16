from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, RadioField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    room = RadioField(u'Select a ChatBot', choices=[
        ('60', 'Chatty [Statistical, Ongoing]'),
        ('10', 'Therapist [Pattern]'), ('20', 'Sun Tsu [Pattern]'),
        ('50', 'Arrogant [Pattern]'), ('30', 'Teen [Pattern]'),
        ('40', "Philosopher [Pattern]"), ('1', 'None [Public]')
    ])
    submit = SubmitField('Enter Chatroom')
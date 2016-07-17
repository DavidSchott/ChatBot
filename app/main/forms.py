from flask.ext.wtf import Form
from wtforms.fields import StringField, SubmitField, RadioField, SelectField
from wtforms.validators import Required

class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Name', validators=[Required()])
    room = SelectField(u'Select a ChatBot', choices=[
        ('60', 'Chatty [Statistical, Continous]'),
        ('10', 'Therapist [Pattern-matching]'), ('20', 'Sun Tsu [Pattern-matching]'),
        ('50', 'Arrogant [Pattern-matching]'), ('30', 'Teen [Pattern-matching]'),
        ('40', "Philosopher [Pattern-matching]"), ('1', 'None [Public]')
    ])
    submit = SubmitField('Enter Chatroom')
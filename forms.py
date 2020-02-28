from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

# class UserForm(FlaskForm):
#     name = StringField('Name', validators=[InputRequired()])
#     email = StringField('Email', validators=[InputRequired()])

class ReqInfoForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    middle_name = StringField('Middle Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    birth_month = StringField('Birth Month (MM)', validators=[InputRequired()])
    birth_day = StringField('Birth Day (DD)', validators=[InputRequired()])
    birth_year = StringField('Birth Year (YYYY)', validators=[InputRequired()])
    contact_num = StringField('Contact Number', validators=[InputRequired()])
    email_add = StringField('Email', validators=[InputRequired()])
    policy_name = StringField('Policy Name', validators=[])
    account_num = StringField('Account Number',validators=[])
    last_int_month = StringField('Last Interaction Month (MM)', validators=[])
    last_int_year = StringField('Last Interaction Year (YYYY)', validators=[])
    benefits = StringField('Benefits', validators=[])
    last_agent = StringField('Last Agent', validators=[])

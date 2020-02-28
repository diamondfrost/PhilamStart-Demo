from __init__ import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(255))
#     email = db.Column(db.String(255), unique=True)
#
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#     def __repr__(self):
#         return '<User %r>' % self.name

class ReqInfo(db.Model):
    query_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    birth_month = db.Column(db.Integer)
    birth_day = db.Column(db.Integer)
    birth_year = db.Column(db.Integer)
    contact_num = db.Column(db.String(255))
    email_add = db.Column(db.String(255), unique=True)
    policy_name = db.Column(db.String(255))
    account_num = db.Column(db.String(255))
    last_int_month = db.Column(db.Integer)
    last_int_year = db.Column(db.Integer)
    benefits = db.Column(db.String(255))
    last_agent = db.Column(db.String(255))

    def __init__(self, query_id, first_name, middle_name, last_name, birth_month, birth_day, birth_year, contact_num, email_add, policy_name, account_num, last_int_month, last_int_year, benefits, last_agent):
        self.query_id = query_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.birth_year = birth_year
        self.contact_num = contact_num
        self.email_add = email_add
        self.policy_name = policy_name
        self.account_num = account_num
        self.last_int_month = last_int_month
        self.last_int_year = last_int_year
        self.benefits = benefits
        self.last_agent = last_agent

    def __repr__(self):
        return ('<ReqInfo %r>' % self.query_id, '<ReqInfo %r>' % self.first_name, '<ReqInfo %r>' % self.middle_name, '<ReqInfo %r>' % self.last_name, '<ReqInfo %r>' % self.birth_month, '<ReqInfo %r>' % self.birth_day, '<ReqInfo %r>' % self.birth_year, '<ReqInfo %r>' % self.contact_num, '<ReqInfo %r>' % self.email_add, '<ReqInfo %r>' % self.policy_name, '<ReqInfo %r>' % self.account_num, '<ReqInfo %r>' % self.last_int_month, '<ReqInfo %r>' % self.last_int_year, '<ReqInfo %r>' % self.benefits, '<ReqInfo %r>' % self.last_agent)

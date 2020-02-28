"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from __init__ import app, db
from flask import render_template, request, redirect, url_for, flash
from forms import ReqInfoForm #UserForm
from models import ReqInfo
# import sqlite3

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('homepage.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/learn')
def learn():
    return render_template('learn (2).html')

@app.route('/plans')
def plans():
    return render_template('plans.html')

@app.route('/vitality')
def vitality():
    return render_template('vitality.html')

@app.route('/connect')
def connect():
    return render_template('connect.html')

# @app.route('/add-user', methods=['POST', 'GET'])
# def add_user():
#     user_form = UserForm()
#
#     if request.method == 'POST':
#         if user_form.validate_on_submit():
#             # Get validated data from form
#             name = user_form.name.data # You could also have used request.form['name']
#             email = user_form.email.data # You could also have used request.form['email']
#
#             # save user to database
#             user = User(name, email)
#             db.session.add(user)
#             db.session.commit()
#
#             flash('User successfully added')
#             return redirect(url_for('show_users'))
#
#     flash_errors(user_form)
#     return render_template('add_user.html', form=user_form)

@app.route('/add-request', methods=['POST', 'GET'])
def add_req():
    req_info_form = ReqInfoForm()

    if request.method == 'POST':
        if req_info_form.validate_on_submit():
            # Get validated data from form
            first_name = req_info_form.first_name.data
            middle_name = req_info_form.middle_name.data
            last_name = req_info_form.last_name.data
            birth_month = req_info_form.birth_month.data
            birth_day = req_info_form.birth_day.data
            birth_year = req_info_form.birth_year.data
            contact_num = req_info_form.contact_num.data
            email_add = req_info_form.email_add.data
            policy_name = req_info_form.policy_name.data
            account_num = req_info_form.account_num.data
            last_int_month = req_info_form.last_int_month.data
            last_int_year = req_info_form.last_int_year.data
            benefits = req_info_form.benefits.data
            last_agent = req_info_form.last_agent.data

            # save user to database
            req = ReqInfo(first_name, middle_name, last_name, birth_month, birth_day, birth_year, contact_num, email_add, policy_name, account_num, last_int_month, last_int_year, benefits, last_agent)
            db.session.add(req)
            db.session.commit()

            flash('Request successfully added')
            return redirect(url_for('show_req'))

    flash_errors(req_info_form)
    return render_template('add_req.html', form=req_info_form)

@app.route('/requests')
def show_req():
    requests = db.session.query(ReqInfo).all()
    return render_template('show_req.html', requests=requests)

# @app.route('/users')
# def show_users():
#     users = db.session.query(User).all() # or you could have used User.query.all()
#
#     return render_template('show_users.html', users=users)

# Flash errors from the form if validation fails

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))

###
# The functions below should be applicable to all Flask apps.
###

# @app.route('/<file_name>.txt')
# def send_text_file(file_name):
#     """Send your static text file."""
#     file_dot_text = file_name + '.txt'
#     return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")

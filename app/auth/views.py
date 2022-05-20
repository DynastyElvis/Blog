from flask import flash, render_template,request,redirect, url_for
from .import auth 
from ..models import User
from app import db
from flask_login import login_user, login_required,logout_user,current_user

from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password,password):
                flash('logged in successfully',category='success')
                login_user(user)
                return redirect(url_for('main.displayquote'))
                
            else:
                flash('incorrect password,try again!', category='error')
        else:
            flash('email does not exist', category='error')
    return render_template('register.html', user=current_user)

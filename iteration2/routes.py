from flask import Flask, session, render_template, request, redirect, g, url_for
from server import app
import csv
import os
from csv_fun import *
from class_int import system

app.secret_key = os.urandom(24)
@app.route('/', methods=['GET', 'POST'])
def index():
    error123 = None
    if request.method == 'POST':
        session.pop('user', None)
        if request.form['password'] == '123' and request.form['username'] == 'admin': 
                  #set password and username!!!!!!!!!!
            session['user'] = request.form['username']
            return redirect(url_for('login'))
        else:
             error123 = 'Invalid Username or Password. Please try again!'
    return render_template('index.html',error=error123)


@app.route('/loggedin')
def login():
    if g.user:
        return redirect(url_for("admin"))
    return redirect(url_for('index'))

#check the session before actually run any request!!!
@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/logout')
def dropsession():
    session.pop('user', None)
    return 'Log out successful!'

    
    
#################################################

@app.route('/admin')
def admin():
    if request.method == 'POST':
        act = request.form['action']
        sys = system()
        action = sys.get_action(act)
        if action == 'add':
            return redirect(url_for("add_question"))
        elif action == 'survey':
            return redirect(url_for("all_surveys"))
        elif action == 'course':
            return redirect(url_for("all_courses"))
        elif action == 'creatSurvey':
            return redirect(url_for("creatSurvey"))
        elif action == 'logout':
            return redirect(url_for("index"))
    return render_template("admin.html")


@app.route("/All_courses",methods=["GET","POST"])
def all_courses():
   courses = print_from_csv("courses.csv")
   return render_template("all_courses.html",courses=courses)


@app.route("/addQuestion",method = ["GET","POST"])
def add_question():
    






    

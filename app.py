import os, random
from flask import Flask, redirect, render_template, request, session, url_for
from random import shuffle


app = Flask(__name__)
app.secret_key = os.urandom(24)

questions = {
    1: {"question": "What is 2 + 2?", "answer": "4"},
    2: {"question": "What is 3 + 3?", "answer": "6"},
    3: {"question": "What colour is the sky?", "answer": "Blue"}
    }
    


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('data/users.txt', 'a') as file:
            file.writelines(request.form['username'] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')

@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    session["correct_answer_count"] = 0
    session["current_question"] = 1
    
    
    if request.method == "POST":
        selected_answer = str(request.form['user_answer'])
        if selected_answer == questions[session["current_question"]]["answer"]:
            session["correct_answer_count"] += 1
            session["current_question"] += 1
        redirect(username)
    
       
           
    return render_template('quiz.html',
    username=username, 
    question_number=session["current_question"], 
    question=questions[session["current_question"]]['question'],
    )

        
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)         




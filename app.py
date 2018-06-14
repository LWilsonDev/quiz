import os, random
from flask import Flask, redirect, render_template, request, session, url_for
from random import shuffle


app = Flask(__name__)
app.secret_key = os.urandom(24)

questions = {
    1: {"question": "What is 2 + 2?", "answer": "4"},
    2: {"question": "What is 3 + 3?", "answer": "6"},
    3: {"question": "What colour is the sky?", "answer": "blue"},
    4: {"question": "What colour is grass?", "answer": "green"}
    }
  
def check_answer(answer):
    if answer == questions[session["current_question"]]["answer"]:
        session["correct_answer_count"] += 1

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('data/users.txt', 'a') as file:
            file.writelines(request.form['username'] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')

@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    if "current_question" not in session:
        session["current_question"] = 1
        session["correct_answer_count"] = 0
    
    if request.method == "POST":
        selected_answer = str(request.form['user_answer']).lower()
        check_answer(selected_answer)
        session["current_question"] += 1
        redirect(username)
    
    if session["current_question"] > len(questions):
        if session['correct_answer_count'] < len(questions)/2:
            low_score = True
        return render_template("leaderboard.html",
        username=username,
        low_score=low_score,
        total_questions=len(questions),
        user_score=session['correct_answer_count'])   
           
    return render_template('quiz.html',
    username=username, 
    question_number=session["current_question"], 
    question=questions[session["current_question"]]['question'],
    )

        
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)         




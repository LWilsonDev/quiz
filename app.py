import os, random
from flask import Flask, redirect, render_template, request, session, url_for
from random import shuffle


app = Flask(__name__)
app.secret_key = os.urandom(24)

questions = {
    1: {"question": "What is 2 + 2?", "answer": "4"},
    2: {"question": "What is 3 + 3?", "answer": "6"},
    3: {"question": "What colour is grass?", "answer": "green"}
    }
  
def check_answer(answer):
    if answer == questions[session["current_question"]]["answer"]:
        session["correct_answer_count"] += 1
        


@app.route('/', methods=['GET', 'POST'])
def index():
    #remove session in case same user is returning
    for key in session.keys():
     session.pop(key)
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if "current_question" not in session:
        session["current_question"] = 1
        session["correct_answer_count"] = 0
    
    if request.method == "POST":
        selected_answer = str(request.form['user_answer']).lower()
        check_answer(selected_answer)
        session["current_question"] += 1
        redirect(url_for('quiz'))
    
    if session["current_question"] > len(questions): 
        #finished quiz
        return redirect(url_for('result'))
        
           
    return render_template('quiz.html',
    username=session['username'], 
    question_number=session["current_question"], 
    question=questions[session["current_question"]]['question'],
    )
    
@app.route('/result', methods=['GET', 'POST']) 
def result():
    if request.method == "POST":
        if request.form['result_btn'] == 'again':
            session['current_question'] = 1
            session['correct_answer_count'] = 0
            return redirect(url_for('quiz'))
        elif request.form['result_btn'] == 'exit':
            return redirect(url_for('index'))
    else:    
        if session['correct_answer_count'] < len(questions)/2:
            low_score = True
        else:
            low_score = False
        return render_template("result.html",
        username=session['username'],
        low_score=low_score,
        total_questions=len(questions),
        user_score=session['correct_answer_count'])   
        
         

        
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)         




import os, random, copy
from flask import Flask, redirect, render_template, request, session
from questions import Questions
from random import shuffle


app = Flask(__name__)
app.secret_key = os.urandom(24)

original_question_list = {
    # format is 'question': [correct_answer, answer2, answer3]
    "What is 2 + 2?": ['4', '6', 'yellow'],
    "What colour is grass?": ['green', '6', 'yellow'],
    "What colour is the sky?": ['Blue', '6', 'yellow']
    }

questions = copy.deepcopy(original_question_list) 
#make copy of questions to shuffle, leaving original list untouched



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('data/users.txt', 'a') as file:
            file.writelines(request.form['username'] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')

@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    
        
    #if "current_question" not in session:
    # The first time the page is loaded, the current question is not set.
    # This means that the user has not started to quiz yet. So set the 
    # current question to question 1 and save it in the session.
    if "current_question" not in session:
    # The first time the page is loaded, the current question is not set.
    # This means that the user has not started to quiz yet. So set the 
    # current question to question 1 and save it in the session.
        
        session["current_question"] = 2    
    return render_template('quiz.html',
    username=username, 
    question_number=session["current_question"], 
    question=questions.keys()[session["current_question"]],
    answers=questions.values()[session["current_question"]],
    )

    #current_question_answers=questions.values()[session["current_question"]],
        
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)         




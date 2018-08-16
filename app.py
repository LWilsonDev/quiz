import os, random, json
from questions import questions
from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

def save_to_leaderboard(filename, data):
    with open(filename, 'a') as file:
        file.writelines(data)

def check_answer(answer):
    if answer == questions[session["current_question"]]["answer"]:
        session["correct_answer_count"] += 1
        session["guess_num"] = 2
        flash(answer.capitalize() + " is correct!")
    elif session["guess_num"] == 2:
        flash("Incorrect! You have one more guess")
        session["guess_num"] -= 1
    elif session["guess_num"] == 1:
        flash("Incorrect! The correct answer was: " + questions[session["current_question"]]["answer"].capitalize())
        session["guess_num"] -= 1
    else:    
        flash("You are out of guesses!")
            
@app.route('/', methods=['GET', 'POST'])
def index():
    #remove session incase same user is returning
    for key in session.keys():
        session.pop(key)
    if request.method == 'POST':
        session['username'] = request.form['username'].capitalize()
        return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if "current_question" not in session:
    #start of game - set up first question
        session["current_question"] = 1
        session["correct_answer_count"] = 0
        session["guess_num"] = 2
    if request.method == "POST":
        if request.form['submit_btn'] == 'submit':
            selected_answer = str(request.form['user_answer']).lower()
            check_answer(selected_answer)
        if request.form['submit_btn'] == 'next':
            session["current_question"] += 1
            session["guess_num"] = 2
            return redirect(url_for('quiz'))
        #if user clicks next then session current question +1 and redirect for quiz    
    if session["current_question"] > len(questions): 
        #finished quiz
        #save score to leaderboard
        save_to_leaderboard('data/leaderboard.txt', 
          '{0}: {1}\n'.format(session['username'], session['correct_answer_count']))
        return redirect(url_for('result'))
    return render_template('quiz.html',
    question_number=session["current_question"], 
    question=questions[session["current_question"]]['question'],
    image=questions[session["current_question"]]['image'],
    guess_count=session['guess_num']
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
        elif request.form['result_btn'] == 'leaderboard':
            return redirect(url_for('leaderboard'))    
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
        
@app.route('/leaderboard', methods=['GET'])    
def leaderboard():
    with open('data/leaderboard.txt', 'r') as f:
        data=f.readlines()
        score_list=[]
    for line in data:
        score_list.append(line)
        sorted_data = sorted(score_list, key=lambda item: int(item.rsplit(': ')[-1].strip()), reverse=True)
    return render_template('leaderboard.html',
    sorted_data=sorted_data)

#sort json data https://stackoverflow.com/questions/26924812/python-sort-list-of-json-by-value
#https://stackoverflow.com/questions/32631581/python-how-do-i-sort-integers-in-a-text-file-into-ascending-and-or-descending-o
        
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)         



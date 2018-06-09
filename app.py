import os
from flask import Flask, redirect, render_template, request
from questions import Questions


app = Flask(__name__)

question_list = [
    "What is 2 + 2?",
    "What colour is grass?",
    "What colour is the sky?"
    ]
    
answer_list = [
    ["4", "2", "apple"], 
    ["6", "4", "green"], 
    ["blue", "one", "yellow"]
    ]    

questions_and_answer = [
    Questions(question_list[0], answer_list[0][0]),
    Questions(question_list[1], answer_list[1][2]),
    Questions(question_list[2], answer_list[2][0]),
    ]

def ask_question(index):
    return question_list[index]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        with open('data/users.txt', 'a') as file:
            file.writelines(request.form['username'] + '\n')
        return redirect(request.form['username'])
    return render_template('index.html')

@app.route('/<username>', methods=['GET', 'POST'])
def user(username):
    return render_template('quiz.html',
    username=username)

    
        
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)         




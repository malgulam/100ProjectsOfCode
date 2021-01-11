#!/usr/bin/python3

#app.py - Main flask runner app

#questions for this quiz are provided by https://quizapi.io/.

#Prerequisites:
#1.)You will need to signup at https://quizapi.io/register
#2.)Copy your api key and paste it in place of your_api_key

#curl https://quizapi.io/api/v1/questions -G \
#-d apiKey=YOUR_API_KEY \
#-d limit=10 #where limit is the number of questions



#imports
from flask import Flask, render_template, redirect
import helpers
app = Flask(__name__)

#global counts variable
global score
score = 0
#function to keep count
def count_keeper(choosen_answer, correct_answer):
    if choosen_answer == correct_answer:
        score += 1
    else:
        pass



#app routes
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/start_quiz', methods=['GET', 'POST'])
def start_quiz():
    questions_answers_dict = helpers.load_questions()
    return render_template('quiz.html', questions_answers_dict = questions_answers_dict)
if __name__ == '__main__':
    app.run()
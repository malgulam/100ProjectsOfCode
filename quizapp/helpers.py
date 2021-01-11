import json

def load_questions():
    questions_answers_dict = {}
    lines = None
    try:
        with open('quizoutput.txt', 'r') as f:
            lines = f.readlines()
    except:
        print('quizoutput.txt does not exists.Run python3 createquiz.py then run python3 jsonify_quiz_output.pu then python3 app.py')
    # print (lines)
    json_ouput = json.loads(lines[0])
    number_of_questions = 0
    for item in json_ouput:
        if 'question' in item.keys():
            number_of_questions += 1
        else:
            pass
    print(f'Number of questions is:{number_of_questions}')
    for i in range(number_of_questions):
        i +=1
        questions_answers_dict[f'question_{i}'] = {}
        for item in json_ouput:
            if 'question' in item.keys():
                questions_answers_dict[f'question_{i}']['question'] = item['question']
            if 'answers' in item.keys():
                questions_answers_dict[f'question_{i}']['answers'] = item['answers']
            if 'correct_answers' in item.keys():
                for value in item['correct_answers'].keys():
                    if item['correct_answers'][value] == 'true':
                        # print('correct_answer_is: ', value[:8])
                        questions_answers_dict[f'question_{i}']['correct_answer'] = value[:8]
            else:
                print(item)
    # print(questions_answers_dict)
    return questions_answers_dict

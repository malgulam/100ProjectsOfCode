import json

#start
print('start')
with open('quizoutput.txt') as f:
    lines = f.readlines()
    print('loaded quiz data')

print('changing to json')
json_output = json.loads(lines[0])
print(json_output)

with open('quizoutput.txt', 'w') as f:
    f.write(json_output)
# for item in json_output:
#     print(item['question'])
#     print('done')

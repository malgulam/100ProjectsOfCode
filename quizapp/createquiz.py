import subprocess

print("start")
subprocess.call("./createquiz.sh", shell=True)
print("done creating quiz")
print("quiz output can be found in quizoutput.txt")



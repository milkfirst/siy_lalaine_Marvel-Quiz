from components.quizQuestions import questions
from components import vars, quizTally

answer1 = vars.questions["q1"][input(questions["q1"]["questions"])]
print(answer1)

vars.quizTotal += answer1
print("+++++++++++++++++++++++\n")

answer2 = vars.questions["q2"][input(questions["q1"]["questions"])]
print(answer2)

vars.quizTotal += answer2
print("+++++++++++++++++++++++\n")

print("total so far: " + str(vars.quizTotal) + "\n")

# after answering all the questions, figure out who your character is

quizTally.total(vars.quizTotal)
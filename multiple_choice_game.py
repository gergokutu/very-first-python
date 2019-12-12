# classes, if statements, loops...
from Question import Question

question_prompts = [
    "\nWhat color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "\nWhat color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "\nWhat color are strawberries?\n(a) Black\n(b) Red\n(c) Brown\n\n",
]

# Create an array of questions
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

# run a function to ask the test
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            # identation means a lot in python >> try it with the next line
            # print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
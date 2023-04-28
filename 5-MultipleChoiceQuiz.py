from Questions import Question

questionPrompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strwaberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b")
]

def run_test(questionsList):
    score = 0
    for question in questionsList:
        userAnswer = input(question.prompt)              
        if userAnswer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
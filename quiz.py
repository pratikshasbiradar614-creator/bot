fruits = ["apple","banana", "cherry"]
print(fruits)
print(fruits[0])
print(fruits[1])
fruits.append("orange")
print(fruits)
print("Number of fruits:", len(fruits))

questions = ["what is 2+2?", "what is the capital of France?"]
for q in questions:
    answer = input(q + " ")
    print("You answered:", answer)
capital = {"France": "Paris","japan":"Tokyo"}
print(capital["France"])
print(capital["japan"])
q1 ={"question":"what is 2+2?","answer":"4"}
print(q1["question"])
print("The answer is:", q1["answer"])
questions = [
    {"question": "what is 2+2?", "answer": "4"},
    {"question": "what is the capital of France?", "answer": "Paris"},
    {"question": "how many days are in a week?", "answer": "7"}
]
print("first question:", questions[0]["question"])
print("Its answer is:", questions[0]["answer"])
for item in questions:
    user_answer = input(item["question"] + " ")
    if user_answer.lower() == item["answer"].lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", item["answer"])
score = 0
for item in questions:
    user_answer = input(item["question"] + " ")
    if user_answer.lower() == item["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", item["answer"])
print("Your total score is:", score, "out of", len(questions))
if score == len(questions):
    print("Excellent! You got all questions right!")
elif score >= len(questions)/2:
    print("Good job")
else:
    print("Keep practising - you will get there!")
    user_answer = input(item["question"]+" ")
    user_answer = user_answer.lower().strip()
    if user_answer == item["answer"].lower():
        print("Correct!")
file = open("scores.txt","w")
file.write("sam scored 3\n")
file.close()
print("saved!")
file = open("scores.txt","a")
file.write("A new score line\n")
file.close()
player = input("What is your name?")
file = open("scores.txt","a")
file.write(player+"scored"+str(score)+"\n")
file.close()
print("Your score was saved!")
quiz_bank ={
    "Maths":[
        {"question":"2+2?","answer":"4"},
        {"question":"10-3?","answer":"7"}
    ],
    "Geography":[
        {"question":"capital of japan ?","answer":"Tokyo"}
    ]
}
print("Categories available:")
for name in quiz_bank:
    print("-",name)
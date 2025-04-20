print()
print("                                Welcome To My Quiz Game")
print("                        --------------------------------------")
print()

Question_data=[
    {"text":"What is our Prime Minister Name:","answer":"B"},
    {"text":"What is our national animal:","answer":"c"},
    {"text":"How many bones are available in a human body:","answer":"A"},
    {"text":"Who is the CEO of Google:","answer":"D"},
    {"text":"Who is the Founder of Microsoft:","answer":"A"}
]

optitions=[
    ["A. Amit Saha","B. Narendra Modi", "C. Rahul Gandhi", "D.Joy Saha"],
    ["A. Elephent","B. Tiger", "C. Lion", "D.Horse"],
    ["A. 206","B. 207", "C. 205", "D.208"],
    ["A. Tim Cook","B. Larry Fink", "C. Bill Gates", "D.Sundar Pitchai"],
    ["A. Bill Gates","B. Sundar Pitchai", "C. James Root", "D.Lee byung"],
]


score=0
def check_answer(user_guess,correct_answer):
    
    if user_guess==correct_answer:
        return True
    else:
        return False
    
for question_num in range (len(Question_data)):
    print()
    print(Question_data[question_num]['text'])

    for i in optitions [question_num]:
        print(i)
    

    guess=input("Enter Your Guess(A/B/C/D):").upper()
    is_corrrect = check_answer(guess,Question_data[question_num]["answer"])

    if is_corrrect:
        print("Correct Answer")
        score+=1
    else:
        print("Icorrect Answer")
        print(f"The Correct Answer is {Question_data[question_num]['answer']}")
    print(f"Your Current Score Is {score}/{question_num+1}")
    print()

print(f"You have given {score} correct answers")
print()

print(f"Your Final Score is {(score/len(Question_data))*100}%")
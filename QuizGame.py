#The aim of this assignment is to create a quiz game that asks questions and checks answers.
#Task 1: Develop a list of questions and answers.
user_questions= [
    
    "1. What is 9 + 5",
    "2. What is 9 * 5",
    "3. What is 9 - 5",
    "4. 9 is > than 5 (true/false) "
    
]

answers=[14, 40, 4, True]
answers_type=[int, int, int, bool]

score=0
#Task 2: Write a function that quizzes the user and takes their answers.
for i in range (len(user_questions)):
    user_answer=input(user_questions[i] + " ")
    try:
        if answers_type[i]==bool:
            converted_answer=user_answer.lower in ["true", "t", "1", "yes", "y"]
        else:
            converted_answer=answers_type[i](user_answer)
    #  ask 3: Score the quiz and give the user feedback on their performance.
      
            if converted_answer== answers[i]:
                print(" Correct!")
                score+=1
            else:
                print( "Wrong Answer....")
    except ValueError:
        print("The input type entered is invalid.")
    print(f" Your final score is {score}/ {len(user_questions)}.")    
                
            
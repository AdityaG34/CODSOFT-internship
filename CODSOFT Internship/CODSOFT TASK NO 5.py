#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

# Sample quiz questions (you can replace this with your own questions)
quiz_data = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Madrid'],
        'correct_answer': 'Paris',
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_answer': 'Mars',
    },
    {
        'question': 'What is 7 x 8?',
        'options': ['56', '64', '42', '72'],
        'correct_answer': '56',
    },
]

# Function to present a question and evaluate the answer
def ask_question(question_data):
    question = question_data['question']
    options = question_data['options']
    correct_answer = question_data['correct_answer']

    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    user_answer = input("Enter the number of your answer: ")
    if user_answer.isdigit():
        user_answer = int(user_answer)
        if 1 <= user_answer <= len(options):
            user_answer = options[user_answer - 1]
        else:
            user_answer = ""
    
    if user_answer.lower() == correct_answer.lower():
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}\n")
        return 0

# Function to play the quiz
def play_quiz(quiz_data):
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of multiple-choice questions.")
    print("Please type the number of your answer.\n")

    score = 0
    for question_data in quiz_data:
        score += ask_question(question_data)

    print(f"Your Score: {score}/{len(quiz_data)}")
    if score == len(quiz_data):
        print("Excellent! You got all the answers correct.")
    elif score >= len(quiz_data) / 2:
        print("Good job!")
    else:
        print("You can do better. Keep practicing!")

# Main function
def main():
    play_quiz(quiz_data)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





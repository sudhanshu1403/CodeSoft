import random

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def welcome(self):
        print("Welcome to the Quiz Game!")
        print("Answer multiple-choice or fill-in-the-blank questions on the chosen topic.")
        print("Let's get started!\n")

    def present_question(self, question):
        print(question["question"])
        for index, choice in enumerate(question["choices"], start=1):
            print(f"{index}. {choice}")
        user_answer = input("Your answer: ")
        return user_answer

    def evaluate_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!\n")
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    def run(self):
        self.welcome()
        random.shuffle(self.questions)
        
        for question in self.questions:
            user_answer = self.present_question(question)
            self.evaluate_answer(user_answer, question["correct_answer"])
        
        print("Quiz completed!")
        print(f"Your score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Congratulations! You got all questions correct.")
        else:
            print("Keep practicing and try again!")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            self.score = 0
            self.run()
        else:
            print("Thank you for playing!")

# Define quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Madrid", "Paris", "Berlin"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    # Add more questions here
]

# Create a QuizGame instance and start the game
quiz = QuizGame(quiz_questions)
quiz.run()

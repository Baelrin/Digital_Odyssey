class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def ask_question(self, question, correct_answer):
        user_answer = input(question).lower().strip()
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")

    def play(self):
        print("Welcome to my computer quiz!")
        playing = input("Do you want to play? ").lower()
        if playing != "yes":
            quit()
        print("Okay! Let's play :)")
        for question, answer in self.questions.items():
            self.ask_question(question, answer)
        print(f"You got {self.score} questions correct!")
        print(f"You got {str(self.score / len(self.questions) * 100)}%.")


if __name__ == "__main__":
    questions = {
        "What does CPU stand for? ": "central processing unit",
        "What does GPU stand for? ": "graphics processing unit",
        "What does RAM stand for? ": "random access memory",
        "What does PSU stand for? ": "power supply",
    }
    game = QuizGame(questions)
    game.play()

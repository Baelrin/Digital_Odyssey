def ask_question(question, correct_answer):
    user_answer = input(question).lower().strip()
    if user_answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0


def main():
    print("Welcome to my computer quiz!")
    playing = input("Do you want to play? ").lower()
    if playing != "yes":
        quit()
    print("Okay! Let's play :)")
    questions = {
        "What does CPU stand for? ": "central processing unit",
        "What does GPU stand for? ": "graphics processing unit",
        "What does RAM stand for? ": "random access memory",
        "What does PSU stand for? ": "power supply",
    }
    score = sum(
        ask_question(question, answer) for question, answer in questions.items()
    )
    print(f"You got {score} questions correct!")
    print(f"You got {str(score / len(questions) * 100)}%.")


if __name__ == "__main__":
    main()

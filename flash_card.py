# Flash Card Quiz

# Dictionary containing questions and answers
flashcards = {
    "What is the capital of India?": "Delhi",
    "What is 5 + 7?": "12",
    "Who developed Python?": "Guido van Rossum",
    "What is the largest planet?": "Jupiter",
    "What is the chemical symbol of water?": "H2O"
}

score = 0

print("===== Flash Card Quiz =====\n")

# Loop through each flashcard
for question, answer in flashcards.items():
    print("Question:", question)
    user_answer = input("Your Answer: ")

    if user_answer.lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", answer, "\n")

print("==========================")
print("Your Score:", score, "/", len(flashcards))
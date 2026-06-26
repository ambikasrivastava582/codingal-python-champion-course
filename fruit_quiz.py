# Fruit Quiz

fruits = {
    "Which fruit is known as the King of Fruits?": "Mango",
    "Which fruit is yellow and curved?": "Banana",
    "Which fruit keeps the doctor away if eaten daily?": "Apple",
    "Which fruit is small, purple, and grows in bunches?": "Grapes",
    "Which fruit is orange in color and rich in Vitamin C?": "Orange"
}

score = 0

print("🍎 Welcome to the Fruit Quiz! 🍌\n")

for question, answer in fruits.items():
    print(question)
    user_answer = input("Your Answer: ")

    if user_answer.lower() == answer.lower():
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect!")
        print("Correct Answer:", answer, "\n")

print("===== Quiz Completed =====")
print("Your Score:", score, "/", len(fruits))

if score == len(fruits):
    print("🎉 Excellent! You got all answers correct.")
elif score >= 3:
    print("👍 Good Job!")
else:
    print("😊 Keep practicing!")
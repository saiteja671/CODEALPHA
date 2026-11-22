import random
words = ["apple", "java", "python", "django", "flask"]
word = random.choice(words)

guessed_letters = []
attempts = 6
print(f"You have {attempts} attempts to guess the word.")

while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord :", display.strip())
    print("Attempts left :", attempts)

    if all(letter in guessed_letters for letter in word):
        print("You won!")
        break

    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts -= 1

if attempts == 0:
    print("\nGame Over")
    print("The correct word was:", word)
import random

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock\n")

user_score = 0
computer_score = 0

while True:
    print("Choose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    options = ["rock", "paper", "scissors"]
    if user_choice not in options:
        print("❌ Invalid choice! Please try again.\n")
        continue

    computer_choice = random.choice(options)
    print("🤖 Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("😐 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ You lose this round!")
        computer_score += 1

    print("📊 Score ➤ You:", user_score, "| Computer:", computer_score)

    play_again = input("🔁 Do you want to play another round? (yes/no): ").lower()
    if play_again != "yes":
        print("\n🎉 Final Score ➤ You:", user_score, "| Computer:", computer_score)
        if user_score > computer_score:
            print("🏆 Congratulations, you won the game!")
        elif user_score < computer_score:
            print("😢 Sorry, the computer won!")
        else:
            print("😎 It's a draw overall!")
        print("Thanks for playing!")
        break
    print()

#Output Display:
# 🎮 Welcome to Rock-Paper-Scissors Game!
# Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock

# Choose one: rock, paper, or scissors
# Your choice: rock
# 🤖 Computer chose: scissors
# ✅ You win this round!
# 📊 Score ➤ You: 1 | Computer: 0
# 🔁 Do you want to play another round? (yes/no): yes

# Choose one: rock, paper, or scissors
# Your choice: rock
# 🤖 Computer chose: paper
# ❌ You lose this round!
# 📊 Score ➤ You: 1 | Computer: 1
# 🔁 Do you want to play another round? (yes/no): yes

# Choose one: rock, paper, or scissors
# Your choice: paper
# 🤖 Computer chose: scissors
# ❌ You lose this round!
# 📊 Score ➤ You: 1 | Computer: 2
# 🔁 Do you want to play another round? (yes/no): yes

# Choose one: rock, paper, or scissors
# Your choice: rock
# 🤖 Computer chose: paper
# ❌ You lose this round!
# 📊 Score ➤ You: 1 | Computer: 3
# 🔁 Do you want to play another round? (yes/no): yes

# Choose one: rock, paper, or scissors
# Your choice: scissors
# 🤖 Computer chose: paper
# ✅ You win this round!
# 📊 Score ➤ You: 2 | Computer: 3
# 🔁 Do you want to play another round? (yes/no): yes

# Choose one: rock, paper, or scissors
# Your choice: rock
# 🤖 Computer chose: paper
# ❌ You lose this round!
# 📊 Score ➤ You: 2 | Computer: 4
# 🔁 Do you want to play another round? (yes/no): no

# 🎉 Final Score ➤ You: 2 | Computer: 4
# 😢 Sorry, the computer won!
# Thanks for playing!
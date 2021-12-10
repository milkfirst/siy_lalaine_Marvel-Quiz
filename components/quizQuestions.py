from components.quizTally import tally

print("WELCOME TO MY LITTLE GUESSING GAME!")
print("Pick a character: Hulk, Spiderman, Gamora or Black Widow")
print("Let me guess who you're thinking about")

ans = input("is your character male or female? (y for male / n for female): ")
tally(ans, "male")

ans = input("is your character from Earth? (y/n): ")
tally(ans, "earth")

ans = input("does your wear a mask? (y/n): ")
tally(ans, "mask")

ans = input("is your character human? (m/f): ")
tally(ans, "human")
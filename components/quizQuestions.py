from components.quizTally import tally

print("U+1F911"+"WELCOME TO MY LITTLE GUESSING GAME!"+"U+1F911")
print("Pick a character: Hulk, Spiderman, Gamora or Black Widow")
print("Let me guess who you're thinking about!"+"U+1F92B")

ans = input("is your character male or female? (y for male / n for female): ")
tally(ans, "male")

ans = input("is your character from Earth? (y/n): ")
tally(ans, "earth")

ans = input("does your wear a mask? (y/n): ")
tally(ans, "mask")

ans = input("is your character human? (m/f): ")
tally(ans, "human")
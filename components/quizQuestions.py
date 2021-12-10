from components.quizTally import tally

ans = input("is your character male or female? (m/f) ")
tally(ans, "male")

ans = input("is your character from Earth? (y/n) ")
tally(ans, "earth")

ans = input("does your wear a mask? (y/n) ")
tally(ans, "mask")

ans = input("is your character human? (m/f) ")
tally(ans, "human")
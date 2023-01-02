import random
import hangman_words
from hangman_art import stages, logo
from replit import clear
alreadygiven =[]
TheWord = random.choice(hangman_words.word_list)
blanks = []
life = 6
Flag = False
print(logo)
for i in TheWord:
    blanks += "_"

while not Flag:
  userinp = input("Guess the word\n").lower()
  clear()
  if userinp not in alreadygiven:
    alreadygiven += userinp
    for i in range(len(TheWord)):
      if userinp == TheWord[i]:
        blanks[i] = userinp
        print(f"Yes {userinp} is in word")
    if userinp not in TheWord:
      life -= 1
      print("You Loose A Life")
      if life == 0:
        print(f"End of game. The answer was {TheWord}")
        Flag = True
    if "_" not in blanks:
      print("Congratulations! You have Won")
      Flag = True
    print(stages[life])
    print("".join(blanks))
  else:
    clear()
    print("You have already given this answer")
    print(stages[life])
    print("".join(blanks))
import random
EASY_LEVEL_ATTEMPTS=15
MEDIUM_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=6
def difficulty_level(level_choosen):
  if level_choosen=='easy':
    return EASY_LEVEL_ATTEMPTS
  elif level_choosen=='medium':
    return MEDIUM_LEVEL_ATTEMPTS
  else:
    return HARD_LEVEL_ATTEMPTS
def check_answer(guessed_number,answer,attempts):
  if guessed_number>answer:
    print("Too high")
    return attempts-1
  elif guessed_number<answer:
    print("Too low")
    return attempts-1
  else:
    print(f"You got it! The answer was {answer}")
def guessing_game():
  print("let me think of a number between 1 to 50")
  answer=random.randint(1,100)
  level=input("choose a difficulty level. type 'easy' or 'medium' or 'hard':")
  attempts=difficulty_level(level)
  guessed_number=0
  while guessed_number!=answer:
    print(f"you have {attempts} attempts remaining to guess the number")
    guessed_number=int(input("Make a guess: "))
    attempts=check_answer(guessed_number,answer,attempts)
    if attempts==0:
      print("you have run out of guesses, you lose")
      return
    elif guessed_number!=answer:
      print("guess again")
  print(f'You have {attempts} attempts remaining to guess the number')
  gussed_number=int(input("make a guess:"))
  check_answer(gussed_number,answer)
guessing_game()
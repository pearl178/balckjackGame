def continue_play():
  ask_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
  if ask_user == 'y':
    return True
  else:
    return False
    
def computer_play(cards,computer_cards):
  continue_play = True
  while continue_play:
    current_score = check_ace(computer_cards)
    if current_score > 21:
      continue_play = False
    else:
      if current_score>17:
        continue_play = False
      else:
        computer_cards.append(random.choice(cards))
        continue_play = True
  return computer_cards

def compare_scores(user,computer):
  if user>21:
    print("You went over. You lose 😭")
  elif user == 21:
    if computer ==21:
      print("You lose.")
    else:
      print("You win!")
  else: #user < 21
    if computer == 21:
      print("You lose.")
    elif computer > 21:
      print("You win!")
    else: #user < 21, computer < 21
      if user>computer:
        print("You win!")
      elif user == computer:
        print("Draw")
      else: #user<computer
        print("You lose.")

def check_ace(cards):
  if 11 in cards:
    if sum(cards)>21:
      cards.remove(11)
      cards.append(1)
      score = sum(cards)
    else:
      score = sum(cards)
  else:
    score = sum(cards)
  return score

import random
ask_1 = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if ask_1 == 'y':
  end_game = False
else:
  end_game = True

while not end_game:
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  # Deal both user and computer a starting hand of 2 random card values.
  user_cards = [random.choice(cards),random.choice(cards)]
  computer_cards = [random.choice(cards),random.choice(cards)]
  
  #Calculate the user's and computer's scores based on their card values.
  #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
  user_score = check_ace(user_cards)
  computer_score = check_ace(computer_cards)
  
  print(f"Your cards: {user_cards}, current scores: {user_score}")
  # Detect when computer or user has a blackjack. (Ace + 10 value card).
  if computer_score==21:
    print(f"Computer's cards: {computer_cards}. Computer's score:{computer_score}\nComputer got blackjack!\nYou lose!")
    end_game = not continue_play()
  else:
    if user_score==21:
      print(f"Computer's cards: {computer_cards} Computer's score:{computer_score}")
      print("Blackjack!\nYou win!")
      end_game = not continue_play()
    elif user_score>21:
      print(f"Computer's first card: {computer_cards[0]} Computer's score:{computer_score}")
      print("You lose.")
      end_game = not continue_play()
    else:
      print(f"Computer's first card: {computer_cards[0]}")
      ask_2 = input("Type 'y' to get another card, type 'n' to pass: ")
      if ask_2 == 'y':
        get_another = True

      while get_another:
        user_cards.append(random.choice(cards))
        user_score = check_ace(user_cards)
        if user_score>=21:
          get_another = False
        else:
          print(f"Your cards: {user_cards}, current scores: {user_score}")
          print(f"Computer's first card: {computer_cards[0]}")
          ask_3 = input("Type 'y' to get another card, type 'n' to pass: ")
          if ask_3 == 'y':
            get_another = True
          else:
            get_another = False

      computer_cards = computer_play(cards,computer_cards)
      print(f"Your final hand: {user_cards}, final score:{user_score}")
      computer_score = sum(computer_cards)
      print(f"Computer's final hand: {computer_cards}, final score:{computer_score}")
      compare_scores(user_score,computer_score)
      
      ask_4 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
      if ask_4 == 'y':
        end_game = False
      else:
        end_game = True

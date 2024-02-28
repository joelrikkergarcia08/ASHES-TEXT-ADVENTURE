from random import randint
from time import sleep
import sys
import os



def ex():
  from main import explore
  global explore
  
def clear_screenb():
  if os.name == 'posix':  # Unix/Linux/macOS
    os.system('clear')
  elif os.name == 'nt':  # Windows
    os.system('cls')
  else:
    print("Clear screen not supported on this platform.")


def blackjack():
  game_progress = True
  while game_progress:
    # score counters
    total_score_player = 0
    total_score_cpu = 0
    repeat_game = 0
    clear_screenb()
    print(
        ".                                  BLACKJACK                                   ."
    )
    print(
        "/////////////////////////////////////////////////////////////////////////////////////////"
    )
    card = randint(1, 11)
    sleep(1)
    print("your first card's value is,", card)
    sleep(1)
    total_score_player += card
    print("ill give you your next card now")
    sleep(1)
    card = randint(1, 11)
    print("your second card's value is,", card)
    total_score_player += card
    print("so the total value of your cards is,", total_score_player)

    if total_score_player > 21:
      print("oops you lost")
    else:
      print(
          "you're below 21 so you're safe, good job, would you like to draw another card to get closer to 21? (y/n)"
      )
      take_card = input("")
      if take_card == "y":
        print("ok here's your card")
        card = randint(1, 11)
        print("the value of the card you have taken is,", card)
        total_score_player += card
        print("so the total value for all of your cards is,",
              total_score_player)
        if total_score_player > 21:
          print("oops you took too many cards and you lost :(")
        else:
          print(
              "very good you're still below 21 now would you like to take another card? (y/n)"
          )
          take_card2 = input("")
          if take_card2 == "y":
            card = randint(1, 11)
            print("the value of the card you have taken is,", card)
            total_score_player += card
            print("the total value of all the cards is ,", total_score_player)
            if total_score_player > 21:
              print(
                  "oops you lost because the total value of your cards went over 21!"
              )
            else:
              print(
                  "nice job you cant take any more cards so that's your final score"
              )
          else:
            print("ok so you'll be sticking with that number then")
      else:
        print("well that's your final total then you got below 21")
    comp1 = randint(1, 11)
    comp2 = randint(1, 11)
    comp3 = randint(1, 11)
    hand = comp1 + comp2
    final = 0
    if 15 > hand:
      final = hand + comp3
      print("# the Bartender has chosen to draw a card #")
      print("the cpu got ,", final)
    else:
      if 15 <= hand <= 17:
        flip_a_coin = randint(0, 1)
        if flip_a_coin == "0":
          print(
              "the cpu has chosen to stand with their cards so they now have 2 cards"
          )
          if hand > 21:
            print(
                "wow that's unlucky! the cpu went over 21 and lost with a final value of,",
                hand)
          else:
            print("the cpu is safe below 21 as its total value is,", hand)
        else:
          print(
              "the cpu has taken a card from the deck to end up with three cards"
          )
          if hand + comp3 > 21:
            print(
                "the cpu has lost and you have won as it has gone over 21 and its total value is,",
                hand + comp3)
          else:
            print("the cpu is below 21 with a total value being,",
                  hand + comp3)
      else:
        print(
            "the cpu stands with a total value of two cards leading to its total value being,",
            hand + comp3)
    print("-------------------------results----------------------------")
    if total_score_player > 21:
      print(
          "you lost automatically as you have gone over 21 meaning the cpu has won"
      )
    elif final < total_score_player < hand + comp3 < 21:
      print("you have won against the computer!")
    elif total_score_player < hand + comp3 < 21:
      print("you lost!")
    elif 21 < hand + comp3:
      print("the computer has lost and you have won!")
    elif 21 < hand + comp3 and 21 < total_score_player:
      print("oops nobody won because both the cpu and you went over 21!")
    elif hand + comp3 == total_score_player:
      print("you drew with the cpu! better luck next time!")
    elif total_score_player == 21:
      print("You got 21!")

    print(
        "////////////////////////////////////////////////////////////////////////////////////////////////////////////////"
    )
    print("                                       this is the end of the game")
    print(
        "                                      would you like to play again?(y/n)")
    

    opt = input("--> ")
    
    if opt == "y":
      print("lets do this again then...")
      blackjack()
    else:
      print("cya then")
      return
      
    
      

    

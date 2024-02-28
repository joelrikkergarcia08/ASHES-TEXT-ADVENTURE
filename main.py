import sys
import os
import pickle
from random import randint
from time import sleep
from blackjack import blackjack

items = {
    "Moonlight Greatsword": 120,
    "Potion": 20,
    "Patches' Broadsword": 70,
    "Estus Flask": 80,
    "Courtyard Key": 100,
    "Flaming Horn": 0,
    "Amalgamation of Chaos": 0
}


class Player:

  def __init__(self, name):
    self.estus = 0
    self.name = name
    self.maxhealth = 100
    self.health = self.maxhealth
    self.base_attack = 10
    self.gold = 20
    self.pots = 0
    self.weap = ["Rusty Sword"]
    self.cweap = ["Rusty Sword"]
    self.gravestatus = 0
    self.diff = 0
    self.alley = 0

  @property
  def attack(self):
    attack = self.base_attack
    if self.cweap == "Rusty Sword":
      attack += 5
    if self.cweap == "Moonlight Greatsword":
      attack += 15
    if self.cweap == "Patches' Broadsword":
      attack += 10
    if self.cweap == "Flaming Horn":
      attack += 50
    if self.cweap == "Amalgamation of Chaos":
      attack += 99999999999
    return attack


class ChaosBeast:

  def __init__(self, name):
    self.name = name
    self.maxhealth = 1000
    self.health = self.maxhealth
    self.normalattack = 60
    self.goldgain = 1000


ChaosIG = ChaosBeast("ABLASION OF CHAOS")


class CourtyardDemon:

  def __init__(self, name):
    self.name = name
    self.maxhealth = 180
    self.health = self.maxhealth
    self.normalattack = 30
    self.goldgain = 120


CourtYardIG = CourtyardDemon("Courtyard Demon")


class Bat:

  def __init__(self, name):
    self.name = name
    self.maxhealth = 20
    self.health = self.maxhealth
    self.normalattack = 15
    self.goldgain = randint(2, 18)


BatIG = Bat("Bat")


class Slime:

  def __init__(self, name):
    self.name = name
    self.maxhealth = 25
    self.health = self.maxhealth
    self.normalattack = 7
    self.goldgain = randint(4, 10)


SlimeIG = Slime("Slime")


class Goblin:

  def __init__(self, name):
    self.name = name
    self.maxhealth = 40
    self.health = self.maxhealth
    self.normalattack = 10
    self.goldgain = randint(5, 15)


GoblinIG = Goblin("Goblin")


class Skeleton:

  def __init__(self, name):
    self.name = name
    self.maxhealth = 80
    self.health = self.maxhealth
    self.normalattack = 8
    self.goldgain = randint(8, 20)


SkeletonIG = Skeleton("Skeleton")


def clear_screen():
  if os.name == 'posix':  # Unix/Linux/macOS
    os.system('clear')
  elif os.name == 'nt':  # Windows
    os.system('cls')
  else:
    print("Clear screen not supported on this platform.")


def difficultye():
  BatIG.maxhealth = 15
  SlimeIG.maxhealth = 18
  GoblinIG.maxhealth = 28
  SkeletonIG.maxhealth = 60
  BatIG.health = BatIG.maxhealth
  SlimeIG.health = SlimeIG.maxhealth
  GoblinIG.health = GoblinIG.maxhealth
  PlayerIG.diff = 1


def difficultyn():
  sleep(0.1)


def difficultyh():
  BatIG.maxhealth = 40
  SlimeIG.maxhealth = 42
  GoblinIG.maxhealth = 47
  SkeletonIG.maxhealth = 85
  BatIG.health = BatIG.maxhealth
  SlimeIG.health = SlimeIG.maxhealth
  GoblinIG.health = GoblinIG.maxhealth
  SkeletonIG.health = SkeletonIG.maxhealth
  PlayerIG.maxhealth = 85
  PlayerIG.diff = 3


def diff():
  ene()
  clear_screen()
  print("  DIFFICULTY SELECTION ")
  print("------------------------")
  print("1) EASY MODE - Enemies have less health (recommended for beginners)")
  print(" ")
  print("2) NORMAL MODE - How the game is designed to be played")
  print(" ")
  print(
      "3) HARD MODE - Enemies have more health and Player Health decreased by 15"
  )
  print(" ")
  print("   NOTE: HARD MODE IS NOT RECOMMENDED FOR BEGINNERS!!!")
  opt = input("--> ")
  if opt == "1":
    clear_screen()
    print("CONFIRM DIFFICULTY? (y/n)")
    opt = input("--> ")
    if opt == "y":
      clear_screen()
      print("DIFFICULTY SET TO EASY MODE")
      BatIG.maxhealth = 15
      SlimeIG.maxhealth = 18
      GoblinIG.maxhealth = 28
      SkeletonIG.maxhealth = 60
      BatIG.health = BatIG.maxhealth
      SlimeIG.health = SlimeIG.maxhealth
      GoblinIG.health = GoblinIG.maxhealth
      SkeletonIG.health = SkeletonIG.maxhealth
      PlayerIG.diff = 1
      opt = input("# press enter to continue #")
    else:
      diff()
  elif opt == "2":
    clear_screen()
    print("CONFIRM DIFFICULTY? (y/n)")
    opt = input("--> ")
    if opt == "y":
      clear_screen()
      print("DIFFICULTY SET TO NORMAL MODE")
      PlayerIG.diff = 2
      opt = input("# press enter to continue #")
    else:
      diff()
  elif opt == "3":
    clear_screen()
    print("CONFIRM DIFFICULTY? (y/n)")
    opt = input("--> ")
    if opt == "y":
      clear_screen()
      print("DIFFICULTY SET TO HARD MODE")
      BatIG.maxhealth = 40
      SlimeIG.maxhealth = 42
      GoblinIG.maxhealth = 47
      SkeletonIG.maxhealth = 85
      BatIG.health = BatIG.maxhealth
      SlimeIG.health = SlimeIG.maxhealth
      GoblinIG.health = GoblinIG.maxhealth
      SkeletonIG.health = SkeletonIG.maxhealth
      PlayerIG.maxhealth = 85
      PlayerIG.health = PlayerIG.maxhealth
      PlayerIG.diff = 3
      opt = input("# press enter to continue #")
    else:
      diff()
  else:
    diff()


def start():
  global stat
  stat = True
  global fakeID
  fakeID = 0
  clear_screen()
  print("What is your name?")
  option = input("--> ")
  global PlayerIG
  PlayerIG = Player(option)
  diff()
  clear_screen()
  print(" ")
  print(
      "STORY : You awake in a cold, emberless cave; devoid of fire and flame.")
  sleep(2)
  print("        Few of your kind still exist for you are one of remaining, ")
  sleep(2)
  print("                                 A S H E N ")
  print(" ")
  sleep(2)
  print(
      "As you begin to leave the cave, a deep penetrating voice resonates; splitting your mind"
  )
  sleep(2)
  opt = input("# press enter to continue # ")
  clear_screen()
  start1()


def main():
  clear_screen()

  # Define the ASCII art for "dark souls"
  dark_souls_ascii = r"""
          8 888888888o.            .8.          8 888888888o.   8 8888     ,88'              d888888o.       ,o888888o.     8 8888      88 8 8888           d888888o.  
          8 8888    `^888.        .888.         8 8888    `88.  8 8888    ,88'             .`8888:' `88.  . 8888     `88.   8 8888      88 8 8888         .`8888:' `88.
          8 8888        `88.     :88888.        8 8888     `88  8 8888   ,88'              8.`8888.   Y8 ,8 8888       `8b  8 8888      88 8 8888         8.`8888.   Y8
          8 8888         `88    . `88888.       8 8888     ,88  8 8888  ,88'               `8.`8888.     88 8888        `8b 8 8888      88 8 8888         `8.`8888.    
          8 8888          88   .8. `88888.      8 8888.   ,88'  8 8888 ,88'                 `8.`8888.    88 8888         88 8 8888      88 8 8888          `8.`8888.    
          8 8888          88  .8`8. `88888.     8 888888888P'   8 8888 88'                   `8.`8888.   88 8888         88 8 8888      88 8 8888           `8.`8888.  
          8 8888         ,88 .8' `8. `88888.    8 8888`8b       8 888888<                     `8.`8888.  88 8888        ,8P 8 8888      88 8 8888            `8.`8888.  
          8 8888        ,88'.8'   `8. `88888.   8 8888 `8b.     8 8888 `Y8.               8b   `8.`8888. `8 8888       ,8P  ` 8888     ,8P 8 8888        8b   `8.`8888.
          8 8888    ,o88P' .888888888. `88888.  8 8888   `8b.   8 8888   `Y8.             `8b.  ;8.`8888  ` 8888     ,88'     8888   ,d8P  8 8888        `8b.  ;8.`8888
          8 888888888P'   .8'       `8. `88888. 8 8888     `88. 8 8888     `Y8.            `Y8888P ,88P'     `8888888P'        `Y88888P'   8 888888888888 `Y8888P ,88P'












                                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⠤⢴⣾⣿⣿⣿⣯⠘⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡟⣾⣿⣿⣠⢠⣀⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠀⠒⢫⣿⣿⣿⣿⣿⣿⢸⡗⣾⣙⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣧⢮⡯⣷⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⡐⣚⣛⡛⠛⠉⢹⣽⣿⣽⠮⠓⣫⣏⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⢀⣴⠟⠋⠩⠉⢩⣷⣾⣿⣽⣷⣿⠤⢋⡥⠚⠳⣾⡏⠉⠉⠙⠻⢦⡀⠀⠀
                                                                            ⠀⢀⡿⢁⠈⢀⡠⢔⣣⠟⠿⣿⣿⣿⣗⡪⠇⠀⣢⡾⠛⣮⡢⢄⡀⠐⡈⢻⡄⠀
                                                                            ⢰⣾⠷⠥⠉⠑⡪⣽⠧⠀⠀⠨⡻⣟⣿⠀⣠⠞⡁⠀⠀⠚⣯⣇⡊⠉⠬⠾⣻⡆
                                                                            ⢨⡿⠤⣆⣒⡬⠞⣿⡑⠀⠀⠀⠀⠈⢳⣞⠁⠀⠀⠀⠀⢁⣿⠳⢥⣒⣨⠤⢿⣅
                                                                            ⢻⣿⣿⢋⠁⠀⢰⡇⠀⠀⠀⢠⢞⢿⣭⡍⢻⢦⡀⠀⠀⠀⢼⡇⠀⠈⠝⣿⣿⡟
                                                                            ⠀⣹⡏⢀⣀⣀⣸⣇⣀⣀⣀⣘⣛⣾⢶⠿⠿⣷⣽⡟⠓⢲⠶⠧⢤⣀⡠⢸⣏⠀
                                                                            ⢠⣿⡟⡿⡝⠀⠐⠀⠁⠈⠈⡽⠁⠀⢸⣓⣚⣿⣿⠧⣤⣄⡀⠀⠀⠈⣽⣧⣿⡀
                                                                            ⠘⢷⣧⣿⢷⣤⣤⣴⡶⣶⣾⣷⢤⣤⢾⠭⢭⣿⣿⣿⣶⣭⣝⡛⠶⠶⣳⣼⣿⡇
                                                                            ⠀⠀⠙⠛⠛⠚⠛⠛⣿⣿⣿⣿⣟⣷⡿⠓⠛⠻⠿⢿⠟⢿⠉⠛⠻⠯⠴⠶⠛⠁
                                                                            ⠀⠀⠀⠀⠀⠀⠀⢠⣿⣽⡯⢿⣿⡟⠷⠶⢲⡖⠶⢼⣴⣾⣔⠀⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⢀⡾⠁⠈⠛⠷⣾⣧⠀⠀⢸⣶⢾⠛⠉⠔⢿⣂⠀⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⣼⠍⠂⠀⢠⢣⣿⣷⠀⠄⢸⣿⡞⡄⠀⠀⡨⢷⠆⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⢸⡣⣄⡀⠀⣎⣿⣿⣿⠀⡀⢺⣿⣿⡸⡀⢀⡰⢝⡧⠀⠀⠀⠀⠀
                                                                            ⠀⠀⠀⠀⠀⠀⠉⠓⠮⠽⣼⠛⠿⠿⠤⠤⠿⠿⠛⢷⠯⠵⠚⠋⠀⠀⠀⠀⠀⠀
"""

  # Print the "dark souls" ASCII art
  print(dark_souls_ascii)

  # Define the menu items
  menu_items = ["1.) START", "2.) LOAD", "3.) EXIT"]

  # Calculate the maximum length of the menu items
  max_item_length = max(len(item) for item in menu_items)

  # Get the terminal size
  term_width, term_height = os.get_terminal_size()

  # Calculate the horizontal padding to center the menu
  padding = (term_width - max_item_length) // 2

  # Calculate the vertical padding to roughly center the menu
  # You can adjust the value based on your preference
  vertical_padding = term_height // 15

  # Print the centered menu
  for i, item in enumerate(menu_items):
    if i == 0:
      print("\n" * vertical_padding)
    print(" " * padding + item)

  opt = input("--> ")

  if opt == "1":
    start()
  elif opt == "2":
    if os.path.exists("savefile") == True:
      clear_screen()
      with open('savefile', 'rb') as f:
        global PlayerIG
        PlayerIG = pickle.load(f)
      print("LOADED SAVE STATE")
      opt = input(" ")
      if PlayerIG.diff == 1:
        difficultye()
      elif PlayerIG.diff == 2:
        difficultyn()
      elif PlayerIG.diff == 3:
        difficultyh()
      start1()


#      loadcanyon()
    else:
      print("NO SAVE FILE DETECTED")
      opt = input(" ")
      main()
  elif opt == "3":
    sys.exit()
  else:
    main()


def start1():
  clear_screen()
  # Define the ASCII art for a dragon
  dragon_ascii = r"""
              _          _
             _/|    _   |\_
           _/_ |   _|\\ | _\
         _/_/| /  /   \|\ |\_\_
       _/_/  |/  /  _  \/\|  \_\_
     _/_/    ||  | | \o/ ||    \_\_
    /_/  | | |\  | \_ V  /| | |  \_\
   //    ||| | \_/   \__/ | |||    \\
  // __| ||\  \          /  /|| |__ \\
 //_/ \|||| \/\\        //\/ ||||/ \_\\
///    \\\\/   /        \   \////    \\\
|/      \/    |    |    |     \/      \|
              /_|  | |_  \
             ///_| |_||\_ \
             |//||/||\/||\|             'LEGENDS ARE NOT BORN OR
              / \/|||/||/\/              MADE, THEY JUST ARE'
                /|/\| \/                      
                \/  |                          -CLIVE BARKER
                """

  # Print the dragon ASCII art
  print(dragon_ascii)
  print("STATS")
  print("-----------------------------------------------------")
  print("Name: ", PlayerIG.name)
  print("Attack: ", PlayerIG.attack)
  print("Gold: ", PlayerIG.gold)
  print("Health: ", PlayerIG.health, "/", PlayerIG.maxhealth)
  print("Current Weapon: ", PlayerIG.cweap)
  print(" ")
  print("ACTIONS")
  print("-----------------------------------------------------")
  print(" ")
  print("1.) Look for a fight")
  print(" ")
  print("2.) Store")
  print(" ")
  print("3.) Save")
  print(" ")
  print("4.) Exit")
  print(" ")
  print("5.) Inventory")
  print(" ")
  print("6.) Explore")
  opt = input("--> ")

  if opt == "1":
    prefight()
  elif opt == "2":
    store()
  elif opt == "3":
    clear_screen()
    with open('savefile', 'wb') as f:
      pickle.dump(PlayerIG, f)
      print("GAME SAVED")
    opt = input(" ")
    start1()
  elif opt == "4":
    clear_screen()
    opt = input("Are you sure? (y/n) ")
    if opt == "y":
      clear_screen()
      sys.exit()
    else:
      start1()
  elif opt == "5":
    inventory()
  elif opt == "6":
    explore()
  else:
    start1()


def explore():
  clear_screen()
  print("You walk around the town and sight a few points of interest")
  print("1.) Graveyard (will be skeletons)")
  print("2.) Tavern")
  print("3.) Alleyway")
  print("4.) Go back home")

  opt = input("--> ")
  if opt == "1":
    grave()
  elif opt == "2":
    tavern()
  elif opt == "3":
    alley()
  elif opt == "4":
    start1()
  else:
    explore()


def alley():
  if PlayerIG.alley == 0:
    clear_screen()
    print(
        "# you look around the damp alleyway and find a small friendly slime #"
    )
    scroll_print("??? - Hai!! :] ")
    print("# you grimace in cringe # ")
    scroll_print(
        "skibislime - Mai name is skibislime and it looks like you need a hand out there"
    )
    scroll_print(
        "skibislime - if you can awnser my riddle ill help you out in battle?!?!?"
    )
    clear_screen()
    scroll_print("skibislime - which flower has two lips?")
    print("1.) Rose")
    print("2.) Tulip")
    print("3.) Lily")
    print("4.) Daisy")
    opt = input("--> ")
    if opt == "2":
      clear_screen()
      scroll_print("skibislime - Correct!!!! yayyayayayayaaay")
      PlayerIG.base_attack += 10
      scroll_print("skibislime - noww i wiw always giw u a hand out thewe!!")
      print(
          "# it seems the peculiar slime will lend you hand in battle increasing average damage by 10!"
      )
      PlayerIG.alley = 1
      opt = input("# press enter to continue # ")
      explore()

    else:
      scroll_print("skibislime - Wrong!!!!! >:(")
      scroll_print("skibislime - yu silly, i going back to ohio now !!")
      print("# the peculiar slime seems to have disappeared #")
      opt = input("# press enter to continue # ")
      explore()

  else:
    clear_screen()
    print("# you turn around as youve already been here #")
    opt = input("# press enter to continue # ")
    explore()


def scroll_print(x):
  for char in x:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(.075)  #this is the time it waits between characters
  print()


def tavern():
  clear_screen()
  print("Bartender - Howdy there partner, what can I get ya?")
  print("1.) Drink")
  print("2.) Talk")
  print("3.) Look around")
  print("4.) Leave")

  opt = input("--> ")
  if opt == "1":
    opt = input("Bartender - Have i seen ya here before kiddo? (y/n) ")
    if opt == "n":
      clear_screen()
      print("Bartender - Alrighty well first imma need to see some ID")
      print("1.) Give fake ID")
      print("2.) Lie")
      print("3.) Run out of the tavern")
      print("4.) Pretend to have a heart attack?!?!?")
      resp = input("--> ")
      if resp == "1":
        clear_screen()
        print("Bartender - Alrighty well I'll give you a drink then...")
        sleep(2)
        scroll_print("Bartender - Wait a minute...")
        scroll_print("Bartender - McLovin? really man?")
        scroll_print(
            "Bartender - So you're telling me that you're a hawaiian organ donor and are exactly 21 years old?"
        )
        scroll_print("Bartender - cmon man get out of here")
        print("# The Bartender takes your Fake ID #")
        opt = input("# press enter to continue # ")
        tavern()
      elif resp == "2":
        clear_screen()
        print("# you tried to lie #")
        scroll_print("Bartender - ...........")

        clear_screen()
        print("# It seems to have worked! #")
        scroll_print("Bartender - hmm, alright heres a beer")
        print("# You regained full health! #")
        PlayerIG.health = PlayerIG.maxhealth
        opt = input("# press enter to continue # ")
        tavern()
      elif resp == "3":
        clear_screen()
        print("# You dashed out of the tavern as graceful as a unicorn #")
        opt = input("# press enter to continue #")
        explore()
      elif resp == "4":
        clear_screen()
        scroll_print("# you begin to writhe on the floor, drooling #")
        scroll_print("Bartender - WHAT THE HELL IS GOING ON ERE!?!")
        scroll_print("# the bartender comes to aid you #")
        scroll_print("# !!! #")
        scroll_print("# You notice his wallet is hanging out of his pocket #")
        opt = input("# Take it? (y/n) # ")
        if opt == "y":
          clear_screen()
          scroll_print("# you slowly manage to steal it from him! #")
          print("# you gained 60 gold! #")
          opt = input("# press enter to continue # ")
          PlayerIG.gold = PlayerIG.gold + 60
          explore()
        else:
          clear_screen()
          print("# you didnt take the wallet #")
          opt = input("# press enter to continue # ")
          explore()
      else:
        tavern()

    elif opt == "y":
      clear_screen()
      scroll_print(
          "Bartender - Dude there is no way in HELL you are being served a drink without an ID"
      )
      scroll_print(
          "Bartender - YEAH i remember you, you gave me a Fake id so now give me ..."
      )
      scroll_print("Bartender - A REAL ID!!!!")
      print("1.) Give real ID")
      print("2.) Leave")
      ID = input("--> ")
      if ID == "1":
        clear_screen()
        print("# you show him another fake ID #")
        print("Bartender - ...")
        scroll_print("Bartender - ....")
        scroll_print("Bartender - .....")
        opt = input("# press enter to continue #")
        clear_screen()
        scroll_print(
            "# something unexpected is happening to the bartender! A transformation! #"
        )
        scroll_print("Bartender(?) - Leave Now.")
        scroll_print("# you dont move an inch #")
        opt = input("# press enter to continue #")
        clear_screen()
        scroll_print(
            "Bar%end£r - Are you sure that this is how you want to die?")
        scroll_print("# you remain speechless #")
        opt = input("# press enter to continue #")
        clear_screen()
        scroll_print("B$r%e&d£r - I see.")
        clear_screen()
        scroll_print("ABLASION OF CHAOS - How dare you. ")
        opt = input("# press enter to continue #")
        clear_screen()
        scroll_print("ABLASION OF CHAOS - ...")
        scroll_print("# you have been warped into the chaos dimension #")
        opt = input("# press enter to continue #")
        clear_screen()
        matrixcool()
        clear_screen()
        chaos(ChaosIG)
      elif ID == "2":
        print("# You left the tavern #")
        opt = input("# press enter to continue # ")
        explore()
      else:
        print("# You left the tavern #")
        opt = input("# press enter to continue # ")
        explore()

  elif opt == "2":
    taverntalk()

  elif opt == "3":
    clear_screen()
    scroll_print(
        "You look around the tavern and you see a drunkard on the floor in the bathroom"
    )
    opt = input("# Talk to him? (y/n) # ")
    if opt == "y":
      drunkard()
    else:
      print("# you should leave him be #")
      opt = input("# press enter to continue # ")
      tavern()

  elif opt == "4":
    clear_screen()
    explore()

  else:
    tavern()


def matrixcool():
  for i in range(0, 1000):
    MatrixNumber = randint(0, 100000000)
    print(MatrixNumber, MatrixNumber, MatrixNumber, MatrixNumber, MatrixNumber,
          MatrixNumber, MatrixNumber, MatrixNumber)


def drunkard():
  clear_screen()
  print(
      "Drunkard - heyyyy bro, by any chance you wouldnt have a bit of coke on you??!?"
  )
  print("1.)Get him a coke")
  print("2.)Leave")
  opt = input("--> ")
  if opt == "1":
    clear_screen()
    scroll_print("Drunkard - Ohh hahahahaaa...")
    scroll_print("Drunkard - HAHAHAHA!!! i didnt mean coca cola..")
    clear_screen()
    scroll_print("Bartender - HEY! are you giving that dude MORE drugs?")
    scroll_print("Drunkard - ...")
    clear_screen()
    scroll_print("Bartender - LEAVE NOW.")
    print("# you rushed out of the tavern #")
    sleep(1)
    opt = input("# press enter to continue #")
    explore()
  elif opt == "2":
    print("# You left the tavern # ")
    opt = input("# press enter to continue # ")
    explore()
  else:
    drunkard()


def taverntalk():
  clear_screen()
  scroll_print("Bartender - Howdy, how are ya?")
  print("# you remain silent #")
  scroll_print("Bartender - not much of a talker are ya then?")
  scroll_print(
      "Bartender - anyhow, you up for a game of blackjack for some coin? (y/n) "
  )
  opt = input("--> ")
  if opt == "y":
    blackjack()
    tavern()
  else:
    tavern()


def chaos(enemy):

  chaos_ascii = '''
     (
        .            )        )
                 (  (|              .
             )   )\/ ( ( (
     *  (   ((  /     ))\))  (  )    )
   (     \   )\(          |  ))( )  (|
   >)     ))/   |          )/  \((  ) \
   (     (      .        -.     V )/   )(    (
    \   /     .   \            .       \))   ))
      )(      (  | |   )            .    (  /
     )(    ,'))     \ /          \( `.    )
     (\>  ,'/__      ))            __`.  /
    ( \   | /  ___   ( \/     ___   \ | ( (
     \.)  |/  /   \__      __/   \   \|  ))
    .  \. |>  \      | __ |      /   <|  /
         )/    \____/ :..: \____/     \ <
  )   \ (|__  .      / ;: \          __| )  (
 ((    )\)  ~--_     --  --      _--~    /  ))
  \    (    |  ||               ||  |   (  /
        \.  |  ||_             _||  |  /
          > :  |  ~V+-I_I_I-+V~  |  : (.
         (  \:  T\   _     _   /T  : ./
          \  :    T^T T-+-T T^T    ;<
           \..`_       -+-       _'  )
 )            . `--=.._____..=--'. ./         (
 '''
  print(chaos_ascii)
  print(PlayerIG.name, " VS ", "AB1A#ION 0F CHAO5")
  print("P1ay#r #ea1th: ", PlayerIG.health, "/", PlayerIG.maxhealth)
  print("A6LAS}ON O@ CHAOS", " H3alth: ", ChaosIG.health, "/",
        ChaosIG.maxhealth)
  print("Po^i0ns: ", PlayerIG.pots)
  print(" ")
  print("/£$^@~2461.) A77a3#")
  print(" ")
  print("~£%^!£^~@2.) D4in~ Po&ion")
  print(" ")
  print("&30$^@503.) TAl9")
  print(" ")
  print("$496710794.) Run")
  print(" ")
  opt = input("--> ")

  if opt == "1":
    fightchaos()
  elif opt == "2":
    drinkchaos()
  elif opt == "3":
    talkchaos()
  elif opt == "4":
    clear_screen()
    scroll_print(
        "ABLASION - WheRe dO yoU tHiNk YoURe GoiNG!!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!"
    )
    opt = input("# press enter to continue # ")
    chaos(ChaosIG)
  else:
    print("hint - the first digit of the numbers.")
    opt = input("# press enter to continue # ")
    chaos(ChaosIG)


def talkchaos():
  clear_screen()
  print("# Your mouth is paralysed! #")
  opt = input("# press enter to continue # ")
  chaos(ChaosIG)


def fightchaos():
  clear_screen()
  PAttack = randint(PlayerIG.attack // 2, PlayerIG.attack)
  EAttack = randint(int(ChaosIG.normalattack / 2), int(ChaosIG.normalattack))

  if PAttack == PlayerIG.attack / 2:
    print("You miss!")
  else:
    ChaosIG.health -= PAttack
    print("You deal ", PAttack, " damage!")

  opt = input(" ")
  if ChaosIG.health <= 0:
    chaoswin()
  clear_screen()

  if EAttack == ChaosIG.normalattack / 2:
    print("T2e Balasion msisesed!#$&")
  else:
    PlayerIG.health -= EAttack
    print("T3h Coahs dleat ", EAttack, " 0am2g5!")

  opt = input(" ")

  if PlayerIG.health <= 0:
    die()
  else:
    chaos(ChaosIG)


def chaoswin():
  clear_screen()
  scroll_print(".........")
  scroll_print("# it seems to be over and you are now back in the village #")
  scroll_print("# your mind feels like its splitting #")
  scroll_print(".........")
  opt = input("# press enter to continue #")
  clear_screen()
  scroll_print("# on the ground lies an amalgamation of chaos #")
  scroll_print("# you feel a strange power coursing through you #")
  opt = input("# press enter to continue #")
  clear_screen()
  scroll_print("# THIS IS THE CHAOS ENDING #")
  opt = input("# press enter to continue #")
  clear_screen()
  PlayerIG.weap.append("Amalgamation of Chaos")
  PlayerIG.gold += 10000000000
  start1()


def grave():
  clear_screen()
  clear_screen()
  print("You stumble into the graveyard")
  sleep(2)
  print("The air is light and brisk yet you begin to sweat and tremble")
  sleep(2)
  print(
      "As you continue a skeletal hand breaks through the damp soil and grabs you!!!"
  )
  sleep(2)
  print("Trying to nudge it away, you slip and fall on the ground!!")
  sleep(2)
  opt = input("# press enter to continue #")
  skelefight()


def skelefight():
  global gravfight
  enemy = SkeletonIG
  gravfight = SkeletonIG
  fight(gravfight)
  if PlayerIG.health <= 0:
    gravelose()
  elif PlayerIG.health > 0:
    gravewin()


def gravelose():
  PlayerIG.gravestatus += 1
  clear_screen()
  print("You have died.")
  opt = input(" ")
  sys.exit()


def gravewin():
  clear_screen()
  PlayerIG.gravestatus += 1
  global enemy
  enemy.health = enemy.maxhealth
  PlayerIG.gold += enemy.goldgain
  print("You have defeated the ", enemy.name)
  print("You got ", enemy.goldgain, " gold!")
  opt = input(" ")
  with open('savefile', 'wb') as f:
    pickle.dump(PlayerIG, f)
  start1()


def ene():
  global enemy
  enemynum = randint(1, 4)
  if enemynum == 1:
    enemy = GoblinIG
  elif enemynum == 2:
    enemy = SkeletonIG
  elif enemynum == 3:
    enemy = BatIG
  elif enemynum == 4:
    enemy = SlimeIG


def prefight():
  global enemy
  enemynum = randint(1, 4)
  if enemynum == 1:
    enemy = GoblinIG
  elif enemynum == 2:
    enemy = SkeletonIG
  elif enemynum == 3:
    enemy = BatIG
  elif enemynum == 4:
    enemy = SlimeIG
  fight(enemy)


def fight(enemy):
  clear_screen()
  print(PlayerIG.name, " VS ", enemy.name)
  print("Player Health: ", PlayerIG.health, "/", PlayerIG.maxhealth)
  print(enemy.name, " Health: ", enemy.health, "/", enemy.maxhealth)
  print("Potions: ", PlayerIG.pots)

  # Insert the sword ASCII art here
  sword_ascii = '''
      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
    '''

  print(sword_ascii)

  print("1.) Attack")
  print("2.) Drink Potion")
  print("3.) Run")
  opt = input("--> ")
  if opt == "1":
    attack(enemy)
  elif opt == "2":
    drinkpot()
  elif opt == "3":
    run(enemy)
  else:
    fight(enemy)


def attack(enemy):
  clear_screen()
  PAttack = randint(PlayerIG.attack // 2, PlayerIG.attack)
  EAttack = randint(enemy.normalattack // 2, enemy.normalattack)

  if PAttack == PlayerIG.attack // 2:
    print("You miss!")
  else:
    enemy.health -= PAttack
    print("You deal", PAttack, "damage!")

  opt = input(" ")
  if enemy.health <= 0:
    win(enemy)
  clear_screen()

  if EAttack == enemy.normalattack // 2:
    print("The enemy missed!")
  else:
    PlayerIG.health -= EAttack
    print("The enemy dealt", EAttack, "damage!")

  opt = input(" ")

  if PlayerIG.health <= 0:
    die()
  else:
    fight(enemy)


def win(enemy):
  clear_screen()
  enemy.health = enemy.maxhealth
  PlayerIG.gold += enemy.goldgain
  print("You have defeated the ", enemy.name)
  print("You got ", enemy.goldgain, " gold!")
  opt = input(" ")
  start1()


def die():
  clear_screen()
  print("You have died.")
  opt = input(" ")
  sys.exit()


def drinkpot():
  clear_screen()
  if PlayerIG.pots == 0:
    print("You have no potions!")
  else:
    PlayerIG.health += 50
    if PlayerIG.health > PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    print("You drank a potion!")
    PlayerIG.pots -= 1
  opt = input(" ")
  fight(enemy)


def run(enemy):
  clear_screen()
  runnum = randint(1, 3)
  if runnum == 1:
    print("You successfully ran away!")
    opt = input(" ")
    start1()
  else:
    print("You failed to get away!")
    opt = input(" ")
    clear_screen()
    EAttack = randint(enemy.normalattack - 5, enemy.normalattack + 5)
    if EAttack == enemy.normalattack - 5:
      print("The enemy missed!")
    else:
      PlayerIG.health -= EAttack
      print("The enemy dealt ", EAttack, " damage!")

    opt = input(" ")

    if PlayerIG.health <= 0:
      die()
    else:
      fight(enemy)


def store():
  clear_screen()
  shopkeeper = '''
                     ____          
        .--""___ ""-,      
      .' .-"" __:-' ;      
     /__:.--""      :      
     \              _`-'\  
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       """  \    :  
    ;;  d.   .-"""d. \ ,-:  
   : '.:$$'-"    :$$  '.-,;
   ;   :^"    "-._T'  ') ::
  /   /      \         ._.'
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.    ,       /  
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"  
       '''
  print(shopkeeper)
  print("Welcome to the shop traveller!")
  print("What would you like to buy?")
  print("1.) Moonlight Greatsword, (120 GOLD)")
  print("2.) Patches' Broadsword, (70 GOLD)")
  print("3.) Potion, (20 GOLD)")
  print(
      "4.) Estus Flask,  (80 GOLD FOR FIRST PURCHASE, 1000 GOLD FOR ALL OTHERS)"
  )
  print("5.) Courtyard Key, (100 GOLD)")
  print("6.) Talk to the shopkeeper")
  print("7.) Back")
  print(" ")
  print("hint -  write the full name of the item you wish to pay for")
  opt = input(" ")

  if opt in items:
    if PlayerIG.gold >= items[opt]:
      clear_screen()
      PlayerIG.gold -= items[opt]
      PlayerIG.weap.append(opt)
      print("You have bought", opt)
      if opt == "Potion":
        PlayerIG.pots += 1
      if opt == "Estus Flask":
        items["Estus Flask"] = 1000
      option = input(" ")
      store()

    else:
      clear_screen()
      print("You dont have enough gold.")
      option = input(" ")
      store()

  elif opt == "t":
    clear_screen()
    shopkeeper = '''
                     ____          
        .--""___ ""-,      
      .' .-"" __:-' ;      
     /__:.--""      :      
     \              _`-'\  
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       """  \    :  
    ;;  d.   .-"""d. \ ,-:  
   : '.:$$'-"    :$$  '.-,;
   ;   :^"    "-._T'  ') ::
  /   /      \         ._.'
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.    ,       /  
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"  
       '''
    print(shopkeeper)
    print("SHOPKEEPER : 'i have a request for you.'")
    print(" ")
    sleep(2)
    print(
        "SHOPKEEPER : 'This world is dry, ashen. We live off the scraps of those more powerful than us.'"
    )
    print(" ")
    sleep(2)
    print(
        "SHOPKEEPER : 'The village in particular has been terrorized by a beast hidden within the dungeon courtyard'"
    )
    print(" ")
    sleep(2)
    print(
        "SHOPKEEPER : 'We hope one day it'll die so that we can live in peace'"
    )
    print(" ")
    sleep(2)
    print(
        "SHOPKEEPER : 'See i'd give ya the key but i gotta make a livin' somehow. Just stop by and get the 'Courtyard Key'"
    )
    print(" ")
    sleep(2)
    print(PlayerIG.name, " : ...")
    opt = input("# press enter to continue #")
    start1()

  elif opt == "7":
    start1()

  else:
    clear_screen()
    print("That item does not exist.")
    opt = input("# press enter to continue # ")
    store()


def inventory():
  clear_screen()
  print("What do you want to do?")
  print("1.) Use/Equip item")
  print("b.) Back")
  opt = input("--> ")
  if opt == "1":
    equip()
  elif opt == "b":
    start1()
  else:
    inventory()


def equip():
  clear_screen()
  print("What do you want to equip/use?")
  for weapon in PlayerIG.weap:
    print(weapon)
  print("b to go back")
  opt = input("--> ")
  if opt == PlayerIG.cweap:
    clear_screen()
    print("you already have that item equipped/used")
    print("# press enter to continue #")
    equip()

  elif opt == "Potion":
    clear_screen()
    PlayerIG.health += 50
    if PlayerIG.health > PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    print("You drank a potion!")
    PlayerIG.pots -= 1
    print("You now have", PlayerIG.health, "health")
    print("#press enter to continue#")
    if PlayerIG.pots == 0:
      PlayerIG.weap.remove("Potion")
    input("")
    inventory()

  elif opt == "Estus Flask":
    clear_screen()
    PlayerIG.maxhealth += 10
    if PlayerIG.health > PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    elif PlayerIG.health <= PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    print("MAX HEALTH +10")
    print("# press enter to continue #")
    if "Estus Flask" in items:
      PlayerIG.weap.remove("Estus Flask")
    input(" ")
    inventory()
  elif opt == "b":
    inventory()
  elif opt in PlayerIG.weap:
    clear_screen()
    if opt == "Courtyard Key":
      preboss()
    else:
      PlayerIG.cweap = opt
      print("You have equipped/used ", opt)
      option = input("# press enter to continue #")
      equip()
  else:
    clear_screen()
    print("You dont have ", opt, " in your inventory")
    equip()


def preboss():
  print("Using the key on the gate to the courtyard, a beast is spotted")
  sleep(2)
  print("You begin to tremble yet suddenly you remember why youre here.")
  sleep(2)
  print("Drawing your blade, you get ready to fight!")
  fightboss(CourtYardIG)


def fightboss(enemy):
  clear_screen()
  print(PlayerIG.name, " VS ", "COURTYARD DEMON")
  print("Player Health: ", PlayerIG.health, "/", PlayerIG.maxhealth)
  print("Courtyard Demon", " Health: ", CourtYardIG.health, "/",
        CourtYardIG.maxhealth)
  print("Potions: ", PlayerIG.pots)

  # Insert the sword ASCII art here
  sword_ascii = '''
                                                                _
                                                              _( (~\
       _ _                        /                          ( \> > \
   -/~/ / ~\                     :;                \       _  > /(~\/
  || | | /\ ;\                   |l      _____     |;     ( \/    > >
  _\\)\)\)/ ;;;                  `8o __-~     ~\   d|      \      //
 ///(())(__/~;;\                  "88p;.  -. _\_;.oP        (_._/ /
(((__   __ \\   \                  `>,% (\  (\./)8"         ;:'  i
)))--`.'-- (( ;,8 \               ,;%%%:  ./V^^^V'          ;.   ;.
((\   |   /)) .,88  `: ..,,;;;;,-::::::'_::\   ||\         ;[8:   ;
 )|  ~-~  |(|(888; ..``'::::8888oooooo.  :\`^^^/,,~--._    |88::  |
 |\ -===- /|  \8;; ``:.      oo.8888888888:`((( o.ooo8888Oo;:;:'  |
 |_~-___-~_|   `-\.   `        `o`88888888b` )) 888b88888P""'     ;
 ; ~~~~;~~         "`--_`.       b`888888888;(.,"888b888"  ..::;-'
   ;      ;              ~"-....  b`8888888:::::.`8888. .:;;;''
      ;    ;                 `:::. `:::OOO:::::::.`OO' ;;;''
 :       ;                     `.      "``::::::''    .'
    ;                           `.   \_              /
  ;       ;                       +:   ~~--  `:'  -';
                                   `:         : .::/  
      ;                            ;;+_  :::. :..;;;  
                                   ;;;;;;,;;;;;;;;,;




    '''

  print(sword_ascii)

  print("1.) Attack")
  print("2.) Drink Potion")
  print("3.) Talk")
  print("4.) Run")
  opt = input("--> ")

  if opt == "1":
    attackboss()
  elif opt == "2":
    drinkpotboss()
  elif opt == "3":
    talk()
  elif opt == "4":
    print("YOU CANT RUN AWAY!!!")
    fightboss(CourtYardIG)
  else:
    fightboss(CourtYardIG)


def attackboss():
  clear_screen()
  PAttack = randint(PlayerIG.attack // 2, PlayerIG.attack)
  EAttack = randint(int(CourtYardIG.normalattack / 2),
                    int(CourtYardIG.normalattack))

  if PAttack == PlayerIG.attack / 2:
    print("You miss!")
  else:
    CourtYardIG.health -= PAttack
    print("You deal ", PAttack, " damage!")

  opt = input(" ")
  if CourtYardIG.health <= 0:
    courtyardwin()
  clear_screen()

  if EAttack == CourtYardIG.normalattack / 2:
    print("The Beast missed!")
  else:
    PlayerIG.health -= EAttack
    print("The Demon dealt ", EAttack, " damage!")

  opt = input(" ")

  if PlayerIG.health <= 0:
    die()
  else:
    fightboss(CourtYardIG)


def courtyardwin():
  clear_screen()
  print("--------------------------------------------")
  print(" # The Courtyard Demon has been defeated! # ")
  opt = input("# press enter to continue #")
  clear_screen()
  scroll_print("# You return to the village and a huge crowd awaits you! # ")
  scroll_print("Ecstatic Man - You did it! You defeated that beast.")
  scroll_print("Pleased woman - You are the hero of our village, Thank you.")
  print("# You look towards the skies in pride #")
  opt = input("# press enter to continue #")
  clear_screen()
  scroll_print(
      "# The skies seem to bloom with warmth - a new era of flame and warmth has begun #"
  )
  scroll_print(
      "# Bartender - You did it kid! Would ya look at that, the worlds beginning to lose its ashes"
  )
  scroll_print("# Slime - The world is no longer ashen friend :]")
  opt = input("# press enter to continue #")
  clear_screen()
  print("# You have now completed the main story #")
  print("# Thank you for playing! #")
  scroll_print(
      "# You may now return to the hub and explore the rest of the world as you wish #"
  )
  opt = input("# press enter to continue #")
  clear_screen()
  print("# The Courtyard Demon dropped 1000 gold and his horn! #")
  PlayerIG.gold += 200
  PlayerIG.weap.append("Flaming Horn")
  PlayerIG.weap.remove("Courtyard Key")
  opt = input("# press enter to continue #")
  start1()


def talk():
  clear_screen()
  print("You try to talk with the demon but he only growls back")
  opt = input(" ")
  fightboss(CourtYardIG)


def drinkchaos():
  clear_screen()
  if PlayerIG.pots == 0:
    print("You have no potions!")
  else:
    PlayerIG.health += 50
    if PlayerIG.health > PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    print("You drank a potion!")
    PlayerIG.pots -= 1
  opt = input(" ")
  chaos(ChaosIG)


def drinkpotboss():
  clear_screen()
  if PlayerIG.pots == 0:
    print("You have no potions!")
  else:
    PlayerIG.health += 50
    if PlayerIG.health > PlayerIG.maxhealth:
      PlayerIG.health = PlayerIG.maxhealth
    print("You drank a potion!")
    PlayerIG.pots -= 1
  opt = input(" ")
  fightboss(CourtYardIG)


main()

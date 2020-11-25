import time #Imports a module to add a pause
import random
global life_cnt
life_cnt=3
global ch_weapon
global ch_key
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
# sword = 0
# flower = 0
#
required = ("\nUse only A or B\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"

def intro(life_cnt):
  # global dead_cnt
  print("---------------------")
  print("Level 1")
  print("---------------------")
  print("Lives available:")
  print(life_cnt)

  # print(weapon)
  print ("After a drunken night out with friends, you awaken the "
  "next morning in a thick, dank forest. Head spinning and " 
  "fighting the urge to vomit, you stand and marvel at your new, "
  "unfamiliar setting. The peace quickly fades when you hear a "
  "grotesque sound emitting behind you. A slobbering orc is "
  "running towards you. You will:")
  time.sleep(1)
  print ("""  A. Grab a nearby rock and throw it at the orc
  B. Get up and run
  """)
  ch_riddle = input(">>> ")

  if ch_riddle in answer_A:
    weapon = pick_weapon()
    key=pick_key()
    print("\n\n---------------------")
    print("Level 2")
    print("---------------------")
    # dead_cnt=3
    if(life_cnt<3):
        life_cnt=life_cnt+1
    else:
        life_cnt=3
    print("Lives still available::")
    print(life_cnt)
    weapon_check(weapon,life_cnt)

  elif ch_riddle in answer_B:
      print("\nWelp, that was quick.")
      # life_cnt=0
      life_cnt-=1
      print("\n\n---------------------")
      print("You missed a life. Go to run!!")
      print("No of lives remaining::")
      print(life_cnt)
      print("---------------------")
      life_cnt = option_run(life_cnt)
      if (life_cnt <=0):
          print("\n\n--------------")
          print("Start fresh as u lost all ur life.Go to start")
          print("---------------")
          life_cnt=3
          intro(life_cnt)
      else:
          # life_cnt = 3
          print("Life count available::")
          print(life_cnt)
          weapon = pick_weapon()
          key = pick_key()
          print("\n\n---------------------")
          print("Level 2")
          print("---------------------")
          # dead_cnt=3
          if (life_cnt < 3):
              life_cnt = life_cnt + 1
          else:
              life_cnt = 3
          print("Lives still available::")
          print(life_cnt)
          weapon_check(weapon, life_cnt)

      # intro(life_cnt)
  else:
    print (required)
    intro(life_cnt)

def weapon_check(w,lc):

    level2_weapon = pick_weapon()
    if (level2_weapon == w):
        option_rock()
    else:
        print("U picked the wrong weapon.So restart from picking the right weapon")
        key = pick_key()
        print("\n\n---------------------")
        print("Level 2")
        print("---------------------")
        # dead_cnt=3
        if (lc < 3):
            lc = lc + 1
        else:
            lc = 3

        weapon_check(w,lc)

def option_rock():
  print ("\nThe orc is stunned, but regains control. He begins "
  "running towards you again. Will you:")
  time.sleep(1)
  print ("""  
  A. Throw another rock
  B. Run towards a nearby cave""")
  ch_rock = input(">>> ")
  # randomness(ch_rock)
  if ch_rock in answer_A:
      print("\nGo back!!")
      option_rock()

  elif ch_rock in answer_B:
      print("\n\n---------------------")
      print("Stop")
      print("---------------------")

  else:
    print (required)
    option_rock()
def option_run(lc):
    print("You run as quickly as possible, but the orc's "
          "speed is too great. You will:")
    time.sleep(1)
    print("""  A. Hide behind boulder 
    B. Run towards an abandoned town
    """)
    ch_run = input(">>> ")
    if ch_run in answer_A:
        print("You're easily spotted. "
              "\n\nYou died!Life endangered")
        lc -= 1
        print("\n\n---------------------")
        print("You missed a life:")
        print(lc)
        print("---------------------")
        # l_endangered=1
        return lc



    elif ch_run in answer_B:
        print("No life endangered")
        return lc
    else:
        print(required)
        option_run()

def pick_weapon():
  print("\n\n---------------------")
  print("Pick a weapon from below")
  print("---------------------")
  print ("\na.Spear\nb.Flower\nc.Sponge")
  global ch_weapon
  ch_weapon= input(">>> ")

  return ch_weapon


def pick_key():
    print("\n\n---------------------")
    print("Pick a key from below")
    print("---------------------")
    print("\na.Square\nb.circle\nc.triangle")
    global ch_key
    ch_key = input(">>> ")
    door=["a", "b", "c"]
    # opt = ch_key
    n = random.choice(door)
    if(n==ch_key):
        return ch_key
    else:
        print("Not matching")
        pick_key()

intro(life_cnt)
    # return n
    # return ch_key
    # print("level 2")

# def option_cave():
#   print ("\nYou were hesitant, since the cave was dark and "
#   "ominous. Before you fully enter, you notice a shiny sword on "
#   "the ground. Do you pick up a sword. Y\n?")
#   choice = input(">>> ")
#   if choice in yes:
#     sword = 1 #adds a sword
#   else:
#     sword = 0
#   print ("\nWhat do you do next?")
#   time.sleep(1)
#   print ("""  A. Hide in silence
#   B. Fight
#   C. Run""")
#
#   choice = input(">>> ")
#   if choice in answer_A:
#       print("\nReally? You're going to hide in the dark? I think "
#             "orcs can see very well in the dark, right? Not sure, but "
#             "I'm going with YES, so...\n\nYou died!")
#       # dead_cave=1
#       # dead_count(dead_cave)
#       dead_cnt=1
#       dead_cnt_cave = dead_count(dead_cnt)
#       intro()
#   elif choice in answer_B:
#       if sword > 0:
#           print("\nYou laid in wait. The shimmering sword attracted "
#                 "the orc, which thought you were no match. As he walked "
#                 "closer and closer, your heart beat rapidly. As the orc "
#                 "reached out to grab the sword, you pierced the blade into "
#                 "its chest. \n\nYou survived!")
#       else:  # If the user didn't grab the sword
#           print("\nYou should have picked up that sword. You're "
#                 "defenseless. \n\nYou died!")
#           dead_cnt = 1
#           dead_cnt_cave = dead_count(dead_cnt)
#           intro()
#   elif choice in answer_C:
#       print("As the orc enters the dark cave, you sliently "
#             "sneak out. You're several feet away, but the orc turns "
#             "around and sees you running.")
#       option_run()
#   else:
#       print(required)
#       option_cave()
#
# def dead_count(cnt):
#     global dead_cnt
#     dead_cnt=dead_cnt+cnt
#     if(dead_cnt>3):
#         print("stop")
#     else:
#         return dead_cnt
#
#


#
# def option_town():
#     print("\nWhile frantically running, you notice a rusted "
#           "sword lying in the mud. You quickly reach down and grab it, "
#           "but miss. You try to calm your heavy breathing as you hide "
#           "behind a delapitated building, waiting for the orc to come "
#           "charging around the corner. You notice a purple flower "
#           "near your foot. Do you pick it up? Y/n")
#     choice = input(">>> ")
#     if choice in yes:
#         flower = 1  # adds a flower
#     else:
#         flower = 0
#     print("You hear its heavy footsteps and ready yourself for "
#           "the impending orc.")
#     time.sleep(1)
#     if flower > 0:
#         print("\nYou quickly hold out the purple flower, somehow "
#               "hoping it will stop the orc. It does! The orc was looking "
#               "for love. "
#               "\n\nThis got weird, but you survived!")
#     else:  # If the user didn't grab the sword
#         print("\nMaybe you should have picked up the flower. "
#               "\n\nYou died!")
#         dead_cnt = 1
#         dead_cnt_intro = dead_count(dead_cnt)
#         intro()



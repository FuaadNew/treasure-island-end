print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island. You mission is to to find the treasure.")
print("You are at a crossroads, where do you want to go?")
Answer= input("left or right?")
if Answer.lower() == "left": 
  print("You've come to a lake. There is an island in the middle of the lake.")
  Answer=input("swim or wait")
  if Answer.lower() == "wait":
    print("Somehthing large moves under the lake, you wait until movement ceases and leap into the water")
    print("You arive at the island, there is a castle with three entrances.")
    Answer= input("Which Door?: RED: BLUE: YELLOW:")
    if Answer.lower() == "red":
      print("The room is full with fire that quickly expands to engulf you. You Die.")
    if Answer.lower() == "blue":
      print('''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"''')
      print("*Something* swings it axe. You die before you can register anything. Game Over.")

    if Answer.lower() == "yellow":
      print('''-----------------------------------------------------
   _                             .-.
  / )  .-.    ___          __   (   )
 ( (  (   ) .'___)        (__'-._) (
  \ '._) (,'.'               '.     '-.
   '.      /  "\               '    -. '.
     )    /   \ \   .-.   ,'.   )  (  ',_)    _
   .'    (     \ \ (   \ . .' .'    )    .-. ( \
  (  .''. '.    \ \|  .' .' ,',--, /    (   ) ) )
   \ \   ', :    \    .-'  ( (  ( (     _) (,' /
    \ \   : :    )  / _     ' .  \ \  ,'      /
  ,' ,'   : ;   /  /,' '.   /.'  / / ( (\    (
  '.'      "   (    .-'. \       ''   \_)\    \
                \  |    \ \__             )    )
              ___\ |     \___;           /  , /
             /  ___)                    (  ( (
          '.'                         ) ;) ;
                                        (_/(_/
----------------------------------------------------
''')
      print("You found the treasure! You win!")

      
  else:
    print("A mounsterous trout springs from the lake")
    print('''
                                     _
                                    (_)
              |    .
          .   |L  /|   .          _
      _ . |\ _| \--+._/| .       (_)
     / ||\| Y J  )   / |/| ./
    J  |)'( |        ` F`.'/        _
  -<|  F         __     .-<        (_)
    | /       .-'. `.  /-. L___       
    J \      <    \  | | O\|.-'  _   
  _J \  .-    \/ O | | \  |F    (_) 
 '-F  -<_.     \   .-'  `-' L__    
__J  _   _.     >-'  )._.   |-'  
`-|.'   /_.           \_|   F    
  /.-   .                _.<     
 /'    /.'             .'  `\    
  /L  /'   |/      _.-'-\
 /'J       ___.---'\|
   |\  .--' V  | `. `
   |/`. `-.     `._)
      / .-.\
    \ (  `\
       `.\
''')
    print("Attacked by trout. You die")
elif Answer.lower() == "right": 
  print('''SSSSSS
.ss.  SP""YS
SSSS  S    S
`SS'  S.  .S
      SSSSSS''')
  print("You fall into a hole and die")


# room names and descriptions have been generated using the help of ChatGPT
# i am aware the rooms are bugged and that the player cannot progress past the first room
# i am unsure of why this is happening since the rooms are matched to how they are listed in the array
# the quit and look functions do work however
# the boss is designed to be weak so that the player can win

# class for player name, health, attack and any items they might have such as keys to open doors
class CPlayer:
    def __init__(self, name, health, attack, inventory):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = []
        
    def IsAlive(self):
        return self.health > 0
    
# similar to player class
class CEnemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def IsAlive(self):
        return self.health > 0
    
# class for rooms, the names, description, enemies, items and a boolean so that the user is required to get a key before advanancing past the first room 
class CRoom:
    def __init__(self, name, description, enemy=None, item=None, isDoorLocked=True):
        self.name = name
        self.description = description
        self.enemy = enemy
        self.item = item
        self.isDoorLocked = isDoorLocked
        
    def RemoveItem(self):
        self.item = None
        
    def UnlockDoor(self):
        self.isDoorLocked = False
        
    def LockDoor(self):
        self.isDoorLocked = True

# prints a game over message for the user  
def GameOver():
    print(""""
Game Over! You did not succeed in your quest to defeat the Behemoth and failed to save Umaros.
Please try again.""")
    
# function for the user to enter their name, choose their class and welcomes them to the game world
def SelectCharacter():
    playerName = input("""Enter your name: 
> """)
    player = CPlayer(playerName,0 ,0 ,0)
    print("\n")
    print("Next you will select your class. Each class has different Attack (ATK) and Hitpoint (HP) values. ")
    characterClass = input("""
Please select your class; Mage, Warrior or Rogue: 
-------------------------------
| Mage    | ATK: 12 | HP: 70  |
| Warrior | ATK: 8  | HP: 100 |
| Rogue   | ATK: 10 | HP: 80  |
-------------------------------
> """).lower()
    
    # input validation so that the user will be asked to try again if they do not input what is asked of them
    while (characterClass != "mage" and characterClass != "warrior" and characterClass != "rogue"):
        print(f"Sorry, you cannot be a {characterClass}")
        characterClass = input("""Please only enter Mage, Warrior or Rogue: 
> """).lower()
    print(f"Welcome {player.name.capitalize()}, it seems you have selected to become a {characterClass.capitalize()}, a good choice.")
    if characterClass == "mage":
        return CPlayer(playerName, 70, 12, 0)
    elif characterClass == "warrior":
        return CPlayer(playerName, 100, 8, 0)
    elif characterClass == "rogue":
        return CPlayer(playerName, 80, 10, 0)

# initialises the bosses name and stats
behemoth = CEnemy("Behemoth", 100, 6)
goblin = CEnemy("Goblin", 40, 4)
skeleton = CEnemy("Skeleton", 30, 6)

# combat function that plays out a fight between the player and an enemy,
# if the players health reaches 0 then the GameOver function will be called
def Combat(player, enemy):
    print(f"You engage in combat with the {enemy.name}!")
    while player.IsAlive() and enemy.IsAlive():
        print(f"{player.name} HP: {player.health}")
        print(f"{enemy.name} HP: {enemy.health}")
        enemy.health -= player.attack
        print(f"You attacked {enemy.name} for {player.attack} damage!")
        if not enemy.IsAlive():
            break
        player.health -= enemy.attack
        print(f"{enemy.name} attacked you for {enemy.attack} damage!")
    if player.IsAlive():
        print(f"You defeated {enemy.name}!")
    else:
        GameOver()
        
# main game function
def main():
    # intoduces player to the mechanics of the game 
    print (f"""
--- Player Instructions and Game Rules ---
Movement:
You can move rooms using the directions: North, East, South or West. 
Please use the map for information about your postition.
Combat:
Upon entry to a room you will be forced into combat if there is an enemy in that room.
Combat is turn based. You the player will start first and can choose to attack or use an item from your inventory.
The enemy will then take their turn to attack.
Rinse and repeat until you or the enemy dies.
It is reccomended to keep your HP above 0!
Hints and tips:
Type 'help' at any time to get hints on what to do at any time during the game.
Type 'look' to get extra information about your current location. This might reveal hidden items.

Next you will be asked to enter your name.
""")
    
    # initialises the players stats and name through the SelectCharacter function
    player = SelectCharacter()
    
    # initalises the rooms for the game
    rooms = [
        CRoom("Frostfire Hall", # room 0
"""
You enter the Frostfire Hall and are greeted by a chilling sight:
towering stone walls, veiled in frost, seemingly imprisoning all who dare enter.
Blue flames flicker from torches along the walls, casting ominous shadows that writhe across the icy surfaces.
You notice something shining on the floor. Maybe you should investigate it further.
"""),
        CRoom("Frostfang Cellar", # room 1
"""
You descend into the Frostfang Cellar, a suffocating sense of cold grips them, as if the very air itself has turned to ice. 
Stone walls, adorned with frost, loom ominously in the dim light, casting elongated shadows that seem to shift with unseen movement.
You notice a goblin peering over at you. What will he do?

         ,      ,
        /(.-""-.)\
    |\  \/      \/  /|
    | \ / =.  .= \ / |
    \( \   o\/o   / )/
     \_, '-/  \-' ,_/
       /   \__/   \
       \ \__/\__/ /
     ___\ \|--|/ /___
   /`    \      /    `\
  /       '----'       \

""",enemy=goblin, item='Master Key', isDoorLocked=True),

        CRoom("Shiver Crypt", # room 2
"""
You venture into the Shiver Crypt, 
a bone-chilling cold envelops you, permeating the very depths of your being.
The crypt's stone walls are adorned with icy stalactites, casting eerie shadows that dance with the flickering torchlight.
In the shadows lurk a skeletal figure, eerily silent, yet its presence exudes a palpable sense of malevolence, as if merely biding time.

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

""", enemy=skeleton),
        CRoom("Arctic Sanctum", # room 3
"""
As you cautiously enter the Arctic Sanctum, a biting cold envelopes you, piercing through even the thickest layers of clothing. 
The chamber's stone walls loom ominously, adorned with jagged icicles that glint menacingly in the dim light.
But you can see the looming oak doors of what would have once been the throne room. The Behemoth must be there...
      ______          ______ 
   ,-' ;  ! `-.    ,-' ;  ! `-.
  / :  !  :  . \  / :  !  :  . \
 |_ ;   __:  ;  ||_ ;   __:  ;  |
 )| .  :)(.  !  |)| .  :)(.  !  |
 |"    (##)  _  ||"    (##)  _  |
 |  :  ;`'  (_) (|  (_) ;`'  :  (
 |  :  :  .     ||  :  :  .     |
 )_ !  ,  ;  ;  |)_ !  ,  ;  ;  |
 || .  .  :  :  ||| .  .  :  :  |
 |" .  |  :  .  ||" .  |  :  .  |
 |mt-2_;----.___||mt-2_;----.___|
 
"""),
        CRoom("Frozen Throne Room", # room 4
"""
As you cautiously enter the Frozen Throne Room, a bone-chilling cold seizes you, permeating your very essence with its icy grip.
The chamber's stone walls rise majestically, adorned with intricate carvings that seem to shiver in the frosty air.
At the far end of the room, the colossal form of the Behemoth looms, its towering figure exuding an aura of primal power as it fixates its gaze upon you.
The final battle lies ahead before you can save Umaros from the Behemoth's icy grip.
""",
enemy=behemoth),
    ]
    
    currentRoom = rooms[0]
    
    # main gameplay loop
    # will check if there is an enemy in the room that is alive,
    while True:
        print(currentRoom.description)
        if currentRoom.enemy and currentRoom.enemy.IsAlive():
            Combat(player, currentRoom.enemy)
            if not player.IsAlive():
                break # will end the game if the players HP reaches 0
            currentRoom.enemy = None
        print("""
What would you like to do?
Move
Look
Ask for help
Quit
""")    
        playerChoice = input("> ").lower()
        # input validation so that the user will be asked to try again if they do not input what is asked of them
        while (playerChoice != "move" and playerChoice != "look" and playerChoice != "ask for help" and playerChoice != "quit"):
            print("That is not an option. Try again. ")
            playerChoice = input("> ")
        # if the player selects move from the previous inputs they will be able to move rooms
        # (this does not work as intended since the player will get stuck in room 0)
        if playerChoice == 'move':
            print("""
Choose which direction you would like to go:
North
East
South
West
""")
            directionChoice = input("> ").lower()
            # if the player enters north then program should check what room they are in 
            # and whether they can move in that direction and tell them they cannot if it is not possible
            if directionChoice == 'north':
                if currentRoom.name == 'Frostfire Hall':
                    print("The door is locked. You need to find a key.")
                elif currentRoom.name == 'Frostfang Cellar':
                    print("You move to the Shiver Crypt. ")
                    currentRoom = rooms[2]
                else:
                    print("You can't go this way.")
            elif directionChoice == 'east':
                if currentRoom.name == 'Frostfang Cellar':
                    print("You move to the Frostfire Hall. ")
                    currentRoom = rooms[0]
                elif currentRoom.name == 'Shiver Crypt':
                    print("You move to the Arctic Sanctum. ")
                    currentRoom = rooms[3]
                elif currentRoom.name == 'Arctic Sanctum':
                    print("You move to the Frozen Throne Room. ")
                    currentRoom = rooms[4]
                else:
                    print("You can't go this way.")
            elif directionChoice == 'south':
                if currentRoom.name == 'Shiver Crypt':
                    print("You move to Frostfang Cellar.")
                    currentRoom = rooms[1]
                elif currentRoom.name == 'Arctic Sanctum':
                    print("You move to the Shiver Crypt. ")
                    currentRoom = rooms[2]
                else:
                    print("You can't go this way.")
            elif directionChoice == 'west':
                if currentRoom.name == 'Frostfire Hall':
                    print("You move to the Frostfang Cellar. ")
                    currentRoom == rooms[1]
                else:
                    print("You can't go this way.")
            else:
                print("That is not an option. Try again.")
        # if the player inputs look then it will give a furthther description of the room
        elif playerChoice == 'look':
            print("You decide to look around the room.")
            if currentRoom.name == "Frostfire Hall":
                print("""
You scan the room, you walk over the the grand hall table,
winestains cover the table and there are still cups left behind.
But what's this shining beneath the table?
You found a key! 

     8 8 8 8                     ,ooo.
     8a8 8a8                    oP   ?b
    d888a888zzzzzzzzzzzzzzzzzzzz8     8b
     `""^""'                    ?o___oP'
""")          
                # adds the item to the users inventory array 
                player.inventory.append("Master Key")
                # removes the item from the room's array
                currentRoom.RemoveItem()
            elif currentRoom.name == "Frostfang Cellar":
                print("""
You look around the room, noticing the old wine bottles.
You wonder what this castle might have been like before it was sacked by the Behmoth.
But there is nothing of imporantce to be found in this room...
""")
            elif currentRoom.name == "Shiver Crypt":
                print("""
The crypts are the deepest, darkest part of the castle.
The remains of bodies scatter the floor, the tombstones are cracked and broken.
Such a haunting place...
But there is nothing of imporantce to be found in this room...
""")
            elif currentRoom.name == "Arctic Sanctum":
                print("""
Although this room is in disgrace now you sense that this might have been one of the castle's prized rooms.
There are remains of paintings littered on the floor.
You walk forward and look up to see a painted ceiling. It reminds you of happier times.
Then you notice something around your feet.
You find a health potion lying on the floor!
""")
            elif currentRoom.name == "Frozen Throne Room":
                print(f"""
You cannot help but get trapped in gaze of the Behemoth.
The colossal figure is seated upon its now frozen throne.
You know what you must do, but should you fail Umaros might be lost to its grip forever...
Press on{player.name}!
""")
        # provides some advice to the player be reiterating the instructions to the player
        elif playerChoice == 'ask for help':
            print(f"Here are some options to help you{player.name}. ")
            print("""
Here are some available commands:
Type move be given options to move North, East, South or West.
Type look to examing your surroundings further.
Type quit to exit the game.
""")
        # quits the game
        elif playerChoice == 'quit':
            print("You have quit the game. ")
            break
        else:
            print("Invalid choice. Try again.")

        input("""Press Enter to continue...
> """)
        
        if currentRoom.enemy and currentRoom.enemy.IsAlive():
            Combat(player, currentRoom.enemy)
            if not player.IsAlive():
                break
            currentRoom.enemy = None

    GameOver()


if __name__ == "__main__":
    main()
    
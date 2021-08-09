import random

inventory = []
PlayerHealthPoints = 20
PlayerDamagePoints = 5
PlayerCash = 20


class Enemy:
    def __init__(self, name, desc, damagepoint, healthpoint):
        self.name = name
        self.desc = desc
        self.damagepoint = damagepoint
        self.healthpoint = healthpoint
    
    def DescribeEnemy(self):
        print("\nName: " + self.name)
        print("Description: " + self.desc)
        print("DP: " + str(self.damagepoint))
        print("HP: " + str(self.healthpoint))
    
    def EnemyAttack(self):
        global PlayerHealthPoints
        DamageDone = random.randrange(0, self.damagepoint)
        print(self.name + " attacks for " + str(DamageDone))
        PlayerHealthPoints = PlayerHealthPoints - DamageDone
        
    def AttackMenu(self):
        global PlayerDamagePoints
        global PlayerHealthPoints
        print(self.name + " attacks!")
        WhoGoesFirstNum = random.randrange(2)
        if (WhoGoesFirstNum == 1):
            self.EnemyAttack()
        
        while True:
            if (PlayerHealthPoints <= 0):
                print("You've died")
                exit(0)
            print("-----------------------------------------------")
            print("What would you like to do: ")
            print("Your HP: " + str(PlayerHealthPoints))
            print("Attack")
            print("Run")
            print("Describe Enemy")
            command = input().lower()
            if (len(command) == 0):
                print("Please input command")
                continue
            elif (command == "attack"):
                DamageDone = random.randrange(0, PlayerDamagePoints)
                print("You attack for " + str(DamageDone))
                self.healthpoint = self.healthpoint - DamageDone
                if (self.healthpoint <= 0):
                    print(self.name + " has been defeated.")
                    break
            elif (command == "run"):
                Run = random.randrange(2)
                if (Run == 0):
                    print("You failed to run away")
                if (Run == 1):
                    print("You successfully run away")
                    break
            elif (command == "describe enemy"):
                self.DescribeEnemy()
                continue
            elif (command in describe_alias):
                self.DescribeEnemy()
                continue
            self.EnemyAttack()     
class Item:
    def __init__(self, name, desc, damagepoint):
        self.name = name
        self.desc = desc
        self.damagepoint = damagepoint

    def UpdateDamagePoints(self):
        global PlayerDamagePoints
        PlayerDamagePoints = self.damagepoint

class Bomb:
    def __init__(self, damagepoint):
        self.damagepoint = damagepoint

    def BlowUp(self):
        global PlayerHealthPoints
        DamageDone = random.randrange(0, self.damagepoint)
        print("You've been blown up for " + str(DamageDone))
        PlayerHealthPoints = PlayerHealthPoints - DamageDone
    
    def Fail(self):
        global PlayerHealthPoints
        Fail = random.randrange(1, 5)
        if (Fail < 2):
            print("The bomb didn't go off, god has spared you today friend.")
        else:
            self.BlowUp()
            if (PlayerHealthPoints <= 0):
                print("You've died")
                exit(0)


class NPC:
    def __init__(self, name, desc, listofitems, listoftalkingpoints):
        self.name = name
        self.desc = desc
        self.listofitems = listofitems
        self.listoftalkingpoints = listoftalkingpoints

    def Talk(self):
        TalkingPoint = random.randrange(0, len(self.listoftalkingpoints))
        print(self.name + ": " + self.listoftalkingpoints[TalkingPoint])
    
    def Trade(self):
        global PlayerCash
        global inventory
        print(self.name + ": " + "Hello weary traveler, take a look at my wares.")
        while(True):
            print(self.name + ": " + "What would you like?")
            rotation = 1
            for x in self.listofitems:
                print(str(rotation) + ". " + x.name)
                rotation = rotation + 1
            Item = input().lower()
            InInventory = False
            Index = 0
            for x in self.listofitems:
                if (Item == x.name):
                    InInventory = True
                else: 
                    Index = Index + 1
            if (InInventory == True):
                Price = random.randrange(1, 20)
                print(self.name + ": " + "Oh that? That's nice. That'll be " + str(Price) + " Doubloons")
                print(self.name + ": " +"Will you take it?")
                Take = input().lower()
                if (Take == "yes"):
                    if (PlayerCash >= Price):
                        print(self.name + ": " + "Good, it's yours")
                        PlayerCash = PlayerCash - Price
                        inventory.append(self.listofitems[Index])
                        del self.listofitems[Index]

                        print(self.name + ": " + "Would you like to continue looking at my wares traveler? Yes or No?")
                        Continue = input().lower()
                        if (Continue == "yes"):
                            continue
                        elif (Continue == "no"):
                            print(self.name + ": " + "Then goodbye dear traveler.")
                            break
                    else:
                        print(self.name + ": " + "Oh that's too bad, doesn't look like you have enough doubloons. Come back when you've got the money.")
                        break
                elif (Take == "no"):
                    print(self.name + ": " + "Oh that's too bad, would you like to continue looking at my wares?")
                    Continue = input().lower()
                    if (Continue == "yes"):
                        continue
                    elif (Continue == "no"):
                        print(self.name + ": " + "Then goodbye dear traveler.")
                        break
            elif (Item == "leave"):
                print(self.name + ": " + "Then goodbye dear traveler.")
                break
            else:
                print(self.name + ": " + "Sorry I don't have that. Try again.")
                continue
    
        
def get_command():
    output = None
    while True:
        print('\nEnter command:', end='')
        command = input().lower().split()
        if len(command) == 0:
            continue
        elif command[0] == 'exit':
            exit(0)
        elif command[0] in checkinv_alias:
            print("Inventory: ")
            if len(command) == 2:
                for i in inventory:
                    if i.name == command[1]:
                        print("Name: " + i.name)
                        print("Description: " + i.desc)
                        print("Damage Point: " + str(i.damagepoint))
            elif len(command) == 1:
                for i in inventory:
                    print(i.name)
        elif command[0] in use_alias:
            if (len(command) > 1):
                for i in inventory:
                    if i.name == command[1]:
                        i.UpdateDamagePoints()
                        print("Using " + i.name)
            else:
                print("Please add item to use")
            
        else:
            output = command
            break
    return output

go_alias = ['go', 'move']
describe_alias = ['describe', 'desc']
use_alias = ["use"]
checkinv_alias = ["check", "checkinv"]

#RoomAliases
Room1_alias = ['room1', 'r1', '1']
Room2_alias = ['room2', 'r2', '2']
Room3_alias = ['room3', 'r3', '3']
Room4_alias = ['room4', 'r4', '4']


def room1():
    description = "This is room1. There is a passage to [room2] and to [room3]."
    print(description)
    print(" 1.Go\Move \n 2. Use \n 3. Check\Checkinv \n 4. Desc\Describe")
    while True:
        command = get_command()
        if command[0] in go_alias:
            if len(command) < 2:
                print('not enough arguments')
                continue
            if command[1] in Room2_alias:
                room2()
                break
            elif command[1] in Room3_alias:
                room3()
                break
            else:
                print("Cannot go there.")
        elif command[0] in describe_alias:
            print(description)
        else:
            print('not a valid command')

Knight = Enemy("Knight", "A rotting knight. Seems has he's been dead for a while. His armor is rusting.", 10, 25)
room2_description = "This is room2. This room is locked. Find a key to unlock it. There is a path to [room1]"
unlocked = False
def room2():
    global room2_description
    global Knight
    global unlocked
    print(room2_description)
    print(" 1.Go\Move \n 2. Use \n 3. Check\Checkinv \n 4. Desc\Describe \n 5. Unlock")
    while True:
        command = get_command()
        if command[0] in go_alias:
            if len(command) < 2:
                print('not enough arguments')
                continue
            if command[1] in Room1_alias:
                room1()
                break
            else:
                print("Cannot go there.")
        elif command[0] == "unlock":
            if (unlocked == False):

                if Room2Key in inventory:
                    unlocked = True
                    room2_description = "This is room2. There is a passage to [room1]"
                    print("You have unlocked the room.")
                else:
                    print("You do not have the room key. Find the room key")
            else:
                print("You've already unlocked the room")
            continue
            
        elif command[0] in describe_alias:
            print(room2_description)
            if (unlocked == True):
                if (Knight.healthpoint <= 0):
                    print("The Knight lays there dead. Poor soul.")
                else: 
                    Knight.AttackMenu()
        else:
            print('not a valid command')

Bomb = Bomb(15)
Room2Key = Item("room2key", "Key that opens Room 2", 0)
room3_description = "This is room3. There is a passge to [room1] and [room4]."
def room3():
    global room3_description
    global Room2Key
    global Bomb
    Bomb.Fail()
    room_items = [Room2Key]
    print(room3_description)
    print(" 1.Go\Move \n 2. Use \n 3. Check\Checkinv \n 4. Desc\Describe")
    while True:
        command = get_command()
        if command[0] in go_alias:
            if len(command) < 2:
                print('not enough arguments')
                continue
            if command[1] in Room1_alias:
                room1()
                break
            if command[1] in Room4_alias:
                room4()
                break
            else:
                print("Cannot go there.")
        
        elif command[0] in describe_alias:
            if set(room_items).issubset(inventory):
                print(room3_description)    
            else:
                print(room3_description)
                print("You Found: ")
                for i in room_items:
                    print(i.name)
                inventory.extend(room_items)        
        else:
            print('not a valid command')


NPC = NPC("Wilbert", "A wary traveler with a backpack of wares.", [Item("long_sword", "A Long sword. Looks sturdy and durable.", 15)], ["Hello dearest traveler", "Hello, want to look at my wares?"])
Sword = Item("short_sword", "Dull short sword. Looks very used, but it will work.", 10)
room4_description = "This is room4. There is a passge to [room3]. There is a traveler in the corner looking to sell his wares."
def room4():
    global room3_description
    global Sword
    global NPC
    room_items = [Sword]
    
    print(room4_description)
    print(" 1.Go\Move \n 2. Use \n 3. Check\Checkinv \n 4. Desc\Describe \n 5. Talk \n 6. Trade")
    while True:
        command = get_command()
        if command[0] in go_alias:
            if len(command) < 2:
                print('not enough arguments')
                continue
            if command[1] in Room3_alias:
                room3()
                break
            else:
                print("Cannot go there.")
        elif command[0] in describe_alias:
            if set(room_items).issubset(inventory):
                print(room4_description)    
            else:
                print(room3_description)
                print("You Found: ")
                for i in room_items:
                    print(i.name)
                inventory.extend(room_items)
        elif command[0] == "talk":
            NPC.Talk()
        elif command[0] == "trade":
            NPC.Trade()
        else:
            print('not a valid command')
room1()

class Player:
    def __init__(self, name, level=1, health=100, gold=0):
        self.name = name
        self.level = level
        self.health = health
        self.gold = gold

    def recieveGold(self,amount):
        self.gold += amount

    def takeDamage(self,damage):
        self.health -= damage
        if (self.health < 0 ):
            self.health = 0

    def printStats(self):
        print(f"Name: {self.name}  Level: {self.level} Health: {self.health} Gold: {self.gold}")

class Enemy():
    def __init__(self, name="Warrior", health=80, attack=24, goldReward=15):
        self.name = name
        self.health = health
        self.attack = attack
        self.goldReward = goldReward

    def attackPlayer(self,player):
        player.takeDamage(self.attack)

def battleEnemy(player, enemy):
    print("Your up against a lvl 3 Warrior!")

    while (enemy.health > 0 and player.health > 0 ):
        playerChoice = int(input("1. Attack\n2. Heal\nEnter your choice: "))
        if playerChoice == 1:
            damage = 13
            enemy.health -= damage
            print("You deal 13 damage")
        elif playerChoice == 2:
            player.health += 35
            print("You use a healing potion to recover")

        if enemy.health > 0:
            enemy.attackPlayer(player)
            print("Warrior attacks you for 24 damage")

        print(f"Your health: {player.health} | Enemy's health: {enemy.health}")

    if player.health <= 0:
        print("\nYou lost this fight.\nHint: Dont forgot to heal. ")
    else:
        player.recieveGold(enemy.goldReward)
        print("\nYou Won!!\nYou are the new fighting champion \nAs a reward you got 15 gold.")

def main():
    print("Welcome, Fighter! ")
    playerName = input("What is your name? ")

    player = Player(playerName)
    print(player.printStats())

    enemy = Enemy()
    battleEnemy(player,enemy)

if __name__ == "__main__" :
    main()
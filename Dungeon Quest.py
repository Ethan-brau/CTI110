
import random
import time

def introduction():
    """Provide the game introduction and backstory."""
    print("=" * 50)
    print("Welcome to Endless Dungeon Quest!".center(50))
    print("=" * 50)
    print("\nSurvive as long as you can, collect treasure, and defeat enemies!")
    print("Each run ends when your health reaches zero.")
    print("Try to achieve the highest score possible!\n")
    time.sleep(1)

def monster_ascii():
    """Return an ASCII art monster."""
    monsters = [
        r"""
    /\___/\
   (  o o  )
   /   ^   \
  / \  _  / \
 /   \ - /   \
    ^  ~  ^
        """,
        r"""
     _____
    /     \
   /       \
  |  ^   ^  |
  |  (o) (o) |
  |    <    |
   \  ~~~  /
    \_____/
        """,
        r"""
      _,_
    ,'.-.`
   /    \ \
  /  /`   `-
 (__/       \
  /   \  /\  \
 /     \/  \  \
     """]
    return random.choice(monsters)

def treasure_ascii():
    """Return an ASCII art treasure chest."""
    treasures = [
        r"""
    _______
   |.-----.|
   ||     ||
   ||_____||
   |_______|
        """,
        r"""
    .--------.
   /          \
  |    ____    |
  |   /    \   |
   \  \____/  /
    '--------'
        """,
        r"""
     ______
    /      \
   /  [][]  \
  |  [][]   |
   \________/
        """]
    return random.choice(monsters)

def choose_character():
    """Let the player select their character class."""
    print("\n" + "=" * 50)
    print("Choose your character:".center(50))
    print("=" * 50)
    print("\n1. Warrior - Strong fighter with high health")
    print("2. Wizard - Magical character with special abilities")
    print("3. Rogue - Stealthy character with high critical hit chance")
    
    while True:
        choice = input("\nEnter the number of your character (1/2/3): ")
        if choice in ['1', '2', '3']:
            characters = {
                '1': {"name": "Warrior", "health": 100, "attack": 15, "gold": 50, "potions": 2},
                '2': {"name": "Wizard", "health": 70, "attack": 20, "gold": 50, "potions": 2},
                '3': {"name": "Rogue", "health": 80, "attack": 12, "gold": 50, "potions": 2}
            }
            return characters[choice]
        print("Invalid choice. Please try again.")

def shop(player):
    """Implement a shop where player can buy upgrades."""
    while True:
        print("\n" + "=" * 30)
        print("SHOP".center(30))
        print("=" * 30)
        print(f"\nYour Gold: {player['gold']}")
        print("1. Health Potion (Restores 30 HP) - 30 Gold")
        print("2. Attack Upgrade (+5 Damage) - 50 Gold")
        print("3. Exit Shop")
        
        choice = input("\nChoose an option (1/2/3): ")
        
        if choice == '1' and player['gold'] >= 30:
            player['gold'] -= 30
            player['potions'] += 1
            print("You bought a Health Potion!")
        elif choice == '2' and player['gold'] >= 50:
            player['gold'] -= 50
            player['attack'] += 5
            print("You upgraded your attack!")
        elif choice == '3':
            break
        else:
            print("Not enough gold or invalid choice!")

def explore_dungeon(player):
    """Manage the player's dungeon exploration."""
    score = 0
    
    while player["health"] > 0:
        print("\n" + "=" * 50)
        print(f"{player['name']} Stats:".center(50))
        print("=" * 50)
        print(f"Health: {player['health']} | Score: {score} | Gold: {player['gold']}")
        print("\n" + "-" * 50)
        print("Choose your action:".center(50))
        print("-" * 50)
        print("\n(E)xplore the dungeon")
        print("(S)hop for items")
        print("(U)se Health Potion")
        print("(Q)uit the adventure")
        print("\n" + "-" * 50)
        
        action = input("\nWhat would you like to do? ").lower()
        
        if action == 'e':
            encounter = random.choices(
                ["monster", "treasure", "trap"], 
                weights=[0.5, 0.1, 0.4]
            )[0]
            
            if encounter == "monster":
                print("\n" + monster_ascii())
                print("\nA fierce monster appears!")
                monster_result = monster_fight(player)
                if monster_result:
                    score += 10
                    player['gold'] += random.randint(5, 15)
            elif encounter == "treasure":
                print("\n" + treasure_ascii())
                treasure = handle_treasure(player)
                if treasure:
                    score += 20
                    player['gold'] += treasure * 10
            else:
                handle_trap(player)
        
        elif action == 's':
            shop(player)
        
        elif action == 'u':
            if player['potions'] > 0:
                heal_amount = 30
                player['health'] = min(player['health'] + heal_amount, 100)
                player['potions'] -= 1
                print(f"You used a potion and restored {heal_amount} HP!")
            else:
                print("No potions available!")
        
        elif action == 'q':
            break
        
        # Small pause to make reading easier
        time.sleep(1)
    
    return score

def monster_fight(player):
    """Simulate a monster encounter."""
    monster_health = random.randint(20, 40)
    
    while monster_health > 0 and player["health"] > 0:
        print(f"\nMonster Health: {monster_health}")
        action = input("Do you want to (A)ttack or (D)efend? ").lower()
        
        if action == 'a':
            damage = random.randint(5, player["attack"])
            monster_health -= damage
            print(f"You deal {damage} damage to the monster!")
            
            if monster_health > 0:
                player_damage = random.randint(3, 10)
                player["health"] -= player_damage
                print(f"The monster hits you for {player_damage} damage!")
        elif action == 'd':
            player_damage = random.randint(1, 5)
            player["health"] -= player_damage
            print(f"You defend and take {player_damage} damage!")
        else:
            print("Invalid action. You lose your turn!")
    
    return monster_health <= 0

def handle_treasure(player):
    """Handle rare treasure discovery."""
    if random.random() < 0.2:  # 20% chance of finding treasure
        treasure_value = random.randint(1, 3)
        print(f"You found {treasure_value} rare treasure!")
        return treasure_value
    print("No treasure found...")
    return 0

def handle_trap(player):
    """Handle trap encounters."""
    trap_damage = random.randint(5, 15)
    player["health"] -= trap_damage
    print(f"You've triggered a trap! You take {trap_damage} damage!")

def main():
    """Main game function to control game flow."""
    introduction()
    player = choose_character()
    
    print(f"\nYou, the {player['name']}, enter the endless dungeon...")
    time.sleep(1)
    
    final_score = explore_dungeon(player)
    
    print("\n" + "=" * 50)
    print("GAME OVER".center(50))
    print("=" * 50)
    print(f"\nYour final score is: {final_score}")
    print(f"You survived as far as you could, brave {player['name']}!")

# This ensures the game only runs if this script is directly executed
if __name__ == "__main__":
    main()

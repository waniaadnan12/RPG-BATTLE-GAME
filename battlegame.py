import random


player = {
  "name": "hero",
  "health": 100,
  "attack": 20
}
enemy = {
  "name": "goblin",
  "health": 80,
  "attack": 15
  }
def show_stats():
  print()
  print("STATS")
  print(f"{player["name"]} HP: {player["health"]}")
  print(f"{enemy["name"]}, HP: {enemy["health"]}")

def calculate_damage(attack):
  return random.randint(attack - 5, attack + 5)

def player_attack(enemy):
  damage = calculate_damage(player["attack"])
  enemy["health"] -= damage
  print()
  print(f"{player["name"]} attacks{enemy["name"]}!")
  print(f"{damage} damage dealt!")
  if enemy["health"] < 0:
    enemy["health"] = 0

  print(f"{enemy["name"]} HP: {enemy["health"]}")

def enemy_attack(player):
  damage = calculate_damage(enemy["attack"])
  player["health"] -= damage
  print()
  print(f"{enemy["name"]} attacks{player["name"]}!")
  print(f"{damage} damage dealt!")
  if player["health"] < 0:
    player["health"] = 0

  print(f"{player["name"]} HP: {player["health"]}")

def use_potion(player):
  old_health = player["health"]
  player["health"] = min(player["health"] +20, 100)
  recovered = player["health"] - old_health
  print()
  print (f"{player["name"]} used a potion!")
  print(f" +{recovered} HP")
  print(f"{player["name"]} HP: {player["health"]}")

def check_winner(player, enemy):
  if enemy["health"] <= 0:
      return "player"
  if player["health"] <= 0:
      return "enemy"
  return None

def battle(player, enemy):
  while True:
      show_stats()
      print()
      print("what do you want to do?")
      print("1. Attack")
      print("2. Potion")

      choice = input("choose 1 or 2: ")
      if choice == "1":
        player_attack(enemy)
      elif choice == "2":
        use_potion(player)
      else:
        print("Invalid Choice")
        continue
      winner = check_winner(player,enemy)
      if winner == "player":
        print()
        print("you won")
        break
      if winner == "enemy":
        print()
        print("you lost")
        break

      enemy_attack(player)
      winner = check_winner(player, enemy)
      if winner == "player":
        print()
        print("you won")
        break
      if winner == "enemy":
        print()
        print("you lost")
        break
def game():
  print("===========")
  print("RPG BATTLE GAME")
  print("===========")  
  print()
  print(f"you are{player["name"]}.")
  print(f"your enemy is{enemy["name"]}.")
  print("defeat the goblin")
  battle(player,enemy)

game()
  
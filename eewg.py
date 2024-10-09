import random

def attack(attacker, defender, attack_name):
    attacks = {
        "Punch": {"chance": 0.8, "damage": 10},
        "Kick": {"chance": 0.6, "damage": 20}
    }

    print(f"{attacker} tries to {attack_name} {defender}!")
    if random.random() < attacks[attack_name]["chance"]:
        damage = attacks[attack_name]["damage"]
        print(f"Hit! {defender} takes {damage} damage.")
        return damage
    else:
        print(f"Miss! {defender} blocked the attack.")
        return 0

def battle():
    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        print(f"\nYour health: {player_health} | Enemy health: {enemy_health}")
        
        # Player's turn
        print("\nChoose your attack:")
        print("1. Punch (80% hit chance, 10 damage)")
        print("2. Kick (60% hit chance, 20 damage)")
        
        choice = input("Enter 1 for Punch or 2 for Kick: ")
        if choice == "1":
            enemy_health -= attack("You", "Enemy", "Punch")
        else:
            enemy_health -= attack("You", "Enemy", "Kick")
        
        if enemy_health <= 0:
            print("\nYou win!")
            break
        
        # Enemy's turn
        enemy_attack = random.choice(["Punch", "Kick"])
        player_health -= attack("Enemy", "You", enemy_attack)
        
        if player_health <= 0:
            print("\nYou lose!")
            break

print("Welcome to the Simple Gladiator Game!")
battle()
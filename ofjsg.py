import random

def print_slow(text):
    print(text)

def attack(attacker, defender, attack_name, hit_chance, damage):
    print_slow(f"{attacker} attempts to {attack_name}...")
    if random.random() < hit_chance:
        print_slow(f"Hit! {defender} takes {damage} damage.")
        return damage
    else:
        print_slow(f"Miss! {defender} dodges the attack.")
        return 0

def player_turn(player_name, enemy_name):
    while True:
        choice = input("Choose your attack (1 for Punch, 2 for Kick): ")
        if choice in ['1', '2']:
            break
        print("Invalid choice. Please enter 1 or 2.")
    
    if choice == '1':
        return attack(player_name, enemy_name, "punch", 0.8, 10)
    else:
        return attack(player_name, enemy_name, "kick", 0.4, 20)

def enemy_turn(enemy_name, player_name):
    if random.random() < 0.4:
        return attack(enemy_name, player_name, "punch", 0.8, 10)
    else:
        return attack(enemy_name, player_name, "kick", 0.4, 20)

def game():
    print_slow("Welcome to the Gladiator Arena!")
    player_name = input("Enter your gladiator name: ")
    enemy_name = random.choice(["Maximus", "Spartacus", "Crixus", "Priscus"])
    
    print_slow(f"\nWelcome, {player_name}! You will be fighting against {enemy_name}.")
    print_slow("Both gladiators start with 100 health.")
    print_slow("Punch: 80% hit chance, 10 damage")
    print_slow("Kick: 40% hit chance, 20 damage")
    print_slow("\nLet the battle begin!")
    
    player_health = 100
    enemy_health = 100
    
    while player_health > 0 and enemy_health > 0:
        print_slow(f"\n{player_name}'s health: {player_health}")
        print_slow(f"{enemy_name}'s health: {enemy_health}")
        
        damage_dealt = player_turn(player_name, enemy_name)
        enemy_health -= damage_dealt
        
        if enemy_health <= 0:
            print_slow(f"\n{enemy_name} has fallen! {player_name} is victorious!")
            break
        
        if damage_dealt == 0:  # Om attack missar, motståndare får gratis attack
            print_slow(f"{enemy_name} seizes the opportunity!")
            damage_taken = enemy_turn(enemy_name, player_name)
            player_health -= damage_taken
        else:
            print_slow(f"\n{enemy_name} prepares to strike back!")
            damage_taken = enemy_turn(enemy_name, player_name)
            player_health -= damage_taken
        
        if player_health <= 0:
            print_slow(f"\n{player_name} has fallen! {enemy_name} is victorious!")
            break

    print_slow("\nThank you for playing!")

game()
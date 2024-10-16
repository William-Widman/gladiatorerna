# Importerar moduler
import random
import time

print("Välkommen till arenan, kämpe.\n\nMänniskor fyllda av blodtörstig förväntan sitter samlade på läktarna,\nderas röster ekar mellan stenmurarna. Solens strålar skär genom dammet\n som virvlar upp från sanden under dina fötter. Framför dig öppnar sig en värld\ndär endast de starkaste överlever, där ära och död är de enda utgångarna.\n\nI den här arenan är varje andetag en kamp för livet. Du står inför dina motståndare –\nlegendariska krigare som, liksom du, slåss för att skriva in sitt namn i historien.\nStålsvärd klingar mot sköldar, och marken dryper av svett och blod.\nBara de som har modet att möta sitt öde, kan lämna arenan med äran i behåll.\nDu är inte bara här för att slåss. Du är här för att vinna. För att överleva.\nFör att bli en legend.\nÄr du redo att ta steget in i historiens mest dödsbringande spel?\n\nLåt striden börja.")

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
def lasso_attempt(attacker, defender):
    print_slow(f"{attacker} tries to catch {defender} with a lasso...")
    if random.random() < 0.5:
        print_slow(f"{defender} is caught in the lasso and is stunned!")
        return True
    else:
        print_slow(f"{defender} dodges the lasso!")
        return False

def break_free(name):
    print_slow(f"{name} attempts to break free from the lasso...")
    if random.random() < 0.5:
        print_slow(f"{name} breaks free from the lasso!")
        return True
    else:
        print_slow(f"{name} is still trapped in the lasso!")
        return False


def player_turn(player_name, enemy_name, enemy_stunned):
    if enemy_stunned:
        print_slow(f"{enemy_name} is stunned and cannot dodge!")
        return attack(player_name, enemy_name, "enhanced punch", 0.9, 15)
    else:
        while True:
            choice = input("Choose your action (1 for Punch, 2 for Kick, 3 for Lasso): ")
            if choice in ['1', '2', '3']:
                break
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        if choice == '1':
            return attack(player_name, enemy_name, "punch", 0.8, 10), False
        elif choice == '2':
            return attack(player_name, enemy_name, "kick", 0.4, 20), False
        else:
            if lasso_attempt(player_name, enemy_name):
                return 0, True
            return 0, False

def enemy_turn(enemy_name, player_name):
    if random.random() < 0.4:
        return attack(enemy_name, player_name, "punch", 0.8, 10)
    else:
        return attack(enemy_name, player_name, "kick", 0.4, 20)

def game():
    print_slow("Welcome to the Gladiator Arena!")
    player_name = input("Enter your gladiator name: ")
    enemy_name = random.choice(["Maximus", "Acastus", "Crixus", "Priscus"])
    
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


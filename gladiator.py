# Importerar moduler
import random

print("Välkommen till arenan, kämpe.\n\nMänniskor fyllda av blodtörstig förväntan sitter samlade på läktarna,\nderas röster ekar mellan stenmurarna. Solens strålar skär genom dammet\n som virvlar upp från sanden under dina fötter. Framför dig öppnar sig en värld\ndär endast de starkaste överlever, där ära och död är de enda utgångarna.\n\nI den här arenan är varje andetag en kamp för livet. Du står inför dina motståndare –\nlegendariska krigare som, liksom du, slåss för att skriva in sitt namn i historien.\nStålsvärd klingar mot sköldar, och marken dryper av svett och blod.\nBara de som har modet att möta sitt öde, kan lämna arenan med äran i behåll.\nDu är inte bara här för att slåss. Du är här för att vinna. För att överleva.\nFör att bli en legend.\nÄr du redo att ta steget in i historiens mest dödsbringande spel?\n\nLåt striden börja.")



def attack(attacker, defender, attack_name, hit_chance, damage):
    print(f"{attacker} försöker att {attack_name}...")
    if random.random() < hit_chance:
        print(f"Träff! {defender} tar {damage} skada.")
        return (damage, attack_name, hit_chance * 100)
    else:
        print(f"Miss! {defender} undviker attacken.")
        return (0, attack_name, hit_chance *100)
    
def lasso_attempt(attacker, defender):
    print(f"{attacker} attempts to lasso {defender}...")
    if random.random() < 0.4:
        print(f"success! {defender} is caught in the lasso!")
        return True
    else:
        print(f"Miss! {defender} evades the lasso!")
        return False

def player_turn(player_name, enemy_name):
    while True:
        choice = input("Välj din attack (1 för Punch, 2 för Kick, 3 för sword attack): ")
        if choice in ['1', '2', '3']:
            break
        print("Ogiltigt svar. Vänligen ange 1, 2, 3")
    
    if choice == '1':
        return attack(player_name, enemy_name, "punch", 0.8, 10)
    elif choice == '2':
        return attack(player_name, enemy_name, "kick", 0.4, 20)
    else:
        return attack(player_name, enemy_name, "Sword attack", 0.5, 15)


def enemy_turn(enemy_name, player_name, difficulty):
    if random.random() < 0.4:
        if difficulty == "normal":
            return attack(enemy_name, player_name, "punch", 0.8, 10)
        else:
            return attack(enemy_name, player_name, "punch", 0.8, 15)
    elif random.random() <0.8:
        if difficulty == "normal":
            return attack(enemy_name, player_name, "kick", 0.4, 20)
        else:
            return attack(enemy_name, player_name, "kick", 0.4, 30)
    else:
        if difficulty == "normal":
            return attack(enemy_name, player_name, "Sword attack", 0.5, 15)
        else:
            return attack(enemy_name, player_name, "Sword attack", 0.5, 22)

def game():
    print("Välkommen till Gladiator Arenan!")
    player_name = input("Ange ditt gladiatornamn: ")
    difficulty = input("Välj svårighetsgrad (normal/svår): ")
    enemy_name = random.choice(["Maximus", "Acastus", "Crixus", "Priscus"])
    
    print(f"\nVälkommen, {player_name}! Du kommer att kämpa mot {enemy_name} på {difficulty} nivå.")
    print("Båda gladiatorerna startar med 100 liv.")
    print("Punch: 80% träffchans, 10 skada (svår: 15 skada)")
    print("Kick: 40% träffchans, 20 skada (svår: 30 skada)")
    print("Sword attack: 50% träffchans, 15 skada (svår: 22 skada)")
    print("\nLåt striden börja!")
    
    player_health = 100
    enemy_health = 100
    
    while player_health > 0 and enemy_health > 0:
        print(f"\n{player_name}'s health: {player_health}")
        print(f"{enemy_name}'s health: {enemy_health}")

        # Lista för att hålla reda på attackerna (återställs varje runda)
        attack_history = []
        
        damage_dealt, attack_name, hit_chance = player_turn(player_name, enemy_name)
        enemy_health -= damage_dealt
        attack_history.append(f"{player_name} använde {attack_name}, träffchans: {hit_chance}%, skada: {damage_dealt}")
        
        if enemy_health <= 0:
            print(f"\n{enemy_name} har fallit! {player_name} är segrare!")
            break
        
        if damage_dealt == 0:  # Om attack missar, motståndare får gratis attack
            print(f"{enemy_name} tar tillfället i akt!")
            damage_taken, attack_name, hit_chance = enemy_turn(enemy_name, player_name, difficulty)
            player_health -= damage_taken
            attack_history.append(f"{enemy_name} använde {attack_name}, Träffchans: {hit_chance}%, Skada: {damage_taken}")
        else:
            print(f"\n{enemy_name} förbereder sig på att slå tillbaka!")
            damage_taken, attack_name, hit_chance = enemy_turn(enemy_name, player_name, difficulty)
            player_health -= damage_taken
            attack_history.append(f"{enemy_name} använde {attack_name}, Träffchans: {hit_chance}%, Skada: {damage_taken}")
        
        if player_health <= 0:
            print(f"\n{player_name} har fallit! {enemy_name} är segrare!")
            break

        print("\nAttackhistorik denna runda:")
        for attack in attack_history:
            print(attack)

    print("Tack för att du spelar!")

game()


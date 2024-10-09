import random

class Gladiator:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class Attack:
    def __init__(self, name, hit_chance, damage):
        self.name = name
        self.hit_chance = hit_chance
        self.damage = damage

def perform_attack(attacker, defender, attack):
    print(f"{attacker.name} attempts to {attack.name} {defender.name}!")
    if random.random() < attack.hit_chance:
        defender.take_damage(attack.damage)
        print(f"Hit! {defender.name} takes {attack.damage} damage.")
    else:
        print(f"Miss! {defender.name} blocked the attack.")

def battle(player, opponent):
    attacks = [
        Attack("Punch", 0.8, 10),
        Attack("Kick", 0.6, 20),
        Attack("Power Strike", 0.4, 30)
    ]

    while player.health > 0 and opponent.health > 0:
        print(f"\n{player.name}: {player.health} HP | {opponent.name}: {opponent.health} HP")
        
        print("\nChoose your attack:")
        for i, attack in enumerate(attacks, 1):
            print(f"{i}. {attack.name} (Hit Chance: {attack.hit_chance*100}%, Damage: {attack.damage})")
        
        choice = int(input("Enter the number of your chosen attack: ")) - 1
        chosen_attack = attacks[choice]
        
        perform_attack(player, opponent, chosen_attack)
        
        if opponent.health > 0:
            opponent_attack = random.choice(attacks)
            perform_attack(opponent, player, opponent_attack)
    
    if player.health > 0:
        print(f"\n{player.name} wins!")
    else:
        print(f"\n{opponent.name} wins!")

# Start the game
player_name = input("Enter your gladiator's name: ")
player = Gladiator(player_name, 100)
opponent = Gladiator("Enemy Gladiator", 100)

print(f"\nWelcome to the arena, {player.name}!")
print(f"You'll be fighting against {opponent.name}.")
print("Let the battle begin!")

battle(player, opponent)
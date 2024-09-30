import random

print("test")

# Initialize fighter names and health points (hp)
fighter_a = {"name": "Fighter A", "hp": 100}
fighter_b = {"name": "Fighter B", "hp": 100}

# Initialize player's money
player_money = 100

# Ask player which fighter they want to bet on
print(f"You have {player_money} money.")
bet_on = input("Which fighter do you want to bet on? (A/B): ").upper()

# Ask player how much they want to bet
bet_amount = int(input("How much do you want to bet?: "))

# Check if the player has enough money to place the bet
if bet_amount > player_money:
    print("You don't have enough money to place that bet!")
    exit()

# Fight loop
while fighter_a["hp"] > 0 and fighter_b["hp"] > 0:
    # Each fighter attacks the other, reducing their hp by a random value between 1 and 20
    damage_to_b = random.randint(1, 20)
    damage_to_a = random.randint(1, 20)
    
    fighter_b["hp"] -= damage_to_b
    fighter_a["hp"] -= damage_to_a

    print(f"{fighter_a['name']} hits {fighter_b['name']} for {damage_to_b} damage. {fighter_b['name']} HP: {fighter_b['hp']}")
    print(f"{fighter_b['name']} hits {fighter_a['name']} for {damage_to_a} damage. {fighter_a['name']} HP: {fighter_a['hp']}")
    print("----------")

# Determine winner or if it's a draw
if fighter_a["hp"] <= 0 and fighter_b["hp"] <= 0:
    print("It's a draw! Both fighters are knocked out.")
    winner = None
elif fighter_a["hp"] <= 0:
    print(f"{fighter_b['name']} wins!")
    winner = "B"
elif fighter_b["hp"] <= 0:
    print(f"{fighter_a['name']} wins!")
    winner = "A"

# Determine if the player won or lost the bet
if winner == bet_on:
    player_money += bet_amount  # Player wins the bet and doubles their money
    print(f"Congratulations! You won the bet. You now have {player_money} money.")
elif winner is None:
    print("It's a draw! You get your money back.")
else:
    player_money -= bet_amount  # Player loses the bet
    print(f"Sorry, you lost the bet. You now have {player_money} money.")

# Game over or restart logic
if player_money <= 0:
    print("You're out of money! Game over.")
else:
    print("Thanks for playing!")

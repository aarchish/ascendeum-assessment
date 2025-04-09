import random

print("Enter the grid size n:")
n = int(input())
last_grid_value = n*n

player1_pos_current = 0
player2_pos_current = 0
player3_pos_current = 0

player1_pos_history = []
player2_pos_history = []
player3_pos_history = []

player1_dice_history = []
player2_dice_history = []
player3_dice_history = []


while(player1_pos_current != last_grid_value or
      player2_pos_current != last_grid_value or
      player3_pos_current != last_grid_value):
    
    p1_dice = random.randrange(1,7,1)
    player1_dice_history.append(p1_dice)
    if(player1_pos_current + p1_dice <= last_grid_value): player1_pos_current += p1_dice
    player1_pos_history.append(player1_pos_current)
    if(player2_pos_current == player1_pos_current):
        player2_pos_current = 0
        player2_pos_history.append(player2_pos_current)
    if(player3_pos_current == player1_pos_current):
        player3_pos_current = 0
        player3_pos_history.append(player3_pos_current)
    if(player1_pos_current == last_grid_value): break

    p2_dice = random.randrange(1,7,1)
    player2_dice_history.append(p2_dice)
    if(player2_pos_current + p2_dice <= last_grid_value): player2_pos_current += p2_dice
    player2_pos_history.append(player2_pos_current)
    if(player1_pos_current == player2_pos_current):
        player1_pos_current = 0
        player1_pos_history.append(player1_pos_current)
    if(player3_pos_current == player2_pos_current):
        player3_pos_current = 0
        player3_pos_history.append(player3_pos_current)
    if(player2_pos_current == last_grid_value): break
    
    p3_dice = random.randrange(1,7,1)
    player3_dice_history.append(p3_dice)
    if(player3_pos_current + p3_dice <= last_grid_value): player3_pos_current += p3_dice
    player3_pos_history.append(player3_pos_current)
    if(player1_pos_current == player3_pos_current):
        player1_pos_current = 0
        player1_pos_history.append(player1_pos_current)
    if(player2_pos_current == player3_pos_current):
        player2_pos_current = 0
        player2_pos_history.append(player2_pos_current)
    if(player2_pos_current == last_grid_value): break


print("Player No: 1")
print("Dice Roll History: ", player1_dice_history)
print("Position History: ", player1_pos_history)
if(player1_pos_current == last_grid_value):
    print("Winner Status: Yes")

print("Player No: 2")
print("Dice Roll History: ", player2_dice_history)
print("Position History: ", player2_pos_history)
if(player2_pos_current == last_grid_value):
    print("Winner Status: Yes")


print("Player No: 3")
print("Dice Roll History: ", player3_dice_history)
print("Position History: ", player3_pos_history)
if(player3_pos_current == last_grid_value):
    print("Winner Status: Yes")

# 21 flag surviver game#
import random, sys, time


print("21 Flags game pits two groups  or two people against each other. Each group takes turns against other removing flags. Participants can removed 1,2 or 3 flags at a time but no more than 3. The group that take out the last flag looses. \n\n\n")


play = str(input("Enter 'yes' to play and 'exit' to quit the program. If you want to play against bot, type in bot for one of the users. ")).lower()
if play == 'yes':
    game = True
elif play == 'exit':
    sys.exit()

flag_number = 21
player_1 = str(input("Please choose username for the first player: ")).upper()
player_2 = str(input("Please choose username for the second player: ")).upper()
turn = 0

def bot():
    winning_strategy = flag_number % 4
    if winning_strategy == 0:
        winning_move = 3
    elif flag_number < 5:
        winning_move = flag_number - 1
    else:
        allowed_max_removed = [1,2,3]
        allowed_max_removed.remove(winning_strategy)
        winning_move = random.choice(allowed_max_removed)    
    return winning_move

def player_turn():
    global turn
    turn += 1
    if turn % 2 != 0:
        b = player_1
    else:
        b = player_2
    return b





    
print("Total number of flags : %s" % flag_number)
while game:
    a = player_turn()
    print("It's %s turn." % a)

    if a == "BOT":
        bot_move = bot()
        flag_removed = bot_move
        time.sleep(1)
        print("thinking...")
        time.sleep(1)
        print('still thinking.....')
        time.sleep(1)
        print("BOT removed %s of flags" % bot_move)
    
    else:
        flag_removed = int(input("Enter the number of flags you want to remove: "))
        
    while flag_removed > 3:
        print("You cannot remove more than 3 flags. It's still %s turn" % a)
        flag_removed = int(input("Enter the number of flags you want to remove: "))
        
    flag_number = flag_number - flag_removed
    print("Number of flag left = %s" % flag_number)
    print("-------------------------------------------------------------")
    if flag_number <= 0:
        print("%s removed the last flag. %s lost the game. " % (a,a))
        break


    
    
    
    

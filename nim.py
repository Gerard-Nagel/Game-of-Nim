import random


def computer_take(sb):
    """
    Takes current ball amount, converts it to an integer and subtracts a random number between
    1 and 4 if a multiple of five and takes away the remainder if not a multiple of 5. Then it converts it back
    to a list by popping and appending.
    :param sb: a list of the current amount of balls
    :return: sb
    """
    comtake = random.randint(1, 4)  # creates a random variable between 1 and 4
    listtoint = int(sb[0])                # converts list to integer
    comtake2 = listtoint % 5              # takes the value of the remainder of balls divided by 5
    if listtoint % 5 > 0:
        sb.pop(0)
        newlistint = listtoint - comtake2
        sb.append(newlistint)
        return sb
    if listtoint % 5 == 0:
        sb.pop(0)
        newlistint = listtoint - comtake
        sb.append(newlistint)
        return sb


def take_balls(sb, t):
    """
    converts sb into an integer, subtracts how many balls the player chose to take, and then converts it back to
    list by popping and appending.
    :param sb: a list of the current amount of balls
    :param t: The number of balls the player wants to take
    :return: sb
    """
    if t == 1:
        listtoint = int(sb[0])      # converts the list into an integer
        sb.pop(0)                   # removes the first item in the list
        newlistint = listtoint - t  # subtracts player choice from integer
        sb.append(newlistint)       # adds new ball amount as the first item of the list
        return sb
    if t == 2:
        listtoint = int(sb[0])
        sb.pop(0)
        newlistint = listtoint - t
        sb.append(newlistint)
        return sb
    if t == 3:
        listtoint = int(sb[0])
        sb.pop(0)
        newlistint = listtoint - t
        sb.append(newlistint)
        return sb
    if t == 4:
        listtoint = int(sb[0])
        sb.pop(0)
        newlistint = listtoint - t
        sb.append(newlistint)
        return sb


def nim():
    """
    this is where the logic for the game resides and the print statements. With many while loops, the game is
    able to keep going until someone wins and the right inputs are entered.
    :return: none
    """
    name = input("Hello! what is your name?")
    print("Nice to meet you " + name + "!")
    y_n = input("Would you like to play the game of Nim with me?")
    ball_list = [1]

    if y_n == "yes":
        game = True
    else:
        game = False
        print("Oh okay then.")
    while game == True:   # allows game to close if the players says no
        starting_balls_int = 0
        while starting_balls_int < 15:
            possible_starting_balls = input("How many balls do you want to start with? 15 or more only ")
            starting_balls_int = int(possible_starting_balls)
            if starting_balls_int >= 15:
                ball_list = [1 * starting_balls_int]    # creates a list
                print(ball_list)
                print("The game starts with", starting_balls_int, "balls.")
        game2 = True
        while game2 is True:     # this prevents the game from restarting on its own
            player_turn = True
            if game == False:
                exit()
            while player_turn:
                take_int = 0
                while take_int < 1 or take_int > 4:
                    take = input("How many balls do you want to take? 1-4")
                    take_int = int(take)
                new_balls = take_balls(ball_list, take_int)
                print("Balls after your turn")
                print(ball_list)
                player_turn = False
            if ball_list == [0]:
                print(name + " wins!")
                game = False
                break
            while not player_turn:
                com_list = computer_take(ball_list)
                print("Balls after computers turn")
                print(com_list)
                player_turn = True
                if ball_list == [0]:
                    print("Computer wins!")
                    game = False


def main():
    """
    Calls the nim function
    :return: none
    """
    nim()


if __name__ == '__main__':    # only runs in this file and not when imported
    main()

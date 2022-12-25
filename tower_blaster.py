""" 

Name : Jannatul Ferdaus

Penn ID: 45739693

Statement of work:
- I received help from recitations, TA office hours, and coursera videos for the CIT 591 course

"""


import random

def print_instructions():
    """This function prints the instructions for the game for the user."""

    instructions = """    You will play tower blaster against the computer. The computer will
    play automatically while the program will ask you for input. You will be dealt 10 bricks in a 
    random order as will the computer. Think of the numbers as the width of the bricks. Your objective
    is to be the first player to arrange 10 bricks in your own tower from the lowest to the highest
    values from top to bottom. Otherwise the tower be unstable due to the 'wider' bricks (those with higher 
    values). Your initial bricks will be placed one on top of each other. 
    
    There will be 40 bricks remaining in the main pile after the first dealing. The top of the main pile
    is turned over to begin the discard pile. On each player's turn, the player may choose to pick
    up the top brick from the discard pile or to pick up the top brick from the main pile. The top brick 
    from the discard pile will be known to both you and the computer. However, the bricks in the main 
    pile will remain a mystery. You may choose to take a chance and choose the brick from the mystery pile
    if you do not like what is given to you in the discard pile. If you reject the mystery brick, it will
    go to the top of the discard pile.
    
    Once a brick is chosen by a player either from the discard pile or the main pile, the player will 
    decide where in the tower to put the brick. The tower is always 10 bricks high and therefore once you 
    replace a brick in your tower, the removed brick from the tower is put on top of the discard pile. If 
    the discard brick is chosen, it MUST be placed in your tower somewhere. The first player to get their
    tower to be in ascending order (top to bottom) wins. """

    # prints the instructions for the user
    print(instructions)

def setup_bricks():
    """Creates a list of numbers from 1 to 61 (61 not included) for the main pile. Discard pile is
    created as an empty list.The main pile and the discard pile is returned as a tuple."""

    # creates a list from 1 to 60 for the main pile
    main_pile = [i for i in range(1, 61)]

    # creates an empty discard list
    discard = []

    # returns main_pile and discard lists as a tuple
    return (main_pile, discard)


def shuffle_bricks(bricks):
    """Takes an input for a type of pile of bricks and shuffles them randomly """
    # Takes an input for a pile of bricks and shuffles the bricks randomly
    random.shuffle(bricks)


def deal_initial_bricks(main_pile):
    """Gets the top brick from the main pile and deals one brick after another alternating between the
    computer and human hand until both lists represented as towers reach the length of 10. Bricks are
    placed one on top of the other as they are dealt. The computer hand and the human hand are then
    returned as a tuple."""

    # Creates the two empty lists, one for the computer hand and one for the human hand
    computer_tower = []
    human_tower = []
    # while loop continues while length of the computer tower and the human tower is not 10
    while len(computer_tower) != 10 and len(human_tower) != 10:
        # the top brick of the main pile is stored in the variable removed_brick
        removed_brick = get_top_brick(main_pile)
        # the removed brick is then inserted at the topmost area of the computer tower (represented as a list)
        computer_tower.insert(0, removed_brick)
        # the top brick is received from the main pile
        removed_brick = get_top_brick(main_pile)
        # the top brick is inserted at the topmost area of the human tower.
        human_tower.insert(0, removed_brick)
    # the computer tower and the human tower is then returned as tuple
    return (computer_tower, human_tower)


def check_bricks(main_pile, discard):
    """ If the main pile has 0 bricks, the discard tower is shuffled and all the discard bricks are added
     to the main pile while all the bricks are removed from the discard pile and then the top brick from
     the main pile is added to the discard pile to start the discard pile again."""
    # checks if the length of the main pile is 0
    if len(main_pile) == 0:
        # randomly shuffles the discard pile
        random.shuffle(discard)
        # checks for each item in the discard pile
        for item in discard:
            # each item in the discard pile is added to the main pile
            main_pile.append(item)
        # for every item in the main pile, the item in the discard pile is removed.
        # this is to ensure that once the main pile is empty, all the bricks from the main pile
        # is given to the discard pile. And the discard pile is empty for now.
        for item in main_pile:
            discard.remove(item)
        # gets the top brick from the main pile
        top_brick = get_top_brick(main_pile)
        # adds the brick to the top of the discard pile
        add_brick_to_discard(top_brick, discard)

def check_tower_blaster(tower):
    """Checks if each successive item in the tower list is larger than the next item in order to see
    if the tower is in ascending order (top to bottom). If it is, it returns True, and otherwise returns
    False if it is not in ascending order."""
    # assigns a random number the value of -1 since every value to check in the tower will be positive
    num = -1
    # checks that each item in the tower is greater than num which starts as -1
    for item in tower:
        # checks if each item in the tower is greater than num
        if item > num:
            # each item in the tower is assigned the num variable if each item is greater than each
            # successive item.
            num = item
        else:
            # if any one of the items in the tower is not greater than the item before it, the
            # function returns False. Indicates tower is not in ascending order.
            return False
    # True is returned if each successive item in the tower is greater than the one before it
    return True


def get_top_brick(brick_pile):
    """Removes the first brick from the tower and returns its value."""
    # removes the topmost brick from the brick pile
    removed_brick = brick_pile.pop(0)
    # returns the brick that was removed
    return removed_brick


def add_brick_to_discard(brick, discard):
    """Inserts a brick to the beginning of the discard pile list."""
    # inserts the brick to the top of the discard pile
    discard.insert(0, brick)


def find_and_replace(new_brick, brick_to_be_replaced, tower, discard):
    """If the brick to be replaced is in the tower, the brick is removed from the tower and added to
    the top of the discard pile. The new brick replaces the old brick a the same location the old brick
    was in."""
    # checks if the brick to be replaced is in the tower
    if brick_to_be_replaced in tower:
        # gets the index of the brick to be replaced and stores it in the variable index
        index = tower.index(brick_to_be_replaced)
        # the tower removes the item based on its place in the tower based on index
        tower.pop(index)
        # the tower inserts the new brick to the same index the old brick was removed from
        tower.insert(index, new_brick)
        # the brick that was replaced is added to the top of the discard tower
        add_brick_to_discard(brick_to_be_replaced, discard)
        # True is returned if the brick was in the tower
        return True
    else:
        # if the brick is not in the tower, False is returned
        return False

def replaceable(discard, new_brick, tower,brick_pile):
    """Asks the user for a brick number that they would like to replace in their tower and if the
    brick is present in the tower, the brick's place is found in the tower and a new brick is put in its
    place. If the user inputs a brick that is not in the tower, the user is prompted that the brick
    is not present in their tower and it re-prompts the user for a brick he or she wants replaced.

    While the user does not input a valid brick number, the user keeps being re-prompted for a brick
    number. Once the user inputs a valid number, the user breaks out of the loop and the function
    tells the user what brick was replaced with what new brick. The user's current tower is then printed.
    """
    # asks the user for input of a brick they would like to replace as an int
    brick_to_be_replaced = int(input("Where do you want to place this brick? Type a brick number to replace in your tower: "))
    # stores the boolean value from the find_and_replace function in a variable called success
    success = find_and_replace(new_brick, brick_to_be_replaced, tower, discard)
    # as long as the find and replace function returns false, the brick is not in the tower is printed
    # the user is re-prompted for a brick number that is actually in the tower
    while success == False:
        print("Brick not in tower.")
        # asks the user for the brick number they'd like replaced and stores it in a variable.
        brick_to_be_replaced = int(input("Please input brick number you'd like replaced: "))
        # stores the boolean value in the variable success again
        success = find_and_replace(new_brick, brick_to_be_replaced, tower, discard)
    # prints what brick the old brick was replaced with and re-prints your tower.
    print("You replaced", brick_to_be_replaced, "with", new_brick)
    print("Your Tower Now:", tower)


def ask_yes_or_no(prompt):
    '''Prints the given prompt as a question to the user."

    - If the user inputs a string which has a first character that is 'y' or 'Y', the function
     returns True.
    - If the user inputs a string which has a first character that is 'n' or 'N', the function
    returns False.
    - Any other response has the question be repeated until the user provides a response that is acceptable.
    '''

    # TODO Insert your code here
    # stores a boolean value into the variable ask_again
    ask_again = True
    # continues the loop as long as ask_again is True
    while (ask_again):
        # takes an input from the user based on a prompt, and stores it in a variable
        user_input = input(prompt)
        # if the stored variable starts with either y/Y, True is returned
        if (user_input.startswith('y') or user_input.startswith('Y')):
            return True
        # if the stores variable starts with either an n/N, False is returned
        elif (user_input.startswith('n') or user_input.startswith('N')):
            return False
        # ask_again is stored as True
        else:
            ask_again = True


def human_player(human_tower, discard, main_pile):
    """Prints the user's tower and tells the user what is at the top of the discard pile. Prompts the user
    to enter 'D' or 'd' for discard or 'm' or 'M' for mystery brick. As long as the response is invalid
    (where the user enters anything besides the letters 'd' or 'm'), the user is re-prompted which
    pile they choose.

    If the response is valid and the response is the letter 'd', the brick on top of
    the discard pile is taken and replaces the brick in the tower the user wants to replace. If the user
    responds with 'm' or 'M', the top brick from the main pile is taken and the user is asked whether
    they want to use the brick. If the user responds with a string that starts with y/Y, the user is
    prompted which brick they would like to replace in their tower and it is replaced as long as it is in
    the tower. If the user responds with a string that starts with a n/N to using the mystery brick, the brick from
    the mystery pile is put into the discard pile. The user's turn to change a brick in the tower is skipped.

    At the end, the human's tower is returned.
     """
    print("\nNOW IT's YOUR TURN!")
    # human tower is printed
    print("This is your tower:", human_tower)
    # the top of the discard pile is printed
    print("The top brick on the discard pile is:", discard[0])
    # invalid_response variable is set as True
    invalid_response = True
    # while there is an invalid response, the while loop continues
    
    while invalid_response:
        # user is continuously asked for 'D'/'d' (to take from discard) or 'M'/'m' (to take from main pile) as prompt
        response = input("Type 'D' to take the discard brick or 'M' for a mystery brick:\n")
        # if the response is one of the appropriate inputs, invalid_response is set to False
        # the while loop discontinues
        if response == 'D' or response == 'd' or response == 'm' or response == 'M':
            invalid_response = False
        else:
            # invalid_response is set to True as long as the response is not the desired choice (letters 'd'/'m')
            invalid_response = True   
    # checks if response is either 'd' or 'D'
    if response == 'D' or response == 'd':
        # gets the top brick of the discard pile and stores it in a variable new_brick
        new_brick = get_top_brick(discard)
        # calls the replaceable function to replace old brick in tower with discard brick
        replaceable(discard, new_brick, human_tower,discard)
    # checks if the response is 'm'/'M'
    elif response == 'M' or response == 'm':
        # gets the top brick from the main pile if response is letter m
        new_brick = get_top_brick(main_pile)
        # prints out what the new brick is that was picked from the main pile
        print("You picked", new_brick, "from the main pile.")
        # prompts if the user would like to use this brick. prompts for a 'y' or 'Y'/ 'n' or 'N' to skip turn
        prompt = "Do you want to use this brick? Type 'Y' or 'y' if you do. Type 'N' or 'n' to skip turn.\n"
        # stores the ask yes or no function returning a boolean value in the response variable
        response = ask_yes_or_no(prompt)
        # if the response is returned True, the top brick from main pile is replaced with a new brick
        if response:
            replaceable(discard, new_brick, human_tower,main_pile)
        # brick is added to the discard pile if the response is not returned True (user inputs string starting with n)
        else:
            add_brick_to_discard(new_brick, discard)
            print("Okay, we will skip your turn for now.")
    # the human tower is returned
    return human_tower

def computer_main_pile_pickup(main_pile, computer_tower, discard):
    """ This function allows the computer to get the top brick from the main pile and check if it
    is reasonable to put it into its tower and replace on of its own bricks. If the top main brick
    is within a specific range or between two numbers, the brick replaces a brick in the computer's tower.
    If it is not within that range, the computer places the top main brick at the top of the discard pile. """
    
    # the top brick from the main pile is stored in a top_main_brick
    top_main_brick = get_top_brick(main_pile)
    # prints the computer is checking top of main pile
    print("The computer is checking the top main pile brick...")
    # checks if the top main brick has a value smaller than or equal to 5
    
    if top_main_brick <= 5:
        # if top main brick is smaller than the first value in the computer tower, finds the brick
        # replaces the brick with the top main pile brick
        if top_main_brick < computer_tower[0]:
            find_and_replace(top_main_brick, computer_tower[0], computer_tower, main_pile)
            print("Computer replaced a brick")
        # if the top main pile brick is not smaller than the top computer brick tower, the brick is added to the discard pile
        else:
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is greater than or equal to 55
    elif top_main_brick >= 55:
        # checks if the top main pile brick is greater than the computer tower's last brick value
        if top_main_brick > computer_tower[9]:
            # finds and replaces the last computer's last value with the top main pile brick
            find_and_replace(top_main_brick, computer_tower[9], computer_tower, main_pile)
            print("Computer replaced a brick")
        else:
            # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 15
    elif top_main_brick <= 15:
        # checks if the top main pile brick is greater than computer tower's top brick value or less than computer tower's third value
        if top_main_brick > computer_tower[0] or top_main_brick < computer_tower[2]:
            # if it fits the range, the computer tower's second brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[1], computer_tower, main_pile)
            print("Computer replaced a brick")
        else:
            # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 20
    elif top_main_brick <= 20:
        # checks if the top main pile brick is greater than computer tower's second brick value or less than computer tower's 4th value
        if top_main_brick > computer_tower[1] or top_main_brick < computer_tower[3]:
            # if it fits the range, the computer tower's third brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[2], computer_tower, main_pile)
            print("Computer replaced a brick")
        # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
        else:
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 25
    elif top_main_brick <= 25:
        # checks if the top main pile brick is greater than computer tower's third brick value or less than computer tower's fifth value
        if top_main_brick > computer_tower[2] or top_main_brick < computer_tower[4]:
            # if it fits the range, the computer tower's 4th brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[3], computer_tower, main_pile)
            print("Computer replaced a brick")
        # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
        else:
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 30
    elif top_main_brick <= 30:
        # checks if the top main pile brick is greater than computer tower's fourth value or less than computer tower's sixth value
        if top_main_brick > computer_tower[3] or top_main_brick < computer_tower[5]:
            # if it fits the range, the computer tower's 5th brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[4], computer_tower, main_pile)
            print("Computer replaced a brick")
        # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
        else:
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 35
    elif top_main_brick <= 35:
        # checks if the top main pile brick is greater than computer tower's fourth brick value or less than computer tower's 7th value
        if top_main_brick > computer_tower[4] or top_main_brick < computer_tower[6]:
            # if it fits the range, the computer tower's 6th brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[5], computer_tower, main_pile)
            print("Computer replaced a brick")
        # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
        else:
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 40
    elif top_main_brick <= 40:
        # checks if the top main pile brick is greater than computer tower's 6th brick value or less than computer tower's 7th value
        if top_main_brick > computer_tower[5] or top_main_brick < computer_tower[7]:
            # if it fits the range, the computer tower's 7th brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[6], computer_tower, main_pile)
            print("Computer replaced a brick")
        # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
        else:
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 45
    elif top_main_brick <= 45:
        # checks if the top main pile brick is greater than computer tower's 7th brick value or less than computer tower's 9th value
        if top_main_brick > computer_tower[6] or top_main_brick < computer_tower[8]:
            # if it fits the range, the computer tower's 8th brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[7], computer_tower, main_pile)
            print("Computer replaced a brick")
        else:
            # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
            add_brick_to_discard(top_main_brick, discard)
    # checks if the top main brick is less than or equal to 55
    elif top_main_brick <= 55:
        # checks if the top main pile brick is greater than computer tower's 8th brick value or less than computer tower's 10th value
        if top_main_brick > computer_tower[7] or top_main_brick < computer_tower[9]:
            # if it fits the range, the computer tower's 9th brick is replaced by the top main brick
            find_and_replace(top_main_brick, computer_tower[8], computer_tower, main_pile)
            print("Computer replaced a brick")
            # adds the top main brick to the top of the discard pile if the brick doesn't fit conditions
        else:
            add_brick_to_discard(top_main_brick, discard)

def get_top_discard_brick(discard):
    """ This function gets the top of the discard brick and prints what the computer picked up and
     that they replaced a brick. The top discard brick is then returned."""
    
    # gets the top discard brick
    top_discard_brick = get_top_brick(discard)
    # prints what brick the computer picked up from discard pile
    print("Computer picked", top_discard_brick, "from the discard pile.")
    print("Computer replaced a brick.")
    # returns the top discard brick
    return top_discard_brick

def computer_play(computer_tower,discard,main_pile):
    """ This function checks to see if the top discard brick fits a specific range of values. If it
    does, it replaces a brick from the computer's tower with the top discard brick. If not, it tries
    to see if the top main pile brick is more acceptable instead. In the end, the computer's tower
    is returned."""
    
    print("\nCOMPUTER'S TURN")
    # checks if the top discard brick has a value smaller than or equal to 5
    if discard[0] <=5:
        # checks if top discard brick is less than first brick for the computer tower.
        if discard[0] < computer_tower[0]:
            # gets the top discard brick
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top computer tower brick with the top discard brick if conditions are valid
            find_and_replace(top_discard_brick, computer_tower[0], computer_tower, discard)
        else:
            # if the conditions are not met for the discard top brick, the computer main pile pickup occurs
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks if the top discard brick is greater than or equal to 55
    elif discard[0] >=55:
        # checks if the top discard brick is greater than the last computer brick
        if discard[0] > computer_tower[9]:
            # top discard brick is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the last computer brick with a top discard brick
            find_and_replace(top_discard_brick, computer_tower[9], computer_tower, discard)
        else:
            # if the conditions for the discard brick are not acceptable, the computer main pile pickup function is called
            # checks to see if the main top brick is now acceptable
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 15
    elif discard[0] <= 15:
        # checks if the top discard brick is greater than the top computer tower brick
        # checks if discard brick is less than the third computer tower brick
        if discard[0] > computer_tower[0] or discard[0]<computer_tower[2]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the second computer tower brick
            find_and_replace(top_discard_brick, computer_tower[1], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 20
    elif discard[0] <= 20:
        # checks if the top discard brick is greater than the 2nd computer tower brick
        # checks if discard brick is less than the 4th computer tower brick
        if discard[0] > computer_tower[1] or discard[0] < computer_tower[3]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the 3rd discard brick with the third computer tower brick
            find_and_replace(top_discard_brick, computer_tower[2], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 25
    elif discard[0] <= 25:
        # checks if the top discard brick is greater than the third computer tower brick
        # checks if discard brick is less than the 5th computer tower brick
        if discard[0] > computer_tower[2] or discard[0] < computer_tower[4]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the 4th computer tower brick
            find_and_replace(top_discard_brick, computer_tower[3], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 30
    elif discard[0] <= 30:
        # checks if the top discard brick is greater than the 4th computer tower brick
        # checks if discard brick is less than the 6th computer tower brick
        if discard[0] > computer_tower[3] or discard[0] < computer_tower[5]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the 5th computer tower brick
            find_and_replace(top_discard_brick, computer_tower[4], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 35
    elif discard[0] <= 35:
        # checks if the top discard brick is greater than the 5th computer tower brick
        # checks if discard brick is less than the 7th computer tower brick
        if discard[0] > computer_tower[4] or discard[0] < computer_tower[6]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the 6th computer tower brick
            find_and_replace(top_discard_brick, computer_tower[5], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 40
    elif discard[0] <= 40:
        # checks if the top discard brick is greater than the 6th computer tower brick
        # checks if discard brick is less than the 8th computer tower brick
        if discard[0] > computer_tower[5] or discard[0] < computer_tower[7]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the 7th computer tower brick
            find_and_replace(top_discard_brick, computer_tower[6], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # checks to see if the top discard brick is less than or equal to 45
    elif discard[0] <= 45:
        # checks if the top discard brick is greater than the 7th computer tower brick
        # checks if discard brick is less than the 9th computer tower brick
        if discard[0] > computer_tower[6] or discard[0] < computer_tower[8]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the 8th computer tower brick
            find_and_replace(top_discard_brick, computer_tower[7], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    # # checks to see if the top discard brick is less than or equal to 55
    elif discard[0] <= 55:
        # checks if the top discard brick is greater than the 8th computer tower brick
        # checks if discard brick is less than the 10th computer tower brick
        if discard[0] > computer_tower[7] or discard[0] < computer_tower[9]:
            # gets the top discard brick and is stored in a variable
            top_discard_brick = get_top_discard_brick(discard)
            # finds and replaces the top discard brick with the 9th computer tower brick
            find_and_replace(top_discard_brick, computer_tower[8], computer_tower, discard)
        else:
            # if the discard brick conditions are not met, the computer main pile pickup function is called
            computer_main_pile_pickup(main_pile, computer_tower, discard)
    else:
        # if the discard brick conditions are not met, the computer main pile pickup function is called
        computer_main_pile_pickup(main_pile, computer_tower, discard)
    #computer's tower is returned
    return computer_tower

def game_over(computer_tower, human_tower):
    """" Checks if the game is over by calling the check_tower_blaster function for the computer tower
    and the human tower. If by calling that function the computer tower is said to be in ascending
    order from left to right, it is printed that the human lost and each player's tower is printed.
    The function then returns True.

    If the human tower is seen to be in ascending order instead, the function prints that the human won.
    Each player's towers are then printed. It is then returned True.

    If neither of the towers are in increasing order, the function returns False."""
    # calls the check_tower_blaster for the computer tower to see if the computer's tower is in ascending order
    if check_tower_blaster(computer_tower):
        # prints you lost
        print("\nOh no! you lost to the computer's tower!")
        # prints out the computer's final tower
        print("\nThe computer's final tower:",computer_tower)
        # prints out the human's final tower
        print("\nYour final tower:", human_tower)
        # function returns True
        return True
    # if the computer tower as an input does now allow the check_tower_blaster function to return True, checks human tower
    # checks if human tower is in ascending order (left to right)
    elif check_tower_blaster(human_tower):
        # prints you won
        print("\nCongratulations! You won!")
        # prints the human's final tower
        print("Your final tower:", human_tower)
        # prints the computer's final tower
        print("\nThe computer's final tower:", computer_tower)
        # function returns True
        return True
    # if neither the human tower or the computer returns True for ascending order , the function returns False
    else:
        return False


def main():
    # prints the instructions for the user
    print_instructions()
    # sets game_running to True
    game_running = True
    # asks if the user is ready to play and allows pressing of any key to start the game.
    input("\nReady to play? (Press any key)")
    # as long as game_running is set to True
    
    while game_running:
        # assigns main_pile its 60 bricks from the setup_bricks function
        # discard is set to an empty list from tuple
        main_pile,discard = setup_bricks()
        # the main pile is shuffled randomly
        shuffle_bricks(main_pile)
        # the computer tower is dealt 10 random bricks from the main pile as well as the human tower
        computer_tower,human_tower = deal_initial_bricks(main_pile)
        # prints computer tower
        print("\nThis is the computer tower:", computer_tower)
        # prints the human tower
        print("\nThis is the human tower:", human_tower)
        # gets the top brick from the main pile
        brick = get_top_brick(main_pile)
        # adds the top brick to the discard pile
        add_brick_to_discard(brick, discard)
        # sets same_game to True
        same_game = True
        # while same_game is set to true, the following functions are called
        
        while same_game:
            # computer_play returns the computer tower and computer_tower stores the tower
            computer_tower = computer_play(computer_tower,discard,main_pile)
            # the check_bricks function is called to see if the main pile is empty
            # discard pile's bricks are added if main pile is empty. top brick of discard comes from top of main pile.
            check_bricks(main_pile, discard)
            # checks if the game is over by checking if the computer tower or human tower is in ascending order
            if game_over(computer_tower,human_tower):
                # same_game is set to False
                same_game = False
                # ask_replay variable stores the question if the user would like to play again once game ends.
                ask_replay = "\nWould you like to play again? (y/n)"
                # if the function returns True by the user entering yes, the current game continues to run
                if ask_yes_or_no(ask_replay):
                    continue
                else:
                    # if the user enters a string starting with n, game_running is set to False
                    # Goodbye is printed to the user before exiting
                    print("Goodbye!")
                    game_running = False
                    # the loop is broken and the game ends
                    break
            
            # the human player function returns the human's tower after the human plays and chooses a brick
            human_tower = human_player(human_tower, discard, main_pile)
            # the check_bricks function is called to see if the main pile is empty
            # discard pile's bricks are added if main pile is empty. top brick of discard comes from top of main pile.
            check_bricks(main_pile, discard)
            # checks if the game is over by inputting the computer tower/human tower
            if game_over(computer_tower,human_tower):
                # sets the same game to False
                same_game = False
                # ask_replay variable stores the question if the user would like to play again once game ends.
                ask_replay = "\nWould you like to play again? (y/n)"
                # if the function returns True by the user entering yes, the current game ends
                # the outer while loop continues and the game starts over.
                if ask_yes_or_no(ask_replay):
                    continue
                else:
                    # if the user enters a string starting with n, game_running is set to False
                    # Goodbye is printed to the user before exiting
                    print("Goodbye!")
                    game_running = False
            # if the game is not over, the current game continues
            # the human and computer continue playing with their current towers
            else:
                continue

if __name__ == "__main__":
    main()

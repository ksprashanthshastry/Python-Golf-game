from random import randint


# function used for input and to validate username
def get_username():
    username = input("Please enter your name: \n").upper()
    while not username.isalpha():
        print("Your username should contain only alphabets. Please try again :(")
        username = input("Please enter your name again:").upper()
    print("Welcome to Golf game, PYTHON STYLE!,", username,)
    return username


# function used to validate par and distance value
def get_number(prompt, minimum, maximum):
    value = input(prompt)
    while not value.isdigit() or int(value) < minimum or int(value) > maximum:
        print("Number entered is invalid. Please try again :( \nNumber has to be between", minimum, "and", maximum)
        value = input(prompt)
    return int(value)


# function used to validate menu and club options
def get_option(prompt, options):
    choice = input(prompt).upper()
    while choice not in options:
        print("Invalid selection, Please try again :( \nPlease choose one among ", options)
        choice = input(prompt).upper()
    return choice.upper()


# function used for receiving club option as an argument from another function and to return
# random output for club chosen
def calculate_club_random(club, distance):
    if club == "D":
        random = randint(80, 120)
    elif club == "I":
        random = randint(24, 36)
    else:
        if distance > 1 or distance < 10:
            random = randint(int(80/100 * distance), int(120/100 * distance))
        else:
            random = randint(8, 12)
    return random


# function used for displaying results
def get_results(count, par_value):
    if count > par_value:
        par_calc = count - par_value
        print("You have completed the round", abs(par_calc), " above par. Better luck next time :)\n ")
    elif count == par_value:
        print("Yippee!! You have completed the round on par.\n ")
    else:
        par_calc = par_value - count
        print("Hurray !! \nYou have completed the round", abs(par_calc), " below par,  Congratulations!! :)\n ")


# function used to define the play option and to loop the game until the distance is 0
def game_play(remaining_distance_value, par_value, club_list):
    count = 0
    print("This hole is", remaining_distance_value, "m distance and par", par_value, "game.\n ")
    # loops until distance is 0
    while remaining_distance_value != 0:
        print("You are", remaining_distance_value, "m away from the hole, after", count,
              "shot/s.\nClub selection: press D for driver, I for Iron, P for Putter.")
        club = get_option("Please select your club: ", club_list).upper()
        shot_length = calculate_club_random(club, remaining_distance_value)
        print("\nYour shot went", shot_length, "meters.")
        remaining_distance_value = abs(remaining_distance_value - shot_length)
        count = count + 1
    print("You have finished this round in", count, "shots.")
    get_results(count, par_value)


def main():

    name = get_username()
    # constants are used as the values they contain do not change
    PAR_MIN = 3
    PAR_MAX = 5
    PAR_PROMPT = "Please enter par for this game (3-5): \n"
    DISTANCE_MIN = 195
    DISTANCE_MAX = 250
    DISTANCE_PROMPT = "Please enter distance you want to play this game for (195 - 250): \n"
    MENU_LIST = ["I", "P", "Q"]
    CLUB_LIST = ["D", "I", "P"]
    MENU_PROMPT = "(I)nstructions\n(p)lay\n(Q)uit\nPlease select one menu from the options:\n"

    par_value = get_number(PAR_PROMPT, PAR_MIN, PAR_MAX)
    distance_value = get_number(DISTANCE_PROMPT, DISTANCE_MIN, DISTANCE_MAX)
    menu_options = get_option(MENU_PROMPT, MENU_LIST)

    # indefinite loop used to keep the game running until user chooses to quit
    while menu_options != "Q":

        if menu_options == "I":
            print("INSTRUCTIONS: \nThis is a simple golf game in which each hole is", distance_value,
                  "meter away with ", par_value, "as par.\nYou can choose from 3 clubs, the Driver, Iron or Putter. \n"
                  "The Driver will hit around 100m, the Iron around 30m and the Putter around 10m.\n"
                  "The putter is best used very close to the hole.\n ")
            print("For each shot, you may use a driver, iron or a putter – each shot will vary in distance.\n"
                  "The average distance each club can hit is:\n(D)river = 100m\n(I)ron = 30m\n(P)utter = 10m\n ")
        else:
            game_play(distance_value, par_value, CLUB_LIST)
        menu_options = get_option("(I)nstructions\n(p)lay\n(Q)uit\nPlease select your menu options:\n",
                                  MENU_LIST).upper()

    print("Thank you for playing", name, ". Hope to see you soon. :)")


main()

# Python Prework Function HW

import numpy as np
import re
import secrets
import string
import time


def print_delay(content = '\n', delay = 0.02, **kwargs):
    """
    Module-level function for char-by-char printing of outputs. Accepts sep and
    end print methods as keyward args (default '' for both).
    """
    
    sep = ''
    end = ''
    
    for el in content:
        print(el, sep = sep, end = end, flush = True)
        time.sleep(delay)
    print()


###############################################################################
# Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input 
# of the function. 
###############################################################################

def hello_name(user_name = None):
    """Requests and processes user name in hypothetical account-creation scenario."""

    prompt = f"\nPlease enter a user name consisting of 5 to 25 letters and/or numbers (maximum 25 characters): "
    
    # Continue requesting input for desired user name until validated
    while True:
        user_name = input(prompt).strip()
        validated_user_name, validation_status = validate_username(user_name)

        if validation_status:
            success_output_message = (
                f"hello_{validated_user_name.upper()}!\n"
                f"(You may change your user name at any time in your profile settings.)"
            )
            print_delay(success_output_message)
            break


def validate_username(user_name):
    """Helper function to validate user's input"""

    validation_status = False
    invalid_inputs = [None, False, '']

    sys_msg_dict = {
        'error_msg': {
            'invalid_input': 'Valid input not detected.',
            'invalid_len': 'User names must be 5 to 25 letters/numbers.',
        },
        'system_action': {
            'available_names': 'The following user names are available: ',
            'random_suffix': 'Appending a random suffix to meet minimum length...',
            'truncating_input': 'Truncating user name to allowed max length...',
        },
    }

    print()

    # On invalid input, generate list of example user names
    if user_name in invalid_inputs:
        available_user_names = '\n '.join([generate_random_username() for _ in range(5)])
        validated_user_name = None

        messages_to_user = (
            f"*** {sys_msg_dict['error_msg']['invalid_input']} ***\n"
            f"{sys_msg_dict['system_action']['available_names']}\n"
            f" {available_user_names}\n"
        )
        
        print_delay(messages_to_user, sep = '\n\n', end = '\n\n')

        return validated_user_name, validation_status

    # On nonempty input, attempt cleaning/validation
    cleaned_user_name = clean_username(user_name)

    if len(cleaned_user_name) > 25:
        messages_to_user = (
            f"*** {sys_msg_dict['error_msg']['invalid_len']} ***\n"
            f"{sys_msg_dict['system_action']['truncating_input']}\n"
        )

        print_delay(messages_to_user, sep = '\n\n', end = '\n\n')

        # After removing spaces/invalid chars, truncate to allowed max with
        validated_user_name = cleaned_user_name[:24]
        validation_status = True

    elif len(cleaned_user_name) < 5:
        messages_to_user = (
            f"*** {sys_msg_dict['error_msg']['invalid_len']} ***\n"
            f"{sys_msg_dict['system_action']['random_suffix']}\n"
        )

        print_delay(messages_to_user, sep = '\n\n', end = '\n\n')

        # Append a random suffix to satisfy hypothetical DB's min-width req
        validated_user_name = append_random_suffix(cleaned_user_name)
        validation_status = True

    else:
        validated_user_name = cleaned_user_name
        validation_status = True

    return validated_user_name, validation_status


def clean_username(user_name):
    """Basic regex to strip input of non-alnum chars"""

    pattern = re.compile(r'[^a-zA-Z0-9]*')
    cleaned_user_name = re.sub(pattern, '', user_name)

    return cleaned_user_name


def append_random_suffix(short_input):
    """
    Helper function that appends a random suffix to user's input to satisfy 
    hypothetical min width
    """

    # Slightly modified approach from the Secrets docs
    char_bank = string.ascii_letters + string.digits
    random_alnum_suffix = ''.join(secrets.choice(char_bank) for _ in range(7))
    lengthened_username = short_input + random_alnum_suffix

    return lengthened_username


def generate_random_username():
    """
    Helper function that generates a random user name to meet hypothetical DB reqs.
    """

    # Slightly modified approach from the Secrets docs
    adjectives = ['cute', 'lovely', 'super', 'awesome', 'happy', 'amazing', 'peaceful']
    animals = ['KITTEN', 'PUPPY', 'PONY', 'FAWN', 'BUNNY', 'PANDA', 'KOALA']

    random_prefix = ''.join(secrets.choice(adjectives) + secrets.choice(animals))
    random_digit_suffix = ''.join(secrets.choice(string.digits) for _ in range(5))
    random_username = random_prefix + random_digit_suffix

    return random_username


# Call function to request user input for Question 1
hello_name()


###############################################################################
# Question 2: Write a python function, first_odds that prints the odd numbers 
# from 1-100 and returns nothing
###############################################################################

def first_odds():
    """
    Prints the odd integers from 1 to 99. Solution 1 is more straightforward.
    Solution 2 was a product of challenging myself to learn more.
    """

    solution_intro_dict = {
    's1': 'Q2, Solution 1: Tabbed printing of odd integers for readability',
    's2': 'Q2, Solution 2: Printing odd integers as ascii art that implies empty return val',
    }

    # Q2, Solution 1
    print_delay()
    print_delay(solution_intro_dict['s1'])

    # Print Solution 1 in readable format
    for idx, odd in enumerate(range(1, 100, 2), 1):
        if idx % 5 != 1:
            print(odd, end = '\t', flush = True)
            time.sleep(0.02)
            
        else:
            print('\n', odd, end = '\t', flush = True)
            time.sleep(0.02)
    print('\n\n')

    # Q2, Solution 2 (printing our odd integers in form fo the word "Nothing" as ascii number art)

    # Coordinates that I extracted via formula from the Google Sheet where I created my ascii number art
    # https://docs.google.com/spreadsheets/d/1n8GHWMUeeZOeERvVvBlRGLQm_dIiv85MY1bW-HAoXSs/edit?usp=sharing

    ascii_art_coordinates = (
    (0, 0), (0, 3),
    (1, 13),
    (2, 0), (2, 1), (2, 3), (2, 10), (2, 13), (2, 17),
    (3, 6), (3, 9), (3, 10), (3, 11), (3, 14), (3, 19), (3, 20), (3, 24), (3, 25),
    (4, 0), (4, 2), (4, 3), (4, 5), (4, 7), (4, 10), (4, 13), (4, 15), (4, 17), (4, 19), (4, 21), (4, 23),
    (5, 5), (5, 7), (5, 10), (5, 17), (5, 23), (5, 25),
    (6, 0), (6, 3), (6, 6), (6, 10), (6, 13), (6, 15), (6, 17), (6, 19), (6, 21), (6, 24),
    (7, 25),
    (8, 23),
    (9, 25),
    (10, 24)
    )

    # Identify the amount of rows and columns needed to hold the art coordinates
    rows = max(i for (i, j) in ascii_art_coordinates)
    cols = max(j for (i, j) in ascii_art_coordinates)

    # Build 2d array from lists, ensuring distinct obj refs for mutability
    grid = [['' for j in range(cols + 1)] for i in range(rows + 1)]

    # Pair each art cell with incremented odd int to simplify array population
    cell_char_pairings = zip(ascii_art_coordinates, range(1, 100, 2))

    # Insert each odd num at assigned cell,
    # Work in lists to avoid memory alloc of np append calls
    for ((row, col), odd) in cell_char_pairings:
        # Error handling added to aid future use/modification of code
        try:
            grid[row][col] = odd
        except IndexError:
            pass

    # Convert to numpy array for cleaner handling of output
    art_array = np.array(grid)

    # Output
    print_delay(solution_intro_dict['s2'])
    print_delay()

    # Pre-build f-string for each scalar in art array to minimize printing lag
    formatted_scalars = [[f"{scalar: <3}" for scalar in row] for row in art_array]

    # Print odds list as ascii art, under 80 chars/line
    for row in formatted_scalars:
        for scalar in row:
            print(scalar, end = '', flush = True)
            time.sleep(0.02)
        print_delay()
    print()


###############################################################################
# Question 3: Please write a Python function, max_num_in_list to return the max
# number of a given list.
###############################################################################

def max_num_in_list(a_list):
    """Returns max number from list assuming valid input"""

    if not a_list or len(a_list) == 0:
        return False
        
    else:
        return max(a_list)
    

###############################################################################
# Question 4: Write a function to return if the given year is a leap year. A 
# leap year is divisible by 4, but not divisible by 100, unless it is also 
# divisible by 400. The return should be boolean Type (true/false).
###############################################################################

def is_leap_year(a_year):
    """Check if input year is a Leap Year."""

    # First expression accounts for main case, second accounts for edge case
    return (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)


###############################################################################
# Question 5: Write a function to check to see if all numbers in list are 
# consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but 
# [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
###############################################################################

def is_consecutive(ints_list):
    """
    Check if input list contains only consecutive numbers, using general
    mathematical observation that the length of a set of unique integers minus
    one will equal the difference between the set's max minus min.
    """
        
    if not ints_list or len(ints_list) == 0:
        return False
        
    else:
    
        # Remove dups
        uniques_set = set(ints_list)
    
        # Named vars for readability in main expression
        set_len = len(uniques_set)
        set_max = max(uniques_set)
        set_min = min(uniques_set)
    
        # Return True for nonempty set with only consecutive integers
        return (set_max - set_min) == (set_len - 1)
        

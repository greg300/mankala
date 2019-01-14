

# Reads a string, displaying a prompt
def read_string(prompt):
    string = raw_input(prompt)
    return string


# Reads an integer with an upper and a lower bound, displaying a prompt
def read_int_min_max(prompt, minimum, maximum):
    # Make sure the arguments are in the correct order
    if minimum >= maximum:
        print "Illegal Arguments: minimum bound cannot be greater than maximum bound."
        return

    integer = raw_input(prompt)

    # Make sure input is an integer
    while not is_int(integer):
        integer = raw_input(prompt)

    # Make sure input is between or equal to the upper and lower bounds
    while int(integer) < minimum or int(integer) > maximum:
        print "\nInvalid input: number must be between %d and %d. \n" % (minimum, maximum)
        integer = raw_input(prompt)

        # Make sure new input is still an integer
        while not is_int(integer):
            integer = raw_input(prompt)

    return int(integer)


# Reads an integer with a lower bound, displaying a prompt
def read_int_min(prompt, minimum):
    integer = raw_input(prompt)

    # Make sure input is an integer
    while not is_int(integer):
        integer = raw_input(prompt)

    # Make sure input is greater than or equal to the lower bound
    while int(integer) < minimum:
        print "\nInvalid input: number must be greater than or equal to %d. \n" % minimum
        integer = raw_input(prompt)

        # Make sure new input is still an integer
        while not is_int(integer):
            integer = raw_input(prompt)

    return int(integer)


# Reads an integer with an upper bound, displaying a prompt
def read_int_max(prompt, maximum):
    integer = raw_input(prompt)

    # Make sure input is an integer
    while not is_int(integer):
        integer = raw_input(prompt)

    # Make sure input is less than or equal to the upper bound
    while int(integer) > maximum:
        print "\nInvalid input: number must be less than or equal to %d. \n" % maximum
        integer = raw_input(prompt)

        # Make sure new input is still an integer
        while not is_int(integer):
            integer = raw_input(prompt)

    return int(integer)


# Reads a char with possibility of choices (list with characters) or none (empty list), displaying a prompt
def read_char(prompt, choices):
    character = raw_input(prompt)

    # Make sure input is a character
    while not is_char(character):
        character = raw_input(prompt)

    # If there are choices
    if len(choices) > 0:

        # Make sure input is one of the choices
        is_valid = False
        while not is_valid:
            for choice in choices:

                # If any of the choices is the input, it is valid
                if character == choice:
                    is_valid = True
                    break
            if not is_valid:
                print "\nInvalid input: choice must be either",

                # Print all choices
                for i in range(0, len(choices)):

                    # If this is the last choice, don't print 'or' again
                    if i == len(choices) - 1:
                        print choices[i] + ".\n"
                    else:
                        print choices[i] + " or",
                character = raw_input(prompt)

                # Make sure new input is still a character
                while not is_char(character):
                    character = raw_input(prompt)

    return character


# Checks to see if input is a character
def is_char(character):
    is_valid = False

    # If input is a number with more than one digit
    if character.isdigit() and len(character) != 1:
        print "\nInvalid input: input cannot be a number and must be exactly 1 character. \n"

    # If input is a number
    elif character.isdigit():
        print "\nInvalid input: input cannot be a number. \n"

    # If input is longer than a single character
    elif len(character) != 1:
        print "\nInvalid input: input must be exactly 1 character. \n"
    else:
        is_valid = True

    # Return True if input is a character
    return is_valid


# Checks to see if input is an integer
def is_int(integer):
    is_valid = True

    # If input begins with a 0 and has numbers, ex. 0010
    if integer[0] == '0' and len(integer) > 1:
        print "\nInvalid input: input must be an integer. \n"
        return False

    # If input is an integer and not a string
    try:
        integer = int(integer)
    except ValueError:
        print "\nInvalid input: input must be an integer. \n"
        is_valid = False

    # Return True if input is an integer
    return is_valid

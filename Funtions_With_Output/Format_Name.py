# Functions With Output


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You entered invalid inputs."
    return f"{f_name} {l_name}".title()


print(format_name(input("What is your First Name? "), input("What is your last name? ")))

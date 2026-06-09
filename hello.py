# hello.py
#
# Your very first program! This file is a "script" — a list of instructions
# the computer runs from top to bottom.
#
# A line starting with "#" is a COMMENT. The computer ignores it; it's just
# a note for humans (like this one).


def greet(name):
    """Return a friendly greeting for the given name.

    A 'function' is a reusable piece of code. You give it some input
    (here, a 'name') and it gives something back (here, a greeting).
    """
    return f"Hello, {name}! Welcome to coding."


# This block runs when you execute the file with: python3 hello.py
if __name__ == "__main__":
    # Change "World" below to your own name, then run the file again!
    message = greet("World")
    print(message)

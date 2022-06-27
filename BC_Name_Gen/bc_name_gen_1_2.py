"""
Generates funny names.
Version 1_1

How: lists of first name and last name
        select random first, then random last
        print first then last
        ask if it should repeat

Psuedo-Code:
    print startup lines
    loop
        load list of first names
        load list of last names
        generate random first name
        stor name in variable
        generate random last name
        store name in variable
        print name as error
        ask to loop
        if yes
            jump to loop
"""
import sys
import random

def main():
    """Generate a random name for Benedict Cumberbatch."""
    print ("\nGenerate a random 'Benedict Cumberbatch' Name")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    while True:
        first = ('Benedict', 'Butternut', 'Battery', 'Bedazzled')
        last = ('Cumberbatch', 'Crinklefries', 'Challenger', 'Charicature',
                'Crinkledpaper')

        first_name = random.choice(first)
        last_name = random.choice(last)

        print(f"""

    {first_name} {last_name}

    """, file=sys.stderr)

        repeat = input("Generate another name (Press Enter or n to quit)?: ")
        if repeat.lower() == 'n':
            break
    input("Press Enter to Exit: ")

if __name__ == "__main__":
    main()

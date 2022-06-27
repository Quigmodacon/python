"""
Verseion 1.0

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
import sys, random

print ("\nGenerate a random 'Benedict Cumberbatch' Name")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

first = ('Benedict', 'Butternut', 'Battery', 'Bedazzled')
last = ('Cumberbatch', 'Crinklefries', 'Challenger', 'Charicature')

firstName = random.choice(first)
lastName = random.choice(last)

print("""

{} {}

""".format(firstName, lastName), file=sys.stderr)

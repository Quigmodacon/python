"""Generate Pig Latin from given input."""
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxy"
def main():
    """Add -[consonant]ay to consonant words and way to vowel words."""
    while True:
        #get input string
        input_string = input("Enter a word to translate: ")
        #check first letter
        if input_string[0].lower() in CONSONANTS:
            #if consonant remove first letter and add -ay
            pig_latin = input_string[1:]
            pig_latin = pig_latin + input_string[0] + "ay"
        elif input_string[0].lower() in VOWELS:
            #else add -way
            pig_latin = input_string + "way"
        #print word
        print(f"\n\n{pig_latin}\n\n")
        #ask to stop
        stop = input("Translate another? (Enter else 'n' to quit) : ")
        #if 'n' break
        if stop.lower() == 'n':
            break
    input("Press enter to quit: ")
        

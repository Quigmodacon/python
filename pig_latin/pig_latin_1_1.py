"""Generate Pig Latin from given input."""
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxy"
def main():
    """Add -[consonant]ay to consonant words and way to vowel words."""
    print("Translate English into Pig Latin.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    while True:
        #get input string
        input_string = input("Enter a word to translate: ").lower()
        #split string into words array
        words = []
        i = 0
        start = 0
        end = 0
        while i != -1:
            end = input_string.find(' ', start)
            words.append(input_string[start, end])
            start = end + 1

        for word in words:
            #check first letter
            if word[0] in CONSONANTS:
                #if consonant remove first letter and add -ay
                pig_latin = word[1:]
                pig_latin = pig_latin + word[0] + "ay"
            elif word[0] in VOWELS:
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

if __name__ == '__main__':
    main()

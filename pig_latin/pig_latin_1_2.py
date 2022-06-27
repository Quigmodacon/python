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
        start = 0
        end = 0
        while end != -1:
            end = input_string.find(' ', start)
            words.append(input_string[start:end])
            start = end + 1

        pig_latin = []
        for word in words:
            #check first letter
            if word[0] in CONSONANTS:
                #if consonant remove first letter and add -ay
                pig_latin_word = word[1:]
                pig_latin_word = pig_latin_word + word[0] + "ay"
            elif word[0] in VOWELS:
                #else add -way
                pig_latin_word = word + "way"
            pig_latin.append(pig_latin_word)

        print("\n\n")
        for word in pig_latin:
            #print word
            print(word + " ", end = '')
        print("\n\n")

        #ask to stop
        stop = input("Translate another? (Enter else 'n' to quit) : ")
        #if 'n' break
        if stop.lower() == 'n':
            break
    input("Press enter to quit: ")

if __name__ == '__main__':
    main()

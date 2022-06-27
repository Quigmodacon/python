"""List letters in scentence as bar chart."""

import pprint

def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    #create dict of letters [letter] : [list]
    bar_chart = {}
    for letter in alpha:
        bar_chart[letter] = []

    #recieve input sentence
    sentence = input("Enter sentence to graph: ")
    #split sentence into dict by letter
    for letter in sentence:
        if letter in alpha:
            bar_chart[letter].append(letter)
    #print dict using pprint
    pp = pprint.PrettyPrinter(indent = 4)
    pp.pprint(bar_chart)
    pass

if __name__ == "__main__":
    main()

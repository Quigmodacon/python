"""Load a dictionary into a list
Arguments:
   -text file name (and directory path, if needed)
   
 Exceptions:
   -IOError if filename not found.
   
 Returns:
   -A list of all words in a text file in lower case.

 Requires-import sys
"""

import sys

def load(file):
    """Open a text file and return a list of lowercase strings.""" 
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print(f"{e}\nError opening {FILE}. Terminating.")
        sys.exit(1)

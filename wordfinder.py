import random
path = 'words.txt'
"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    """ Random word search from provided dictionary  """

    def __init__(self, path):
        """  Opens path to dictionary  """
        
        with open(path, 'r', encoding='utf-8') as dict_file:
            self.words = self.parse(dict_file)
        print(f"{len(self.words)} were read")

    def parse(self, dict_file):
        """   Convert file to a list  """

        return [word.strip() for word in dict_file if word.strip().isalpha()]

    def random(self):
        """  Gets random word   """

        return random.choice(self.words)
    
wf = WordFinder("words.txt")
print(wf.random())


class SpecialWordFinder(WordFinder):
    """ WordFinder that excludes blank lines/comments  """

    def parse(self, dict_file):
        ''' removing blanks/comments from dict_file   '''

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith('#')]
    

swf = SpecialWordFinder("words.txt")
print(swf.random())
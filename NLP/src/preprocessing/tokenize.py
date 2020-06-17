import re


class StringTokenize:
    
    def __init__(self, string):
        self.string = string
        
    def tokenize(self, pattern=' '):
        return re.split(pattern, self.string)

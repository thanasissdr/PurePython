class StringConvert:
    def __init__(self, string):
        self.string = string

    def to_lower(self):
        self.string = self.string.lower()
        return self

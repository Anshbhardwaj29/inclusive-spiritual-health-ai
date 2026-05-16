class CrisisHandler:
    def __init__(self):
        # Expanded keywords for better detection
        self.keywords = ["suicide", "marna", "die", "kill myself", "end my life", "hurt myself", "zindagi khatam", "hopeless", "no reason to live"]

    def is_crisis(self, text):
        return any(word in text.lower() for word in self.keywords)
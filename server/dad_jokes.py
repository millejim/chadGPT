# Generates random dad jokes for entertainment purposes
class DadJokeGenerator:
    """A class that generates and manages dad jokes."""
    
    def __init__(self):
        """Initialize the DadJokeGenerator with a collection of jokes."""
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I'm reading a book about anti-gravity. It's impossible to put down!",
            "What do you call a fake noodle? An impasta!",
            "I used to hate facial hair, but then it grew on me.",
            "Why did the scarecrow win an award? He was outstanding in his field!"
        ]
    
    def get_random_joke(self):
        """Return a random dad joke from the collection."""
        import random
        return random.choice(self.jokes)
    
    def add_joke(self, joke):
        """Add a new joke to the collection."""
        self.jokes.append(joke)
    
    def get_all_jokes(self):
        """Return all jokes in the collection."""
        return self.jokes

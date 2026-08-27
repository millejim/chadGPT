"""
Dad Jokes Generator Module

This module provides functionality to generate and manage dad jokes.
"""

import random
from typing import Dict, List


class DadJokeGenerator:
    """A generator for classic dad jokes."""
    
    # Collection of dad jokes
    JOKES: List[Dict[str, str]] = [
        {
            "setup": "Why don't scientists trust atoms?",
            "punchline": "Because they make up everything!"
        },
        {
            "setup": "I'm reading a book about anti-gravity.",
            "punchline": "It's impossible to put down!"
        },
        {
            "setup": "Why did the scarecrow win an award?",
            "punchline": "He was outstanding in his field!"
        },
        {
            "setup": "I told my wife she was drawing her eyebrows too high.",
            "punchline": "She looked surprised."
        },
        {
            "setup": "Why don't eggs tell jokes?",
            "punchline": "They'd crack each other up!"
        },
        {
            "setup": "What did the ocean say to the beach?",
            "punchline": "Nothing, it just waved."
        },
        {
            "setup": "Why don't skeletons fight each other?",
            "punchline": "They don't have the guts!"
        },
        {
            "setup": "What do you call a fake noodle?",
            "punchline": "An impasta!"
        },
        {
            "setup": "Why did the coffee file a police report?",
            "punchline": "It got mugged!"
        },
        {
            "setup": "What do you call a sleeping bull?",
            "punchline": "A dozer!"
        },
        {
            "setup": "I used to hate facial hair, but then it grew on me.",
            "punchline": "Now I can't imagine life without it."
        },
        {
            "setup": "Why don't oysters share their pearls?",
            "punchline": "Because they're shellfish!"
        },
        {
            "setup": "What's the best thing about Switzerland?",
            "punchline": "I don't know, but the flag is a big plus."
        },
        {
            "setup": "Why did the bicycle fall over?",
            "punchline": "It was two-tired!"
        },
        {
            "setup": "What do you call a bear with no teeth?",
            "punchline": "A gummy bear!"
        },
        {
            "setup": "Why did the Oreo go to the dentist?",
            "punchline": "To get its filling!"
        },
        {
            "setup": "What kind of key opens a banana?",
            "punchline": "A monkey!"
        },
        {
            "setup": "Why don't you ever see a hippo hiding in a tree?",
            "punchline": "Because they're really good at it!"
        },
        {
            "setup": "What do you call a dog magician?",
            "punchline": "A Labracadabrador!"
        },
        {
            "setup": "Why is no one friends with Dracula?",
            "punchline": "Because he's a pain in the neck!"
        }
    ]
    
    @classmethod
    def get_random_joke(cls) -> Dict[str, str]:
        """
        Get a random dad joke.
        
        :return: Dictionary containing 'setup' and 'punchline' keys
        """
        return random.choice(cls.JOKES)
    
    @classmethod
    def get_all_jokes(cls) -> List[Dict[str, str]]:
        """
        Get all available dad jokes.
        
        :return: List of all jokes
        """
        return cls.JOKES.copy()
    
    @classmethod
    def get_joke_by_index(cls, index: int) -> Dict[str, str]:
        """
        Get a dad joke by index.
        
        :param index: Index of the joke (0-based)
        :return: Dictionary containing 'setup' and 'punchline' keys
        :raises IndexError: If index is out of range
        """
        if not 0 <= index < len(cls.JOKES):
            raise IndexError(f"Joke index {index} out of range. Available jokes: {len(cls.JOKES)}")
        return cls.JOKES[index]
    
    @classmethod
    def get_joke_count(cls) -> int:
        """
        Get the total number of available jokes.
        
        :return: Number of jokes in the collection
        """
        return len(cls.JOKES)

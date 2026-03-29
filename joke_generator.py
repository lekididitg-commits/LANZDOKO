import requests
import random

class JokeGenerator:
    def __init__(self):
        self.api_url = 'https://official-joke-api.appspot.com/jokes/random'

    def fetch_joke(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            joke = response.json()
            return f"{joke['setup']} - {joke['punchline']}"
        except requests.RequestException as e:
            return f"Error fetching joke: {e}"

    def random_joke(self):
        return self.fetch_joke()

if __name__ == '__main__':
    generator = JokeGenerator()
    print(generator.random_joke())
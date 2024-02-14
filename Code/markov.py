"""Implement a markov chain"""
import random

class Markov:
    """Create a class that stores transition probabilites for different states"""
    def __init__(self, order=1):
        """
        Desc: Initilize class Markov
        Params: self represents the instance and order which is set to 1 by default
        Return: None
        """
        # Set order equal to 1
        self.order = order
        # Create a empty dictionary
        self.markov = {}

    # --------------------------
    def add_state(self, text):
        """
        Desc: Add a state forming a chain
        Params: self represents the instance and text which is set to empty by default
        Return: the state
        """
        for i in range(len(text) - self.order):
            # Create a tuple of characters starting from i-th index
            sequence = tuple(text[i:i + self.order])
            # Add the i-th index to self.order which is set to 1
            new_state = text[i + self.order]

            if sequence in self.markov:
                # Add the value of new_state to the list at the key(sequence)
                self.markov[sequence].append(new_state)
            else:
                # Assign the value of new_state to the list at the key(sequence)
                self.markov[sequence] = [new_state]

    # -------------------------------
    def generate_corpus(self, length):
        """
        Desc: Generate a corpus randomly 
        Params: self represents the instance and length which is set to 0 by default
        Return: Random word in a corpus that is mostly English or the state
        """
        # Select a random key from the dictionary
        current_state = random.choice(list(self.markov.keys()))
        # Create a list of random keys
        state = list(current_state)

        for _ in range(length - self.order):
            if current_state in self.markov:
                # Randomly choose the next state from a list based on the current state
                new_state = random.choice(self.markov[current_state])
                # Append the line above to state on line 39
                state.append(new_state)
                # Set the current state by retrieving the last elements
                current_state = tuple(state[-self.order:])
            else:
                break
        return state


# Add some text, maybe could add a txt file
new_text = ["A man,", "a plan,", "a canal:", "Panama!", "A dog,", "a panic in a pagoda!"]

# Create a new Markov model/chain and set the state
corpus_chain = Markov(order=1)
corpus_chain.add_state(new_text)

# Generate text randomly
generate_corpus = corpus_chain.generate_corpus(length=10)
print(' '.join(generate_corpus))

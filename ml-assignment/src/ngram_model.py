import random

class TrigramModel:
    def __init__(self):
        """
        Initializes the TrigramModel.
        """
        # TODO: Initialize any data structures you need to store the n-gram counts.
        self.trigram_counts = {}
        self.bigram_counts = {}
        self.vocab = set()
       
        pass

    def fit(self, text):
        """
        Trains the trigram model on the given text.

        Args:
            text (str): The text to train the model on.
        """
        # TODO: Implement the training logic.
        # This will involve:
        # 1. Cleaning the text (e.g., converting to lowercase, removing punctuation).
        # 2. Tokenizing the text into words.
        # 3. Padding the text with start and end tokens.
        # 4. Counting the trigrams.

        # SPECIAL CASE: Empty training text
        if not text.strip():
            self.trigram_counts = {}
            self.bigram_counts = {}
            self.vocab = set()
            return


        # 1. Lowercase
        text = text.lower()

        # 2. Removing Punctuation
        for p in ".,!?;:\"'()[]{}":
            text = text.replace(p, "")

        # 3.Tokenize
        words = text.split()

        # 4. Padding start and end tokens
        words = ["<s>", "<s>"] + words + ["<s>"]

        # 5. Couting trigrams
        for i in range(len(words)-2):
            w1, w2, w3 = words[i], words[i+1], words[i+2]

            self.vocab.add(w1)
            self.vocab.add(w2)
            self.vocab.add(w3)

            # trigram count update  
            if (w1, w2) not in self.trigram_counts:
                self.trigram_counts[(w1, w2)] = {}
                
            if w3 not in self.trigram_counts:
                self.trigram_counts[(w1, w2)][w3] = 0

            self.trigram_counts[(w1, w2)][w3] += 1

            # bigram count Update
            if (w1, w2) not in self.bigram_counts:
                self.bigram_counts[(w1, w2)] = 0

            self.bigram_counts[(w1, w2)]  += 1    


        pass

    def generate(self, max_length=50):
        """
        Generates new text using the trained trigram model.

        Args:
            max_length (int): The maximum length of the generated text.

        Returns:
            str: The generated text.
        """
        # TODO: Implement the generation logic.
        # This will involve:
        # 1. Starting with the start tokens.
        # 2. Probabilistically choosing the next word based on the current context.
        # 3. Repeating until the end token is generated or the maximum length is reached.
        
        # Special Case: empty training text
        if len(self.trigram_counts) == 0:
            return ""

        # 1. Start with <s>, <s>
        w1, w2 = "<s>", "<s>"
        generated_words = []

         # 2. Generate words one by one
        for _ in range(max_length):

            # If this context never occurred in training
            if (w1, w2) not in self.trigram_counts:
                break

            next_words_dict = self.trigram_counts[(w1, w2)]

            # 3. Select next word based on probability
            total_count = self.bigram_counts[(w1, w2)]
            words = []
            probs = []

            for word, count in next_words_dict.items():
                words.append(word)
                probs.append(count / total_count)

            # Random weighted choice
            next_word = random.choices(words, probs)[0]

            # Stop if end token
            if next_word == "</s>":
                break

            # Add to output
            generated_words.append(next_word)

            # Shift context
            w1, w2 = w2, next_word

        # Return sentence
        return " ".join(generated_words)

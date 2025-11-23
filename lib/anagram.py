# your code goes here!
# anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # normalize to lowercase
        self.sorted_word = sorted(self.word)

    def match(self, word_list):
        matches = []
        for w in word_list:
            # avoid matching the word with itself (common requirement in anagram problems)
            if w.lower() != self.word:
                if sorted(w.lower()) == self.sorted_word:
                    matches.append(w)
        return matches

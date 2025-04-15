def get_num_words(text):
        words = text.split()
        return len(words)

def get_num_letters(text):
        lower_words = [letter.lower() for letter in text]
        letter_counts = {}
        for letter in lower_words:
                if letter not in letter_counts:
                        letter_counts[letter] = 1
                else:
                        letter_counts[letter] += 1
        return letter_counts
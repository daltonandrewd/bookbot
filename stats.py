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

def sort_on(item):
        return item["num"]

def format_data(letter_counts):
        formatted = []
        for letter, num in letter_counts.items():
                formatted.append({"letter": letter, "num": num})
        formatted.sort(reverse=True, key=sort_on)
        return formatted

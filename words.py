def print_upper_words(words, starts_with):
    for word in words:
        for letter in starts_with:
            if word.startswith(letter):
                print(word.upper())
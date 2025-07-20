def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    words = text.split()
    char_dict = {}
    for word in words:
        for char in word:
            if char.isalpha():
                char = char.lower()
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
    return char_dict

def sorted_count_chars(chars_dict):
    return sorted(chars_dict.items(), key=lambda x: x[1], reverse=True)

punctuation_marks = [',', '!', '?', '.']
vowel_letters = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

def remove_punctuation_marks(word):
    for symbol in punctuation_marks:
        word = word.replace(symbol, '')
    return word


def words_count(words):
    return len(words)


def get_longest_word(words):
    longest_word = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word


def get_vowel_letters_count(words):
    vowel_letters_count = 0

    for word in words:
        for letter in word:
            if letter in vowel_letters:
                vowel_letters_count += 1

    return vowel_letters_count


def get_count_non_identical_words(words):
    non_identical_words = {}

    for word in words:
        if word in non_identical_words:
            non_identical_words[word] += 1
        else:
            non_identical_words[word] = 1

    return non_identical_words


text = input("Введите текст: ").lower()

clean_words = []
for word in text.split():
    clean_word = remove_punctuation_marks(word)
    if clean_word != "":
        clean_words.append(clean_word)

print(f"Кол-во слов: {words_count(clean_words)}")
print(f"Самое длинное слово: {get_longest_word(clean_words)}")
print(f"Кол-во гласных букв: {get_vowel_letters_count(clean_words)}")

frequencies = get_count_non_identical_words(clean_words)
for word, count in frequencies.items():
    print(f"{word}: {count} раз(а)")
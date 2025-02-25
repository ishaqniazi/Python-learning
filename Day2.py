# input by user and then count words

from os.path import split

user_input = input("write your sentence: ")
word_count = (user_input.split())
print(word_count)
print(len(word_count))

# reversed = user_input[::-1]
# print(reversed)

# input by user and then reverse the sentence

def reversed_sentence (user_input):
    words = user_input.split()
    reversed_sen= " ".join(reversed(words))
    return reversed_sen

print(reversed_sentence(user_input))

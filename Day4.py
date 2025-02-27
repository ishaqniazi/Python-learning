import inflect
p = inflect.engine()
num = 123
words = p.number_to_words(num)
print(words)

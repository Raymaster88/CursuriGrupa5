import random
list = ["restaurant", "cinaemca", "envelope", "phpytnon"]
random_word = random.choice(list)
# print(random_word)
lives = 7
# while lives > 0:
unknown = len(random_word) * ' _ '
f_let = random_word[0]
l_let = random_word[-1]
# poz = 0
# for letter in random_word:
#     if f_let == letter:
#         unknown[poz] = letter
#         poz += 1
# print(unknown)
word_list = []
for i in random_word:
    if random_word[0] != i and random_word[-1] !=i:
        word_list.append("_")
    else:
        word_list.append(i)
guess = input("Make a guess:")
if guess in random_word:
    nr_app = random_word.count(guess)
    if nr_app > 1:
        for i in random_word:
            print (random_word.index(guess))




#     word_list.append(i)
# for j in range (len(random_word)):
#     if random_word[j] in
#

# print (word_list)







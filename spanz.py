
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
            print (random_word.index(guess



-----------------------------------------------------------------------------------------------

# input word
word=list(input('word>> '))
secret_word=[]

lives=int(7)
visible_letters=[word[0],word[-1]]

for i in range(0,len(word)):
    # print(word[i])
    if word[i] not in visible_letters:
       secret_word.append('_')
    else:
        secret_word.append(word[i])

print(' '.join(secret_word))

guess_list=[]
lives=int(7)

while '_' in secret_word:
    guess = input("Guess >> ")

    while guess in guess_list or guess in secret_word:
            guess = input("Already have it. Guess again >> ")

    if lives==0:
        print('game over')
        break

    elif guess not in word:
        print(f"wrong. You have {lives} left")
        lives-=1
        print(lives)



    for i in range(0,len(word)):

        if  guess == word[i] :
            secret_word[i] = guess
            print(' '.join(secret_word))
            guess_list.append(guess)
            #print(guess_list)





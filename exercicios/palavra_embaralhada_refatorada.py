import random


def guess_scrambled_word():
    word = random.choice(['cachorro', 'passarinho', 'baleia'])
    scrambled_word = "".join(random.sample(word, len(word)))
    print(scrambled_word)
    guess = input('Que palavra é essa?\n')

    tries = 2
    while tries > 0:
        if word == guess:
            print(f'Acertou!! A palavra é {word}')
            break
        else:
            print(f'Tente novamente. Restantes: {tries}')
            guess = input('Que palavra é essa?\n')
            tries -= 1


guess_scrambled_word()

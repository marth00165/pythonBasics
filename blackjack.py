from random import randint

card_total = 0


def welcome():
    print('Welcome To Ro-Jack Rohit\'s blackjack game!')


def deal(total):
    card1 = randint(1, 11)
    card2 = randint(1, 11)
    total += total + card1 + card2
    print(f' first card: {card1}')
    print(f' second card: {card2}')
    compare(total)


def compare(total):
    if total < 21:
        print(f' Your total is: {total}')
        while total < 21:
            hit_stand = input('Hit or Stand?: ')
            if hit_stand == 'h':
                card3 = randint(1, 11)
                print(card3)
                total += card3
                print(total)
            else:
                print(f'Your total is {total}!')
                break
        else:
            print('You Bust!')
    else:
        print('You Bust!')


def runner():
    welcome()
    deal(card_total)


runner()

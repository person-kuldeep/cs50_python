import random
import datetime


def main():
    x = int(input("Enter num of cards to draw: "))
    print(random_card(x))


def random_card(x):
    """
    Docstring for random_card
    """
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    random.seed(str(datetime.datetime.now()))
    cards = random.choices(suits, weights=[40, 30, 20, 10], k=x)

    return cards


if __name__ == "__main__":
    main()

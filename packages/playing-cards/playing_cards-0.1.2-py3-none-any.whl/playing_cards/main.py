# ♠♤ ♥♡ ♣♧ ♦♢
__version__ = '0.1.0'

import random
import sys

def build_card():
    total_cards = []
    four_suits = ["♠", "♡", "♣", "♢"] # 四種花色
    tag_char = {1: "A", 11: "J", 12: "Q", 13: "K"}
    for item in four_suits:
        for x in range(1, 13+1):
            card = tag_char.get(x)
            if card is None:
                card = str(x)
            d_tuple = (card, item)    # 包裝成 tuple
            total_cards.append(d_tuple)
    return total_cards

def get_random_card():
    cards = build_card()
    random.shuffle(cards)
    return cards

def main(piece):
    cards = get_random_card()
    n = 1
    for i, item in enumerate(cards):
        if i % piece == 0 or i == 0:
            print()
            print(str.format("Player {: 2}:", n), end=' ')
            n += 1
        d = item[1]+item[0]
        s = str.ljust(d, 3, ' ')
        print(s, end=" ")

def run():
    argv = sys.argv[1:]
    piece = int(argv[0]) if argv else 4
    
    p = int(52 / piece)
    if 52 % piece:
        main(p+1)
    else:
        main(p)

if __name__ == "__main__":
    run()
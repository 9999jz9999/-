# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:39:41 2024

@author: kkjj1
"""

import random

def create_deck():
    """建立一副撲克牌"""
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    """洗牌"""
    random.shuffle(deck)

def deal_cards(deck):
    """發牌給四個人"""
    hands = [[] for _ in range(4)]
    for i, card in enumerate(deck):
        hands[i % 4].append(card)
    return hands

def sort_cards(hands):
    """依照數字大小排序"""
    for hand in hands:
        hand.sort(key=lambda x: (int(x[0]) if x[0].isdigit() else 10 if x[0] == 'J' else 11 if x[0] == 'Q' else 12 if x[0] == 'K' else 13, x[1]))

def print_hands(hands):
    """顯示四個人的手牌"""
    for i, hand in enumerate(hands):
        print(f"Player {i + 1}:", end=" ")
        for card in hand:
            print(f"{card[0]}{card[1]}", end=" ")
        print()

def main():
    deck = create_deck()
    shuffle_deck(deck)
    hands = deal_cards(deck)
    sort_cards(hands)
    print_hands(hands)

if __name__ == "__main__":
    main()

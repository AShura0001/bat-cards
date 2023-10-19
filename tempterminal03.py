import random


num_cards_avl = 16
card_set_1 = []
card_set_2 = []
while (len(card_set_1) < 8) :
    card_rank_a = random.randint(1, 17)
    if (card_rank_a not in card_set_1):
        print(card_rank_a) 
        card_set_1.append(card_rank_a)
while (len(card_set_2) < 8) :
    card_rank_b = random.randint(1, 17)
    if (card_rank_b not in card_set_1) and (card_rank_b not in card_set_2):
        print(card_rank_b)
        card_set_2.append(card_rank_b)


print(card_set_1)
print(card_set_2)
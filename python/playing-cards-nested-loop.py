import random
def playing_cards():
    suit = ("\u2660", "\u2665", "\u2666", "\u2663")
    rank = list("A23456789")+["10"]+list("JQK")
    deck = []
    for s in suit:
        for r in rank:
            deck.append(r + s)
    return deck

d=playing_cards()


random.shuffle(d)
#print(d)

p = random.sample(d, 1)
print(p)
def load(filename):
    deck_one = []
    deck_two = []
    file = open(filename)
    line = file.readline().strip('\n')
    line = file.readline().strip('\n')
    while not line == "":
        deck_one.append(line)
        line = file.readline().strip('\n')
    line = file.readline().strip('\n')
    for line in file:
        deck_two.append(line.strip('\n'))

    file.close()
    return deck_one, deck_two


def play_game(deck1, deck2):
    round = 1
    while len(deck_player_one) > 0 and len(deck_player_two) > 0:
        card_one = int(deck_player_one.pop(0))
        card_two = int(deck_player_two.pop(0))
        if card_one > card_two:
            deck_player_one.append(card_one)
            deck_player_one.append(card_two)
        else:
            deck_player_two.append(card_two)
            deck_player_two.append(card_one)
        # print("Round " + str(round))
        # print("Player 1:" + str(deck_player_one))
        # print("Player 2:" + str(deck_player_two))
        round += 1


def play_game_recursive(deck1, deck2):
    round_count = 1
    rounds = []

    while len(deck1) > 0 and len(deck2) > 0:
        round_sig = [str(deck1), str(deck2)]
        if round_sig in rounds:
            break
        rounds.append(round_sig)

        card_one = int(deck1.pop(0))
        card_two = int(deck2.pop(0))

        if len(deck1) >= card_one and len(deck2) >= card_two:
            r_deck1 = deck1[0:card_one]
            r_deck2 = deck2[0:card_two]
            play_game_recursive(r_deck1, r_deck2)
            if len(r_deck1) == 0:
                deck2.append(card_two)
                deck2.append(card_one)
            else:
                deck1.append(card_one)
                deck1.append(card_two)

        elif card_one > card_two:
            deck1.append(card_one)
            deck1.append(card_two)
        else:
            deck2.append(card_two)
            deck2.append(card_one)

        # print("Round " + str(round_count))
        # print("Player 1:" + str(deck1))
        # print("Player 2:" + str(deck2))
        round_count += 1


data = load('day22.txt')
deck_player_one = data[0]
deck_player_two = data[1]
print("Starting decks:")
print("Player 1: " + str(deck_player_one))
print("Player 2: " + str(deck_player_two))

play_game(deck_player_one, deck_player_two)

print()
score = 0
if len(deck_player_two) == 0:
    print("Player 1 wins " + str(deck_player_one))
    for x, card in enumerate(reversed(deck_player_one)):
        score += int(card) * (x + 1)
else:
    print("player 2 wins " + str(deck_player_two))
    for x, card in enumerate(reversed(deck_player_two)):
        score += int(card) * (x + 1)

print()
print("Answer part 1: " + str(score))
print()

data = load('day22.txt')
deck_player_one = data[0]
deck_player_two = data[1]
print("Starting decks:")
print("Player 1: " + str(deck_player_one))
print("Player 2: " + str(deck_player_two))

play_game_recursive(deck_player_one, deck_player_two)

print()

score = 0
if len(deck_player_two) == 0:
    print("Player 1 wins " + str(deck_player_one))
    for x, card in enumerate(reversed(deck_player_one)):
        score += int(card) * (x + 1)
else:
    print("player 2 wins " + str(deck_player_two))
    for x, card in enumerate(reversed(deck_player_two)):
        score += int(card) * (x + 1)

print()
print("Answer part 2: " + str(score))

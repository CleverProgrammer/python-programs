
"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

ALL_HANDS = range(1, 7)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.
    hand: full yahtzee hand
    Returns an integer score
    >>> score((1, 5, 5, 2, 3))
    10
    >>> score((1, 4, 1, 4, 6))
    8
    >>> score((1, 1, 1, 1, 1))
    5
    >>> score((2, 3, 4, 5, 6))
    6
    """
    max_value = 0
    for num in hand:
        if num * hand.count(num) > max_value:
            max_value = num * hand.count(num)
    return max_value


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.
    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled
    Returns a floating point expected value
    >>>expected_value((2, 2), 6, 2)
    5.833333333333333
    """
    new_score = 0
    total_score = 0.0
    all_possibilities_for_free_dice = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)

    if not all_possibilities_for_free_dice:
        return score(held_dice)

    for possibility in all_possibilities_for_free_dice:
        new_hand = possibility + held_dice
        new_score = score(new_hand)
        total_score += new_score
    return total_score / len(all_possibilities_for_free_dice)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
    hand: full yahtzee hand
    Returns a set of tuples, where each tuple is dice to hold

    """
    #  Use this to cross-reference impossible holds
    hand_value_counter = {}
    for value in hand:
        if value not in hand_value_counter:
            hand_value_counter[value] = 1
        else:
            hand_value_counter[value] += 1

    # Generate all possible holds
    hold_choices = []
    for length in range(len(hand) + 1):
        for held_cards in gen_all_sequences(hand, length):
            hold_choices.append(held_cards)
    hold_choices = set([tuple(sorted(x)) for x in hold_choices])

    # Store impossible holds indexes
    hold_choices_indices_to_remove = []
    hold_choices = list(hold_choices)
    for impossible_tuple_idx, tuple_ in enumerate(hold_choices):
        for value in tuple_:
            if tuple_.count(value) > hand_value_counter[value]:
                hold_choices_indices_to_remove.append(impossible_tuple_idx)
                break

    # Remove impossible indexes from hold_choice
    for impossible_hold_idx in hold_choices_indices_to_remove[::-1]:
        hold_choices.pop(impossible_hold_idx)
    print(len(hold_choices))
    return set(hold_choices)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.
    hand: full yahtzee hand
    num_die_sides: number of sides on each die
    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_expected = 0.0
    max_hand = None
    max_length = len(hand)
    for hand in gen_all_holds(hand):
        expected_val = expected_value(hand, num_die_sides, max_length - len(hand))
        if expected_val > max_expected:
            max_expected = expected_val
            max_hand = hand
    return (max_expected, max_hand)


print(strategy((4, 4, 5, 1, 6), 6))

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""
import unittest
# import codeskulptor
# codeskulptor.set_timeout(20)


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
    """
    #  hand looks like --> (1,2,3,4,5,6)
    max_value = 0
    for num in hand:
        if num * hand.count(num) > max_value:
            max_value = num * hand.count(num)
    return max_value


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice:     dice that you will hold (tuple)
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    #  (1,2,3,4,5,6) / 6  ==> 3.5
    held_dice = (2, 2)
    num_die_sides = 6
    num_free_dice = 5
    enumerations = gen_all_sequences(num_die_sides, num_free_dice)  #
    possible_hands = []
    
    return 0.0


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    return set([()])


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return (0.0, ())


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print("Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score)


# run_example()

class Yahtzee(unittest.TestCase):

    def test_score(self):
        self.assertEqual(score([6, 4, 4, 2, 2, 2]), 8)
        self.assertEqual(score([6, 4, 4, 2, 2, 6]), 12)
        self.assertEqual(score([1, 1, 1, 1, 1, 5]), 5)

    def test_expected_value(self):
        self.assertAlmostEqual(expected_value((2, 2), 6, 2), 5.8333333333)


suite = unittest.TestLoader().loadTestsFromTestCase(Yahtzee)
unittest.TextTestRunner(verbosity=2).run(suite)


#import poc_holds_testsuite
# poc_holds_testsuite.run_suite(gen_all_holds)

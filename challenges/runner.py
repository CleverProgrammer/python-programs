import random
chosen_number = 1


def base_strategy():

    return random.randrange(1, 10)


def computer_strategy(scores, player_answers, computer_answers, total_iterations, current_iteration):
    # Add your solution here
    print("player_answers: %s" % player_answers)
    return chosen_number


def compute_score(player_answer, computer_answer, scores):
    if player_answer + 1 == computer_answer:  # computer_answer is lower by 1
        scores['computer'] += 2
    elif computer_answer + 1 == player_answer:
        scores['player'] += 2
    elif player_answer < computer_answer:  # player answer is lower by more than 1
        scores['player'] += 1              # add one point for player
    elif player_answer > computer_answer:  # computer answer is lower by more than 1
        scores['computer'] += 1            # add one point for computer
    return scores


def calculate_winner(scores, outcomes):
    if scores['player'] > scores['computer']:
        outcomes['player'] += 1
    elif scores['computer'] > scores['player']:
        outcomes['computer'] += 1
    else:
        outcomes['ties'] += 1
    return outcomes


# run!

if __name__ == '__main__':
    print("trying: %s" % chosen_number)
    iterations = 100
    scores = {'player': 0, 'computer': 0}
    outcomes = {'player': 0, 'computer': 0, 'ties': 0}
    player_nums = []
    computer_nums = []
    for x in range(0, iterations):
        while scores['player'] < 5 and scores['computer'] < 5:
            player_answer = base_strategy()
            computer_answer = computer_strategy(
                scores, player_nums, computer_nums, iterations, x)
            player_nums.append(player_answer)
            computer_nums.append(computer_answer)
            compute_score(player_answer, computer_answer, scores)
        calculate_winner(scores, outcomes)
        scores = {'player': 0, 'computer': 0}
        player_nums = []
        computer_nums = []
    print('Results - Player {0}, Computer {1}, Tie {2}'.format(
        outcomes['player'], outcomes['computer'], outcomes['ties']))

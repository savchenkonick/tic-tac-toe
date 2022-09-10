"""Tic-tac-toe game with "AI".
Also known as Noughts and Crosses or X's and O's.
Game has 3 modes: easy, medium and hard.

Hard:
    The algorithm that implements this is called minimax. It's a brute force
    algorithm that maximizes the value of the AI's position and minimizes the
    worth of its opponent's.

    It calculates all possible moves that might be played during the game,
    and choose the best one based on the assumption that its opponent will also
    play perfectly. So, it doesn't rely on the mistakes of its opponent and
    plays the game without fault from start to finish regardless of
    the opponent's skill!

Medium:
    When the AI is playing at medium difficulty level, it makes moves using the
    following logic:
        - If it already has two in a row and can win with one further move, it
         does so.
        - If its opponent can win with one move, it plays the move necessary
         to block this.
        - Otherwise, it makes a random move.

Easy: in this mode algorithm just makes move randomly


To start the game please type command: start <player 1> <player2>
for example: start user hard
or: start hard user


Functions:
    make_ai_move_hard()

    Start recursion of function simulate_moves_hard to find out all possible
    game combinations. If it finds finishing game state it calculates and stores
    score for that move using minimax algorithm depending on how many steps is
    required to achieve it.
    If winning combination on the next move score_increment = 100
    If winning combination is under 10 moves it calculates:
                                                    score_increment = 10 - iter
    Else: score_increment = 0
"""
import random


class GameState:
    matrix = []
    test_coordinates = {}
    matrix_state = []
    USER = 'USER'
    GAME_MODE = {'PLAYER1': '',
                 'PLAYER2': '',
                 'AI_MODE': '',
                 'AI_PLAYS': '',
                 'USER_PLAYS': '',
                 'AVAILABLE_MODES': ['EASY', 'USER', 'MEDIUM', 'HARD']}


def make_matrix(user_input):
    game.matrix = [list(user_input[i * 3:i * 3 + 3]) for i in range(3)]


def make_matrix_hard():
    game.matrix = [list(game.matrix_state[i * 3:i * 3 + 3]) for i in range(3)]


def print_matrix():
    print('---------')
    for i in range(len(game.matrix)):
        print(f'| {game.matrix[i][0]} {game.matrix[i][1]} {game.matrix[i][2]} |')
    print('---------')


def game_finished():
    counter_of_space = 0

    for row in game.matrix:
        counter_of_space += row.count(' ')

    x_wins = o_wins = 0
    tests = []
    for i in range(3):
        tests.append([[i, j] for j in range(3)])
    for i in range(3):
        tests.append([[j, i] for j in range(3)])
    tests.append([[i, i] for i in range(3)])
    tests.append([[abs(i - 2), i] for i in range(2, -1, -1)])

    count_x = count_o = 0
    for test in tests:
        for coordinates in test:
            if game.matrix[coordinates[0]][coordinates[1]] == 'X':
                count_x += 1
            if game.matrix[coordinates[0]][coordinates[1]] == 'O':
                count_o += 1
        if count_x == 3:
            x_wins += 1
        if count_o == 3:
            o_wins += 1
        count_x = 0
        count_o = 0

    if x_wins > 0:
        print('X wins')
        return True

    elif o_wins > 0:
        print('O wins')
        return True

    elif counter_of_space == 0:
        print('Draw')
        return True
    else:
        return False


def game_finished_hard_sim(matrix_to_test):
    counter_of_space = matrix_to_test.count(' ')
    x_wins = o_wins = 0
    tests = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    count_x = count_o = 0
    for test in tests:
        for coordinate in test:
            if matrix_to_test[coordinate] == 'X':
                count_x += 1
            if matrix_to_test[coordinate] == 'O':
                count_o += 1
        if count_x == 3:
            x_wins += 1
        if count_o == 3:
            o_wins += 1
        count_x = 0
        count_o = 0

    if x_wins > 0:
        return 'xwins'

    elif o_wins > 0:
        return 'owins'

    elif counter_of_space == 0:
        return 'draw'
    else:
        return False


def game_finished_hard():
    counter_of_space = game.matrix_state.count(' ')
    x_wins = o_wins = 0
    tests = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    count_x = count_o = 0
    for test in tests:
        for coordinate in test:
            if game.matrix_state[coordinate] == 'X':
                count_x += 1
            if game.matrix_state[coordinate] == 'O':
                count_o += 1
        if count_x == 3:
            x_wins += 1
        if count_o == 3:
            o_wins += 1
        count_x = 0
        count_o = 0

    if x_wins > 0:
        print('X wins')
        return 'xwins'

    elif o_wins > 0:
        print('O wins')
        return 'owins'

    elif counter_of_space == 0:
        print('Draw')
        return 'draw'
    else:
        return False


def sim_game_finished(sim_matrix):
    counter_of_space = 0

    for row in sim_matrix:
        counter_of_space += row.count(' ')

    x_wins = o_wins = 0
    tests = []
    for i in range(3):
        tests.append([[i, j] for j in range(3)])
    for i in range(3):
        tests.append([[j, i] for j in range(3)])
    tests.append([[i, i] for i in range(3)])
    tests.append([[abs(i - 2), i] for i in range(2, -1, -1)])

    count_x = count_o = 0
    for test in tests:
        for coordinates in test:
            if sim_matrix[coordinates[0]][coordinates[1]] == 'X':
                count_x += 1
            if sim_matrix[coordinates[0]][coordinates[1]] == 'O':
                count_o += 1
        if count_x == 3:
            x_wins += 1
        if count_o == 3:
            o_wins += 1
        count_x = 0
        count_o = 0

    if x_wins > 0:
        return 'x_wins'

    elif o_wins > 0:
        return 'o_wins'

    elif counter_of_space == 0:
        return 'draw'
    else:
        return False


def coordinates_input():
    user_coordinates = []
    valid_move = False
    valid_coordinate = bool
    while not valid_move:
        user_coordinates_input = input('Enter the coordinates:')
        try:
            user_coordinates = [int(x) - 1 for x in user_coordinates_input.split()]
        except TypeError:
            print('You should enter numbers!')
            continue
        if len(user_coordinates) != 2:
            continue
        for coordinate in user_coordinates:
            if coordinate < 0 or coordinate > 2:
                valid_coordinate = False
        if not valid_coordinate:
            print('Coordinates should be from 1 to 3!')
            continue
        position = game.matrix[user_coordinates[0]][user_coordinates[1]]
        if position == 'X' or position == 'O':
            print('This cell is occupied! Choose another one!')
            continue
        valid_move = True
    return user_coordinates


def make_user_move(user_coordinates, x_or_o):
    game.matrix[user_coordinates[0]][user_coordinates[1]] = x_or_o


def make_user_move_hard(coordinate, x_or_o):
    game.matrix_state[coordinate] = x_or_o


def make_ai_move_easy(x_or_o):
    available_coordinates = []
    i = 0
    for row in game.matrix:
        for position in row:
            if position == ' ':
                available_coordinates.append(i)
            i += 1
    random_position = random.choice(available_coordinates)
    coordinate1 = random_position // 3
    coordinate2 = random_position % 3
    print(f'Making move level "{game.GAME_MODE["AI_MODE"].lower()}"')
    game.matrix[coordinate1][coordinate2] = x_or_o


def make_ai_move_medium(x_or_o):
    checking_move = ['O', 'X']
    if x_or_o == 'O':
        checking_move = ['X', 'O']

    tests = []
    for i in range(3):
        tests.append([[i, j] for j in range(3)])
    for i in range(3):
        tests.append([[j, i] for j in range(3)])
    tests.append([[i, i] for i in range(3)])
    tests.append([[abs(i - 2), i] for i in range(2, -1, -1)])

    enemy = count_space = 0
    space_temp = 0
    for _ in range(0, 2):
        for test in tests:
            for coordinates in test:
                if game.matrix[coordinates[0]][coordinates[1]] == checking_move[_]:
                    enemy += 1
                if game.matrix[coordinates[0]][coordinates[1]] == ' ':
                    count_space += 1
                    space_temp = coordinates
            if count_space == 1 and enemy == 2:
                game.matrix[space_temp[0]][space_temp[1]] = x_or_o
                print(f'Making move level "{game.GAME_MODE["AI_MODE"].lower()}"')
                return
            enemy = count_space = 0

    make_ai_move_easy(x_or_o)


def hard_coordinates_input():
    valid_move = False
    valid_coordinate = bool
    while not valid_move:
        user_coordinates_input = input('Enter the coordinates:')
        try:
            user_coordinates = [int(x) - 1 for x in user_coordinates_input.split()]
        except TypeError:
            print('You should enter numbers!')
            continue
        if len(user_coordinates) != 2:
            continue
        for coordinate in user_coordinates:
            if coordinate < 0 or coordinate > 2:
                valid_coordinate = False
        if not valid_coordinate:
            print('Coordinates should be from 1 to 3!')
            continue
        coordinate = user_coordinates[0] * 3 + user_coordinates[1]
        position = game.matrix_state[coordinate]
        if position == 'X' or position == 'O':
            print('This cell is occupied! Choose another one!')
            continue
        valid_move = True
    return coordinate


def game_mode():
    valid_input = True
    while True:
        print('Tic-Tac-Toe game. \n'
              'AI can play at different levels: easy, medium, hard\n'
              'To start the game please type command: \n'
              'start <player 1> <player2>\n'
              'for example: start user hard\n'
              'or: start hard user\n'
              'type exit to quit')
        user_input = input('Input command:').split()
        if user_input[0] == 'exit':
            return user_input[0]

        elif len(user_input) != 3:
            print('Bad parameters!')
            continue

        elif user_input[0] == 'start':
            i = 1
            for word in user_input[1:len(user_input)]:
                if word.upper() not in game.GAME_MODE['AVAILABLE_MODES']:
                    valid_input = False
                    break
                game.GAME_MODE[f'PLAYER{i}'] = user_input[i].upper()
                if user_input[i] != 'user':
                    game.GAME_MODE['AI_MODE'] = user_input[i].upper()
                i += 1

            if not valid_input:
                print('Bad parameters!')
                continue

            return None
        else:
            print('Bad parameters!')


def simulate_moves_hard(original_coordinate, prev_matrix, x_or_o, iter):

    if game_finished_hard_sim(prev_matrix):
        if iter == 0:
            score_increment = 100
        elif iter < 10:
            score_increment = 10 - iter
        else:
            score_increment = 0

        if game_finished_hard_sim(prev_matrix) == 'draw':
            game.test_coordinates[original_coordinate]['draw'] += 1

        if game_finished_hard_sim(prev_matrix) == 'xwins':
            game.test_coordinates[original_coordinate]['xwins'] += 1
            if game.GAME_MODE['AI_PLAYS'] == 'X':
                game.test_coordinates[original_coordinate]['scores'] += score_increment
            if game.GAME_MODE['AI_PLAYS'] == 'O':
                game.test_coordinates[original_coordinate]['scores'] -= score_increment

        if game_finished_hard_sim(prev_matrix) == 'owins':
            game.test_coordinates[original_coordinate]['owins'] += 1
            if game.GAME_MODE['AI_PLAYS'] == 'O':
                game.test_coordinates[original_coordinate]['scores'] += score_increment
            if game.GAME_MODE['AI_PLAYS'] == 'X':
                game.test_coordinates[original_coordinate]['scores'] -= score_increment
        return

    if x_or_o == 'X':
        x_or_o = 'O'
    else:
        x_or_o = 'X'
    next_matrix = prev_matrix[:]
    available_coordinates = []
    i = 0
    for position in next_matrix:
        if position == ' ':
            available_coordinates.append(i)
        i += 1

    for coordinate in available_coordinates:
        next_matrix[coordinate] = x_or_o

        if game_finished_hard_sim(next_matrix):
            # score_increment = 0
            if iter == 0:
                score_increment = 100
            elif iter < 10:
                score_increment = 10 - iter
            else:
                score_increment = 0

            if game_finished_hard_sim(next_matrix) == 'draw':
                game.test_coordinates[original_coordinate]['draw'] += 1

            if game_finished_hard_sim(next_matrix) == 'xwins':
                game.test_coordinates[original_coordinate]['xwins'] += 1
                if game.GAME_MODE['AI_PLAYS'] == 'X':
                    game.test_coordinates[original_coordinate]['scores'] += \
                        score_increment
                if game.GAME_MODE['AI_PLAYS'] == 'O':
                    game.test_coordinates[original_coordinate]['scores'] -= \
                        score_increment

            if game_finished_hard_sim(next_matrix) == 'owins':
                game.test_coordinates[original_coordinate]['owins'] += 1
                if game.GAME_MODE['AI_PLAYS'] == 'O':
                    game.test_coordinates[original_coordinate]['scores'] += \
                        score_increment
                if game.GAME_MODE['AI_PLAYS'] == 'X':
                    game.test_coordinates[original_coordinate]['scores'] -= \
                        score_increment
            return
        next_matrix[coordinate] = ' '
    # if game is not finished call function again for deeper move
    for coordinate in available_coordinates:
        next_matrix[coordinate] = x_or_o
        simulate_moves_hard(original_coordinate, next_matrix[:], x_or_o, iter + 1)
        next_matrix[coordinate] = ' '


def make_ai_move_hard():
    game.test_coordinates = {}

    i = 0
    for position in game.matrix_state:
        if position == ' ':
            game.test_coordinates[i] = {'xwins': 0,
                                        'owins': 0,
                                        'draw': 0,
                                        'scores': 0}
        i += 1
    x_or_o = game.GAME_MODE['AI_PLAYS']

    iteration = 0
    next_matrix = game.matrix_state[:]
    for original_coordinate in game.test_coordinates:
        next_matrix[original_coordinate] = x_or_o
        simulate_moves_hard(original_coordinate, next_matrix[:], x_or_o,
                            iteration)
        next_matrix[original_coordinate] = ' '

    probabilities = {}
    for key, value in game.test_coordinates.items():
        probabilities[key] = value['scores']

    maxvalue = max(probabilities.values())
    next_move = list(filter(lambda x: x[1] == maxvalue, probabilities.items()))
    next_move_rand = random.choice(next_move)[0]
    game.matrix_state[next_move_rand] = game.GAME_MODE['AI_PLAYS']


def hard_game():
    while True:
        if game.GAME_MODE['PLAYER1'] == 'USER':
            game.GAME_MODE['USER_PLAYS'] = 'X'
            game.GAME_MODE['AI_PLAYS'] = 'O'
            hard_user_coordinates = hard_coordinates_input()
            make_user_move_hard(hard_user_coordinates, game.GAME_MODE['USER_PLAYS'])
        elif game.GAME_MODE['PLAYER1'] == 'HARD':
            game.GAME_MODE['AI_PLAYS'] = 'X'
            game.GAME_MODE['USER_PLAYS'] = 'O'
            make_ai_move_hard()

        make_matrix_hard()
        print_matrix()
        if game_finished_hard():
            break

        if game.GAME_MODE['PLAYER2'] == 'USER':
            game.GAME_MODE['USER_PLAYS'] = 'O'
            game.GAME_MODE['AI_PLAYS'] = 'X'
            hard_user_coordinates = hard_coordinates_input()
            make_user_move_hard(hard_user_coordinates, game.GAME_MODE['USER_PLAYS'])
        elif game.GAME_MODE['PLAYER2'] == 'HARD':
            game.GAME_MODE['USER_PLAYS'] = 'X'
            game.GAME_MODE['AI_PLAYS'] = 'O'
            make_ai_move_hard()

        make_matrix_hard()
        print_matrix()
        if game_finished_hard():
            break


def make_move(x_or_o):
    if x_or_o == 'X' and game.GAME_MODE['PLAYER1'] == game.USER:
        user_coordinates = coordinates_input()
        make_user_move(user_coordinates, x_or_o)
    elif x_or_o == 'O' and game.GAME_MODE['PLAYER2'] == game.USER:
        user_coordinates = coordinates_input()
        make_user_move(user_coordinates, x_or_o)
    elif game.GAME_MODE['AI_MODE'] == 'EASY':
        make_ai_move_easy(x_or_o)
    elif game.GAME_MODE['AI_MODE'] == 'MEDIUM':
        make_ai_move_medium(x_or_o)
    elif game.GAME_MODE['AI_MODE'] == 'HARD':
        make_ai_move_hard()


if __name__ == '__main__':
    game = GameState
    mode = game_mode()
    if mode == 'exit':
        exit()
    initial_state = '         '
    game.matrix_state = list(initial_state)
    make_matrix(initial_state)
    print_matrix()
    if game.GAME_MODE['AI_MODE'] == 'HARD':
        hard_game()
        exit()
    while True:
        make_move('X')
        print_matrix()
        if game_finished():
            break
        make_move('O')
        print_matrix()
        if game_finished():
            break

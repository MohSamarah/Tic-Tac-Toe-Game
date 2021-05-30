import copy
import math

X = "X"
O = "O"
EMPTY = None
best_action = tuple


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count = 0
    o_count = 0
    state_player = board
    for i in range(3):
        for j in range(3):
            if state_player[i][j] == X:
                x_count += 1
            elif state_player[i][j] == O:
                o_count += 1

    if x_count > o_count:
        return O
    return X


def actions(board):
    new_states = set()
    state_action = board
    for i in range(3):
        for j in range(3):
            if state_action[i][j] == EMPTY:
                tup = (i, j)
                new_states.add(tup)
    return new_states


def result(board, action):
    state_result = copy.deepcopy(board)
    state_result[action[0]][action[1]] = player(board)
    return state_result


def winner(board):
    value = board[0][0]
    if board[0][1] == value and board[0][2] == value and value is not None:
        return value
    if board[1][1] == value and board[2][2] == value and value is not None:
        return value
    if board[1][0] == value and board[2][0] == value and value is not None:
        return value
    value = board[0][1]
    if board[1][1] == value and board[2][1] == value and value is not None:
        return value
    value = board[0][2]
    if board[1][1] == value and board[2][0] == value and value is not None:
        return value
    if board[1][2] == value and board[2][2] == value and value is not None:
        return value
    value = board[1][0]
    if board[1][1] == value and board[1][2] == value and value is not None:
        return value
    value = board[2][0]
    if board[2][1] == value and board[2][2] == value and value is not None:
        return value
    return None


def terminal(board):
    if winner(board) is not None:
        return True
    elif EMPTY not in board[0] and EMPTY not in board[1] and EMPTY not in board[2]:
        return True
    return False


def utility(board):
    if terminal(board):
        if winner(board) == 'X':
            return 1
        elif winner(board) == 'O':
            return -1
        return 0


def minimax(board):
    global best_action

    def best_move_x(board):
        global best_action
        best_score = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = min_value(new_board)
            if best_score < score:
                best_score = score
                best_action = action
                if best_score == 1:
                    return best_action
        return best_action

    def best_move_o(board):
        global best_action
        best_score = math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = max_value(new_board)
            if best_score > score:
                best_score = score
                best_action = action
                if best_score == -1:
                    return best_action
        return best_action

    def max_value(state):
        if terminal(state):
            return utility(state)
        v = -math.inf
        for action in actions(state):
            v = max(v, min_value(result(state, action)))
            if v == 1:
                return v
        return v

    def min_value(state):
        if terminal(state):
            return utility(state)
        v = math.inf
        for action in actions(state):
            v = min(v, max_value(result(state, action)))
            if v == -1:
                return v
        return v

    if player(board) == 'X':
        return best_move_x(board)
    else:
        return best_move_o(board)

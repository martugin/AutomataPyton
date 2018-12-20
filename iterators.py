from typing import *
from automata import Automaton, LetterAction


def next_letter(action: LetterAction) -> bool:
    """
    Obtains the next letter action
    :param action: previous action
    :return: True, if the action is not the last
    """
    index = len(action)-1
    while index >= 0 and action[index] == len(action)-1:
        action[index] = 0
        index -= 1
    if index >= 0:
        action[index] += 1
        return True
    return False


def iter_all_dfa(letters_count: int, states_count: int) -> Iterable[Automaton]:
    """
    Iteration of all DFAs with fixed letters and states count
    :param letters_count: letters count
    :param states_count: states count
    :return: Iterable of all DFAs
    """
    automaton = Automaton(
        [LetterAction([0] * states_count) for _ in range(letters_count)])
    while True:
        yield automaton
        letter_num = letters_count - 1
        while letter_num >= 0 and not next_letter(automaton[letter_num]):
            letter_num -= 1
        if letter_num < 0:
            break

from dataclasses import dataclass
from typing import *
from collections import deque
from automata import Automaton


@dataclass
class BfsState:
    """
    Information for one vertex in BFS
    """
    front: int  # Number of wave front
    letter: int  # incoming letter
    previous: FrozenSet[int]  # previous set


ALPHABET = "abcdefgh"


def bfs(automaton: Automaton,
        start_set: frozenset,
        check_end: Callable[[FrozenSet[int]], bool],
        check_error: Callable[[FrozenSet[int]], bool],
        ) -> Tuple[int, str]:
    """
    BFS for a way from start set to some final set in a given automaton
    :param automaton: automaton
    :param start_set: start set
    :param check_end: end-set checking function
    :param check_error: forbidden set acting function
    :return: pair: length of shortest reaching word and word
    """
    visited = {}  # type: Dict[FrozenSet[int], BfsState]
    sets_queue = deque([start_set])
    visited[start_set] = BfsState(0, -1, frozenset())

    while len(sets_queue) > 0:
        cur_set = sets_queue.popleft()
        front = visited[cur_set].front + 1
        for index, letter in enumerate(automaton):
            new_set = letter.apply_to_set(cur_set)
            if new_set not in visited and not check_error(new_set):
                visited[new_set] = BfsState(front, index, cur_set)
                sets_queue.append(new_set)

            if check_end(new_set):
                word = ""
                set_ = new_set
                while True:
                    bfs_state = visited[set_]
                    if bfs_state.front == 0:
                        break
                    word = ALPHABET[bfs_state.letter] + word
                    set_ = bfs_state.previous
                return front, word
    return -1, ""


def find_sync_word(automaton: Automaton):
    """
    Finds the shortest synchronizing word in a given automaton
    :param automaton: automaton to search the synchronizing word
    :return: pair: length of shortest synchronizing word and word
    """
    return bfs(automaton,
               frozenset(range(automaton.states_count)),
               lambda set_: len(set_) == 1,
               lambda set_: -1 in set_
               )

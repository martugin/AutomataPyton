from typing import *


class LetterAction:
    """
    An action of one automaton letter
    """
    def __init__(self, action: List[int]):
        """
        The constructor for LetterAction
        :param action: transition function
        """
        self._action = action

    def __str__(self):
        """
        :return: String representation of the class object
        """
        return " ".join(map(str, self._action))

    def __repr__(self):
        return self.__str__

    def __len__(self):
        return len(self._action)

    def __getitem__(self, item: int) -> int:
        return self._action[item]

    def __setitem__(self, key: int, value: int):
        self._action[key] = value

    def apply(self, state: int) -> int:
        """
        Apply the letter to the state
        :param state: initial state
        :return: result state
        """
        return self._action[state]

    def apply_to_pair(self, pair: Tuple[int, int]) -> Tuple[int, int]:
        """
        Apply the letter to the pair of states
        :param pair: initial pair
        :return: result pair
        """
        (first, second) = pair
        return self.apply(first), self.apply(second)

    def apply_to_set(self, states: FrozenSet[int]) -> FrozenSet[int]:
        """
        Apply the letter to the set of states
        :param states: initial set
        :return: result set
        """
        return frozenset({self.apply(x) for x in states})


class Automaton:
    """
    DFA
    """
    def __init__(self, letters: List[LetterAction]):
        self._letters = letters

    def __str__(self):
        return "\n".join(map(str, self.letters))

    def __repr__(self):
        return self.__str__

    def __len__(self):
        return len(self.letters)

    def __getitem__(self, item: int) -> LetterAction:
        return self.letters[item]

    def __iter__(self):
        return (letter for letter in self.letters)

    @property
    def letters(self) -> List[LetterAction]:
        """ List of automaton letters """
        return self._letters

    @property
    def letters_count(self) -> int:
        """ Number of automaton letters """
        return len(self._letters)

    @property
    def states_count(self) -> int:
        """ Number of automaton states """
        if self.letters_count > 0:
            return len(self._letters[0])
        else:
            return 0

    def apply(self, letter: int, state: int) -> int:
        """
        Apply the letter to the state
        :param letter: letter number
        :param state: initial state
        :return: result state
        """
        return self.letters[letter].apply(state)

    def apply_to_set(self, letter: int, states: FrozenSet[int]) -> FrozenSet[int]:
        """
        Apply the letter to the set of states
        :param letter: letter number
        :param states: initial set
        :return: result set
        """
        return self.letters[letter].apply_to_set(states)

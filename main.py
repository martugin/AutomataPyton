import iterators
import algorithms


def main():
    for automaton in iterators.iter_all_dfa(2, 5):
        length, word = algorithms.find_sync_word(automaton)
        if length >= 16:
            print(automaton)
            print(str(length) + " " + word + "\n")


if __name__ == "__main__":
    main()

import copy
import random

from generator import generate_puzzle as _generate_puzzle
from default_puzzles import DEFAULT_PUZZLES


def get_puzzle(difficulty='medium'):
    return _generate_puzzle(difficulty)


def get_default_puzzle(difficulty='medium'):
    options = DEFAULT_PUZZLES.get(difficulty)
    if not options:
        return _generate_puzzle(difficulty)
    choice = random.choice(options)
    return copy.deepcopy(choice['puzzle']), copy.deepcopy(choice['solution'])

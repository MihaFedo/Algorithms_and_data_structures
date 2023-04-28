import sys
from typing import Tuple

COUNT_INPUT_LINES = 4

def input_data() -> Tuple[int, list]:
    n = int(sys.stdin.readline().rstrip())
    game_data = ''
    for i in range(COUNT_INPUT_LINES):
        game_data += sys.stdin.readline().rstrip()
    return n, list(game_data)

def input_list_into_dict(input_list: list) -> dict:
    game_data_dict = dict((i, input_list.count(i)) for i in input_list if i != '.')
    return game_data_dict

def main() -> None:
    n, game_data = input_data()
    game_data_dict = input_list_into_dict(game_data)
    result = sum(1 for i in game_data_dict.values() if i <= 2 * n)
    print(result)


if __name__ == '__main__':
    main()
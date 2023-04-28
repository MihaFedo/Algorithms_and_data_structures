import sys
from typing import Tuple, Union

class Deque:
    def __init__(self, n) -> None:
        self.__deque = [None] * n
        self.__max_n = n
        self.__head = n - 1
        self.__tail = 0
        self.__size = 0
    
    def is_empty(self) -> bool:
        return self.__size == 0

    def border_index_increase(self, border_index) -> int:
        return (border_index + 1) % self.__max_n

    def border_index_decrease(self, border_index) -> int:
        return (border_index - 1) % self.__max_n
        

    def push_back(self, item_value) -> None:
        if self.__size < self.__max_n:
            self.__deque[self.__tail] = item_value
            self.__tail = self.border_index_increase(self.__tail)
            self.__size += 1
        else:
            print('error')
    
    def push_front(self, item_value) -> None:
        if self.__size < self.__max_n:
            self.__deque[self.__head] = item_value
            self.__head = self.border_index_decrease(self.__head)
            self.__size += 1
        else:
            print('error')
   
    def pop_front(self) -> Union[str, int]:
        if self.is_empty():
            return 'error'
        item_for_del = self.border_index_increase(self.__head)
        pop_front_item_value = self.__deque[item_for_del]
        self.__deque[item_for_del] = None
        self.__head = item_for_del
        self.__size -= 1
        return pop_front_item_value
    
    def pop_back(self) -> Union[str, int]:
        if self.is_empty():
            return 'error'
        item_for_del = self.border_index_decrease(self.__tail)
        pop_back_item_value = self.__deque[item_for_del]
        self.__deque[item_for_del] = None
        self.__tail = item_for_del
        self.__size -= 1
        return pop_back_item_value

def input_data() -> Tuple[int, list]:
    n_com = int(sys.stdin.readline().rstrip())
    m = int(sys.stdin.readline().rstrip())
    command_list = []
    for i in range(n_com):
        command_list.append(sys.stdin.readline().rstrip())
    return m, command_list


def main() -> None:
    m, command_list = input_data()
    deque = Deque(m)
    for command in command_list:
        try:
            print(getattr(deque, command)())
        except AttributeError:
            getattr(deque, command.split()[0])(command.split()[1])


if __name__ == '__main__':
    main()
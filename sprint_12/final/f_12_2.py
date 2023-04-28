import sys
import operator

OPS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
}

class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(int(item))

    def pop(self) -> int:
        return self.items.pop()
    
    def peek(self) -> None:
        return self.items[-1]


def calc(item_1, oper, item_2) -> int:
    return OPS[oper](item_1, item_2)


def main() -> None:
    stack = Stack()
    stroka = sys.stdin.readline().rstrip().split()
    for i in stroka:
        if i in OPS.keys():
            item_2 = stack.pop() 
            item_1 = stack.pop()
            res = calc(item_1, i, item_2)
            stack.push(res)
        else:
            stack.push(i)
    print(stack.peek())
    


if __name__ == '__main__':
    main()

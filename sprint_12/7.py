import sys

class StackMaxEffective:
    def __init__(self):
        self.items = []
        self.cur_max = []

    def push(self, item):
        if len(self.items) == 0:
            self.cur_max.append(item)
        else:
            if item >= self.cur_max[-1]:
                self.cur_max.append(item)
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return print('error')
        else:
            pop_item = self.items.pop()
            if pop_item == self.cur_max[-1]:
                self.cur_max.pop()
            return pop_item
        

    def get_max(self):
        if len(self.items) == 0:
            return None
        else:
            return self.cur_max[-1]

def main():
    stack = StackMaxEffective()
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        stroka = sys.stdin.readline().rstrip()
        if stroka == 'get_max':
            print(stack.get_max())
        elif stroka == 'pop':
            stack.pop()
        else:
            stroka = stroka.split()
            stack.push(int(stroka[1]))
    


if __name__ == '__main__':
    main()

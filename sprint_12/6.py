import sys

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return print('error')
        else:
            return self.items.pop()
        

    def get_max(self):
        if len(self.items) == 0:
            return None
        else:
            return max(self.items)

def main():
    stack = StackMax()
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        stroka = sys.stdin.readline().rstrip().split()
        if stroka[0] == 'get_max':
            print(stack.get_max())
        elif stroka[0] == 'pop':
            stack.pop()
        else:
            stack.push(int(stroka[1]))
    


if __name__ == '__main__':
    main()

import sys

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0
    
    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size < self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return print('error')
   
    def pop(self):
        if self.is_empty():
            return None
        pop_item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return pop_item
        

    def peek(self):
        if self.is_empty():
            return None
        peek_item = self.queue[self.head]
        return peek_item

def main():
    n_com = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    queue = MyQueueSized(n)
    for i in range(n_com):
        stroka = sys.stdin.readline().rstrip()
        if stroka == 'peek':
            print(queue.peek())
        elif stroka == 'pop':
            print(queue.pop())
        elif stroka == 'size':
            print(queue.size)
        else:
            stroka = stroka.split()
            queue.push(int(stroka[1]))
    


if __name__ == '__main__':
    main()
import sys

class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item

class MyQueue:
    def __init__(self):
        self.size = 0
        self.start_node = None

    def put(self, item):
        new_node = Node(item)
        if self.start_node == None:
            self.start_node = new_node
            self.size = 1
        else:
            n = self.start_node
            while n.next_item:
                n = n.next_item
            n.next_item = new_node
            self.size += 1
            
    def size_q(self):
        return self.size
    
    def get(self):
        if self.size == 0:
            return 'error'
        first_item_del = self.start_node.value
        self.start_node = self.start_node.next_item
        self.size -= 1
        return first_item_del

def main():
    n_com = int(sys.stdin.readline().rstrip())
    
    queue = MyQueue()
    for i in range(n_com):
        stroka = sys.stdin.readline().rstrip()
        if stroka == 'get':
            print(queue.get())
        elif stroka == 'size':
            print(queue.size_q())
        else:
            stroka = stroka.split()
            queue.put(int(stroka[1]))
    


if __name__ == '__main__':
    main()
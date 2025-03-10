class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, valor):
        self.queue.append(valor)
    
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue          
    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Elemento" q.queue)
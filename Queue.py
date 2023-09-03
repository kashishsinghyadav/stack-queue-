queue=[]
def enqueue():
    data=int(input('enter the data'))
    queue.append(data)
    print(queue)
    
def dequeue():
    queue.pop(0)
    print(queue)
    
    
def peek():
    print('the peek element')
    print(queue[-1])
    
    
def p():
    print(queue)
    
    
while True:
    ele=int(input('enter the number'))
    if ele==1:
        enqueue()
    elif ele==2:
        dequeue()
    elif ele==3:
        peek()
    elif ele==4:
        p()
    else:
        break

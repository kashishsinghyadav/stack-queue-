stack=[]
def push():
    ele=int(input('enter the elemnt'))
    stack.append(ele)
    print(stack)
    
def pop():
    stack.pop()
    print(stack)
def size():
    print('the size of stack is')
    print(len(stack))
    
def peek():
    ele=stack[-1]
    print('the peek ele of stack is',ele)
    
    
while True:
    n=int(input('enter the choice'))
    if n==1:
        push()
    elif n==2:
        pop()
    elif n==3:
        size()
    elif n==4:
        peek()
    else:
        break
    
    
    
    
    
    
    
    
    
    
    

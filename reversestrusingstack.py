def reversestring(st):
    stack=[]
    ans=''
    for i in range(len(st)):
        stack.append(st[i])
    
    i=0  
    while stack:
        ans+=stack.pop()
        
    return ans
    
st='abc'
print(reversestring(st))



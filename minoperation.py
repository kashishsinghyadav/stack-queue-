class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]

        n=len(s)

        for i in range(n):
            
            if stack and s[i]==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
            
           
        return len(stack)
        

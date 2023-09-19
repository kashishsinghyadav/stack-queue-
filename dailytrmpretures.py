class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        

        n=len(temperatures)
        ans=[0]*n
        c=0

        for i in range(n-1,-1,-1):
            
            curr=temperatures[i]
            while stack and temperatures[stack[-1]]<=curr:
               
                stack.pop()
            if len(stack)==0:
                ans[i]=0
            else:
                ans[i]=stack[-1]-i

            stack.append(i)
        return ans

        
        

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for a in asteroids:
            while stack and a<0 and stack[-1]>0:
                res=a+stack[-1]
                if res<0:
                    stack.pop()
                elif res>0:
                    a=0
                else:
                    a=0
                    stack.pop()
            if a:
                stack.append(a)
        return stack
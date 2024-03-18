class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #convert=-1
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


        '''
        for i in range(len(asteroids)-1,-1,-1):
            if len(asteroids)>1:
                a=asteroids.pop()
                b=asteroids.pop()

                if a<=-1 and b>-1:
                    a*=convert

                    if a>b:
                        a*=convert
                        asteroids.append(a)
                    elif a<b:
                        asteroids.append(b)
                else:
                    asteroids.append(b)
                    asteroids.append(a)
        return asteroids
        '''
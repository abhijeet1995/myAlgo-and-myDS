class GeeksforGeeks:
    def geekgame(self,N,X,Y,turn):
        if turn==0 and N==0:
            return False
        if turn==1 and N==0:
            return True
        if turn==0 and N==1:
            return True
        if turn==1 and N==1:
            return False
        res=False
        if turn==0:
            if X<=N:
                res=res or self.geekgame(N-X,X,Y,1)
            if Y<=N:
                res=res or self.geekgame(N-Y,X,Y,1)
            res=res or self.geekgame(N-1,X,Y,1)
            return res
        else:
            if X<=N:
                res=res or self.geekgame(N-X,X,Y,0)
            if Y<=N:
                res=res or self.geekgame(N-Y,X,Y,0)
            res =res or self.geekgame(N-1,X,Y,0)
            return res
t=input()
a=GeeksforGeeks()
for i in range(0,int(t)):
    N,X,Y=input().split(' ')
    if a.geekgame(int(N),int(X),int(Y),0):
        print('G')
    else:
        print('N')

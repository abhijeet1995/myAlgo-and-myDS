class Name:
    def __init__(self):
        self.ar=[]
    def sumtotal(self,A):
        s=0
        for element in A:
            s+=element
        return s

    def maxsumcont(self,A):
        if len(A)==0:
            return
        temp=self.sumtotal(A)
        #print("temp="+str(temp))
        try:
            if self.max < temp:
                self.max = temp
        except AttributeError:
            self.max=temp
        #print("max="+str(self.max))
        self.maxsumcont(A[1:])
        self.maxsumcont(A[1:len(A)-1])
        self.maxsumcont(A[:len(A)-1])
        return self.max

n=Name()
print(n.maxsumcont([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))

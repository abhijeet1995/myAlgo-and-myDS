class FindPath:
    def min_of(self,a,b):
        if a>b:
            return b
        else:
            return a

    def find_path(self,path):
        if path[0]==0 or len(path)==0:
            return float('inf')
        cal=[0]*len(path)
        for i in range(1,len(path)):
            cal[i]=float('inf')
            for j in range(0,i):
                if j+path[j]>=i and cal[j]!=float('inf'):
                    cal[i]=self.min_of(cal[j]+1,cal[i])
                    break

        return cal[len(cal)-1]

a=FindPath()
result=a.find_path([1,3,5,8,9,2,6,7,6,8,9])
print(result)

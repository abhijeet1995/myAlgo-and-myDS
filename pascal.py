def generate(A):
        br=[]
        for i in range(0,A):
            ar=[]
            temp=pow(11,i)
            print(temp)
            if temp//10==0:
                print(temp)
                ar.append(temp)
            else:
                while temp!=0:
                    ar.insert(0,temp%10)
                    temp=temp//10
            br.append(ar)
        return br
print(generate(100))

def largestNumber(A):
        B=""
        for i in range(0,len(A)):
            temp=A[i]
            if A[i]/10==0:
                temp2=temp
                temp=A[i]
            else:
                temp1=A[i]
                while temp1!=0:
                    temp2=temp
                    temp=temp1%10
                    temp1/=10
            if B=="":
                B=B+str(A[i])
            else:
                if temp2>temp:
                    B=B+str(A[i])
                else:
                    B=str(A[i])+B
        return B
print(largestNumber([36,5,4,9,85]))

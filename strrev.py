def reverseWords(A):
        A=A.strip().split()
        B=""
        i=len(A)-1
        while i>=0:
            if len(A[i])!=0:
                B=B+" "+A[i]
            i-=1
        return B.strip()
print(reverseWords("      my    name   is   abhijeet  "))

def maxof(a,b):
    if a>b:
        return a
    else:
        return b

def lcs(A,B):
    if len(A)==0 or len(B)==0:
        return 0
    elif A[len(A)-1]==B[len(B)-1]:
        return 1+lcs(A[:len(A)-1],B[:len(B)-1])
    else:
        return maxof(lcs(A[:len(A)-1],B),lcs(A,B[:len(B)-1]))

print(lcs('AGGTAB','GXTXAYB'))

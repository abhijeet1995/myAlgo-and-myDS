def merge(A, B):
	    i=0
	    j=0
	    res=[]
	    while i<len(A) and j<len(B):
	        if A[i]>B[j]:
	            res.append(B[j])
	            j+=1
	        elif A[i]<B[j]:
	            res.append(A[i])
	            i+=1
	        else:
	            res.append(A[i])
	            res.append(B[j])
	            i+=1
	            j+=1
	    while i<len(A):
	        res.append(A[i])
	        i+=1
	    while j<len(B):
	        res.append(B[j])
	        j+=1
	    return res
print(merge([1,3,5],[2,4]))

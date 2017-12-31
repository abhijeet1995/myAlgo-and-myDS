max=0
def ip(B):
    C=B[::-1]
    if C==B:
        if len(B)>max:
            max=len(B)
        return True
    else:
        return False

def longestPalindrome(A):
    x=ip(A)
    if x:
        if max==len(A):
            return A
    longestPalindrome(A[1:])
    longestPalindrome(A[:len(A)-1])
    longestPalindrome(A[1:len(A)-1])

longestPalindrome("abhijeet")

class Solution:
	# @param A : string
	# @return an integer
	def sum(a,b):
	    if a=='M':
	        if b=='M':
	            return 2000
	        elif b=='D':
	            return 1500
	        elif b=='C':
	            return 1100
	        elif b=='L':
	            return 1050
	        elif b=='X':
	            return 1010
	        elif b=='V':
	            return 1005
	        elif b=='I':
	            return 1001
	    elif a=='D':
	        if b=='D':
	            return 1000
	        elif b=='C':
	            return 600
	        elif b=='L':
	            return 550
	        elif b=='X':
	            return 510
	        elif b=='V':
	            return 505
	        elif b=='I':
	            return 501
	    elif a=='C':
	        if b=='C':
	            return 200
	        elif b=='L':
	            return 150
	        elif b=='X':
	            return 110
	        elif b=='V':
	            return 105
	        elif b=='I':
	            return 101
	    elif a=='L':
	        if b=='L':
	            return 100
	        elif b=='X':
	            return 60
	        elif b=='V':
	            return 55
	        elif b=='I':
	            return 51
	    elif a=='X':
	        if b=='X':
	            return 20
	        elif b=='V':
	            return 15
	        elif b=='I':
	            return 11
	    elif a=='V':
	        if b=='V':
	            return 10
	        elif b=='I':
	            return 6
	    elif a=='I':
	        if b=='I':
	            return 2

	def sub(a,b):
	    if a=='M':
	        if b=='D':
	            return 500
	        elif b=='C':
	            return 900
	        elif b=='L':
	            return 950
	        elif b=='X':
	            return 990
	        elif b=='V':
	            return 995
	        elif b=='I':
	            return 999
	    elif a=='D':
	        if b=='C':
	            return 400
	        elif b=='L':
	            return 450
	        elif b=='X':
	            return 490
	        elif b=='V':
	            return 495
	        elif b=='I':
	            return 499
	    elif a=='C':
	        if b=='L':
	            return 50
	        elif b=='X':
	            return 90
	        elif b=='V':
	            return 95
	        elif b=='I':
	            return 99
	    elif a=='L':
	        if b=='X':
	            return 40
	        elif b=='V':
	            return 45
	        elif b=='I':
	            return 49
	    elif a=='X':
	       if b=='V':
	            return 5
	       elif b=='I':
	            return 9
	    elif a=='V':
	       if b=='I':
	            return 4

	def romanToInt(self, A):
	    sum=0
        t=len(A)
        t=t-1
        for i in range(t,0,-2):
            temp=A[i];
            temp1=-1
            if i>0:
                temp1=A[i-1];
            if temp=='M':
                if temp1!=-1:
                    if temp1=='M':
                        sum=sum+add(temp,temp1)
                    else:
                        sum=sum+sub(temp,temp1)
                else:
                    sum=sum+1000;
            elif temp=='D':
                if temp1!=-1:
                    if temp1=='D' or temp1=='M':
                        sum=sum+add(temp,temp1)
                    else:
                        sum=sum+sub(temp,temp1)
                else:
                    sum=sum+500;
            elif temp=='C':
                if temp1!=-1:
                    if temp1=='D' or temp1=='M' or temp1=='C':
                        sum=sum+add(temp,temp1)
                    else:
                        sum=sum+sub(temp,temp1)
                else:
                    sum=sum+100;
            elif temp=='L':
               if temp1!=-1:
                    if temp1=='D' or temp1=='M' or temp1=='C' or temp1=='L':
                        sum=sum+add(temp,temp1)
                    else:
                        sum=sum+sub(temp,temp1)
               else:
                    sum=sum+50;
            elif temp=='X':
                if temp1!=-1:
                    if temp1=='D' or temp1=='M' or temp1=='C' or temp1=='L' or temp1=='X':
                        sum=sum+add(temp,temp1)
                    else:
                        sum=sum+sub(temp,temp1)
                else:
                    sum=sum+10;
            elif temp=='V':
                if temp1!=-1:
                    if (temp1=='D' or temp1=='M' or temp1=='C' or temp1=='L' or temp1=='X' or temp1=='V'):
                        sum=sum+add(temp,temp1)
                    else:
                        sum=sum+sub(temp,temp1)
                else:
                    sum=sum+5;
            else:
                if temp1!=-1:
                    sum=sum+add(temp,temp1)
                else:
                    sum=sum+1
    return sum

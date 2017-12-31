def activity(start, finish):
    i=0
    print(i)
    for j in range(1,len(start)):
        if start[j]>=finish[i]:
            print(j)
            i=j

start=[]
finish=[]
n=int(input('enter no of jobs'))
for i in range(0,n):
    start.append(int(input('enter start time: ')))
    finish.append(int(input('enter finish time: ')))

for i in range(0,len(finish)-1):
     for j in range(i+1,len(finish)):
         if finish[j]<finish[i]:
             temp=finish[j]
             finish[j]=finish[i]
             finish[i]=temp
             temp=start[j]
             start[j]=start[i]
             start[i]=temp
activity(start, finish)

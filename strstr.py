def strStr(haystack, needle):
        #print("inside function")
        for i in range(0,len(haystack)):
            #print("inside 1st loop")
            #print("haystack = ",str(haystack[i]))
            #print("needle = "+str(needle[i]))
            if haystack[i]==needle[0]:
                #print("haystack = ",str(haystack[i]))
                #print("needle = "+str(needle[i]))
                temp=i
                for j in range (0,len(needle)):
                    print("haystack = ",str(haystack[temp]))
                    print("needle = "+str(needle[j]))
                    if haystack[temp]==needle[j]:
                        temp+=1
                    else :
                        break
                if len(needle)==temp-i:
                    return i
        #print("outside of main loop")
        return -1
print(strStr("my name is abhijeet"," name "))

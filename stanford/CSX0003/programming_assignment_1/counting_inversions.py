#numberlist = [1,2,4,5,432,24,79,75,89,72]
def Sort_And_Count(numberList,length):
    if length==1:
        return numberList,0
    else :
        B,X= Sort_And_Count(numberList[:length//2],length//2)
        C,Y= Sort_And_Count(numberList[(length//2):],length-(length//2))
        D,inv_count= new_function(B,C)
    return D,(X+Y+inv_count)
    
array_1=[8]
array_2=[4,7]

def new_function(array_1,array_2):
    merged_array=[]
    a1_index=a2_index=0
    count=0
    #i<j and b[i]>c[j] ==> count+=1
    while a1_index<len(array_1) and a2_index<len(array_2):
        if array_1[a1_index]>array_2[a2_index]:
            count+=len(array_1[a1_index:])
            merged_array.append(array_2[a2_index])
            a2_index+=1
        else:
            merged_array.append(array_1[a1_index])
            a1_index+=1
    merged_array+=array_1[a1_index:]
    merged_array+=array_2[a2_index:]
    return merged_array,count


# numberlist = [6,1,3,0]
# Sort_And_Count(numberlist,len(numberlist))

# new_function(array_1,array_2)
def loadNumbers():
    File = open("IntegerArray.txt","r")
    data = File.readlines()
    return [int(num.strip()) for num in data]

numberlist = loadNumbers()
# numberlist=[8,7,4]
# numberlist = [1,2,4,5,432,24,79,75,89,72]
print(Sort_And_Count(numberlist,len(numberlist)))



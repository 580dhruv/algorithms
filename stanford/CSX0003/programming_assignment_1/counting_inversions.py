def sort_and_count(number_list,length):
    if length==1:
        return number_list,0
    else :
        left_half,left_inner_inv= sort_and_count(number_list[:length//2],length//2)
        right_half,right_inner_inv= sort_and_count(number_list[(length//2):],length-(length//2))
        merged_list,inv_count= merge_and_count_split_inversions(left_half,right_half)
    return merged_list,(left_inner_inv+right_inner_inv+inv_count)

def merge_and_count_split_inversions(left_half,right_half):
    merged_array=[]
    left_array_index=right_array_index=0
    count=0    
    while left_array_index<len(left_half) and right_array_index<len(right_half):
        if left_half[left_array_index]>right_half[right_array_index]:
            count+=len(left_half[left_array_index:])
            merged_array.append(right_half[right_array_index])
            right_array_index+=1
        else:
            merged_array.append(left_half[left_array_index])
            left_array_index+=1
    merged_array+=left_half[left_array_index:]
    merged_array+=right_half[right_array_index:]
    return merged_array,count

def load_numbers():
    file = open("IntegerArray.txt","r")
    file_data = file.readlines()
    return [int(num.strip()) for num in file_data]

number_list = load_numbers()
print(sort_and_count(number_list,len(number_list)))



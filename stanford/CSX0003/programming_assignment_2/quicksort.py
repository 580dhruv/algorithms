def load_numbers():
    file = open('QuickSort.txt','r')
    number_list = file.readlines()
    return [int(number.strip()) for number in number_list]

total = 0
def count_comparisons(number_list,length):
    merged =[]
    print("number_list :",number_list)
    if length<=1:
        return number_list
    else :
        p = choose_pivot(number_list)
        index = partition_number_list(number_list,p)
        print("index :",index)
        left_half = number_list[:index]
        right_half = number_list[index+1:]
        print("left :",left_half,"right :",right_half)
        first_half = count_comparisons(left_half,len(left_half))
        second_half = count_comparisons(right_half,len(right_half))
        merged+=first_half+second_half
        print("merged :", merged)
        merged.insert(index,p)
        print("merged :", merged)
        return merged

def choose_pivot(number_list):
    return number_list[0]

def partition_number_list(number_list,pivot):
    left = 0
    right = len(number_list)
    boundary_point=left+1
    for iterator_index in range(left+1,right):
        if number_list[iterator_index]< pivot:
            number_list[boundary_point],number_list[iterator_index] = number_list[iterator_index], number_list[boundary_point]
            boundary_point += 1
    number_list[left],number_list[boundary_point-1] = number_list[boundary_point-1],number_list[left]
    print("Partition numberlist :",number_list)
    return boundary_point-1


number_list = list(load_numbers())
# number_list =[3,8,2,5,1,4,7,6]
# number_list =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# number_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# number_list = [5, 1, 8, 3, 7, 10, 2, 9, 6, 4]
# number_list = [5, 3, 8, 3, 1, 7, 5, 3, 2, 8]
# number_list = [7, 7, 7, 7, 7, 7, 7, 7]
print(number_list)
print(count_comparisons(number_list,len(number_list)))


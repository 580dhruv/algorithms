# importing required modules
import random
# method to load_numbers from the file
def load_numbers(filename):
    file = open(filename,"r")       # opening the file in read mode
    data = file.read()              # reading the data from the opened file above
    # separating the data using ',' from the read data and typecasting to int
    number_list = [int(number) for number in data.split(',')]
    return number_list              # returning the cleaned number_list
# method to find the ith order statistic from the number_list
def number_selection(number_list,length,order_statistic):
    if length==1:                   # validating the length of number whether it is 0 or not
        return number_list[0]           # returning the number at 0th index in the number_list
    else:
        pivot = pivot_selection(number_list,length)     # calling pivot selection method which will return the pivot
        partition_index = partition_number_list(number_list,pivot)  # partition number_list around pivot
        if partition_index==order_statistic:    # checking whether partition_index and order statistic are equal are not
            return pivot                               # return pivot
        if partition_index>order_statistic:     # checking whether partition index is greater than the order statistic
            return number_selection(number_list[:partition_index],partition_index,order_statistic)  # return left part of the partition
        if partition_index<order_statistic:     # checking whether partition index is less than the order statistic
            return number_selection(number_list[partition_index+1:],length-partition_index-1,order_statistic-partition_index-1)  # return right part of the partition
# method which partitions the number_list along the pivot
def partition_number_list(number_list,pivot):
    pivot_index = number_list.index(pivot)      # index of the pivot in the number_list
    if pivot_index!=0:                          # validating the pivot_index for not equal to 0
        number_list[0],number_list[pivot_index] = pivot,number_list[0]      # changing pivot and number_list[0] inplace in number_list
        pivot_index = number_list.index(pivot)  # updating the index of the pivot
    # initializing the variables
    left = 0
    right = len(number_list)
    boundary_point = left + 1
    for iterator_index in range(left + 1, right):   # iterating from left+1 index to right most index
        if number_list[iterator_index] < pivot:         # validating whether the number_list[iterator_index] is less than pivot
            number_list[boundary_point], number_list[iterator_index] = number_list[iterator_index], number_list[
                boundary_point]    # changing number_list[boundary_pivot] and number_list[iterator_index] inplace in numberlist
            boundary_point += 1    # incrementing boundary_point by 1
    # changing number_list[left] and number_list[boundary_point] inplace in number_list
    number_list[left], number_list[boundary_point - 1] = number_list[boundary_point - 1], number_list[left]
    return boundary_point-1     # returns the boundary_point-1
# method which returns the randomly selected pivot from the number_list
def pivot_selection(number_list,length):
    random_index = random.randint(1, length-1)  # randomly selecting index
    pivot = number_list[random_index]              # initializing the pivot using the random_index
    return pivot                                   # returning the initialized pivot
number_list = load_numbers("number_file.txt")   # creating list of numbers from the file
# number_list=[3, 2, 9, 7, 5, 6, 1, 8, 4]       # test case example
order_statistic = random.randint(1,len(number_list))  # generating random order statistic
print("Order statistic :",order_statistic)
# calling number_selection method which will find you the ith order statistic(ith smallest number when sorted) from the number_list
number_order_statistic = number_selection(number_list,len(number_list),order_statistic-1)
print("Number at",order_statistic,"th order statistic is :",number_order_statistic)







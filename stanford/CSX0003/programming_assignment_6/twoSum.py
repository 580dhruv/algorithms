# purpose : function which read raw data from the file and creates appropriate data structures
def read_file(filename): # filename=> the name of your file
    hash_num_list = set()             # initialized a set
    with open(filename, 'r') as file:
        for row in file:
            num = int(row.strip())    # typecasting to int
            hash_num_list.add(num)    # adds int to the set
    return list(hash_num_list)        # return the typecasted set
# compute the no of possible of target between the given range
def compute_two_sum(array_list,lower = -10000,upper = 10000):  # array_list => list of numbers
    hash_num_list = {}                                # initialized the hashtable/ dictionary
    for num in array_list:
        hash_num_list[num] = 1
    count = 0
    for target in range(-10000, 10001):
        keys = hash_num_list.keys()
        for num in keys:
            num_2 = target - num                    # x+y =t so here y = t-x
            if num_2 != num and num_2 in hash_num_list:  # checking x not equal to y and is in the list
                count += 1                          # incrementing count by 1
                break
    return count
hash_num_list  = read_file('twosumData.txt')
target_length = compute_two_sum(hash_num_list)
print("total target :",target_length)
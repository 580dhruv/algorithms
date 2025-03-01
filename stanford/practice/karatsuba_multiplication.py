def divide_number(number):
    number= str(number)
    print(number)
    length_number = len(number)
    print(length_number)

    first_half = number[:length_number//2]
    second_half = number[length_number//2:]
    return int(first_half),int(second_half)

def karatsuba_multiplication (numb_1, numb_2):
    first_half_1, second_half_1 = divide_number(numb_1)
    first_half_2, second_half_2 = divide_number(numb_2)

    print(first_half_1, second_half_1)
    print(first_half_2, second_half_2)

    first_half = first_half_1*first_half_2
    print("first_half :",first_half)
    second_half = second_half_1*second_half_2
    print("second_half :",second_half)
    cross = (first_half_1+ second_half_1)*(first_half_2+ second_half_2)
    print("cross :",cross)
    difference = cross-first_half-second_half
    print("difference :",difference)
    length = len(str(numb_1))
    return (first_half*(10**length))+second_half+(difference*(10**(length/2)))


print(karatsuba_multiplication(1234,5678))
print(karatsuba_multiplication(4826,7604))
print(4826*7604)
print(karatsuba_multiplication(45231,78965))
print(78965*45231)
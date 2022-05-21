# using join() + list comprehension
# converting binary list to integer
def binToDec(test_list):
    res = int("".join(str(x) for x in test_list), 2)

    return res

# printing result
# print ("The converted integer value is : " + str(binToDec(a)))

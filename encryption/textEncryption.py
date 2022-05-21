import keyGen as kg
import numpy as np
import decimal_to_binary as dTb

#takes message input
r = float(input("r: "))
Xo = float(input("Xo: "))
message = input("What is your message : ") 

messageSize = len(str(message))

def plainTextToASCII(test_list):
  
    # Convert String list to ascii values
    # using loop + ord()
    res = []
    for ele in test_list:
        res.extend(ord(num) for num in ele)
  
    # print("The ascii list is : " + str(res))

    return res

# print("len of mess: ", messageSize)

# generating key as long as list
key = kg.keyGen(Xo, r,messageSize)

# print("key generated",key)

ascii_list = plainTextToASCII(message)
# print("After function call",ascii_list)


#XOR the two lists
def XOR_lists(lst1, lst2):
#     final_list = lst1^lst2
    result = list(a^b for a,b in zip(lst1,lst2))
    return result
    

def decimalToBinary(myList):
    # i = 0
    # image_matrix = []
    # for width in range(messageSize):
    row = []
    for i in range(messageSize):
    #     try:
            # row.append(binarySequence(XOR_lists(ascii_list, key)[i]))
            row.append(dTb.decimalToBinary(XOR_lists(ascii_list, key)[i]))
    #     except:
    #         row=[(binarySequence(XOR_lists(ascii_list, key)[i]))]
    # try:
    #     image_matrix.append(row)
    # except:
    #         image_matrix = [row]

    # with open("binaryImageSequenceNewMatrix.txt", 'w') as output:
    #     for row in image_matrix:
    #         output.write(str(row) + '\n')
    with open("binaryImageSequenceNewMatrix.txt", 'w') as output:
        for item in row:
            output.write('%s\n' %item)
    # print("Genrated in fn debug",row)
    # return image_matrix  #return binary sequence of pixel values of an image
    return row





# concatenates the 2-dimensional binary list to strig
binaryString = ''.join(decimalToBinary(XOR_lists(ascii_list, key)))

# make couples eg 1010 as "10" "10"
binary_list = [binaryString[i: i+2] for i in range(0, len(binaryString), 2)]

# DNA encoding
DNA_encoding = {
    "00": "C",
    "01": "T",
    "10": "A",
    "11": "G"
} 
DNA_list = []
for num in binary_list:
    for i in list(DNA_encoding.keys()):
        if num == i:
            DNA_list.append(DNA_encoding.get(i))

DNA_str = "".join(DNA_list)


print("\nKey List: ",key)
print("\nASCII list",ascii_list)
print('\nASCII XOR key =',XOR_lists(ascii_list, key))

print("\nbinary converted list: ",decimalToBinary(XOR_lists(ascii_list, key)))

print("\nstring",binaryString)
print("\nbinary list",binary_list)

print("\nThe string represented by single-letter codes is :" + "\n" + DNA_str + "\n")
# print(DNA_str)
file = open('DNA_sequence.txt','w') 
file.write(DNA_str)
# print("File saved")
file.close() 
# print("xored matrix")
# print(XOR_lists(ascii_list, key))

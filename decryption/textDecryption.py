import re
import keyGen as kg
import binary_list_to_decimal as bTd

r = float(input("r: "))
Xo = float(input("Xo: "))
# opening the file in read mode
my_file = open("DNA_sequence.txt", "r")

# reading the file
data = my_file.read()


data_into_list = data.replace('\n', ' ').split(".")

# d = {'A' :'00','C' : '10','G':'01','T': '11'}
DNA_encoding = {
    "C": "00",
    "T": "01",
    "A": "10",
    "G": "11"
} 

# patterns = ['GAGTGAGGGATCGAGGGAATGGACGGCGGGAAGGGAGATTGAGTGGACGAAGGGAAGACAGGCG']

for binarySequence in data_into_list:
    for c in binarySequence:
        binarySequence = re.sub(c,DNA_encoding[c],binarySequence)


# binary_str = binarySequence

binary_list = [binarySequence[i: i+8] for i in range(0, len(binarySequence), 8)]

# def binaryToDecimal(myList):
#     decimal_list = []
#     # size = len(myList)/8
#     size = 6
#     for i in range(size):
#         # print(binary_list[i], " ",binary_list[i+1])
#         decimal_list.append(str(bTd.binToDec(binary_list)[i]))
    
#     # print(decimal_list)
#     return decimal_list

# converting binary list sequence to decimal
decimal_list = []
for i in binary_list:
    decimal_list.append(bTd.binToDec(i))

# key generation
key = kg.keyGen(Xo, r,len(decimal_list))
# print("debug",bTd.binToDec(binary_list))

def XOR_lists(lst1, lst2):
#     final_list = lst1^lst2
    result = list(a^b for a,b in zip(lst1,lst2))
    return result

ASCII_list = XOR_lists(decimal_list, key)

res = ""
for val in ASCII_list:
    res = res + chr(val)
  


# printing the data
print("DNA cipher ",data_into_list)
print("DNA to binary string: ",binarySequence)
print("Procured binary list: ",binary_list)
print("Decimal List: ",decimal_list)
print("key: ",key)
print("Final ASCII values",ASCII_list )

# Printing resultant string
print ("Message: ",str(res),"\n")
# print("decimal list: ",binaryToDecimal(binary_list))

my_file.close()

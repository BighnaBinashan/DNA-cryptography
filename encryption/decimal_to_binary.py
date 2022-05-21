def decimalToBinary(n):
    bnr = bin(n).replace('0b', '')
    x = bnr[::-1]  #reverse the array

    while len(x) < 8:
        x += '0'
    bnr = x[::-1]

    return bnr

# print(decimalToBinary(73)) 

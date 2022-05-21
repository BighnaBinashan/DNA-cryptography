# Fucntion to generate key using chaotic map

def keyGen(x,r,size):
    key = []
    for i in range(size):

        x = r*x*(1-x) #1-D logistic map Xn+1 = r*Xn(1-Xn);
        key.append(int((x*pow(10, 16))%256)) #key = (x * 10^16)%256
        # key.append(int((x*256)))
        # key.append(x)

    return key
# print(keyGen(0.5, 3.9999, 10))
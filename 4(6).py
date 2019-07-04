import random
def function(L,n):
    number = 0
    counter1 = 1
    counter2 = 0
    L2 = []
    for x in range(n):
        L2.append(random.randrange(L[0],L[len(L)-1]))
    L2 = sorted(L2)
    for x in L2:
        if ((L2[x-1]==L2[x])&(x!=0)):
            counter1 +=1
        else :
            if (counter1>=counter2):
                number = L2[x-1]
            counter2=counter1
            counter1 = 0
    return number
def main():
    number = 6
    L = (3, 4, 6, 2, 1, 2, 4, 5, 1, 4, 2, 5)
    print(function(L,number))
main()

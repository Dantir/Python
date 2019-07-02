import random
def function (L,n):
    L2 = []
    for x in range(n):
        L2.append(random.randrange(L[0],L[len(L)-1]))
    L2 = sorted(L2)
    if n%2==1:
        value =L2[int(n/2+1)]
    else:
        value = (L2[int(n/2)]+L2[int(n/2+1)])/2
    print (value)
def main():
    L = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    function(L,(int(input("How many elements you want to choose?\n"))))
main()

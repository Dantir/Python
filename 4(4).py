import random
def function (L,n):
    for x in range(n):
        value = random.randrange(L[0],L[len(L)-1])
    value = value/n
    print (value)
def main():
    L = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    function(L,(int(input("How many elements you want to choose?\n"))))
main()

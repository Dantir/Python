def function(string):
    D = dict()
    string = string.lower()
    for i in string:
        if i in D:
            D[i]+=1
        else:
            D[i]=1
    print(D)
    print("The most frequent letter is "+max(D.keys()))
    D2 = dict()
    D2['vowels']=0
    D2['consonants']=0
    vowelslist = 'a','e','i','o','u'
    for i in string:
        if i in vowelslist:
            D2['vowels']+=1
        else:
            D2['consonants']+=1
    print(D2)
def main():
    string = 'Amaretto'
    function(string)
main()

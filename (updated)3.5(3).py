text = {0 :['Bald','Hairy'],1:['Rat','Cat','Dog'],2:['Ran','Crawled'],3:['Hastily','Slowly','Quietly','Loudly'],4:['In the sewers','On the roof']}
def function(*numbers):
    i = 0
    for x in numbers:
        print(text[i][x])
        i+=1
def main():
    function(0,2,1,3,1)
main()

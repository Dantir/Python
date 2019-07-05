def function(inpu,outpu):
    buffer = []
    read = open(inpu,'r')
    write = open(outpu,'w+')
    for line in read:
        buffer.append(line)
    print(buffer)
    i=1
    while(i<=len(buffer)-1):
        if (len(buffer[i-1])>=len(buffer[i])):
            buffer[i-1],buffer[i]=buffer[i],buffer[i-1]
        i+=1
    print(buffer)
    for element in buffer:
        write.write(element)
    read.close()
    write.close()
def main():
    inpu = 'data.txt'
    outpu= 'final.txt'
    function(inpu,outpu)
main()

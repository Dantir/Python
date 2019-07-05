##function that reads the first n lines of the file

def ReadLines(fileName,n):
    i = 0
    file = open(fileName)
    for line in file:
        if i<n:
            print(line)
            i+=1
    file.close()
def main():
    file = ('data.txt')
    number = 2
    ReadLines(file,number)
main()

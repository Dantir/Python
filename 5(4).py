def easyfunction(F):
    file = open(F,'r')
    text = file.read()
    text=text.upper()
    file = open(F,'w')
    file.write(text)
    file.close()
    return file
def complicatedfunction(F):
    file = open(F,'r')
    text = file.read()
    buffer=''
    for x in text:
        if ((ord(x)>96) & (ord(x)<123)):
            buffer+=(chr(ord(x)-32))
        else:
            buffer+=x
    file = open(F,'w')
    file.write(buffer)
    file.close()
    return file
def main():
    file = 'data.txt'
    complicatedfunction(file)
main()

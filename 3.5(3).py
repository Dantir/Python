text = {0 :'The deadlines',1:'Closer',2:'Were getting',3:'And'}
def function(*numbers):
    for x in numbers:
        print(text[x])
def main():
    function(0,2,1,3,1)
main()

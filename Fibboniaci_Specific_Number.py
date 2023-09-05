location=int(input("Enter the location for your number in the fibboniaci sequence"))
first_number=0
second_number=1
sum=0
i=0
if(location<1):
    print("Wrong Input")
elif(location==1):
    print("0")
elif(location==2):
    print("1")
def fibboniaci(x,y,z):
    for i in range(2, location):
        x=y+z
        y=z
        z=x
    print(x)   

fibboniaci(sum,first_number,second_number)



    

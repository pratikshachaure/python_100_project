def runcase(rem):
    if rem==9:
        print("Nine")
    elif rem==8:
        print("Eight")
    elif rem==7:
        print("Seven")
    elif rem==6:
        print("Six")
    elif rem==5:
        print("Five")
    elif rem==4:
        print("Four")
    elif rem==3:
        print("Three")
    elif rem==2:
        print("Two")
    elif rem==1:
        print("One")
number = int(input("Enter the number:- "))
rem = 0
while number != 0:
    rem = number % 10
    number = number // 10
    runcase(rem)

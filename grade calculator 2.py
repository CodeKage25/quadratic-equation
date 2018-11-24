print("Enter 'x' for exit")
print("Enter marks obtained in 5 subject: ")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())
if mark1 =='x':
        exit();
else:
    sum = mark1 + mark2 + mark3 + mark4 + mark5
    average = sum/5
    if(average>=70 and average<=100):
       print("your grade is A")
    elif(average>=60 and average<=69):
        print("your grade is B")
    elif(average>=50 and average<=59):
        print("your grade is C")
    elif(average>=40 and average<=49):
        print("your grade is D")
    elif(average>=0 and average<=39):
        print("your grade is F")
    else:
        print("strange grade....!!!")

sub1 = eval(input("enter the marks of subject 1 = "))
sub2 = eval(input("enter the marks of subject 2 = "))
sub3 = eval(input("enter the marks of subject 3 = "))
percentage = ((sub3 + sub2 + sub1)*100)/300
print("your percentage = " + str(percentage))

if percentage>=90:
    print(" grade = A+")
elif percentage<90 and percentage>=80:
    print("grade = A")
elif percentage<80 and percentage>=70:
    print("grade = B")
elif percentage<70 and percentage>=60:
    print("grade = C")
elif percentage<60 and percentage>=50:
    print("grade = D")
else:
    print("fail")

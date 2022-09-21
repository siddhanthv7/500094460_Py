sub1 = eval(input("enter the marks of subject 1 = "))
sub2 = eval(input("enter the marks of subject 2 = "))
sub3 = eval(input("enter the marks of subject 3 = "))
percentage = ((sub3 + sub2 + sub1)*100)/300
print("your percentage = " + str(percentage))

if percentage>=95:
    print(" grade = A+")
elif percentage<95 and percentage>=85:
    print("grade = A")
elif percentage<85 and percentage>=75:
    print("grade = B")
elif percentage<75 and percentage>=65:
    print("grade = C")
elif percentage<65 and percentage>=55:
    print("grade = D")
else:
    print("fail")

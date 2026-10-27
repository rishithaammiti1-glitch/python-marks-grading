name=input("enter a name:")
n=int(input("enter a number of subjects:"))
total=0
for i in range(1,1+n):
    marks=float(input("enter marks:"))
    total+=marks
    percentage=total/n
if total>=90:
    grade="A"
    performance="outstanding"
elif total>=80:
    grade="B"
    performance="excellent"
elif total>=70:
    grade="C"
    performance="very good"
elif total>=60:
    grade="D"
    performance="good"
elif total>=50:
    grade="E"
    performance="average"
else:
    grade="F"
    performance="poor"
print("NAME:",name)
print("SUBJECTS:",n)
print("TOTAL MARKS:",total)
print("PERCENTAGE:",round(percentage,2),"%")
print("GRADE:",grade)
print("PERFORMANCE:",performance)
    

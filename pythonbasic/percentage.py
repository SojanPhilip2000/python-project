mark1=60
mark2=85
mark3=90
total=mark1+mark2+mark3
percent=((total/300)*100)
if percent>=90:
    grade="A"
elif percent>=80:
    grade= "B"
else:
    grade= "PASS"
print(grade)

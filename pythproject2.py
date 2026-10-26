#2

students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
for i in students:
    print(f"{i} {sum(students[i])/len(students[i]):.2f}");

high=0
for i in students:
    avg=sum(students[i])/len(students[i])
    if avg > high:
        top=i;
        high=avg
    if  avg>=85:
        grade="A"
    elif avg>=70:
        grade="B"
    elif avg>=50:
        grade="C"
    else:
        grade="F"
    print(f"{i} {avg:.2f} {grade}")
    print("Topper : ",top)
    
while True:
    print("1. Add Student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")
    user= int(input("Enter Your Query : "))
    if user==1:
        new= int(input("Student Name : "))
        if new in students:
            print("Student Already Exists")
            continue
        cream=[]
        for i in range(3):
            marks=int(input("Enter Marks: "))
            key=0
            if marks>101 and marks<1:
                print("Invalid Input")
                key=1;
                break
            cream.append(marks)
        students[new]=cream
        if key==1:
            continue
    if user==2:
        print(students)
    if user==3:
        top=0
        for i in students:
            total=0
            for j in students[i]:
                total+=j
            if total > top:
                Topper= i
                top=total
        print("Topper: ",Topper)
    if user==4:
        print("Thank you! \nGood Bye!")
        break

        
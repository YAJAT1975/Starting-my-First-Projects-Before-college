restart =True
while restart:
    print("Student Data base ")
    name=str(input("Name"))
    Student = []
    Student.append(int(input("Enter Physics Marks")))
    Student.append(int(input("Enter Chemistry Marks")))
    Student.append(int(input("Enter Maths Marks")))
    Student.append(int(input("Enter English Marks")))
    Student.append(int(input("Enter Computer Marks")))
    MaximumMarks= 500
    MarksObtained=0
    Up90=0
    Down40=0
    for val in Student:
        MarksObtained=val+MarksObtained
        if(val>=90):
            Up90 =Up90+1
        if(val<=40):
            Down40=Down40+1
    Percentage=  (MarksObtained/MaximumMarks)*100
    MaximumSubjectMark=max(Student)
    MinimumSubjectMark=min(Student)
    Grade=""
    Result="Pass"
    if(Percentage>=90):
        Grade="A+"
    elif(Percentage>=80):
        Grade="A"
    elif(Percentage>=70):
        Grade="B"
    elif(Percentage>=60):
        Grade="C"
    elif(Percentage>=50):
        Grade="D"
    elif(Percentage>=40):
        Grade="E"
    else:
        Grade="F"
        Result="Fail"
    print("Student Name ", name)
    print("  Marks ",MarksObtained,"/",MaximumMarks)
    print("Maximum Subject Mark ", MaximumSubjectMark)
    print("Minimum Subject Mark ", MinimumSubjectMark)
    print("Grade ", Grade)
    print("Result", Result)
    print("Next Student Enter Y else N")
    if(input()=="Y"):
        restart=True
    else:
        restart=False



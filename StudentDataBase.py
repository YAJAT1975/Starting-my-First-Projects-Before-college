with open("Data.txt","a+") as f:
    def AddStudent():
        restart =True
        while restart:
            
            name=str(input("Name"))
            RollNo=(int(input("Enter Roll Number")))
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
            f.write("Student Roll No ", RollNo)
            f.write("Student Name ", name)
            f.write("  Marks ",MarksObtained,"/",MaximumMarks)
            f.write("Maximum Subject Mark ", MaximumSubjectMark)
            f.write("Minimum Subject Mark ", MinimumSubjectMark)
            f.write("Grade ", Grade)
            f.write("Result", Result)
            print("Next Student Enter Y else N")
            if(input()=="Y"):
                restart=True
            else:
                restart=False
    
    
    
    def ViewStudents():
        f.read()
    


    def Search(a):
        restart=True
        founding="Student Roll No  ",a


        while restart:
            search=  f.readline()
            if(search==founding):
                print(search)
                n = 1;
                while n!=6 :
                    print(f.readline())
                    n +=1
                break

            elif (search==""):
                restart=False
    print("Student Database ")
    restart=True
    while restart:
        print("For Adding Student Enter 1 ")
        print("For Display Students Data Enter 2 ")
        print("For Searching Student  3 ")
        print("For Exit Enter 4")
        User=int(input("Please Enter your choise"))
        if(User==1):
             AddStudent()
        elif(User==2):
             ViewStudents
        elif(User==3):
            print("enter roll no")
            a=int(input())
            Search(a)
        elif(User==4):
            restart=False
        else:
            print("Invalid input")
def MarksManager():
    """This is a student marks manager system where student details, marks per subject and 
    overall marks are displayed based on the user input by name.
    Along with there will be 2 part of this system would be admin to upload marks and 
    student as user to fetch marks
    First input: Whom we are talking to: admin/user
    if admin - please add the marks with subject name
    if user - please enter student name or id to fetch the details"""
    studentList = []

    def user(name):
        student = list(filter(lambda item: item['name'].lower() == name, studentList))
        if name in student[0]['name'].lower():
            return student[0]["subjects"]
        else:
            return "This student is not in our record"

    def Admin():
        studentName = input("Please enter student name:").capitalize()
        
        listOfSubjectsWithMarks = dict({ "name": studentName, "subjects": dict({})})
        def subjectWithMarks():
            if (len(listOfSubjectsWithMarks["subjects"]) >= 2):
                print("You are done with adding marks for this student")
            else:
                subject = str(input("Please enter subject name:").lower())
                marks = int(input("Please enter marks:"))
                listOfSubjectsWithMarks["subjects"].update({subject: marks})
            if len(listOfSubjectsWithMarks["subjects"]) < 2: subjectWithMarks()
        subjectWithMarks()
        studentList.append(listOfSubjectsWithMarks)
        print(studentList)
        addMore = input("Do you want to add more student details?(yes/no):").lower()
        if (addMore == "yes"):
            Admin()
        else:
            isProceed = input("Do you want to fetch the student details?(yes/no):").lower()
            if (isProceed == 'yes'):
                print(user(str(input("May I know the student name:").lower())))
       
    role = input("May I know who is requesting? (admin/user):").lower()
    if (role == "admin"):
        Admin()
    if (role == "user"):
        print(user(str(input("May I know the student name:").lower())))

MarksManager()
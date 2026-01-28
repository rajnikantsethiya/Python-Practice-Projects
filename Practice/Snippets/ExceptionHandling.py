def Student(age):
    try:
        if int(age) > 18:
            print("Student is eligible for admission")
        else: raise Exception()
    except:
       print("Age is not defined")
    finally:
        print("Student registered")
    
Student(11)
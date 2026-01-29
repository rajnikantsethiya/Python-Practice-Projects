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

# Creating own exception error
class EmployeeError(Exception): pass
class Office(Exception):
    def __init__(self, employee, *args):
        super().__init__(*args)
        self.employee = employee
    
    def Play(self):
        try:
            if not isinstance(self.employee, str):
                raise ValueError("Please provide the employee name correctly !")
            elif self.employee in ["Raj", "Rishi", "Prashant"]:
                print("Play carrom !", type(self.employee))
            else:
                raise EmployeeError("This employee is not allowed to play !")
        except Exception as e:
            print("Error", e)
        finally:
            print("Thanks for playing !")

ofc = Office("Rauhul")
ofc.Play()
ofc = Office(123)
ofc.Play()
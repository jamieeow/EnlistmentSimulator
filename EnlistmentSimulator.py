students = []
admins = []
offerings = []

class Class:
	def __init__(self, coursename, coursecode, day, time):
		self._coursename = coursename
		self._coursecode = coursecode
		self._day = day
		self._time = time
		
	def get_coursename(self):
		return self._coursename
	def get_coursecode(self):
		return self._coursecode
	def get_day(self):
		return self._day
	def get_time(self):
		return self._time

class Student:
	def __init__(self, username, password):
		self._username = username
		self._password = password
		self._classes = []
		
	def get_username(self):
		return self._username
	
	def get_password(self):
		return self._password
		
	def get_classes(self):
		return self._classes
	
class Admin:
	def __init__(self, username, password):
		self._username = username
		self._password = password		
	
	def get_username(self):
		return self._username
	
	def get_password(self):
		return self._password


def initial_screen():
    print("1 - Login")
    print("2 - Register")
    prompt = input("What you do? ")
    
    if prompt == "1":
        login_screen()
    elif prompt == "2":
        register()
    else:
        initial_screen()

def register():
    print("1 - Student")
    print("2 - Admin")
    prompt = input("Register as: ")
    
    if prompt == "1":
        register_student()
    elif prompt == "2":
        register_admin()
    else:
        register()

def register_student():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    student = Student(username, password)
    students.append(student)
    print("Register Successfully!")
    
    initial_screen()
    
def register_admin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    admin = Admin(username, password)
    admins.append(admin)
    print("Register Successfully!")
    initial_screen()

def login_screen():	
    print("1 - Student")
    print("2 - Admin")
    prompt = input("Login as a: ")
	
    if prompt == "1":
        student_login()
    elif prompt == "2":
    	admin_login()
    else:
        login_screen()

def student_login():
	username = input("Enter username: ")
	password = input("Enter password: ")
	
	success = "false"
	for x in students:
	    print(x.get_username(), x.get_password())
	    if x.get_username() == username and x.get_password() == password:
	        print("\nLogin successfully!\n")
	        global logged_student
	        logged_student = x
	        main_screen()
	        success = "true"
	        break
	    else:
	        success = "false"
	
	if success == "false":
	    print("Student not registered or wrong password!\n")
	    initial_screen()


def admin_login():
	username = input("Enter username: ")
	password = input("Enter password: ")
	
	success = "false"
	for x in admins:
	    if x.get_username() == username and x.get_password() == password:
	        print("\nLogin successfully!\n")
	        admin_screen()
	        success = "true"
	        break
	    else:
	        success = "false"
	        
	if success == "false":
	    print("Admin not registered or wrong password!\n")
	    initial_screen()

def show_classes(classes):
    print("---------------------------------------------------------------------------------------")
    print("|\tCourse Name \t|\tCourse Code \t|\tDay \t|\tTime")
    
    for x in classes:
        print("|\t", x.get_coursename(), "\t|\t", x.get_coursecode(), "\t|\t", x.get_day(), "\t|\t", x.get_time())
	
def add_class():
	show_classes(offerings)
	
	code = input("Enter Course Code to be added: ")
	
	for x in offerings:
		if x.get_coursecode() == code:
			logged_student.get_classes().append(x)
			break
			
	else:
		print("Successfully added\n\n")

def remove_class():
	classes = logged_student.get_classes()
	
	show_classes(classes)
	
	code = input("Enter Course Code: ")
	
	for x in range(len(classes)):
		if classes[x].get_coursecode() == code:
			del(classes[x])
			break
			
	else:
		print("Successfully removed\n\n")
	
def swap_classes():
	remove_class()
	print("NOW SELECT WHICH CLASS TO BE SWAPPED")
	add_class()
	
	
def main_screen():
	print("\nSubjects of", logged_student.get_username())
	
	show_classes(logged_student.get_classes())
	
	print("1 - add a class")
	print("2 - remove a class")
	print("3 - swap classes")
	print("4 - logout")
	
	action = input("What u want do? ")
	print(action)
	if action == '1':
		print("ADD A CLASS")
		add_class()
	elif action == '2':
		print("REMOVE A CLASS")
		remove_class()
	elif action == '3':
		print("SWAP CLASSES")
		swap_classes()
	elif action == '4':
		initial_screen()
	
	main_screen()

def admin_screen():
    print("COURSE OFFERINGS")
    show_classes(offerings)
    print("1 - add a class")
    print("2 - remove a class")
    print("3 - logout")
    
    action = input("What u want do? ")
    print(action)
    if action == '1':
    	print("ADD A CLASS")
    	admin_add()
    elif action == '2':
    	print("REMOVE A CLASS")
    	admin_remove()
    elif action == '3':
    	initial_screen()
    else:
    	admin_screen()
    
def admin_add():
    coursename = input("Enter course name: ")
    coursecode = input("Enter course code: ")
    day = input("Enter day: ")
    time = input("Enter time: ")
    
    offering = Class(coursename, coursecode, day, time)
    
    offerings.append(offering)
    admin_screen()

def admin_remove():
    show_classes(offerings)
    
    code = input("Enter course code to be removed: ")
    
    for x in offerings:
        if x.get_coursecode() == code:
            offerings.remove(x)
            print("Course Removed Successfully!")
            break
        
    admin_screen()


initial_screen()





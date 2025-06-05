class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()  # Calls the menu when object is created

    def menu(self):  # Fixed: This is now at the correct level
        user_input = input("""
Welcome to Chat Book 
How would you like to proceed?

1. Press 1 to signup
2. Press 2 to signin
3. Press 3 to write a post
4. Press 4 to message a friend
5. Press any other key to exit
""")

        if user_input == '1':
           self.signin()  # You can later replace 'pass' with actual functionality
        elif user_input == '2':
            self.signup()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        elif user_input == '5':
            pass
        else:
            exit()

    def signup(self):
        email=input("Enter you email here")

        pwd=input("Setup your password Here")
        
        self.username=email
        self.password=pwd

        print("User has signed up sucessfully \n ")

        self.menu()

    def signin(self):
        if self.username=='' and self.password=='':
            print("Please sign up first by pressing 1 in main menu")
        
        else:
            uname=input("Enter your User Name")
            pwd=input("Enter your Password")

            if self.username==uname and self.password=pwd:
                print("You have signed in successfully")
                self.loggedin = True

            else:
                print("Please input correct Credentials..")

        print('\n')
        self.menu()


# Create an object to run the program
obj = Chatbook()

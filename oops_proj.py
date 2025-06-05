class Chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()  # Start with the menu

    def menu(self):
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
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        # elif user_input == '5':
        #     print("👋 Exiting Chatbook. Goodbye!")
        #     exit()
        else:
            print("👋 Exiting Chatbook. Goodbye!")
            exit()

    def signup(self):
        email = input("Enter your email: ")
        pwd = input("Set your password: ")
        self.username = email
        self.password = pwd
        print("✅ User has signed up successfully.\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("⚠️ Please sign up first by pressing 1 in main menu.")
        else:
            uname = input("Enter your username: ")
            pwd = input("Enter your password: ")

            if self.username == uname and self.password == pwd:
                print("✅ You have signed in successfully.")
                self.loggedin = True
            else:
                print("❌ Incorrect credentials. Please try again.")
        print()
        self.menu()

    def my_post(self):
        if self.loggedin:
            txt = input("Enter your message here: ")
            print(f"📝 Your post: {txt}")
        else:
            print("⚠️ You need to sign in to post something.")
        print()
        self.menu()

    def sendmsg(self):
        if self.loggedin:
            txt = input("Enter your message here: ")
            frnd = input("Whom to send the message? ")
            print(f"📩 Your message: '{txt}' has been sent to {frnd}.")
        else:
            print("⚠️ You need to sign in to send a message.")
        print()
        self.menu()


# Start the program
user1 = Chatbook()

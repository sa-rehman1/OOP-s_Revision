class Account:
    account_count = 1000
    bank_name = "HDFC"

    def __init__(self, name, username, password, initial_balance):
        Account.account_count += 1
        self.account_number = Account.account_count
        self.__balance = initial_balance
        self.__transaction_history = []
        self.name = name
        self.username = username
        self.password = password
        self.logged_in = False
        self.withdrawal_limit = 3
        print(f"\n Account created successfully. Your account number is {self.account_number}")
    
    def login(self):
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        if self.username == uname and self.password == pwd:
            print("Logged in successfully!\n")
            self.logged_in = True
        else:
            print("Invalid credentials.\n")
            self.logged_in = False

    def deposit(self):
        if not self.logged_in:
            print("Please login first.\n")
            return
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("⚠️ Invalid amount.\n")
                return
            self.__balance += amount
            self.__transaction_history.append(f"Deposited ₹{amount}")
            print(f"✅ ₹{amount} deposited successfully.\n")
        except ValueError:
            print("❌ Enter a valid number.\n")

    def withdraw(self):
        if not self.logged_in:
            print("❌ Please login first.\n")
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount + 100 > self.__balance:
                print("❌ Insufficient balance.\n")
            elif self.withdrawal_limit < 1:
                print("⚠️ Withdrawal limit exceeded.\n")
            else:
                self.__balance -= (amount + 100)  # ₹100 fee
                self.withdrawal_limit -= 1
                self.__transaction_history.append(f"Withdrew ₹{amount} (₹100 fee)")
                print(f"✅ ₹{amount} withdrawn successfully with ₹100 fee.\n")
        except ValueError:
            print("❌ Enter a valid number.\n")

    def view_balance(self):
        if not self.logged_in:
            print("❌ Please login first.\n")
            return
        print(f"💰 Current Balance: ₹{self.__balance}\n")

    def view_transactions(self):
        if not self.logged_in:
            print("❌ Please login first.\n")
            return
        print("📄 Transaction History:")
        for entry in self.__transaction_history:
            print(f" - {entry}")
        print()

    def menu(self):
        while True:
            print("----- 🏦 SmartBank Menu -----")
            print("1. Login")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Balance")
            print("5. View Transactions")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.login()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                self.view_balance()
            elif choice == '5':
                self.view_transactions()
            elif choice == '6':
                print("👋 Thank you for using SmartBank.\n")
                break
            else:
                print("❌ Invalid choice. Try again.\n")


class PremiumAccount(Account):
    def __init__(self, name, username, password, initial_balance):
        super().__init__(name, username, password, initial_balance)
        self.withdrawal_limit = 5  # Increased limit for premium users

    def withdraw(self):
        if not self.logged_in:
            print("❌ Please login first.\n")
            return
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self._Account__balance:  
                print("❌ Insufficient balance.\n")
            elif self.withdrawal_limit < 1:
                print("⚠️ Withdrawal limit exceeded.\n")
            else:
                self._Account__balance -= amount 
                self.withdrawal_limit -= 1
                self._Account__transaction_history.append(f"Withdrew ₹{amount}")
                print(f"✅ ₹{amount} withdrawn successfully (No fee for premium users).\n")
        except ValueError:
            print("❌ Enter a valid number.\n")

    @staticmethod
    def premium_benefits():
        print("🎉 Access to premium lounge activated!\n")



premium_user = PremiumAccount("Bob", "bob456", "bob@pass", 10000)
premium_user.menu()

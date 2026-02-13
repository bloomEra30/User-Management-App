class User: #data
    counter = 1  #class variable
    def __init__(self,username,email,password):
        self.id = User.counter
        self.username = username
        self.email = email
        self.password = password

class UserManager: #business logic
    def __init__(self):
        self.users = [] #acts like databse table
        self.current_user = None #no one is logged in

    def register(self):
        username = input("Enter Username: ") 
        email = input(" Enter Email: ")
        password = input("Enter Password: ")  


        #check if email already exists
        for user in self.users:
            if user.email == email:
                print("Email already registered!")
                return
        new_user = User(username,email,password) 
        self.users.append(new_user)
        print("Registration successful!")

    def login(self):
        if self.current_user:
            print("Already logged in!")
            return

        email = input("Enter email: ")
        password = input("Enter password: ")


        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                print("Login successful!")
                return
            
        print("Invalid email or password.")


    def view_profile(self):
        if not self.current_user:
            print("Please login first.")
            return
        
        print("\n --- Profile ---")
        print("ID: ", self.current_user.id)
        print("Username: " ,self.current_user.username)
        print("Email: ", self.current_user.email)


    def update_profile(self):
        if not self.current_user:
            print("Please login first.")
            return

        new_username = input("Enter new username: ")
        self.current_user.username = new_username 
        print("Profile updated successfully.")



    def delete_user(self):
        if not self.current_user:
            print("Please login first.")
            return

        self.users.remove(self.current_user) 
        self.current_user = None
        print("Account deleted successfully.")


def main():
    manager = UserManager()

    while True:
        print('\n1. Register')
        print('2. Login')
        print('3. View Profile')
        print('4. Update Profile')
        print('5. Delete Profile')
        print('6. Exit')

        choice = input("Choice option: ")

        if choice == '1':
            manager.register()
        elif choice == '2':
            manager.login()
        elif choice == '3':
            manager.view_profile()
        elif choice == '4':
            manager.update_profile()
        elif choice == '5':
            manager.delete_user()
        elif choice == '6':
            print("GoodBye!")
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()            




    
                







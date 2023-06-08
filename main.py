from operation_user import UserOperation
from operation_admin import AdminOperation
from operation_customer import CustomerOperation
from io_interface import IOInterface

def main():
    # Register admin account
    
    AdminOperation.register_admin()
    print("Admin user registered successfully")

    while True:
        IOInterface.main_menu()
        choice = IOInterface.get_user_input("Enter your choice: ", 1)[0]
        if choice == '1':
            user_name = input("please input the name of the user:")
            user_password  = input("please input the password of the user:") 
            userdetails = UserOperation.login(user_name, user_password)
            if userdetails is None:
                print("The user needs to be registered in the system.")
            else:
                print("The user login is successfull.")
        elif choice == '2':
            user_name = input("Enter username: ")
            user_password = input("Enter password: ")
            user_email = input("Enter email: ")
            user_mobile = input("Enter mobile: ")
            #print ("Registering admin user if not registered already)
            #AdminOperation.register_admin()  # Call the register_admin() method from AdminOperation
            success = CustomerOperation.register_customer(user_name, user_password, user_email, user_mobile)
            print("Registration successful:", success)
            #if success:
                #print("Customer registered successfully.")
            #else:
                #print("Failed to register customer.")

if __name__ == "__main__":
    main()
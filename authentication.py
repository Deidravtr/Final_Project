# Deidra Driscoll
# Software Development Fundamentals
# Programming_lab_8, This program is an authentication system that requires a
# username and password from a json file called database to allow access to
# a registered user. If the password is incorrect 3 times, lock the user out of the
# system. If correct, however, grant access to the system using the logged_in user
# defined function. If a user wants to create an account, check that the username
# does not already exist. If it doesn't, then the database will be updated with the
# new account.


# Import json
import json


class Authentication:
    # No attributes in constructor
    def __init__(self):
        pass

    # Define database with username and password as parameters
    def database(self, username, password):
        # Set/call database function equal to new_database
        new_database = self.database_json()
        # Create exception handling for key error (KeyError only pops up if username doesn't exist)
        try:
            # Check if user entered username and password is in database
            if new_database[username] == password:
                # Return true
                return True
            else:
                # Return false
                return False
        except KeyError:
            return False


    # Define database json (This is the actual database that I had to account for in this program to get it to work
    # properly)
    def database_json(self):
        # Create database
        database_json = {}
        # Create try exception handling
        try:
            # Open a read file (databse.json)
            with open("database.json", "r") as f:
                # Load key value pairs from file into dictionary
                dictionary_from_file = json.load(f)
                # Load dictionary with local variable username and password
                for username, password in dictionary_from_file.items():
                    # Update database
                    database_json[username] = password
                    # Return database
                return database_json
        except FileNotFoundError:
            with open("database.json", "w") as f:
                json.dump(database_json, f, indent=2)
            print("Error opening file. Please try again.\n")



    # Define authenticate (Choice 1)
    def authenticate(self, username, password):
        new_database = self.database_json()
        # Check that username is in the database
        if username in new_database:
            # Call database function with parameters username and password, then check if the returned value is true
            if self.database(username, password) == True:
                # Return to main
                return self.logged_in()
                # If no password entered were correct, lock user out of system.
            else:
                locked_out = str("You are locked out of the system")
                return locked_out
        # If username not in database (accounted for exception handling)
        if username not in new_database:
            does_not_exist = str("Username does not exist")
            # Return to main
            return does_not_exist


    # Define new user (Choice 2)
    def new_user(self, username, password):
        # Set/call database function equal to new_database
        new_database = self.database_json()
        while username in new_database:
            return "Username already exists"
        # Update new database with new password
        new_database[username] = password
        # Call database function with parameters username and password, then check if the returned value is False
        if self.database(username, password) == False:
            # Create try-exception handling for writing file
            try:
                # Open file
                with open("database.json", "w") as f:
                    # "dump" contents of new database in the file
                    json.dump(new_database, f, indent=2)
                return "Account successfully created."
            # End exception handling
            except IOError:
                print("Error writing file.")



    # Define logged in
    def logged_in(self):
        logged_in_successfully = str("Welcome to the top secret system.")
        return logged_in_successfully


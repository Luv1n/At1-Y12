from classes.user import User
from flask import abort
from data import users
import re
import html

def user_auth_register(email, password, first_name, last_name):


    #xxs preventions

    email = html.escape(email)
    first_name = html.escape(first_name)
    last_name = html.escape(last_name)
    password = html.escape(password)

    
    email = email.lower()  # Normalize the email to lowercase
    if email in users:
        abort(401, description="Email already exists")

     #input validation
    if password is None:
        abort(401, description="Password Cannot Be Empty")
    
    if first_name is None:
        abort(401, description="First Name Cannot Be Empty")
    if not re.match("^[A-Za-z]+$", first_name):
        abort(401, description="First Name Cannot Contain Numbers or Special Characters")
    
    
    if last_name is None:
        abort(401, description="Last Name Cannot Be Empty")
    if not re.match("^[A-Za-z]+$", last_name):
        abort(401, description="Last Name Cannot Contain Numbers or Special Characters")

    new_user = User(email, first_name, last_name, password)
    users[email] = new_user  # Store the user object by email
    


    return new_user.token

def user_auth_login(email, password_input):
        #xxs preventions
    email = html.escape(password_input)
    password_input = html.escape(password_input)

    email = email.lower()  # Normalize the email to lowercase
     #input validation
    if email not in users:
        abort(401, description="Email does not exist")

    user = users[email]
    if password_input is None:
        abort(401, description="Password Cannot Be Empty")
    else:
        password_input = html.escape(password_input)
        if not user.verify_password(password_input):
            abort(401, description="Invalid password")
    
    
    # Generate a new token and update the user's token attribute
    user.token = user.generate_token(email)
    
    # Return the new token
    return user.token


def user_auth_logout(token):
    # Loop through all users in the dictionary
    for user in users.values():
        if user.token == token:  # Check if the token matches
            user.revoke_token()  # Revoke the token
            return  # Exit the function after revoking the token
    
    # If no matching token is found, abort with an error
    abort(401, description="Token does not exist")

def user_auth_validate_token(token):

    for user in users.values():
        print(f'{user.email} is for {user.token}')

    for user in users.values():
        if user.token == token:  # Check if the token matches
            return True  # Token found, return True
 #input validation
    abort(401, description="Token does not exist")

def user_auth_login(email, password):
    email = email.lower()  # Normalize the email to lowercase
     #input validation
    if email not in users:
        abort(401, description="Email does not exist")
    
    user = users[email]
    if password is None:
        abort(401, description="Password Cannot Be Empty")
    else:
        if not user.verify_password(password):
            abort(401, description="Invalid password")
    
    
    # Generate a new token and update the user's token attribute
    user.token = user.generate_token(email)
    
    # Return the new token
    return user.token


def user_auth_logout(token):
    # Loop through all users in the dictionary
    for user in users.values():
        if user.token == token:  # Check if the token matches
            user.revoke_token()  # Revoke the token
            return  # Exit the function after revoking the token
    
    # If no matching token is found, abort with an error
    abort(401, description="Token does not exist")

def user_auth_validate_token(token):
    for user in users.values():
        if user.token == token:  # Check if the token matches
            return True  # Token found, return True

    abort(401, description="Token does not exist")
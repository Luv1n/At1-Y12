from classes.user import User
from flask import abort
from data import users

def user_auth_register(email, password, first_name, last_name):
    email = email.lower()  # Normalize the email to lowercase
    if email in users:
        abort(400, description="Email already exists")
    
    new_user = User(email, first_name, last_name, password)
    users[email] = new_user  # Store the user object by email

    return new_user.token

def user_auth_login(email, password_input):
    email = email.lower()  # Normalize the email to lowercase
    
    if email not in users:
        abort(401, description="Email does not exist")
    
    user = users[email]
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

    abort(401, description="Token does not exist")

def user_auth_login(email, password):
    email = email.lower()  # Normalize the email to lowercase
    
    if email not in users:
        abort(400, description="Email does not exist")
    
    user = users[email]
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
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/r_tcpi1q)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16591760&assignment_repo_type=AssignmentRepo)
# FastFinance API Security Enhancement

## Table of Contents

- [Assessment Overview](#assessment-overview)
- [Front-End Interface](#front-end-interface)
- [Video Run-through](#video-run-through)
- [Setup](#setup)
- [Running the Front-end](#running-the-front-end)
- [Stage 1 - Basic](#stage-1---basic)
- [Stage 2 - Intermediate](#stage-2---intermediate)
- [Stage 3 - Advanced](#stage-3---advanced)
- [Forum API Description](#forum-api-description)

## Assessment Overview

### Scenario

You have been employed as a junior software engineer at **TechSecure Solutions**, a company that specialises in developing secure software architectures. Your task is to fix a broken API for a client, **FastFinance**, a small fintech company that provides financial services through their web and mobile apps. This project will be divided into three stages of development, each increasing in difficulty.

FastFinance's API has been reported to contain several vulnerabilities that could expose sensitive financial data, leaving their users at risk. You have been provided with the API source code and a report from a security audit highlighting the following security concerns:

### Task

Students will create a testing report and include relevant documentation such as SAST and DAST tests. The Python API will be built in three stages, ensuring systematic development and comprehensive coverage of all planned functionalities. The creation and submission of the practical component will be completed through the EdStem platform. Its associated documentation will be created on Microsoft Word utilising the scaffold provided. A submission must be generated before the task's due date on Canvas; this will facilitate accessibility and ease of use for all stakeholders involved in the educational process.

## Front-End Interface

Our front-end for the Forum application is written in **Next.js**. HELLO

## Setup

There are a few steps to run the front end. First, we must configure the back-end and front-end together:

1. **Clone the GitHub repository:**

2. **Install Node.js** (the JS runtime environment).

3. **Execute the server:**
    ```bash
    python3 server.py
    ```
    Host the server on the next available port.

    **Note:** Ensure to remove the backslash from the copied URL. The front-end API calls will fail if the URL isn't correct.

    **Warning:** Using the run button on the Ed workspace will not host the server. You need to manually open up the terminal and run the Python script to host the Flask back-end server.

## Running the Front-end

1. **Install Dependencies:**
    ```bash
    npm install
    ```
    Execute this command in the terminal within your current working directory or front-end folder to install all external libraries.

2. **Start the Front-End Server:**
    ```bash
    npm run dev
    ```
    The terminal should generate a URL where you can interact with the front end, similar to `https://localhost:3000`.

    **Note:** You will need to close and reopen the server using `python3 server.py` for any changes on the server back-end to take effect on the front-end.

## Stage 1 - Basic

### Stage 1.1 - Password Hashing

**Security Features to Implement:** Confidentiality, Authentication

To begin the assignment, you will redesign the Python `User` class to ensure that the user's password is hashed using cryptographic methods before being stored.

- **Location:** Inside the `classes` folder, modify the `user.py` file.

**Specifications:**

Your implementation must include the following security features:

1. **Confidentiality**
    - Replace the `password` attribute with `password_hash`, ensuring the password is never stored in plain text.
    - Create the `hash_password` method to handle password hashing (using the SHA256 algorithm). Call this method during the initialisation process.

2. **Authentication**
    - Update the `verify_password` method to also call the `hash_password` method to validate if the stored (hashed) password matches the input password.

**Example:**
```python
# Create a new user with email and password
user = User(email="rianni@kings.edu.au", first_name="Rocco", last_name="Ianni", password="HelloThere")

# Verify the password
password_attempt = "HelloThere"
if user.verify_password(password_attempt):
    print("Password verification successful.")
else:
    print("Password verification failed.")
```

**Note:** The `verify_password` method should abstract the use of cryptographic hashing of the user's password.

**Hint:** Use the `hashlib` library for cryptographic hashing.

### Stage 1.2 - Input Validation

**Security Features Addressed:** Integrity, Accountability

In this task, you will implement input validation to ensure that data sent from the user's client-side (via an API request) meets specific criteria before being processed by the back end.

- **API Description:** Refer to the ed-page for details on each route and their respective functions.
- **Server Routes:** Located in `server.py` (e.g., `/auth/register/`).
- **Helper Functions:** Located within each route (e.g., `admin_auth_register`).

**Example: Handling Invalid Email Input**
```python
users = {}  # Stored in data.py in your code

def admin_auth_register(email):
    email = email.lower()  # Normalise to lowercase for case sensitivity
    if email in users:
        abort(400, description="Email already exists in data")
```

**Hint:** Use the `abort()` function to handle any error exceptions. The error will be raised automatically and handled with the `try` and `except` blocks inside each route in `server.py`.

**Note:** HTTP servers should primarily obtain data with minimal logic to reduce complexity and improve readability.

### Stage 1.3 - Input Sanitisation (XSS Vulnerabilities)

**Vulnerabilities Addressed:** Cross-site Scripting (XSS)

Similar to Stage 1.2, your task is to sanitise any potentially harmful user input to minimise cross-site scripting (XSS) attacks. Implement this across all routes that retrieve data from user inputs.

**Example: Sanitising User Input**
```python
users = {
    ...
    'email': 'mienna@kings.edu.au',
    'first_name': '&lt;script&gt;alert(\'XSS Attack!\');&lt;/script&gt;',
    ...
}
```

## Stage 2 - Intermediate

### Stage 2.1 - Session Management

**Execution Efficiency:** Session Management  
**Vulnerability Addressed:** Broken Authentication and Session Management  
**Security Feature:** Authorisation

Currently, the broken implementation uses the client's email as the session token, which is vulnerable to session hijacking. Your task is to implement secure session management through session tokens to authenticate specific users.

**Specifications:**

Implement the following security features in the `User` class:

1. **Cryptographically Secure Tokens**
    - Replace the `generate_token` method to generate a cryptographically secure session token to prevent session hijacking.

2. **Session Validation**
    - Add the `validate_token` method to check whether a provided token matches the stored token for secure authentication as session management.

3. **User Data Dictionary**
    - The `user_data` method should exclude the token from the returned data.

**Example:**
```python
# Register new user and return a session_token for user Rocco
user = User(email="rianni@kings.edu.au", first_name="Rocco", last_name="Ianni", password="HelloThere")
session_token = user.token

# Returns TRUE for valid token
if user.validate_token(session_token):
    print('Valid token')

# Returns FALSE for invalid token 
invalid_token = "123456"
if user.validate_token(invalid_token):
    print('Invalid token')
    abort(401, description="Invalid user session token")
```

**Implementation Notes:**
- Ensure that the user is authorised to use the session token for every single server route.
- **Hint:** Create a helper function that can be called inside each route to validate both the session and CSRF token.

### Stage 2.2 - CSRF Protection

**Security Features:** Encryption  
**Vulnerability Addressed:** Cross-site Request Forgery (CSRF)

Consider a situation where an attacker gains control of a user session and obtains the session token. The existing code allows them to create a legitimate request on behalf of an unauthorised user.

Your task is to create Cross-Site Request Forgery (CSRF) tokens to ensure that only authorised users can make API requests to the server.

**Specifications:**

Implement the following features in each server route:

1. **CSRF Token Generation**
    - Refactor the existing `generate_token` method so that the `csrf_token` is derived from the session token.
    - The `csrf_token` should be added as an extra attribute in the `User` class.

2. **CSRF Validation**
    - Add the `validate_csrf_token` method to ensure that each request carries a valid CSRF token, which matches the one derived from the session token.
    - This will be checked for every API request or form submission.

**Example:**
```python
# Register new user and get the csrf_token tied to this user session
user = User(email="rianni@kings.edu.au", first_name="Rocco", last_name="Ianni", password="HelloThere")
csrf_token = user.csrf_token
session_token = user.token

if user.validate_token(session_token) and user.validate_csrf_token(csrf_token):
    print("API request is authorised.")
else:
    print("Unauthorised API request. Invalid session or CSRF token.")
```

**Note:** The `csrf_token` is stored on the front end and sent via the header of the HTTP request and encrypted.

**Front-End Example:**
```javascript
const token = "Some unique session token"

const response = await fetch(SERVER_URL + '/auth/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `session token ${token}`
    },
});
```

### Stage 2.3 - Race Conditions

**Vulnerability Addressed:** Race Conditions

Your task is to modify the code to ensure data handling is done asynchronously. In each server route or helper function that requires data insertion or deletion, implement `async` and `await` to handle data updates concurrently.

**Example:**
```python
# Ensure Flask is installed with async support
# Install Flask with async:
pip install flask[async]
```

## Stage 3 - Advanced

### Stage 3.1 - Invalid Forwarding

**Vulnerability Addressed:** Invalid Forwarding and Redirecting

Our current implementation uses `window.ref` to handle page redirection, which makes the application vulnerable to XSS attacks. Your task is to:

1. Replace the `window.ref` logic with **Next.js's** `next/router` methods (`router.push()` or `router.replace()`).
2. Ensure the target URL for redirection is controlled and safe from manipulation.

**Implementation Notes:**
- Stage 3.1 will need to be implemented locally on the provided front-end.

### Stage 3.2 - Token Storage

**Vulnerability Addressed:** XSS Attacks on Token Storage

Currently, session tokens are stored in local storage, which is vulnerable to XSS attacks. To mitigate this risk, you will:

1. Replace local storage token handling with secure, HTTP-only cookies.
2. Ensure the session token is stored in an HTTP-only cookie on the server side and is not accessible via client-side JavaScript.

**Implementation Example:**

**Server-Side:**
```python
# Create response and set session token as HTTP-only cookie
response = make_response(jsonify({"message": "User registered successfully"}))
response.set_cookie('session_token', user.token, httponly=True, secure=True)
```

**Front-End:**
```javascript
const token = "Some unique session token"

const response = await fetch(SERVER_URL + '/auth/login', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `session token ${token}`
    },
});
```

**Note:** The front end must send the data through the encrypted header over the body to prevent API hijacking.

## Forum API Description

### Authorisation Routes

#### `POST /auth/register`

Registers a new user and returns a session token.

- **Parameters:**
    - `email` (body)
    - `password` (body)
    - `firstName` (body)
    - `lastName` (body)

- **Responses:**
    - **200:** User registered successfully returns a unique token.
        ```json
        {
            "message": "User registered successfully",
            "token": "token"
        }
        ```
    - **400:** If any of the following are true:
        - Email incorrect format
        - Password doesn't have one unique character, one upper or lowercase character, and is less than eight characters long
        - `nameFirst` is less than 2 characters or more than 20 characters.
        - `nameLast` is less than 2 characters or more than 20 characters.
    - **409:** Email already registered.

#### `POST /auth/login`

Logs in an existing user and returns a session token.

- **Parameters:**
    - `email` (body)
    - `password` (body)

- **Responses:**
    - **200:** The user logs in successfully and returns a unique token.
        ```json
        {
            "message": "User logged in successfully",
            "token": "some_token"
        }
        ```
    - **401:** Incorrect password input.
    - **400:** The email format is incorrect.

#### `DELETE /auth/logout`

Logs out the currently authenticated user.

- **Parameters:**
    - `email` (body)
    - `password` (body)
    - `sessionToken` (body)

- **Responses:**
    - **200:** User logged out successfully.
        ```json
        {
            "message": "User logged out successfully"
        }
        ```
    - **401:** Invalid session token.

#### `POST /auth/validate`

Validates if a user is in session.

**Note:** `/auth/validate` API is called from the front-end to grant authorisation to certain web pages.

- **Parameters:**
    - `sessionToken` (body)

- **Responses:**
    - **200:** Token is valid and user is in session.
        ```json
        {
            "message": "Token is valid and user is in session"
        }
        ```
    - **401:** Invalid session token.

### Forum Routes

#### `POST /forum/new/question`

Creates a new forum with a question.

- **Parameters:**
    - `title` (body)
    - `forumQuestion` (body)
    - `sessionToken` (body)

- **Responses:**
    - **200:** New forum created successfully.
        ```json
        {
            "message": "Forum created successfully"
        }
        ```
    - **400:** If any of the following are true:
        - The title is either less than 3 characters long or more than 10 characters long.
    - **409:** Title already exists for another quiz.
    - **401:** Invalid session token.

#### `GET /forum/retrieve`

Retrieves all the forums from in-memory storage.

**Note:** The forums in the in-memory dictionary can be empty or `{}`.

- **Parameters:** None

- **Responses:**
    - **200:** Forums retrieved from back-end successfully.
        ```json
        {
            "message": "All forum data returned successfully"
        }
        ```

#### `POST /forum/reply/submit`

Adds a reply to a specific forum.

- **Parameters:**
    - `forumId` (body)
    - `reply` (body)
    - `sessionToken` (body)

- **Responses:**
    - **200:** Reply to forum added successfully.
        ```json
        {
            "message": "Forum reply added successfully"
        }
        ```
    - **404:** Forum not found with invalid forum id.
    - **401:** Invalid session token.
    - **400:** If any of the following are true:
        - Reply is more than 100 characters in length.
        - Reply is an empty string.
```

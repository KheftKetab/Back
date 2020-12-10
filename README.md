# KheftKetab Sample Project

An open-source project to test and learn `django-rest-framework`.

 ## How to run.
 
 - Make sure that you have installed `python` programming language and `virtualenv` package, using the following commands:
     
     1. It should return the current version of python otherwise you didn't install python correctly.
        ```
        python --version
        ```
      
     2. Same as _part 1_. 
        ```
        virtualenv --version
        ```
    
    
- Clone the project to access it locally:
    ```
    git clone https://github.com/KheftKetab/Back
    ```


- It's time to create a new virtualenv environment to keep track and manage installed packages:

    ```
    virtualenv --python=python3 <virtual-env-name>
    ```
  
- Activate your virtualenv environment:
    ```
    source <path-to-virtualenv>/bin/activate
    ``` 
- Installed packages used in project, by entering below piece of code where `requirements.txt` file located: 
    ```
    (<virtual-env-name>) pip install -r requirements.txt
    ```
  
 - Execute the following command to run server on your local computer where `manage.py` located:
    ```
    (<virtual-env-name>) python manage.py runserver
    ```
   
   
 ## Features 
 
 ### User
 - [X] User Registration/Login
 - [X] User Authentication using JWT
 - [ ] User Forgot Password
 - [ ] User Activation Email
 - [ ] User Activation SMS
 - [ ] User Change Password
 - [X] User Actions Postman Test 

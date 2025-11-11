"""
Password Manager Password Class Script
Author: Carlos Navarro-Montanez
Date: November 11th, 2025
For each password entry, this class holds the following attributes:
- pass_id: Unique identifier for the password entry
- pass_app: Name of the application or service associated with the password
- pass_user: Username associated with the password
- pass_value: The actual password string
"""

class Password:
    def __init__(self, pass_id, pass_app, pass_user, pass_value):
        self.pass_id = pass_id
        self.pass_app = pass_app
        self.pass_user = pass_user
        self.pass_value = pass_value
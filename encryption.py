"""
Password Manager Encryption Script
Author(s): Carlos Navarro-Montanez
Date: November 11th, 2025
"""
from password import Password
from argon2 import PasswordHasher as ph

#Encrypt password using Argon2 algorithm and return hashed value
def encrypt_password(password: Password) -> str:
    hashed_password = ph().hash(password.pass_value)
    return hashed_password

#Ensure password has correctly been hashed and can be retrieved
def verify_password(password: Password, hashed_value: str) -> bool:
    try:
        return ph().verify(hashed_value, password.pass_value)
    except:
        return False
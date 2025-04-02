import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special, use_uppercase, use_lowercase):
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type."
    
    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔐 Advanced Password Generator")


use_digits = st.checkbox("Include numbers")
use_special = st.checkbox("Include special characters")
use_uppercase = st.checkbox("Include uppercase letters", value=True)
use_lowercase = st.checkbox("Include lowercase letters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special, use_uppercase, use_lowercase)
    st.success(f"Your generated password: `{password}`")
    
    if st.button("Copy to Clipboard"):
        st.code(password, language='')
import streamlit as st
import random
import string
import hashlib
import requests
import pyperclip
import datetime

# Function to generate a strong password
def generate_password(length=12, use_digits=True, use_special=True, use_upper=True, use_lower=True):
    char_pool = ""
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    
    if not char_pool:
        return "Select at least one character set!"
    
    return ''.join(random.choices(char_pool, k=length))

# Function to check password strength
def check_strength(password):
    strength = "Weak"
    length = len(password)
    
    if length >= 12 and any(char.isdigit() for char in password) and any(char.isupper() for char in password) and any(char in string.punctuation for char in password):
        strength = "Strong"
    elif length >= 8:
        strength = "Medium"
    
    return strength

# Function to check if password is pwned
def is_pwned(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    
    if response.status_code == 200:
        hashes = (line.split(':') for line in response.text.splitlines())
        return any(suffix == h for h, _ in hashes)
    
    return False

# Streamlit UI
st.set_page_config(page_title="Advanced Password Generator", layout="wide")
st.title("🔐 Advanced Password Generator")

# User settings
length = st.slider("Select password length:", 6, 32, 12)
use_digits = st.checkbox("Include Numbers", True)
use_special = st.checkbox("Include Special Characters", True)
use_upper = st.checkbox("Include Uppercase Letters", True)
use_lower = st.checkbox("Include Lowercase Letters", True)
num_passwords = st.number_input("Generate multiple passwords:", min_value=1, max_value=10, value=1, step=1)

# Generate password(s)
if st.button("Generate Password"):
    passwords = [generate_password(length, use_digits, use_special, use_upper, use_lower) for _ in range(num_passwords)]
    
    for pwd in passwords:
        strength = check_strength(pwd)
        st.text_input(f"Generated Password ({strength}):", pwd, key=pwd)
        if is_pwned(pwd):
            st.warning("⚠️ This password has been found in a data breach! Consider using a stronger one.")
        
        if st.button(f"Copy to Clipboard ({pwd[:4]}...)", key=f"copy_{pwd}"):
            pyperclip.copy(pwd)
            st.success("Password copied to clipboard!")

# Password expiry
expiry_days = st.slider("Set password expiration time (days):", 1, 365, 30)
expiry_date = datetime.datetime.now() + datetime.timedelta(days=expiry_days)
st.write(f"🔒 This password will expire on: **{expiry_date.strftime('%Y-%m-%d')}**")

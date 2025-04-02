# Advanced Password Generator

## Overview

The **Advanced Password Generator** is a powerful and secure tool that allows users to generate strong, customizable passwords with various security features. It ensures password strength, prevents breaches, and provides additional functionalities such as bulk password generation and expiration settings.

## Features

### 1️⃣ **Password Customization**
- **Set Password Length** – Choose the desired length for your password.
- **Character Customization** – Include or exclude uppercase letters, numbers, and special characters.
- **Multiple Passwords** – Generate multiple passwords at once.

### 2️⃣ **Security Enhancements**
- **Password Strength Meter** – Check password strength in real-time.
- **Breach Detection** – Verify if the password has been compromised using the Have I Been Pwned API.
- **Auto-Expiration** – Set an expiration date for the password.
- **Clipboard Copy** – Easily copy generated passwords.

### 3️⃣ **User Experience & Storage**
- **Dark Mode Support** – Toggle between light and dark themes.
- **Save Passwords** – Option to store generated passwords securely in a database.
- **Export to File** – Download generated passwords as a text or CSV file.

## Installation

### Prerequisites

- Python 3.x
- Streamlit
- SQLite (for optional password storage)
- Requests (for breach detection API)

### Steps to Install

1. Clone the repository:
    ```bash
    git clone https://github.com/your-repo/password-generator.git
    cd password-generator
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    streamlit run app.py
    ```

5. Open the app in your browser at `http://localhost:8501`.

## How to Use

1. **Select Preferences**: Adjust password length and customization options.
2. **Generate Passwords**: Click the "Generate" button to create a secure password.
3. **Check Strength & Security**: View the password strength meter and breach detection results.
4. **Copy or Save**: Copy the password to the clipboard or save it securely.
5. **Download**: Export passwords to a text or CSV file for future use.

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

Owned By Datta Manas

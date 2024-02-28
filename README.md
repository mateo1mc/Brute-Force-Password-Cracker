# Time Brute Force Password Cracker
This Python script is a simple brute force password cracker that employs a time-based approach to crack passwords character by character. 
It prompts the user to input a password and then iterates through each character of the password using a brute force method until it successfully matches each character. 
The script measures the time taken to crack the password.

## Features
- Brute force approach to crack passwords character by character.
- Measures the time taken to crack the password.
- Supports a wide range of characters including uppercase letters, lowercase letters, numbers, and special characters.

## How it Works
- The script prompts the user to input a password.
- It iterates through each character of the password using a brute force method.
- For each character, it generates random guesses until it matches the character of the password.
- Once all characters are matched, the password is revealed, and the time taken to crack the password is displayed.

## Usage
1. Clone the repository:

    ```
    git clone https://github.com/mateo1mc/TimeBruteForcePasswordCracker.git
    ```
2. Navigate to the directory:

    ```
    cd password-cracker
    ```
3. Run the Python script:

    ```
    python password_cracker.py
    ```

4. Follow the prompts to input your desired password.

## Requirements

- Python 3.x
- Random module
- Time module
- OS module

## Note

- This program is for educational purposes only and should not be used for malicious activities.
- The brute-force method used in this program may not be efficient for cracking complex passwords.


## Author




# PBKDF2 Password Cracker

This project is a simple dictionary-based password cracker implemented in Python.

It reads hashed passwords from an input file, generates possible password candidates based on common patterns, hashes each candidate using PBKDF2-HMAC-SHA1, and compares the result with the target hashes. If a match is found, the original password is written to `Passwords.txt`.

## Features

- Reads user data from `hashedPasswords.txt`
- Uses PBKDF2-HMAC-SHA1 with:
  - salt: `ajou`
  - iterations: `500`
  - key length: `16 bytes`
- Generates password candidates using:
  - common words
  - common numeric patterns
  - capitalized words
  - special characters
  - username-based combinations
- Writes cracked passwords to `Passwords.txt`

## Input Format

The input file must be named `hashedPasswords.txt` and follow this format:

[number]:[username]:[hashed password]

Example:

1:babarian:1a48fa206295b0a6f86a4060b17897ad

## Output Format

The output file is `Passwords.txt` and follows this format:

[number]:[username]:[password]

Example:

1:babarian:Qwerty1

## How It Works

1. Read all users from `hashedPasswords.txt`
2. Store target hashes in a set for fast lookup
3. Store hash-to-user mapping in a dictionary
4. Generate candidate passwords from:
   - predefined words
   - number patterns
   - special characters
   - usernames in the input file
5. Hash each candidate with PBKDF2-HMAC-SHA1
6. If the generated hash matches a target hash, save the result
7. Write all found passwords to `Passwords.txt`

## How to Run

```bash
python3 main.py
import hashlib
users = []

with open("hashedPasswords.txt", "r") as file:
    for i in file:
        i = i.strip()
        number, username, hashed_password = i.split(":")
        users.append({
            "number": number,
            "username": username,
            "hashed_password": hashed_password
        })

words = ["password", "qwer", "hello", "apple", "ajou", "user", "abcd", "abc"]

nums = ["1234", "0000", "1111", "2026", "2222"]

possible_passwords = []

salt = b"ajou"

for word in words:
    for num in nums:
        possible_passwords.append(word+num)

for password in possible_passwords:
    hashed = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 500, 16).hex()
    for user in users:
        if hashed == user["hashed_password"]:
            with open("Passwords.txt", "w") as result:
                result.write(f"{user["number"]}:{user["username"]}:{hashed}")
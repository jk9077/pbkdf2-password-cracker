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

words = ["password", "qwer", "qwert", "hello", "apple", "ajou", "user", "abcd", "abc", "asd", 
         "asdf", "asdfg", "my", "pass", "admin", "qwerty", "zxcv"]

nums = ["1234", "0000", "1111", "2026", "2222", "12", "123", "12345", "123456"]
for i in range(10):
    nums.append(str(i))

special_chars = ["!", "@", "#", "!!", "@@", "##", "*", "**"]


possible_passwords = []



salt = b"ajou"

for word in words:
    for num in nums:
        possible_passwords.append(word+num)
        possible_passwords.append(word.capitalize()+num)
        for special in special_chars:
            possible_passwords.append(word+num+special)
            possible_passwords.append(word.capitalize()+num+special)

for user in users:
    for num in nums:
        possible_passwords.append(user["username"]+num)
        possible_passwords.append(user["username"].capitalize()+num)
        for special in special_chars:
            possible_passwords.append(user["username"]+num+special)
            possible_passwords.append(user["username"].capitalize()+num+special)

with open("Passwords.txt", "w") as result:
    for user in users:
        for password in possible_passwords:
            hashed = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 500, 16).hex()
            if hashed == user["hashed_password"]:
                result.write(f"{user["number"]}:{user["username"]}:{password}\n")
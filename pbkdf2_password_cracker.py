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
for user in users:
    print(user)

password = "goodjob"
salt = b"ajou"

ex = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 500, 16).hex()

for user in user:
    if ex == user["hashed_password"]:
        with open("Passwords.txt", "w") as result:
            result.write(f"{user["number"]}:{user["username"]}:{ex}")
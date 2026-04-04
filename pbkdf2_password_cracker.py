import hashlib

def try_password(candidate):
    hashed = hashlib.pbkdf2_hmac("sha1", candidate.encode(), salt, 500, 16).hex()

    if hashed in target_hashes:
        for number, username in hash_to_users[hashed]:
            found_passwords.add((number, username, candidate))

users = []
target_hashes = set()
hash_to_users = {}

with open("hashedPasswords.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        number, username, hashed_password = line.split(":")
        users.append({
            "number": number,
            "username": username,
            "hashed_password": hashed_password
        })

for user in users:
    h = user["hashed_password"]
    target_hashes.add(h)

    if h not in hash_to_users:
        hash_to_users[h] = []

    hash_to_users[h].append((user["number"], user["username"]))

words = [
    "password", "qwer", "qwert", "hello", "apple", "ajou", "user",
    "abcd", "abc", "asd", "asdf", "asdfg", "my", "pass",
    "admin", "qwerty", "zxcv"
]

nums = ["1234", "0000", "1111", "2026", "2222", "12", "123", "12345", "123456"]
for i in range(10):
    nums.append(str(i))

special_chars = ["!", "@", "#", "!!", "@@", "##", "*", "**"]

salt = b"ajou"
found_passwords = set()


for word in words:
    for num in nums:
        try_password(word + num)
        try_password(word.capitalize() + num)

        for special in special_chars:
            try_password(word + num + special)
            try_password(word.capitalize() + num + special)

for user in users:
    username = user["username"]

    for num in nums:
        try_password(username + num)
        try_password(username.capitalize() + num)

        for special in special_chars:
            try_password(username + num + special)
            try_password(username.capitalize() + num + special)

with open("Passwords.txt", "w") as result:
    for number, username, password in found_passwords:
        result.write(f"{number}:{username}:{password}\n")
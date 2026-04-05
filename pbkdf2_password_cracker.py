import hashlib

users = []
target_hashes = set()
hash_to_users = {}
salt = b"ajou"
found_passwords = set()

def try_password(password):
    hashed = hashlib.pbkdf2_hmac("sha1", password.encode(), salt, 500, 16).hex()

    if hashed in target_hashes:
        for number, username in hash_to_users[hashed]:
            found_passwords.add((number, username, password))

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
    "admin", "qwerty", "zxcv", "apple", "banana", "dragon", "aaaa", "bbbb", "cccc", "dddd",
    "test", "login", "love", "chicken", "maple", "sun", "star", "jk", "good", "bad", "star",
    "guest", "root", "asdfgh", "dog", "cag"]

nums = ["1234", "0000", "1111", "2026", "2222", "12", "123", "12345", "123456", 
        "3333", "4444", "5555", "00", "2000", "2025", "2024", "2023", "2020", "2021", "2022",
        "11", "22", "33", "44", "55"]
for i in range(10):
    nums.append(str(i))

special_chars = ["!", "@", "#", "!!", "@@", "##", "*", "**"]


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
    for number, username, password in sorted(found_passwords, key=lambda x: int(x[0])):
        result.write(f"{number}:{username}:{password}\n")
import sys
import hashlib
import bcrypt
import itertools
import string

password = ""
count = 0
alpha = string.printable

# Function for brute-force attack
def bruteForce(size, attempt=""):
    global count
    if size == 0:
        if attempt == password:
            crack = attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            bruteForce(size - 1, newTry)

# Function for dictionary attack
def dictionaryAttack(dictionary_files):
    global count

    for dictionary_file in dictionary_files:
        with open(dictionary_file, 'r', encoding='latin-1') as file:
            words = file.read().splitlines()

        for word in words:
            count += 1
            if word == password:
                crack = word
                print("Cracked password: " + crack)
                print(count, " tries")
                exit()


def bruteForceBcrypt(pwd):
    counter = 0
    for length in range(1, 999): 
        for comb in itertools.product(alpha, repeat=length):
            target = "".join(comb)
            counter += 1
            encodeTarget = target.encode('utf-8') 
            if (bcrypt.checkpw(encodeTarget, pwd.encode('utf-8'))):
                print("Cracked password: " + target + " in " + str(counter) + " tries")
                sys.exit()


# Function for MD5 hash brute-force attack
def bruteForceMD5Hash(size, attempt=""):
    global count
    if size == 0:
        hashed_attempt = hashlib.md5(attempt.encode()).hexdigest()
        if hashed_attempt == password:
            crack = attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            bruteForceMD5Hash(size - 1, newTry)

def bruteForceSHA256Hash(size, attempt=""):
    global count
    if size == 0:
        hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()
        if hashed_attempt == password:
            crack = attempt
            print("Cracked password: " + crack)
            print(count, " tries")
            exit()
    else:
        for x in range(32, 127):
            count += 1
            newTry = attempt + chr(x)
            bruteForceSHA256Hash(size - 1, newTry)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 passwordCrack.py [plaintext password or hash] [argument]")
        sys.exit(1)

    password = sys.argv[1]
    method = sys.argv[2]

    if method == "-p":
        # Brute-force attack
        for i in range(1, 99):
            bruteForce(i)
    elif method == "-d":
        # Dictionary attack
        dictionary_files = ["dictionary1.txt", "dictionary2.txt", "dictionary3.txt"]
        dictionaryAttack(dictionary_files)
        print("Password not found in any of the dictionaries. Switching to brute force attack.")
        for i in range(1, 99):
            bruteForce(i)
    elif method == "-m":
        # MD5 hash brute-force attack
        for i in range(1, 99):
            bruteForceMD5Hash(i)
    elif method == "-s":
        # SHA-256 hash brute-force attack
        for i in range(1, 99):
            bruteForceSHA256Hash(i)
    elif method == "-b":
        # Bcrypt hash brute-force attack
        bruteForceBcrypt(password)
    else:
        print("Invalid choice. Use -p for plaintext brute force, -d for dictionary attack, -m for MD5 hash cracking, -s for SHA-256 hash cracking, and -b for Bcrypt hash cracking.")

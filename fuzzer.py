import subprocess
import string

# Function to generate passwords/hashes
def generate_passwords():
    characters = string.digits + string.ascii_lowercase
    for i in range(len(characters)):
        yield characters[i]
        for j in range(len(characters)):
            yield characters[i] + characters[j]
            for k in range(len(characters)):
                yield characters[i] + characters[j] + characters[k]
                for l in range(len(characters)):
                    yield characters[i] + characters[j] + characters[k] + characters[l]

# Function to run the command
def run_command(password, argument):
    command = ['python3', 'passwordCrack.py', password, argument]
    subprocess.run(command)

# Main function
def main():
    argument = input("What function would you like to test? Enter -p for plaintext brute force, -d for dictionary, -m for MD5, and -s for SHA-256 ")
    print("Starting testing now. Use Ctrl+C (Windows) or Cmd+Z (macOS) to terminate program.")
    passwords = generate_passwords()
    for password in passwords:
        run_command(password, argument)

if __name__ == "__main__":
    main()

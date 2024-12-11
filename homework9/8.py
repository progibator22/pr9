import re

def parse_email(email):
    pattern = r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$"
    match = re.match(pattern, email)
    if match:
        username, domain = match.groups()
        return username, domain
    else:
        return None, None

def main():
    email = input("Enter your email: ").strip()
    username, domain = parse_email(email)
    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("Invalid email format.")

if __name__ == "__main__":
    main()

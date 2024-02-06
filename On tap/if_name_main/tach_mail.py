def emailProcess(email: str):
    username = email[0:email.index("@")]
    domain = email[email.index("@")+1:]
    return [username, domain]

def printMsg(msn, dmn):
    print(f"Username is {msn}, Domain is {dmn}")

def main():
    email = input("Please enter email address! ").strip()
    usn, dmn = emailProcess(email)
    printMsg(usn, dmn)

if __name__ == "__main__":
    main()
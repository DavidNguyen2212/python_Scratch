from tach_mail import emailProcess, printMsg

def main():
    emails = ["cc@example.com", "liverpool@ccc.def.vn", "vodoi@hotmail.com"]
    for email in emails:
        usn, dmn = emailProcess(email)
        printMsg(usn, dmn)

if __name__ == "__main__":
    main()
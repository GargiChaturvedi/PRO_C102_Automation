import dropbox
import os

def composeMsg(sirOrMadam, subName, testOrAssignment, studentName, grade):
    msg = "Dear " + sirOrMadam + ",\n" + "Please note that I have successfully submitted the " + subName + " " + testOrAssignment + ". Kindly assess it and give your valuable feedback.\nYour student,\n" + studentName + "\n" + grade
    with open('message.txt', 'w') as f:
        f.write(msg)
        f.close()
    
    print("File updated! Your polite message is as follows:")
    with open('message.txt', 'r') as f:
        print(f.read())   

def main():
    print("Welcome to Polite Message Composer!")
    print("This is an initiative to make students realize the value of respecting your teachers, communicating with them politely and becoming their favourite!")
    print("So let's compose a polite message for you!")
    gender = input("Is your teacher a sir or ma'am?\n")
    subject = input("What subject do they teach?\n")
    testOrAssignment = input("Is it a test or assignment?\n")
    studentName = input("Finally, please enter your name\n")
    grade = input("And your grade\n")
    print("Check message.txt for the results!")
    composeMsg(gender, subject, testOrAssignment, studentName, grade)

    accessToken = "sl.BON98GjCtTpKXQhsyybmM0vgP6ujPBGgYbs1xwAdkiGamqOyD-dNJHeS5S-lAARHWtKbKWp-8TVQBR7MgOU5tHQr5h9lA16SLXuWsfVjcpSaV4YYrf4IPL6tAmcVso_bnH4lX7yFoKM"
    dbx = dropbox.Dropbox(accessToken)
    with open("message.txt", "rb") as f:
        fileTo = "/message.txt"
        dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
    print("Message File uploaded to Dropbox!")


main()

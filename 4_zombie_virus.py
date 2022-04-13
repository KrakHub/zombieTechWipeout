from distutils import command
from tkinter import *
from tkinter.filedialog import askopenfile
import smtplib, ssl


# Actual email stuff
def send_message():
    sender_email = "rosalez_alaina@student.mahoningctc.com"
    sender_password = "matbvaghbujuhoti"

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,sender_password)

    print("Login Successful")
    
    address_info = address.get()
    subject_info = subject.get()
    email_body_info = email_body.get()
    email_text = 'Subject: {}\n\n{}'.format(subject_info, email_body_info)
    

    server.sendmail(sender_email,address_info,email_text)

    print("Message Sent")

    address_entry.delete(0,END)
    subject_entry.delete(0,END)
    email_body_entry.delete(0,END)


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass

# Code for the App
app = Tk()
app.geometry("750x400")
app.title("Python Emails")

heading = Label(text="Zombie Virus Python Mail",bg="lavender",fg="black",font="10",width="500",height="3")
heading.pack()

address_field = Label(text="Recipient Address :")
subject_field = Label(text="Subject :")
email_body_field = Label(text="Message :")
attachment_field = Label(text="File :")

address_field.place(x=15,y=80)
subject_field.place(x=15,y=120)
email_body_field.place(x=15,y=160)
attachment_field.place(x=15,y=200)

address = StringVar()
subject = StringVar()
email_body = StringVar()
attachment = Button(app, text='Upload File', command = lambda:open_file() )

address_entry = Entry(textvariable=address,width="30")
subject_entry = Entry(textvariable=subject,width="30")
email_body_entry = Entry(textvariable=email_body,width="30")
attachment_entry = Button(app, text='Upload File', command = lambda:open_file() )

address_entry.place(x=15,y=100)
subject_entry.place(x=15,y=140)
email_body_entry.place(x=15,y=180)
attachment_entry.place(x=15,y=220)

button = Button(app,text="Send Message",bg="IndianRed",command=send_message,width="30",height="2")
button.place(x=15,y=260)


mainloop()

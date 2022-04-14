from distutils import command, file_util
from tkinter import *
from tkinter.filedialog import askopenfile
import smtplib
import imghdr
from email.message import EmailMessage


# Actual email stuff
def send_message():
    Sender_Email = "rosalez_alaina@student.mahoningctc.com"
    Reciever_Email = "ccpoynter03@gmail.com"
    password = input('Enter your email account password: ')

    newMessage = EmailMessage()
    newMessage['Subject'] = "Check out the new logo" 
    newMessage['From'] = Sender_Email
    newMessage['To'] = Reciever_Email
    newMessage.set_content('Let me know what you think. Image attached!') 

    with open('360.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(Sender_Email, password)
        smtp.send_message(newMessage)

    print("Message Sent")

    address_entry.delete(0,END)
    subject_entry.delete(0,END)
    email_body_entry.delete(0,END)


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '.png')])
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
attachment = file_util

address_entry = Entry(textvariable=address,width="30")
subject_entry = Entry(textvariable=subject,width="30")
email_body_entry = Entry(textvariable=email_body,width="30")
attachment_entry = Button(app, text='Upload File', command = open_file() )

address_entry.place(x=15,y=100)
subject_entry.place(x=15,y=140)
email_body_entry.place(x=15,y=180)
attachment_entry.place(x=15,y=220)

button = Button(app,text="Send Message",bg="IndianRed",command=send_message,width="30",height="2")
button.place(x=15,y=260)


mainloop()
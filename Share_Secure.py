import os
from tkinter import *
import socket  
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

# Get the path of the current script
script_dir = os.path.dirname(__file__)  # This gives the directory where Share_Secure.py is located

# Function to construct the path for images dynamically
def get_image_path(image_name):
    return os.path.join(script_dir, "Images", image_name)

def Send():
    window = Toplevel(root)
    window.title("Send")
    window.geometry('450x560+500+200')
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                              title="Select Image File",
                                              filetype=(('file_type', '*.txt'), ('all files', '*.*')))

    def sender():
        s = socket.socket()
        host = socket.gethostname()
        port = 8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('waiting for any incoming connections....')
        conn, addr = s.accept()
        file = open(filename, 'rb')
        file_data = file.read(1024)
        conn.send(file_data)
        print("Data has been transmitted successfully..")

    # Load icons and backgrounds using the relative path
    image_icon1 = PhotoImage(file=get_image_path("send.png"))
    window.iconphoto(False, image_icon1)

    Sbackground = PhotoImage(file=get_image_path("sender.png"))
    Label(window, image=Sbackground).place(x=-2, y=0)

    Mbackground = PhotoImage(file=get_image_path("id.png"))
    Label(window, image=Mbackground, bg='#f4fdfe').place(x=100, y=260)

    host = socket.gethostname()
    Label(window, text=f'ID: {host}', bg='white', fg='black').place(x=140, y=290)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=select_file).place(x=160, y=150)
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg='#000', fg="#fff", command=sender).place(x=300, y=150)

    window.mainloop()

def Receive():
    main = Toplevel(root)
    main.title("Receive")
    main.geometry('450x560+500+200')
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def receiver():
        ID = SenderID.get()
        filenamel = incoming_file.get()
        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        file = open(filenamel, 'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been received successfully")

    # Load icons and backgrounds using the relative path
    image_icon1 = PhotoImage(file=get_image_path("receive.png"))
    main.iconphoto(False, image_icon1)

    Hbackground = PhotoImage(file=get_image_path("receiver.png"))
    Label(main, image=Hbackground).place(x=-2, y=0)

    logo = PhotoImage(file=get_image_path('profile.png'))
    Label(main, image=logo, bg="#f4fdfe").place(x=10, y=250)

    Label(main, text="Receive", font=('arial', 20), bg="#f4fdfe").place(x=100, y=280)

    Label(main, text="Input sender id", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=340)
    SenderID = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    SenderID.place(x=20, y=370)
    SenderID.focus()

    Label(main, text="filename for the incoming file:", font=('arial', 10, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    incoming_file = Entry(main, width=25, fg="black", border=2, bg='white', font=('arial', 15))
    incoming_file.place(x=20, y=450)

    imageicon = PhotoImage(file=get_image_path("arrow.png"))
    rr = Button(main, text="Receive", compound=LEFT, image=imageicon, width=130, bg="#39c790", font="arail 14 bold", command=receiver)
    rr.place(x=20, y=500)

    main.mainloop()

# icon
image_icon = PhotoImage(file=get_image_path("icon.png"))
root.iconphoto(False, image_icon)

Label(root, text="File Transfer", font=('Acumin Varible Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_image = PhotoImage(file=get_image_path("send.png"))
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)

recieve_image = PhotoImage(file=get_image_path("receive.png"))
recieve = Button(root, image=recieve_image, bg="#f4fdfe", bd=0, command=Receive)
recieve.place(x=300, y=100)

# label
Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

background = PhotoImage(file=get_image_path("background.png"))
Label(root, image=background).place(x=-2, y=323)

root.mainloop()

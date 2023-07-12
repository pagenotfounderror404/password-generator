import json
from tkinter import *
from  tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols) ]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list= password_numbers+password_symbols+password_letters

    random.shuffle(password_list)

    password=''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def enter_password():

    webe=web_entry.get()
    emaile= email_entry.get()
    passworde=password_entry.get()
    new_data={webe:{"email": emaile,
                    "password": passworde, }}
    if len(webe)==0 or len(emaile)==0 or len(passworde)== 0:
        messagebox.showerror(title="Oops",message="You have left some fields empty")
    else:
        # web_password = webe + "   |   " + emaile + "   |    " + passworde + "\n"
        ans = messagebox.askyesno(message="Are you sure?")
        if ans == True:
            try:
                with open("Password Manager.json","r") as f:
                    data=json.load(f)
            except :
                with open("Password Manager.json", "w") as f:
                    json.dump(new_data,f, indent=4 )
            else:
                data.update(new_data)
                with open("Password Manager.json","w") as f:
                    json.dump(data, f, indent=4)
                    # f.write(web_password)
            finally:
                web_entry.delete("0", "end")
                email_entry.delete("0", "end")
                email_entry.insert(0, "ayushac.2000@gmail.com")
                password_entry.delete("0", "end")

def find_password():
    r=web_entry.get()
    mb = messagebox
    with open("Password Manager.json","r") as f:
        data= json.load(f)
        if r in data:
            mb.showinfo("Details",f"email:{data[r]['email']}\nPassword:{data[r]['password']}")
        else:
            mb.showerror("Error","You haven't created any account on this website")




# ---------------------------- UI SETUP ------------------------------- #
from tkinter import Button

font=("Times new Roman",16)
font1=("Calibri",10)
w=Tk()
w.title("Password Manager")
w.config(padx=100, pady=50)
c=Canvas(height=200,width=300)
p=PhotoImage(file="logo.png")
c.create_image(100,100, image= p)
c.grid(row=0,column=1)


web=Label(text="Website", font= font)
web.grid(row=1, column=0)
web.config(padx=2, pady=2)


search= Button(text="Search", font=font1, width=14, command=find_password)
search.grid(row=1, column=2)

email=Label(text="Email-ID", font= font)
email.grid(row=2, column=0)
email.config(padx=2, pady=2)


password=Label(text="Password", font= font)
password.grid(row=3, column=0)
password.config(padx=2, pady=3)

web_entry_v=StringVar()
web_entry= Entry(font=font1, width=31, textvariable=web_entry_v)
web_entry.grid( row=1, column=1, columnspan=1,sticky=E)
web_entry.focus()

email_entry_v=StringVar()
email_entry= Entry(font=font1, width=35, textvariable=email_entry_v)
email_entry.grid( row=2, column=1, columnspan=2)
email_entry.insert(0,"ayushac.2000@gmail.com")

password_entry_v= StringVar()
password_entry= Entry(font=font1, width=19, textvariable=password_entry_v)
password_entry.grid( row=3, column=1)

genpass= Button(text= "Generate Password", width=14, command=generate_password)
genpass.grid(row=3, column=2, sticky=W)

add= Button(text="Add", width=60, command=enter_password)
add.grid(row=4, column=1, columnspan=2, sticky=E)


w.mainloop()




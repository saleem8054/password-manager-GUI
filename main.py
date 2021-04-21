from tkinter import *
from tkinter import messagebox
import random
import clipboard

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_random_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(4, 6)
    nr_numbers = random.randint(4, 6)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    
    if password_entry.get() == "":
        password_entry.insert(0,password)
        window.clipboard_clear()
        window.clipboard_append(password)
    else:
        messagebox.showinfo(title="Oops",message="The field already contains the password.")
             

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website_name = website_name_entry.get()
    user_email = email_label_entry.get()
    user_password = password_entry.get()
    
    if website_name != "" and user_password != "":
    
        is_ok = messagebox.askokcancel(title=website_name,message=f"These are the details entered: \n"
                                                                    f"Email: {user_email}\n"
                                                                    f"Password: {user_password}\n"
                                                                    f"is it okay to save?")
        if is_ok:   
            with open("data.txt",'a') as file:
                file.write(f"{website_name} | {user_email} | {user_password}\n\n")
            website_name_entry.delete(0,'end')
            password_entry.delete(0,'end')
    else:
        messagebox.showinfo(title="Oops",message="Please do not leave any field empty")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

lock_image = PhotoImage(file="./logo.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=lock_image)
canvas.grid(row=0,column=1)

website_name_label = Label(text="Website:")
website_name_label.grid(row=1,column=0)

website_name_entry = Entry(width=45)
website_name_entry.focus()
website_name_entry.grid(row=1,column=1,columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_label_entry = Entry(width=45)
email_label_entry.insert(0,"saleem@gmail.com")
email_label_entry.grid(row=2,column=1,columnspan=2)
#email_label.config(pady=10)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password:",command=generate_random_password)
generate_password_button.grid(row=3,column=2)


add_button = Button(text="Add",width=43,command=save_to_file)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
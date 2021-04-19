from tkinter import *

YELLOW = "#f7f5dd"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_name_entry.grid(row=1,column=1,columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

email_label_entry = Entry(width=45)
email_label_entry.grid(row=2,column=1,columnspan=2)
#email_label.config(pady=10)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)

password_entry = Entry(width=25)
password_entry.grid(row=3,column=1)

generate_password_button = Button(text="Generate Password:")
generate_password_button.grid(row=3,column=2)


add_button = Button(text="Add",width=43)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()
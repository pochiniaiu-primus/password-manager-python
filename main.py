from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

entry_website = Entry()
entry_website.insert(END, string="")
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")

entry_email_username = Entry()
entry_email_username.insert(END, string="")
entry_email_username.grid(column=1, row=2, columnspan=2, sticky="EW")

entry_pass = Entry()
entry_pass.insert(END, string="")
entry_pass.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=35)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

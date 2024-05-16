from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_pass.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nWebsite: {website}\n"
                                                              f"Email: {email}\nPassword: {password}\nIs it OK to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0, 'end')
                entry_email_username.delete(0, 'end')
                entry_pass.delete(0, 'end')

                data_file.close()
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
entry_website.focus()
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

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

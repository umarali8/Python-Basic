from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def handle_login():
    username = username_input.get()
    password = password_input.get()

    # Demo credentials
    if username == "admin" and password == "1234":
        messagebox.showinfo("Meezan Bank", "Login Successful")
    else:
        messagebox.showerror("Meezan Bank", "Invalid Username or Password")

root = Tk()
root.title("Meezan Bank Login")
root.geometry("380x550")
root.configure(bg="#006341")  # Meezan-style green



# Load Logo
img = Image.open(r"C:\OneDrive\Desktop\Python\GUI\meezan-logo.png")
img = img.resize((140, 140))
photo = ImageTk.PhotoImage(img)

logo = Label(root, image=photo, bg="#006341")
logo.pack(pady=20)

title = Label(
    root,
    text="Meezan Bank",
    font=("Verdana", 22, "bold"),
    fg="white",
    bg="#006341"
)
title.pack()

subtitle = Label(
    root,
    text="Secure Internet Banking",
    font=("Verdana", 10),
    fg="white",
    bg="#006341"
)
subtitle.pack(pady=(0, 20))

# Username
Label(
    root,
    text="Username",
    font=("Verdana", 11),
    fg="white",
    bg="#006341"
).pack(anchor="w", padx=40)

username_input = Entry(root, font=("Verdana", 11), width=30)
username_input.pack(ipady=6, pady=(5, 15))

# Password
Label(
    root,
    text="Password",
    font=("Verdana", 11),
    fg="white",
    bg="#006341"
).pack(anchor="w", padx=40)

password_input = Entry(root, show="*", font=("Verdana", 11), width=30)
password_input.pack(ipady=6, pady=(5, 25))

# Login Button
login_btn = Button(
    root,
    text="Login",
    command=handle_login,
    bg="#D4AF37",      # Gold
    fg="black",
    font=("Verdana", 11, "bold"),
    width=20,
    height=2
)
login_btn.pack()

# Footer
footer = Label(
    root,
    text="© 2026 Meezan Bank - Demo Login",
    bg="#006341",
    fg="white",
    font=("Arial", 9)
)
footer.pack(side=BOTTOM, pady=15)

root.mainloop()